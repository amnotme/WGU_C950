from src.parser import Parser
from typing import List, Union
from models.truck import Truck
from models.hub import Hub
from models.package import (
    Package
)
from src.data_loader import Loader
from constants import (
    DISTANCES_DATA_FILE,
    PACKAGES_DATA_FILE
)



hubs_parser: Parser = Parser(file_path=DISTANCES_DATA_FILE)
hubs: List[Hub] = Loader.load_hubs(hubs_parser=hubs_parser)


for hub in hubs:
    print(hub)


packages_parser: Parser = Parser(file_path=PACKAGES_DATA_FILE)
packages: List[Package] = Loader.load_packages(packages_parser=packages_parser)


for package in packages:
    print(package)

