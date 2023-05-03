from typing import Any, List, Union

from constants import (AT_HUB_TEXT, DISTANCES_COLUMNS_END,
                       DISTANCES_COLUMNS_START, DISTANCES_DATA_SHEET,
                       DISTANCES_ROWS_END, DISTANCES_ROWS_START,
                       HUBS_COLUMNS_END, HUBS_COLUMNS_START, HUBS_ROWS_END,
                       HUBS_ROWS_START)
from pandas import DataFrame

from models.hub import Hub
from models.package import Package
from src.graph import Graph
from src.parser import Parser


class Loader:

    @staticmethod
    def load_graph_distances(graph: Graph, distances_parser: Parser, hubs: List[Hub]) -> Graph:
        distances_dataframes: DataFrame = distances_parser.get_range_of_cells(
            DISTANCES_DATA_SHEET,
            start_row=DISTANCES_ROWS_START,
            end_row=DISTANCES_ROWS_END,
            start_col=DISTANCES_COLUMNS_START,
            end_col=DISTANCES_COLUMNS_END,
            filler=''
        )

        df_row_index: int = 0
        for df_row in distances_dataframes.itertuples():
            for df_column_index in range(1, df_row_index + 2):
                graph.add_edge(hub1=hubs[df_row_index], hub2=hubs[df_column_index -1], distance=df_row[df_column_index])
            df_row_index += 1
        return graph


    @staticmethod
    def load_graph_hubs(graph: Graph, hubs: List[Hub]) -> Graph:
        for hub in hubs:
            graph.add_node(hub)

        return graph

    @staticmethod
    def load_hubs(hubs_parser: Parser) -> List[Hub]:
        hubs: List[Hub] = []

        hubs_dataframes: DataFrame = hubs_parser.get_range_of_cells(
            DISTANCES_DATA_SHEET,
            start_row=HUBS_ROWS_START,
            end_row=HUBS_ROWS_END,
            start_col=HUBS_COLUMNS_START,
            end_col=HUBS_COLUMNS_END,
        )

        for hub in hubs_dataframes.itertuples():
            hubs.append(
                Hub(
                    hub_name=hubs_parser.sanitize_hub_names(cell=hub[1], cell_index=1),
                    address=hubs_parser.sanitize_hub_names(cell=hub[2], cell_index=1),
                    zipcode=int(hubs_parser.sanitize_hub_names(cell=hub[2], cell_index=2))
                )
            )
        return hubs

    @staticmethod
    def load_packages(packages_parser: Parser) -> List[Package]:

        packages: List[Package] = []

        packages_dataframe: DataFrame = packages_parser.get_cells(
            sheet_name='packages',
            filler=''
        )

        for package in packages_dataframe.itertuples():
            packages.append(
                Package(
                    package_id=package.package_id,
                    address=package.address,
                    city=package.city,
                    state=package.state,
                    zipcode=package.zip,
                    delivery_time=packages_parser.validate_delivery_time(package.deadline),
                    weight=package.mass,
                    status=AT_HUB_TEXT,
                    notes=package.notes
                )
            )

        return packages