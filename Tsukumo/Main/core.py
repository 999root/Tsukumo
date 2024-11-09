
import os
from ..Util import error

class Core:
    """
    A core class that initializes the repository and local package storage setup 
    for the package manager.
    """

    def __init__(self, repo_url: str | None = None, package_data_path: str | None = None) -> None:
        """
        Initializes the Core instance with repository URL and package storage path.
        
        Parameters:
        - repo_url (str | None): The URL of the repository where packages are stored. 
                                 If None, an error message is triggered.
        - package_data_path (str | None): The path where downloaded packages will be stored locally. 
                                          Defaults to "repository" if not provided.

        Raises:
        - Exception: If an unexpected error occurs during initialization.
        """
        try:
            # Set the local directory for storing packages; default is "repository" if not provided.
            self.PACKAGE_DATA_PATH = package_data_path or "repository"
            # Create the directory if it doesn’t already exist.
            os.makedirs(self.PACKAGE_DATA_PATH, exist_ok=True)

            # Check if the repository URL is provided; raise an error if missing.
            if repo_url is None:
                error("REPO_URL", "You need to enter a repo URL for the package manager to work.")
            else:
                self.REPO_URL = repo_url  # Assign the provided URL to an instance variable.

            # Set the allowed file extensions for packages (e.g., .tar.gz, .tar).
            self.ALLOWED_EXTENSIONS = {'tar.gz', 'tar'}

        except Exception as e:
            # Catch any unexpected exceptions and display an error message.
            error("Unknown Exception", e)

    def allowed_file(self, filename: str) -> bool:
        """
        Checks if the provided file has an allowed extension.

        Parameters:
        - filename (str): The name of the file to check.

        Returns:
        - bool: True if the file has an allowed extension, False otherwise.
        """
        # Verify that the filename has an extension and that it’s in the allowed set.
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS
