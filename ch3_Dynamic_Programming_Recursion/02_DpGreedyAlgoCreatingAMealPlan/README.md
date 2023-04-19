# 3.8 Greedy Algorithm: Creating A Meal Plan

# Specification

In this lab you will write a greedy algorithm that creates a daily food plan according to some restrictions:

- The total calories must not exceed 2000.
- The plan must come as close as possible to matching a target amount of calories from one of the three macronutrients: protein, carbohydrates, or fat.

For example, the user might choose to set a goal of 30% protein for the daily meal plan. Your program will attempt to produce a meal plan that has a total of 2000 calories, with 30% of those calories coming from protein.

# Supporting classes

### `Food` class

A `Food` object represents a single serving of a food item that can be part of a meal plan.

Data members:

- `name` - a name to identify the food, for output display
- `protein` - grams of protein in one serving
- `carbs` - grams of carbohydrates in one serving
- `fat` - grams of fat in one serving
- `calories` - total calories in one serving (note that calories come from more than just protein, carbs and fat, so this number is greater than the sum of the three nutrients used in this lab)
- `fraction` - the fraction of a serving to be used in a meal plan (between 0.0 and 1.0, inclusive)
- `protein_calories`
- `carbs_calories`
- `fat_calories`

Methods:

- `set_fraction(p)` - assigns the `fraction` data member with `p` (between 0.0 and 1.0 inclusive), and calculates new values for `calories`, `protein_calories`, `carbs_calories` and `fat_calories` accordingly.
- `__str__()` - returns a string representing the food and nutrient contents.

### `MealPlan` class

A `MealPlan` object is the collection of `Food` objects selected for a single day's meal plan.

Data members:

- `foods` - the list of `Food` objects that are part of the meal plan
- `total_calories` - total calories of the meal plan
- `total_protein_calories` - total calories from protein in the meal plan
- `total_carbs_calories` - total calories from carbohydrates in the meal plan
- `total_fat_calories` - total calories from fat in the meal plan

Provided methods:

- `percent_nutrient(nutrient)` - returns the current percent value (in range [0.0, 1.0]) of the given nutrient in the current meal plan, by calories.
- `percent_nutrient_with_food(food, nutrient)` - returns the total percent (in range [0.0, 1.0]) of the given nutrient *if* the given food were added. The food item is *not* added to the the meal plan by the method; the method is just for speculation only.
- `calories_with_food(food)` - returns the total calories the meal plan *would have*, if the given food were added. The food item is *not* added to the meal plan by this method; the method is just for speculation only.
- `__str__()` - returns a string listing the foods selected for the meal plan along with summary information about calorie content.

Methods for you to complete:

- `fraction_to_fit_calorie_limit(food, calorie_limit)` - returns the fraction (in the range [0.0, 1.0]) of a serving of the specified food item that is needed to make the entire meal plan exactly match the given calorie limit. If an entire serving can fit and the meal plan will be below the calorie limit, then the method returns 1.0. The food item is *not* added to the meal plan by this method; the method is just for speculation only.
- `fraction_to_fit_nutrient_goal(food, nutrient, goal)` - returns the fraction (in the range [0.0, 1.0]) of a serving of the specified food item that is needed to make the entire meal plan exactly match the given nutrient composition goal. If an entire serving can fit and the meal plan will be below the nutrient composition goal, then the method returns 1.0. The food item is *not* added to the meal plan by this method; the method is just for speculation only.
- `meets_calorie_limit(calorie_limit, threshold)` - returns `True` if the current meal plan has a total calorie content that falls within the given threshold of the specified calorie limit, otherwise returns `False`.
- `meets_nutrient_goal(nutrient, goal, threshold)` - returns `True` if the current meal plan has a total percent nutrient composition (by calories) that falls within the given threshold of the specified composition goal, otherwise returns `False`.

Be sure to read the description of each method carefully, and test them individually with various values to be sure they work correctly. The main algorithm will depend on these methods working properly!

## The main program

When the program is executed, the user is prompted for some information:

- the name of the food data file (a string entered from an input prompt)
- the nutrient (protein, carbs or fat) that the user wishes to set a goal for (selected from a menu)
- the goal amount (percent of calories) the selected nutrient must compose of the meal plan (a float value entered from an input prompt)

Example: selecting a meal plan with 30% protein from the `nutrients_1000.txt` data file:

```
Enter name of food data file: nutrients_1000.txt

        1 - Set maximum protein
        2 - Set maximum carbs
        3 - Set maximum fat
        4 - Exit program

Enter choice (1-4): 1
What percentage of calories from protein is the goal? 30

```

The program must be able to handle errors when entering the nutrient and nutrient goal information; when the user enters a value that is of the wrong type (like a string instead of an integer) or a value that is out of range, then an error message is displayed and the user is prompted again.

Once the information has been input from the user, the meal plan is created. You are to complete the function `create_meal_plan()`, which is called from the main program. The basic algorithm for building the meal plan is:

- Sort the list of available foods according to the *heuristic* described below.
- For each food item in the list:
    - add the food if:
        - it is not "empty" (too few calories or too few of the target nutrient), and
        - an entire serving can be added, or
        - an entire serving can't be added, but there is a fraction of a serving that doesn't violate either constraint (total calories or percent nutrient)
    - if the food item was added, check if the meal plan meets both the target calorie content and the percent nutrient content (within acceptable thresholds, as described below)
        - if the meal plan meets the requirements, exit the loop; otherwise continue to the next food item
- display the final meal plan

## Details

- A meal plan matches the calorie limit if total calories fall in the range [1999.9, 2000.1].
- A meal plan matches the nutrient goal if the total percent calories of the target nutrient comes within 0.1%. Ex. If the goal is 30% protein, a protein calorie content in the range [29.9%, 30.1%] is successful.
- Only allow fractional servings greater than or equal to 0.05.
- Only include `Food` objects with a calorie content greater than or equal to 0.1.
- Only include `Food` objects that are greater than or equal to 0.1% calories by the selected nutrient. Ex. If the selected nutrient is protein, ignore `Food` items where `protein_calories / calories < 0.001`.

### Greedy algorithm heuristic

Iterate through the food item list in *descending* order of the user's selected nutrient percent composition. Ex. for setting maximum protein content, sort the `Food` object list by decreasing `protein_calories`.

### Food data file

Food item information is in a text file with one food item specified per line. A food item line is formatted as follows:

- A text string representing the name of the food item, along with serving size information, followed by a colon (":");
- A float value representing the amount of protein in a single serving, in grams, followed by a comma (",");
- A float value representing the amount of carbohydrates in a single serving, in grams, followed by a comma (",");
- A float value representing the amount of fat in a single serving, in grams, followed by a comma (",");
- A float value representing the total calories in a single serving.

```
<Food Info>: <grams_protein>, <grams_carbs>, <grams_fat>, <total_calories>

```

The food items do not appear in any particular order. You must complete the `load_food_data()` function to parse the data file line-by-line, and return a list of `Food` objects created from the parsed data.

# Examples
1. 30% protein

```
Enter name of food data file: nutrients_1000.txt

        1 - Set maximum protein
        2 - Set maximum carbs
        3 - Set maximum fat
        4 - Exit program

Enter choice (1-4): 1
What percentage of calories from protein is the goal? 30
1: [1.0000] Beef, brisket, flat half, separable lean and fat, trimmed to 1/8" fat, choice, raw (1 steak / 434.0 grams) (P=78.6408,C=0.5208,F=96.131,E=1206.52)
2: [0.3207] Turkey, retail parts, drumstick, meat and skin, cooked, roasted (1 drumstick / 275.0 grams) (P=77.5775,C=0.0,F=25.7675,E=173.7324451060661)
3: [1.0000] Fast foods, submarine sandwich, turkey, roast beef and ham on white bread with lettuce and tomato (12 inch sub / 413.0 grams) (P=44.0258,C=84.0868,F=9.9946,E=602.98)
4: [0.0502] Cheese, mozzarella, nonfat (1 cup, shredded / 113.0 grams) (P=35.821,C=3.955,F=0.0,E=7.994115976331346)
5: [0.1840] Gravy, au jus, canned (1 can / 298.0 grams) (P=3.576,C=7.45,F=0.596,E=8.773438917602562)
Total Calories: 2000.0
        Protein: 0.30
        Carbs: 0.17
        Fat: 0.52
```

2. 10% fat

```
Enter name of food data file: nutrients_1000.txt

        1 - Set maximum protein
        2 - Set maximum carbs
        3 - Set maximum fat
        4 - Exit program

Enter choice (1-4): 3
What percentage of calories from fat is the goal? 10
1: [1.0000] Bread stuffing, bread, dry mix (1 package (6 oz) / 170.0 grams) (P=18.7,C=129.54,F=5.78,E=656.2)
2: [0.3926] Soup, beef and mushroom, low sodium, chunk style (1 cup / 251.0 grams) (P=10.793,C=24.0458,F=5.773,E=68.00000000000001)
3: [1.0000] Teff, uncooked (1 cup / 193.0 grams) (P=25.669,C=141.1409,F=4.5934,E=708.31)
4: [1.0000] Cookies, oatmeal, prepared from recipe, with raisins (1 oz / 28.35 grams) (P=1.8428,C=19.3914,F=4.5927,E=123.3225)
5: [0.0881] Puddings, banana, dry mix, regular, with added oil (1 package (3.12 oz) / 88.0 grams) (P=0.0,C=77.792,F=4.4,E=29.998642857144432)
6: [1.0000] Corn flour, masa, enriched, white (1 cup / 114.0 grams) (P=9.6444,C=87.3126,F=4.2066,E=413.82)
7: [0.1077] Onions, young green, tops only (1 stalk / 12.0 grams) (P=0.1164,C=0.6888,F=0.0564,E=0.3488571428556497)
Total Calories: 2000.0
        Protein: 0.12
        Carbs: 0.79
        Fat: 0.10
```
