from typing import List
import csv

from constants import (
    AT_HUB_TEXT,
    DISTANCES_CSV_FILE, PACKAGES_CSV_FILE
)

from model.hub import Hub
from model.package import Package
from src.graph import Graph
from src.parser import Parser


class Loader:
    """
    Loads data from a spreadsheet into objects.
    """

    @staticmethod
    def load_graph_distances_from_csv(
            graph: Graph,
            hubs: List[Hub]
    ) -> Graph:
        """
        Loads the distances between hubs from a spreadsheet into a graph.

        Args:
            graph: The graph to load the distances into.
            hubs: The list of hubs to use to map the row and column indices
            to hub objects.

        Returns:
            The graph with the distances loaded.
        """
        with open(DISTANCES_CSV_FILE, 'r') as csv_file:
            distances_data = csv.reader(csv_file)

            df_row_index: int = 0
            for idx, df_row in enumerate(distances_data):
                if idx < 1:
                    continue
                else:
                    for df_column_index in range(2, df_row_index + 2):
                        graph.add_edge(
                            hub1=hubs[df_row_index],
                            hub2=hubs[df_column_index - 2],
                            distance=float(df_row[df_column_index])
                        )

                    df_row_index += 1
        return graph

    @staticmethod
    def load_graph_hubs(graph: Graph, hubs: List[Hub]) -> Graph:
        """
        Loads the hubs from a spreadsheet into a graph.

        Args:
            graph: The graph to load the hubs into.
            hubs: The list of hubs to use to map the row and column indices
                to hub objects.

        Returns:
            The graph with the hubs loaded.
        """
        for hub in hubs:
            graph.add_node(hub)

        return graph

    @staticmethod
    def load_hubs_from_csv(hubs_parser: Parser) -> List[Hub]:
        """
        Loads the hubs from a spreadsheet.

        Args:
            hubs_parser: The parser to use to parse the spreadsheet.

        Returns:
            The list of hubs loaded from the spreadsheet.
        """

        hubs: List[Hub] = []

        with open(DISTANCES_CSV_FILE, 'r') as csv_file:
            hubs_data = csv.reader(csv_file)

            for idx, hub in enumerate(hubs_data):
                if idx == 0:
                    continue
                else:
                    h: Hub = Hub(
                        hub_name=hubs_parser.sanitize_hub_names(
                            cell=hub[0], cell_index=1
                        ),
                        address=hubs_parser.sanitize_hub_names(
                            cell=hub[1], cell_index=1
                        ),
                        zipcode=int(
                            hubs_parser.sanitize_hub_names(
                                cell=hub[1], cell_index=2
                            )
                        )
                    )
                    hubs.append(h)
            return hubs

    @staticmethod
    def load_packages_from_csv(packages_parser: Parser) -> List[Package]:
        """
        Loads the packages from a spreadsheet.

        Args:
            packages_parser: The parser to use to parse the spreadsheet.

        Returns:
            The list of packages loaded from the spreadsheet.
        """
        packages: List[Package] = []
        with open(PACKAGES_CSV_FILE, 'r') as csv_file:
            packages_data = csv.reader(csv_file)

            for idx, package in enumerate(packages_data):
                if idx == 0:
                    continue
                else:
                    packages.append(
                        Package(
                            package_id=int(package[0]),
                            address=package[1],
                            city=package[2],
                            state=package[3],
                            zipcode=int(package[4]),
                            delivery_time=(
                                packages_parser.validate_delivery_time_from_cell(
                                    cell=package[5]
                                )
                            ),
                            weight=int(package[6]),
                            status=AT_HUB_TEXT,
                            notes=package[7] if package[7] else "",
                        )
                    )

        return packages
