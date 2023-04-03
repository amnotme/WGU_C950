import sys, operator, random
from nutrition import Food, MealPlan
# Constants to be used by the greedy algorithm.
NUTRIENT_THRESHOLD = 0.001
FRACTION_THRESHOLD = 0.05
CALORIE_THRESHOLD = 0.1
MAX_CALORIES = 2000


def load_nutrient_data(filename):
    # Open file, read food items one line at a time,
    # create Food objects and append them to a list.
    # Return the list once the entire file is processed.

    foods_list: list = []
    try:
        with open(filename, 'r') as file:
            reader = file.read()
            for row in reader.strip().split('\n'):
                data = row.split(':')
                name = data[0]

                raw_values = data[1].split(',')
                sanitized_values = [ float(val.strip()) for val in raw_values ]
                if len(sanitized_values) < 4:
                    raise Exception("There are not enough values")
                else:
                    food = Food(
                        name=name,
                        protein=sanitized_values[0],
                        fat=sanitized_values[1],
                        carbs=sanitized_values[2],
                        calories=sanitized_values[3]
                        )
                    foods_list.append(food)
    except Exception as ex:
        print(f"{ex}")
    return foods_list

def sort_food_list(foods, nutrient):
    # Sort the food list based on the percent-by-calories of the
    # given nutrient ('protein', 'carbs' or 'fat')
    # The list is sorted in-place; nothing is returned.
    foods.sort(key = operator.attrgetter(nutrient), reverse = True)

def _over_calorie_fraction(plan, calorie_fraction, goal, food, nutrient):
    if plan.percent_nutrient_with_food(food, nutrient) <= goal + NUTRIENT_THRESHOLD:
        plan.add_food(food)
    else:
        nutrient_fraction = plan.fraction_to_fit_nutrient_goal(food,nutrient, goal)
        if nutrient_fraction > FRACTION_THRESHOLD:
            food.set_fraction(nutrient_fraction)
            plan.add_food(food)


def _under_calorie_fraction(plan, calorie_fraction, goal, food, nutrient):
    if calorie_fraction > CALORIE_THRESHOLD:
        nutrient_fraction = plan.fraction_to_fit_nutrient_goal(food, nutrient, goal)
        if nutrient_fraction > FRACTION_THRESHOLD:
            food.set_fraction(min(calorie_fraction, nutrient_fraction))
            plan.add_food(food)


def create_meal_plan(foods, nutrient, goal):
    # A greedy algorithm to create a meal plan that has MAX_CALORIES
    # calories and the goal amount of the nutrient (e.g. 30% protein)
    plan = MealPlan()
    sort_food_list(foods, nutrient)

    for food in foods:
        if food.calories == 0 and getattr(food, nutrient) == 0: continue

        # Calculate the calorie_fraction of food allowed to fit the calorie limit;
        calorie_fraction = plan.fraction_to_fit_calories_limit(food, MAX_CALORIES)

        if calorie_fraction >= 1.0:
            _over_calorie_fraction(plan, calorie_fraction, goal, food, nutrient)
        else:
            _under_calorie_fraction(plan, calorie_fraction, goal, food, nutrient)

        if plan.meets_calorie_limit(MAX_CALORIES, CALORIE_THRESHOLD) and plan.meets_nutrient_goal(nutrient, goal, NUTRIENT_THRESHOLD):
            break

    return plan


def _get_option(valid_options):
    nutrient = ''
    option: int = 0
    while option not in ELIGIBLE_OPTIONS:
        text = ""
        print_menu()
        option = int(input())
        if option not in ELIGIBLE_OPTIONS:
            text = "Invalid choice! Enter an integer from 1-4!"
        print(f"Enter choice (1-4): {text}")
    valid_options[option] = True

def print_menu():
    print()
    print("\t1 - Set maximum protein")
    print("\t2 - Set maximum carbs")
    print("\t3 - Set maximum fat")
    print("\t4 - Exit program")
    print()

if __name__ == "__main__":
    # 1. Load the food data from the file (change this to a user
    # prompt for the filename)
    filename = input("Enter name of food data file:")
    foods = load_nutrient_data(filename)

    MAX_P: int = 1
    MAX_C: int = 2
    MAX_F: int = 3
    EXIT:  int = 4

    ELIGIBLE_OPTIONS = [
        MAX_P, MAX_C, MAX_F, EXIT
    ]


    valid_options: dict = {
        MAX_P: False,
        MAX_C: False,
        MAX_F: False,
        EXIT: False,
    }

    options_map: dict = {
        MAX_P: 'protein',
        MAX_C: 'carbs',
        MAX_F: 'fat',
    }
    # 2. Display menu and get user's choice. Repeat menu until a
    # valid choice is entered by the user (1-4, inclusive).
    try:
        _get_option(valid_options)
    except Exception as ex:
        print("Enter choice (1-4): Invalid choice! Enter an integer from 1-4!")
        _get_option(valid_options)

    # 3. Prompt user for goal nutrient percent value. Repeat prompt
    # until a valid choice is entered by the user (0-100, inclusive)

    if valid_options[EXIT]:
        exit()
    else:
        nutrient: str = '';
        valid_options.pop(4)
        for key, option in valid_options.items():
            if option:
                nutrient = options_map[key];
    try:
        goal = int(input("What percentage of calories from protein is the goal? "))
        while goal < 0 or goal > 100:
            goal = int(input("What percentage of calories from protein is the goal? "))
    except Exception as ex:
        print(f"{ex}. Please be sure to select a percentage between 0-100")

    # 4. Run greedy algorithm to create the meal plan.
    plan = create_meal_plan(foods, nutrient, goal)

    # 5. Display plan.
    print(plan)
