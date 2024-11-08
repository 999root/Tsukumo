from flask import Flask, request, send_from_directory, jsonify, render_template
import os
from werkzeug.utils import secure_filename
import tarfile
import shutil

app = Flask(__name__)

# Directory to store uploaded packages
PACKAGE_DIR = "repository"
os.makedirs(PACKAGE_DIR, exist_ok=True)

# Allowed file extensions for uploaded packages (including .tar)
ALLOWED_EXTENSIONS = {'tar.gz', 'tar'}

def allowed_file(filename):
    """Check if the file is allowed based on extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Render a simple UI to list, upload, and delete packages."""
    packages = os.listdir(PACKAGE_DIR)
    return render_template("index.html", packages=packages)

@app.route('/packages', methods=['GET'])
def list_packages():
    """API endpoint to list all available packages."""
    packages = os.listdir(PACKAGE_DIR)
    return jsonify(packages)

@app.route('/packages', methods=['POST'])
def upload_package():
    """API endpoint to upload a new .tar.gz or .tar package."""
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(PACKAGE_DIR, filename))
        return jsonify({"message": f"Package {filename} uploaded successfully"}), 201
    else:
        return jsonify({"error": "Invalid file format. Only .tar and .tar.gz files are allowed."}), 400

@app.route('/packages/<package_name>', methods=['DELETE'])
def delete_package(package_name):
    """API endpoint to delete a package."""
    package_path = os.path.join(PACKAGE_DIR, package_name)
    if os.path.exists(package_path):
        os.remove(package_path)
        return jsonify({"message": f"Package {package_name} deleted successfully"}), 200
    else:
        return jsonify({"error": "Package not found"}), 404

@app.route('/packages/<package_name>', methods=['GET'])
def download_package(package_name):
    """Serve package file for download."""
    return send_from_directory(PACKAGE_DIR, package_name)

@app.route('/compile', methods=['POST'])
def compile_package():
    """Compile multiple uploaded files into a .tar.gz or .tar package."""
    if 'files' not in request.files:
        return jsonify({"error": "No files provided"}), 400

    files = request.files.getlist('files')
    if len(files) < 1:
        return jsonify({"error": "At least one file is required"}), 400

    # Create a temporary directory to store the files
    temp_dir = os.path.join(PACKAGE_DIR, "temp")
    os.makedirs(temp_dir, exist_ok=True)

    # Save uploaded files in the temporary directory
    for file in files:
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(temp_dir, filename))

    # Create a tar.gz or tar archive from the files
    tar_filename = "compiled_package.tar.gz"  # You can adjust to use .tar if needed
    tar_filepath = os.path.join(PACKAGE_DIR, tar_filename)

    with tarfile.open(tar_filepath, "w:gz") as tar:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                tar.add(os.path.join(root, file), arcname=file)

    # Cleanup temporary directory
    shutil.rmtree(temp_dir)

    return jsonify({"message": f"Compiled package {tar_filename} created successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
