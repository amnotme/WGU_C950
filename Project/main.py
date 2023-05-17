from dispatch.dispatcher import Dispatcher
from datetime import time
from constants import DELAYED_START_TIME, MM_USER_MENU


class MainMenu:

    finished: bool
    dispatcher: Dispatcher

    def __init__(self):
        self.finished = False
        self.dispatcher = Dispatcher()

    def _option_selection(self) -> str:
        print("Please make a selection from the menu:")
        for selection in MM_USER_MENU:
            print(selection)
        selection: str = input("Enter 1-3 or Q to exit")
        return selection


    def _option_one(self):
        print("Running full end of day report:")
        self.dispatcher.load_truck_with_packages(truck_id=1)
        self.dispatcher.load_truck_with_packages(truck_id=2)

        driver_one_time: time = self.dispatcher.begin_delivery(
            truck=self.dispatcher.trucks[0]
        )
        driver_two_time: time = self.dispatcher.begin_delivery(
            truck=self.dispatcher.trucks[1]
        )

        if driver_two_time > driver_one_time:
            self.dispatcher.load_truck_with_packages(truck_id=3)
            self.dispatcher.begin_delivery(
                truck=self.dispatcher.trucks[2],
                begin_time=max(driver_one_time, DELAYED_START_TIME)
            )
        else:
            self.dispatcher.load_truck_with_packages(truck_id=3)
            self.dispatcher.begin_delivery(
                truck=self.dispatcher.trucks[2],
                begin_time=max(driver_two_time, DELAYED_START_TIME)
            )

        self.dispatcher.end_delivery_report()

    def interface(self):

        while not self.finished:
            selection = self._option_selection()

            if selection == '1':
                self._option_one()
            if selection == 'Q':
                print("Exiting dispatch tracking")
                self.finished = True


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


