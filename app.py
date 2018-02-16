from flask import Flask, render_template, request
from saladvice import bases, sauces, ingredients, n_ingredients

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    # number of ingredients
    n_ingredients_ = request.form['n_ingredients'] if 'n_ingredients' in request.form else n_ingredients[0]
    save_n_ingredients = 'save_n_ingredients' in request.form

    # base
    base = request.form['base'] if 'base' in request.form else bases[0]
    save_base = 'save_base' in request.form

    # sauce
    sauce = request.form['sauce'] if 'sauce' in request.form else sauces[0]
    save_sauce = 'save_sauce' in request.form

    # ingredient 1
    ingredient1 = request.form['ingredient1'] if 'ingredient1' in request.form else ingredients[0]
    save_ingredient1 = 'save_ingredient1' in request.form

    # ingredient 2
    ingredient2 = request.form['ingredient2'] if 'ingredient2' in request.form else ingredients[1]

    # ingredient 3
    ingredient3 = request.form['ingredient3'] if 'ingredient3' in request.form else ingredients[2]

    # ingredient 4
    ingredient4 = request.form['ingredient4'] if 'ingredient4' in request.form else ingredients[3]

    # ingredient 5
    ingredient5 = request.form['ingredient5'] if 'ingredient5' in request.form else ingredients[4]

    # ingredient 6
    ingredient6 = request.form['ingredient6'] if 'ingredient6' in request.form else ingredients[5]

    return render_template('index.html',
                           n_ingredients_list=[str(i) for i in n_ingredients],   # must be str since html will send option value (=str)
                           n_ingredients=n_ingredients_,
                           save_n_ingredients=save_n_ingredients,
                           bases=bases,
                           base=base,
                           save_base=save_base,
                           sauces=sauces,
                           sauce=sauce,
                           save_sauce=save_sauce,
                           ingredients=ingredients,
                           ingredient1=ingredient1,
                           save_ingredient1=save_ingredient1,
                           ingredient2=ingredient2,
                           ingredient3=ingredient3,
                           ingredient4=ingredient4,
                           ingredient5=ingredient5,
                           ingredient6=ingredient6)


if __name__ == '__main__':
    app.run(debug=True)
