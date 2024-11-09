<div align="center"><img src="https://giffiles.alphacoders.com/222/222022.gif"></div>
<h1 align="center">Tsukumo Client Package Manager</h1>

The **Tsukumo Client Package Manager** is a lightweight client for managing and installing packages from a remote repository. It allows you to download, install, and manage dependencies of packages, all while interacting with a remote server-side package manager (which is separate from this client).

This client can be used to interact with a package repository and install packages locally. It includes the ability to check installed packages, download packages, unpack them, and install any dependencies they may have.

## Features

- **Download Packages**: Downloads `.tar` and `.tar.gz` packages from a remote repository.
- **Install Packages**: Installs packages locally and handles any dependencies.
- **Unpack Packages**: Unpacks downloaded packages and extracts their contents to the local directory.
- **List Installed Packages**: Lists all installed packages in the local repository.
- **Dependency Management**: Automatically installs required dependencies when installing a package.

## Requirements

Before using Tsukumo, ensure that you have the following:

- Python 3.x
- `requests` library (for HTTP requests)
  - Install it via `pip install requests`

## Installation

To get started with Tsukumo, you can install it directly by cloning the repository or by copying the files to your project.

### Clone the repository

***
git clone https://github.com/your-username/tsukumo-client.git
cd tsukumo-client
***

### Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Example

To start using Tsukumo, create an instance of the `Tsukumo` class and pass the `repo_url` (the URL of the remote package server) and the local `package_data_path` (where packages will be stored locally).

```
from Tsukumo import Tsukumo

# Initialize the Tsukumo package manager
pkg_manager = Tsukumo(repo_url="http://localhost:8080/api/packages", package_data_path="repository")

# Install a package
package_name = "rice_pack-1.0.0"
pkg_manager.install_package(package_name)

# List installed packages
pkg_manager.list_installed_packages()
```

### Key Functions

Here are the core methods available in the `Tsukumo` class:

#### 1. `install_package(package_name: str)`

Installs a package from the remote repository. This method also handles the installation of dependencies.

**Example:**

```bash
pkg_manager.install_package("rice_pack-1.0.0")
```

#### 2. `list_installed_packages()`

Lists all the installed packages in the local repository.

**Example:**

```bash
pkg_manager.list_installed_packages()
```

#### 3. `allowed_file(filename: str)`

Checks if a file is a valid package based on its file extension (`.tar.gz` or `.tar`).

**Example:**

```bash
pkg_manager.allowed_file("some_package.tar.gz")
```

#### 4. `download_package(package_name: str)`

Downloads a package from the remote repository to the local `package_data_path`.

**Example:**

```bash
pkg_manager.download_package("rice_pack-1.0.0.tar.gz")
```

#### 5. `unpack_package(package_tar_path: str)`

Unpacks the downloaded package into the local directory.

**Example:**

```bash
pkg_manager.unpack_package("path/to/rice_pack-1.0.0.tar.gz")
```

#### 6. `get_metadata_from_tar(package_tar_path: str)`

Extracts metadata (such as dependencies) from the downloaded `.tar` package.

**Example:**

```bash
metadata = pkg_manager.get_metadata_from_tar("path/to/rice_pack-1.0.0.tar.gz")
print(metadata)
```

#### 7. `install_dependencies(package_name: str)`

Installs any dependencies listed in the `metadata.json` file inside the package.

**Example:**

```bash
pkg_manager.install_dependencies("rice_pack-1.0.0")
```

## Configuration

### Local Package Storage

The default path for storing packages locally is the `repository` folder, but you can customize this when initializing the `Tsukumo` class by passing a custom `package_data_path` argument.

```bash
pkg_manager = Tsukumo(repo_url="http://localhost:8080/api/packages", package_data_path="my_custom_path")
```

### Remote Repository URL

The `repo_url` parameter is required to specify the base URL for the remote package repository. This URL should point to the server-side package manager.

```bash
pkg_manager = Tsukumo(repo_url="http://localhost:8080/api/packages")
```

## File Extensions

Tsukumo currently supports the following package file extensions:

- `.tar.gz`
- `.tar`

## Error Handling

If there are any issues during operations, such as missing repository URLs or invalid file formats, Tsukumo will raise informative error messages. You can define your custom error handler by updating the `error` function located in the `Util.py` file.

### Example Error Handling:

```bash
def error(message, title):
    print("\n\n")
    print(f" _____________")
    print(f" |")
    print(f" | Error: {title}")
    print(f" |")
    print(f" | Issue: {message}")
    print(f" |____________\n\n")
```

## Troubleshooting

- **Remote Repository Not Found**: Ensure that the repository URL is correct and accessible.
- **Package Download Failed**: Check if the package file exists in the repository and ensure that the file extension is supported.
- **Dependency Installation Fails**: Verify that the `metadata.json` file inside the package lists all dependencies correctly.

## License

This package is licensed under the MIT License. See `LICENSE` for more information.
