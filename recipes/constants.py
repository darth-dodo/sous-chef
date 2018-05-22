SOUPS = 'SO'
DESSERTS = 'DR'
APPETIZERS = 'AZ'
MAINS = 'MN'
SIDES = 'SD'
CONDIMENTS = 'CD'
SNACKS = 'SC'
BEVERAGES = 'BG'

CATEGORIES = (
    (SOUPS, 'Soups'),
    (DESSERTS, 'Desserts'),
    (APPETIZERS, 'Appetizers'),
    (MAINS, 'Main Course'),
    (SIDES, 'Side Dishes'),
    (CONDIMENTS, 'Condiments'),
    (SNACKS, 'Snacks'),
    (BEVERAGES, 'Beverages'),
)


EASY = '1'
MEDIUM = '2'
HARD = '3'

RECIPE_DIFFICULTY = (
    (EASY, 'Easy'),
    (MEDIUM, 'Medium'),
    (HARD, 'Hard')
)

LOCALLY = 'LO'
ONLINE = 'ON'
EXOTIC = 'EX'

INGREDIENT_AVAILABILITY = (
    (LOCALLY, 'Locally'),
    (ONLINE, 'Online'),
    (EXOTIC, 'Exotic')
)