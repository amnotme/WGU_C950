"""
Leopoldo Hernandez Oliva
WGU Student ID: 002520248

2023-05-18
"""

from datetime import datetime, time
from typing import Optional

from constants import (
    DEFAULT_DELIVERY_END_TIME,
    DELAYED_START_TIME,
    MM_USER_MENU,
    DEFAULT_MAXIMUM_NUMBER_OF_PACKAGES
)
from dispatch.dispatcher import Dispatcher
from utils.color_printer import ColorPrinter as cp


class MainMenu:
    finished: bool
    dispatcher: Optional[Dispatcher]

    def __init__(self):
        self.finished = False
        self.dispatcher = None
        self.printer = cp()

    def _option_selection(self) -> str:
        """
        Displays the menu to the user and prompts for a menu selection.

        Returns:
            str: The user's menu selection.

        """
        self.dispatcher = Dispatcher()
        self.printer.print_color(text="\n--------------------------------------", color_code=cp.CYAN)
        self.printer.print_color(text="Please make a selection from the menu:", color_code=cp.CYAN)
        self.printer.print_color(text="--------------------------------------", color_code=cp.CYAN)

        # Display the menu options

        for selection in MM_USER_MENU:
            self.printer.print_color(text=selection, color_code=cp.GREEN)

        # Prompt the user for a selection
        self.printer.print_color(text="Enter 1-3 or Q to exit: ", color_code=cp.UNDERLINE)
        selection: str = (input()).lower()
        return selection

    def _option_one(self):
        """
        Executes option one: running a full end-of-day report.

        """
        # Start color printing
        self.printer.print_color(text="", color_code=cp.GREEN, terminate_color=False)

        self._start_dispatcher()
        self.dispatcher.end_delivery_report()

        # Reset printer
        self.printer.reset_color()

    def _option_two(self):
        """
        Executes option two: running a timed report for a specific time.

        """
        # Start color printing
        self.printer.print_color(text="", color_code=cp.BLUE, terminate_color=False)

        parsed_time: Optional[time] = None

        print("Please enter a time between 08:00 - 17:00 to get a detailed schedule of \n"
              "all packages at that moment. Please use 24-hour format.")

        while parsed_time is None:
            parsed_time = self._time_parser(input())

        self._start_dispatcher(new_delivery_stop_time=parsed_time)
        self.dispatcher.end_delivery_report(end_time=parsed_time)

        # Reset printer
        self.printer.reset_color()

    def _option_three(self):
        """
        Executes option three: running a package schedule report for a specific time and package.

        """

        # Start color printing
        self.printer.print_color(text="", color_code=cp.PURPLE, terminate_color=False)
        parsed_time: Optional[time] = None
        package_number: Optional[int] = None

        print("Please enter a time between 08:00 - 17:00 to get package schedule.\n"
              "Please use 24-hour format.\n")

        while parsed_time is None:
            parsed_time = self._time_parser(input())

        print(f"Please enter a package number you'd like to track. \n"
              f"Choose between 1 and {DEFAULT_MAXIMUM_NUMBER_OF_PACKAGES}\n")

        while package_number is None:
            package_number = self._package_parser(input())

        self._start_dispatcher(new_delivery_stop_time=parsed_time)
        self.dispatcher.indexed_packages.print_package(package_number)

        # Reset printer
        self.printer.reset_color()

    def _start_dispatcher(
            self,
            new_delivery_stop_time: Optional[time] = None
    ):
        """
        Starts the dispatcher's operations by loading trucks with packages and beginning deliveries.

        Args:
            new_delivery_stop_time (Optional[time]): The new delivery stop time to use, if provided.

        """
        # Set the end time for deliveries based on the provided new_delivery_stop_time or use the default value
        end_time: time = (
            new_delivery_stop_time
            if new_delivery_stop_time
            else DEFAULT_DELIVERY_END_TIME
        )

        # Load packages into trucks 1 and 2
        self.dispatcher.load_truck_with_packages(truck_id=1)
        self.dispatcher.load_truck_with_packages(truck_id=2)

        # Begin delivery for truck 1 and truck 2
        driver_one_time: time = self.dispatcher.begin_delivery(
            truck=self.dispatcher.trucks[0], end_time=end_time
        )
        driver_two_time: time = self.dispatcher.begin_delivery(
            truck=self.dispatcher.trucks[1], end_time=end_time
        )

        # Determine the start time based on the maximum time between driver_one_time, driver_two_time, and DELAYED_START_TIME
        start_time: time = max(driver_one_time, driver_two_time, DELAYED_START_TIME)

        # Calculate the remaining time for deliveries
        time_remaining: float = self.dispatcher.calculate_remaining_time(
            start_time=start_time,
            end_time=end_time
        )

        if time_remaining > 0:
            # Load packages into truck 3 if there is time remaining
            self.dispatcher.load_truck_with_packages(truck_id=3)
            self.dispatcher.begin_delivery(
                truck=self.dispatcher.trucks[2],
                begin_time=start_time,
                end_time=end_time
            )
        else:
            # Adding time to the last truck to keep report uniform.
            self.dispatcher.trucks[2].truck_clock = datetime.combine(
                self.dispatcher.trucks[2].truck_clock.today(),
                end_time
            )

    def _package_parser(self, package_id: str) -> Optional[int]:
        """
        Parses a package ID string and returns the corresponding package number.

        Args:
            package_id (str): The package ID to parse.

        Returns:
            Optional[int]: The package number if parsing is successful, or None if parsing fails.

        """
        package_number: Optional[int] = None

        try:
            # Attempt to convert the package ID to an integer
            package_number = int(package_id)

            # Check if the package number is within the valid range
            if package_number > DEFAULT_MAXIMUM_NUMBER_OF_PACKAGES or package_number < 1:
                print(f"That's not a valid package. \n"
                      f"Please enter a package number between 1-{DEFAULT_MAXIMUM_NUMBER_OF_PACKAGES}")
                package_number = None
        except ValueError as e:
            print(f"You entered {str(e)}. \n"
                  f"Please enter a package number between 1-{DEFAULT_MAXIMUM_NUMBER_OF_PACKAGES}")

        return package_number

    def _time_parser(self, time_to_parse: str) -> Optional[time]:
        """
        Parses a string representation of time and returns a time object.

        Args:
            time_to_parse (str): The time to parse in string format (e.g., "13:00").

        Returns:
            Optional[datetime.time]: A time object representing the parsed time, or None if parsing fails.

        """
        parsed_time: Optional[time] = None

        try:
            if len(time_to_parse) == 5:
                # Split the time string into hours and minutes
                hours, minutes = time_to_parse.split(':')
                hours = int(hours)
                minutes = int(minutes)

                # Check if the parsed hours and minutes are within the valid range
                if hours < 8 or hours > 17 or minutes > 59 or minutes < 0:
                    print("Please enter a time between 08:00 and 17:00.")
                else:
                    # Create a time object using the parsed hours and minutes
                    parsed_time = time(hour=hours, minute=minutes)
            else:
                print("Please enter time using 24-hour format, i.e., 13:00, 08:00")
        except ValueError as e:
            print(f"You entered {str(e)}. Please enter a time between 08:00 and 17:00.")

        return parsed_time

    def interface(self):
        """
        Main interface for the dispatch tracking system.

        Notes:
            The function enters a loop until self.finished becomes True.
            It prompts the user for an option selection and executes the corresponding action.

        """
        while not self.finished:
            # Prompt the user for an option selection
            selection = self._option_selection()

            # Execute the corresponding action based on the selection
            if selection == '1':
                print("Running full end of day report:\n")
                self._option_one()
            elif selection == '2':
                print("Running timed report:\n")
                self._option_two()
            elif selection == '3':
                print("Running single package report:\n")
                self._option_three()
            elif selection == 'q':
                self.printer.print_color(text="Exiting dispatch tracking", color_code=cp.BOLD)
                self.finished = True
            else:
                self.printer.print_color(text="That selection is invalid", color_code=cp.RED)


if __name__ == "__main__":
    """
    This is the main entry point to the program.
    
    As most enterprises with a supply-chain workflow. The workflow is delegated
    to several workgroups that orchestrate product handling, storage / warehousing
    delivering and customer follow-up.
    
    Our Program will handle most aspect of a delivering network including:
    1. Time management.
    2. Package delivery optimaization.
    3. Information loop to dispatch / user via synchronized alerting
    
    We are assuming that at this given date. Our logistics office has accounted
    for 40 items that need to be delivered, by at most, the delivery deadline
    tied to the package.
    
    A Dispatcher, in the background, will have already assembled the requisitioning /
    packaging and has assigned them to delivery routes.
    
    We have at, at most, 2 drivers clocking in at 8 am and ending shift
    at 5 pm or when all items have been delivered.
    
    There are 3 trucks with packages and we must assume that the driver
    finishing their original route first, will return to pick up a second
    truck with loaded items and will, no earlier than 9:05 am, start delivering them.
    """
    menu: MainMenu = MainMenu()

    menu.interface()
