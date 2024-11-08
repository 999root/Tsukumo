from flask import Blueprint, render_template
import os

views_bp = Blueprint("views_bp", __name__, template_folder="../templates")

PACKAGE_DIR = "repository"

@views_bp.route('/')
def index():
    """Render a simple UI to list, upload, and delete packages."""
    packages = os.listdir(PACKAGE_DIR)
    return render_template("index.html", packages=packages)
