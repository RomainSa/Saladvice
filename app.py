from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def hello_world():
    if request.method == 'POST':
        return render_template('index.html', colours=[('red', False), ('green', False), ('blue', False), ('black', False)], notes=['do', 're', 'mi'], selected=True)
    else:
        return render_template('index.html', colours=[('red', False), ('green', False), ('blue', False)], notes=['do', 're', 'mi'])


if __name__ == '__main__':
    app.run(debug=True)
