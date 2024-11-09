
import os

class Lister:
    """
    A class responsible for listing all installed packages in the local package directory.
    """

    def list_installed_packages(self) -> None:
        """
        Lists all packages currently installed in the specified local storage directory.
        
        This method retrieves the contents of the directory defined by `self.PACKAGE_DATA_PATH`, 
        which is assumed to be set elsewhere in the code, and prints each package name.
        """
        
        # Retrieve all items in the local package storage directory.
        try:
            installed_packages = os.listdir(self.PACKAGE_DATA_PATH)
            
            # Print the header for the list of installed packages.
            print("Installed packages:")
            
            # Loop through and print each package found in the directory.
            for package in installed_packages:
                print(f"  - {package}")
        
        except FileNotFoundError:
            # Error message if the directory doesn't exist.
            print("Package directory not found. Please check the PACKAGE_DATA_PATH.")
        except Exception as e:
            # General exception handling for other unforeseen errors.
            print(f"An error occurred while listing packages: {e}")
