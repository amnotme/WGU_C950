import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def _str(self):
        return f"({self.x}, {self.y})"


def _distance_formula(point: Point, current_point: Point) -> int:
    return math.sqrt(((point.x - current_point.x)**2) + ((point.y - current_point.y)**2))

def _create_point(x: int, y: int) -> Point:
    return Point(x, y)

def _advance(current_point: Point, x_forward: int, y_forward: int) -> Point:
    return _create_point(current_point.x + x_forward, current_point.y + y_forward)

def _back(current_point: Point, x_y_back: int) -> Point:
    return _create_point(current_point.x - x_y_back, current_point.y - x_y_back)

def main():

    x_p = int(input())
    y_p = int(input())
    point = Point(x_p, y_p)


    moves_x = int(input())
    moves_y = int(input())
    moves_b = int(input())

    current_point = _create_point(0, 0)
    original_distance = _distance_formula(point, current_point)

    counter = 0

    running = True

    while running:
        counter += 1

        old_point = current_point
        if counter % 3 == 0:
            current_point = _advance(current_point, moves_x, moves_y)
            current_point = _back(current_point, moves_b)
        else:
            current_point = _advance(current_point, moves_x, moves_y)


        distance = _distance_formula(point, current_point)

        if (original_distance >= distance and distance < 1):
            original_distance = distance
            running = False
            old_point = current_point

        elif (original_distance >= distance):
            original_distance = distance

        else:
            running = False
            counter -= 1




    print(f"Point P: ({point.x},{point.y})")
    print(f"Arrival point: ({old_point.x},{old_point.y})")
    print(f"Distance between P and arrival: {original_distance:.6f}")
    print(f"Number of iterations: {counter}")


main()
