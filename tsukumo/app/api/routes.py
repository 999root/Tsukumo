# /api/routes.py
from flask import request, send_from_directory, jsonify, render_template, abort
from werkzeug.utils import secure_filename
import os
import tarfile
import shutil
import logging
import hashlib
from datetime import datetime, timedelta
from . import api_bp  # Import the blueprint object

# Directory to store uploaded packages
PACKAGE_DIR = "repository"
os.makedirs(PACKAGE_DIR, exist_ok=True)

# Allowed file extensions for uploaded packages
ALLOWED_EXTENSIONS = {'tar.gz', 'tar'}

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Helper function to check file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Helper function to calculate SHA-256 checksum of a file
def calculate_checksum(file_path):
    hash_algo = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()

@api_bp.route('/')
def index():
    """Render a simple UI to list, upload, and delete packages."""
    packages = os.listdir(PACKAGE_DIR)
    return render_template("index.html", packages=packages)

@api_bp.route('/packages', methods=['GET'])
def list_packages():
    """API endpoint to list all available packages."""
    packages = os.listdir(PACKAGE_DIR)
    return jsonify(packages)

@api_bp.route('/packages', methods=['POST'])
def upload_package():
    """API endpoint to upload a new .tar.gz or .tar package with checksum verification."""
    if 'file' not in request.files:
        logging.warning("No file provided in request")
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(PACKAGE_DIR, filename)
        file.save(file_path)

        # Calculate checksum
        checksum = calculate_checksum(file_path)
        logging.info(f"Uploaded package {filename} with checksum {checksum}")

        return jsonify({
            "message": f"Package {filename} uploaded successfully",
            "checksum": checksum
        }), 201
    else:
        logging.warning("Invalid file format attempt")
        return jsonify({"error": "Invalid file format. Only .tar and .tar.gz files are allowed."}), 400

@api_bp.route('/packages/<package_name>', methods=['DELETE'])
def delete_package(package_name):
    """API endpoint to delete a package."""
    package_path = os.path.join(PACKAGE_DIR, package_name)
    if os.path.exists(package_path):
        os.remove(package_path)
        logging.info(f"Package {package_name} deleted successfully")
        return jsonify({"message": f"Package {package_name} deleted successfully"}), 200
    else:
        logging.warning(f"Package {package_name} not found for deletion")
        return jsonify({"error": "Package not found"}), 404

@api_bp.route('/packages/<package_name>', methods=['GET'])
def download_package(package_name):
    """Serve package file for download with checksum verification."""
    package_path = os.path.join(PACKAGE_DIR, package_name)
    if os.path.exists(package_path):
        checksum = calculate_checksum(package_path)
        logging.info(f"Serving package {package_name} with checksum {checksum}")
        return send_from_directory(PACKAGE_DIR, package_name, as_attachment=True)
    else:
        logging.warning(f"Package {package_name} not found for download")
        return jsonify({"error": "Package not found"}), 404

@api_bp.route('/compile', methods=['POST'])
def compile_package():
    """Compile multiple uploaded files into a .tar.gz package asynchronously."""
    if 'files' not in request.files:
        logging.warning("No files provided for compilation")
        return jsonify({"error": "No files provided"}), 400

    files = request.files.getlist('files')
    if len(files) < 1:
        logging.warning("Attempted compilation with no files")
        return jsonify({"error": "At least one file is required"}), 400

    # Create a temporary directory to store the files
    temp_dir = os.path.join(PACKAGE_DIR, "temp")
    os.makedirs(temp_dir, exist_ok=True)

    # Save uploaded files in the temporary directory
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(temp_dir, filename))
        else:
            logging.warning(f"Invalid file {file.filename} skipped")

    # Create a tar.gz archive from the files
    tar_filename = "compiled_package.tar.gz"
    tar_filepath = os.path.join(PACKAGE_DIR, tar_filename)

    with tarfile.open(tar_filepath, "w:gz") as tar:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                tar.add(os.path.join(root, file), arcname=file)

    # Calculate checksum for the compiled package
    checksum = calculate_checksum(tar_filepath)
    logging.info(f"Compiled package created with checksum {checksum}")

    # Cleanup temporary directory
    shutil.rmtree(temp_dir)

    return jsonify({
        "message": f"Compiled package {tar_filename} created successfully",
        "checksum": checksum
    }), 201
