
import os
import requests

class Downloader:
    """
    A class for downloading packages from a specified repository URL.
    """

    def download_package(self, package_name: str) -> str | None:
        """
        Downloads a package file from the repository URL and saves it locally.

        Parameters:
        - package_name (str): The name of the package file to be downloaded.
        
        Returns:
        - str | None: The path to the downloaded package file if successful, 
                      otherwise None.
        """
        
        # Construct the full URL for the package by appending the package name to the repository URL.
        url = f"{self.REPO_URL}/{package_name}"
        print(f"Downloading {package_name} from {url}...")

        # Make an HTTP GET request to download the package as a stream.
        response = requests.get(url, stream=True)
        
        # Check if the request was successful (HTTP status code 200).
        if response.status_code == 200:
            # Define the local path where the package will be saved.
            package_tar_path = os.path.join(self.PACKAGE_DATA_PATH, package_name)
            
            # Open the local file path in write-binary mode and save the content.
            with open(package_tar_path, "wb") as f:
                f.write(response.content)
            
            print(f"Downloaded {package_name} successfully.")
            return package_tar_path  # Return the path to the downloaded file.
        
        else:
            # If the request failed, print an error message with the status code.
            print(f"Failed to download {package_name}. HTTP Status Code: {response.status_code}")
            return None  # Return None to indicate the download was unsuccessful.
        
    def download_package_to_location(self, package_name: str, destination_path: str) -> str | None:
        """
        Downloads a package to a specific location.
        """
        url = f"{self.REPO_URL}/{package_name}"
        print(f"Downloading {package_name} from {url} to {destination_path}...")
        response = requests.get(url, stream=True)
        
        if response.status_code == 200:
            package_tar_path = os.path.join(destination_path, package_name)
            with open(package_tar_path, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {package_name} successfully to {destination_path}.")
            return package_tar_path
        else:
            print(f"Failed to download {package_name}. HTTP Status Code: {response.status_code}")
            return None
