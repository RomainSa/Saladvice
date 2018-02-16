from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    n_ingredients = request.form['n_ingredients'] if 'n_ingredients' in request.form else '4'
    save_n_ingredients = 'save_n_ingredients' in request.form
    return render_template('index.html',
                           n_ingredients_list=['4', '5', '6'],   # must be str since html will send option value (=str)
                           n_ingredients=n_ingredients,
                           save_n_ingredients=save_n_ingredients)


if __name__ == '__main__':
    app.run(debug=True)
