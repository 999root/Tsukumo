import os
import tarfile
import json

class MetadataManager:
    """
    A class responsible for managing metadata and dependencies for packages.
    """

    def get_metadata_from_tar(self, package_tar_path: str) -> dict | None:
        """
        Extracts the metadata.json file from a given package tar file.

        Parameters:
        - package_tar_path (str): The file path of the package's tar archive.

        Returns:
        - dict | None: A dictionary containing metadata information if found; 
                       None if metadata.json is missing or extraction fails.
        """
        try:
            # Open the tar file for reading
            with tarfile.open(package_tar_path, "r") as tar:
                # Loop through the tar file members to find metadata.json
                for member in tar.getmembers():
                    if member.name == "metadata.json":
                        # Extract and load the metadata as a dictionary
                        file = tar.extractfile(member)
                        metadata = json.load(file)
                        return metadata
            # Return None if metadata.json was not found
            return None
        except Exception as e:
            # Log any errors that occur during extraction
            print(f"Error extracting metadata from {package_tar_path}: {e}")
            return None

    def install_dependencies(self, package_name: str) -> None:
        """
        Installs all dependencies listed in the metadata of the given package.

        Parameters:
        - package_name (str): The name of the package whose dependencies are to be installed.
        
        Assumes that dependencies are specified in the package's metadata.json file.
        """
        # Construct the path to the package tar file
        package_tar_path = os.path.join(self.PACKAGE_DATA_PATH, f"{package_name}.tar")
        # Extract metadata to find dependencies
        metadata = self.get_metadata_from_tar(package_tar_path)
        
        # Check for dependencies in metadata
        if metadata and "dependencies" in metadata:
            dependencies = metadata["dependencies"]
            # Iterate over dependencies and install each one
            for dep_name, dep_version in dependencies.items():
                print(f"Installing dependency: {dep_name} (version {dep_version})")
                # Install each dependency package
                self.install_package(dep_name)

    def install_package(self, package_name: str) -> None:
        """
        Installs a package by downloading, unpacking, and installing its dependencies.

        Parameters:
        - package_name (str): The name of the package to install.
        
        This method checks if the package already exists locally before downloading.
        """
        # Define the path where the package will be installed
        package_path = os.path.join(self.PACKAGE_DATA_PATH, package_name)
        # If the package already exists, print a message and exit
        if os.path.exists(package_path):
            print(f"Package {package_name} is already installed.")
            return
        
        # Attempt to download the package in .tar.gz format
        package_file = f"{package_name}.tar.gz"
        package_tar_path = self.download_package(package_file)
        
        # If .tar.gz download fails, try the .tar format
        if not package_tar_path:
            package_file = f"{package_name}.tar"
            package_tar_path = self.download_package(package_file)
            # Exit if neither format was found
            if not package_tar_path:
                return

        # Unpack the downloaded package and install its dependencies
        self.unpack_package(package_tar_path)
        self.install_dependencies(package_name)

    def install_package_to_location(self, package_name: str, destination_path: str) -> None:
        """
        Installs a package to a specific location (including dependencies).
        """
        package_tar_path = self.download_package(package_name)
        if package_tar_path:
            self.unpack_package_to_location(package_tar_path, destination_path)
            self.install_dependencies_to_location(package_name, destination_path)