import os
import tarfile

class Unpacker:
    """
    A class responsible for unpacking package files into a specified directory.
    """

    def unpack_package(self, package_tar_path: str) -> None:
        """
        Unpacks a .tar or .tar.gz package file to the designated directory.

        Parameters:
        - package_tar_path (str): The file path of the package's tar archive.

        This method extracts the contents of the tar archive into `self.PACKAGE_DATA_PATH`.
        It also checks for the presence of a `rice_pack` folder within the unpacked contents 
        and lists its files if it exists.
        """
        try:
            # Open the tar file in read mode and extract all contents.
            with tarfile.open(package_tar_path, "r") as tar:
                # Extract all files to the package data directory
                tar.extractall(self.PACKAGE_DATA_PATH)
                print(f"Unpacked {package_tar_path} successfully.")

                # List the contents of the package data directory for confirmation
                extracted_files = os.listdir(self.PACKAGE_DATA_PATH)
                print(f"Contents of {self.PACKAGE_DATA_PATH}: {extracted_files}")
                
                # Check for the 'rice_pack' subfolder and display its contents if present
                rice_pack_folder = os.path.join(self.PACKAGE_DATA_PATH, 'rice_pack')
                if os.path.exists(rice_pack_folder):
                    print(f"Extracted rice_pack folder contents: {os.listdir(rice_pack_folder)}")
                else:
                    print("No rice_pack folder found after extraction.")
                    
        except Exception as e:
            # Handle any errors during unpacking and display a message
            print(f"Error unpacking {package_tar_path}: {e}")

    def unpack_package_to_location(self, package_tar_path: str, destination_path: str) -> None:
        """
        Unpacks a .tar or .tar.gz package to a specific directory.
        """
        try:
            with tarfile.open(package_tar_path, "r") as tar:
                tar.extractall(destination_path)
                print(f"Unpacked {package_tar_path} successfully to {destination_path}.")
                extracted_files = os.listdir(destination_path)
                print(f"Contents of {destination_path}: {extracted_files}")
        except Exception as e:
            print(f"Error unpacking {package_tar_path} to {destination_path}: {e}")
