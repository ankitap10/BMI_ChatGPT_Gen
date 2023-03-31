from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        bmi = weight / (height / 100) ** 2
        return render_template('result.html', bmi=bmi)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

