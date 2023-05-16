from dispatch.dispatcher import Dispatcher
from datetime import time


if __name__ == "__main__":
    dispatcher = Dispatcher()

    dispatcher.load_truck_with_packages(truck_id=1)
    dispatcher.load_truck_with_packages(truck_id=2)

    driver_one_time = dispatcher.begin_delivery(dispatcher.trucks[0])
    driver_two_time = dispatcher.begin_delivery(dispatcher.trucks[1])


    if driver_two_time > driver_one_time:
        dispatcher.load_truck_with_packages(truck_id=3)
        dispatcher.begin_delivery(dispatcher.trucks[2], begin_time=driver_one_time)
    else:
        dispatcher.load_truck_with_packages(truck_id=3)
        dispatcher.begin_delivery(dispatcher.trucks[2], begin_time=driver_two_time)

    dispatcher.end_delivery_report()

