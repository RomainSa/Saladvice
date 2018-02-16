n_ingredients = [4, 5, 6]
ingredients = ['crème fraiche', 'ciboulette', 'persil', 'aneth', 'ail', 'oignon', 'céleri', 'paprika',
               'moutarde', 'citron']
sauces = ['ranch', 'mielmoutarde']
bases = ['riz', 'pates', 'salade', 'pates/salade']


class Ingredient:
    """
    A basic ingredient
    """

    def __init__(self, name):
        self.name = name


class Base(Ingredient):
    """
    A salad base
    """

    def __init__(self, name):
        if name not in bases:
            raise NameError('Unknown base: {}'.format(name))
        self.name = name


class Sauce:
    """
    A sauce
    """

    def __init__(self, name):
        self.name = name
        if name not in sauces:
            raise NameError('Unknown sauce: {}'.format(name))
        self.ingredients = ingredients
        if name == 'ranch':
            for ingredient in ingredients:
                self.ingredients.append(Ingredient(ingredient))


class Salad:
    """
    A salad
    """

    def __init__(self, base, sauce, n_ingredients, ingredients=list()):
        self.base = base
        self.sauce = sauce
        self.n_ingredients = n_ingredients
        if self.n_ingredients < len(ingredients):
            raise ValueError('Number of ingredients is inferior to ingredients given as input')

    def choose_ingredients(self):
        return None


if __name__ == '__main__':
    my_salad = Salad(base=Base('pates'), sauce=Sauce('ranch'), n_ingredients=4)
    my_salad.choose_ingredients()
