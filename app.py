from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = calculate_bmi(weight, height)
        return render_template('result.html', bmi=bmi)
    return render_template('index.html')

def calculate_bmi(weight, height):
    # Calculate BMI using the formula: BMI = weight (kg) / (height (m))^2
    bmi = weight / (height ** 2)
    return round(bmi, 2)

if __name__ == '__main__':
    app.run(debug=True)

