
from .core import Core
from .downloader import Downloader
from .unpacker import Unpacker
from .metadata import MetadataManager
from .lister import Lister

class Tsukumo(Core, Downloader, Unpacker, MetadataManager, Lister):
    """
    Tsukumo is a package manager that handles downloading, unpacking, 
    installing, and managing packages and their dependencies.

    This class combines functionality from Core, Downloader, Unpacker, 
    MetadataManager, and Lister to provide a comprehensive solution 
    for managing packages in a local repository.
    """
    
    def __init__(self, repo_url: str | None = None, package_data_path: str | None = None) -> None:
        Core.__init__(self, repo_url, package_data_path)
