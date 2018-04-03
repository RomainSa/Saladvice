import re
import pickle


# load file line by line
file = 'algo/data/BDD_clean_CR.txt'
column_regex = '^([a-zA-Z]+)=(.*?)$'
column_ingr = 'ingr'
encoding = 'latin-1'

# extract all column names


with open(file, 'r+', encoding=encoding) as f:
    columns = []
    for line in f:
        m = re.search(column_regex, line)
        if m is not None:
            columns.append(m.group(1))
    print(set(columns))


columns = {'prepa', 'avis', 'url', 'titre', 'niveau', 'type', 'recette', 'cout', 'cuiss', 'ingr'}

# extract all ingredients to a list (on recipe per element)
with open(file, 'r+', encoding=encoding) as f:
    writing = False
    ingredients = []
    data = []
    for line in f:
        # search for column
        m = re.search(column_regex, line)
        if m is not None:
            # we found a new column
            column = m.group(1)
            if column == column_ingr:
                # ingredient column
                writing = True
                data.append(m.group(2))
            else:
                # not ingredient column
                if len(data) > 0:
                    ingredients.append(data)   # saves data
                data = []   # goes back to 0
                writing = False
        else:
            # no column found
            if writing:
                data.append(line)

# encoding management
ingredients_temp = []
for recipe in ingredients:
    recipe_temp = []
    for ingredient in recipe:
        try:
            recipe_temp.append(ingredient.encode('latin-1').decode('utf-8'))
        except UnicodeDecodeError:
            pass
    ingredients_temp.append(recipe_temp)

ingredients = ingredients_temp

# saves it to list
pickle.dump(ingredients, open('algo/data/ingredients.pkl', 'wb'))
