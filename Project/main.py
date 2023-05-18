from datetime import datetime, time
from typing import Optional

from constants import (
    DEFAULT_DELIVERY_END_TIME,
    DELAYED_START_TIME,
    MM_USER_MENU
)
from dispatch.dispatcher import Dispatcher


class MainMenu:
    finished: bool
    dispatcher: Optional[Dispatcher]

    def __init__(self):
        self.finished = False
        self.dispatcher = None

    def _option_selection(self) -> str:

        self.dispatcher = Dispatcher()
        print("\n--------------------------------------")
        print("Please make a selection from the menu:")
        print("--------------------------------------")
        for selection in MM_USER_MENU:
            print(selection)
        selection: str = (input("Enter 1-3 or Q to exit: \n")).lower()
        return selection

    def _option_one(self):

        self._start_dispatcher()
        self.dispatcher.end_delivery_report()

    def _option_two(self):

        print("Plesase enter a time between 08:00 - 17:00 to get a detailed scheduled of \n"
              "all packages at that moment. Please use 24-hour format.")
        parsed_time: Optional[time] = None

        while parsed_time is None:
            parsed_time = self._time_parser(input())
        self._start_dispatcher(new_delivery_stop_time=parsed_time)
        self.dispatcher.end_delivery_report(end_time=parsed_time)

    def _option_three(self):
        pass

    def _start_dispatcher(
            self,
            new_delivery_stop_time: Optional[time] = None
    ):
        end_time: time = (
            new_delivery_stop_time
            if new_delivery_stop_time
            else DEFAULT_DELIVERY_END_TIME
        )

        self.dispatcher.load_truck_with_packages(truck_id=1)
        self.dispatcher.load_truck_with_packages(truck_id=2)

        driver_one_time: time = self.dispatcher.begin_delivery(
            truck=self.dispatcher.trucks[0], end_time=end_time
        )
        driver_two_time: time = self.dispatcher.begin_delivery(
            truck=self.dispatcher.trucks[1], end_time=end_time
        )

        start_time: time = max(driver_one_time, driver_two_time, DELAYED_START_TIME)
        time_remaining: float = self.dispatcher.calculate_remaining_time(
            start_time=start_time,
            end_time=end_time
        )

        if time_remaining > 0:
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

        while not self.finished:
            selection = self._option_selection()
            if selection == '1':
                print("Running full end of day report:")
                self._option_one()
            elif selection == '2':
                print("Running timed report:")
                self._option_two()
            elif selection == '3':
                self._option_three()
            elif selection == 'q':
                print("Exiting dispatch tracking")
                self.finished = True
            else:
                print("That selection is invalid")


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
