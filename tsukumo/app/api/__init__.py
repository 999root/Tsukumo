# /api/__init__.py
from flask import Blueprint

# Create a blueprint for the API
api_bp = Blueprint('api', __name__)

from . import routes  # Import routes to register them with the blueprint
