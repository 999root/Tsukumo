from flask import Flask
from api import api_bp
from views import views_bp
import os

app = Flask(__name__)

# Directory to store uploaded packages
PACKAGE_DIR = "repository"
os.makedirs(PACKAGE_DIR, exist_ok=True)

# Register blueprints
app.register_blueprint(api_bp, url_prefix="/api")
app.register_blueprint(views_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
