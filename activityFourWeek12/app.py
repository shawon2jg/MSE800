from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def calculate_bmi():
    bmi = None
    classification = None
    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            if height <= 0 or weight <= 0:
                raise ValueError("Invalid input")
            bmi = round(weight / (height ** 2), 2)
            if bmi < 18.5:
                classification = 'Underweight'
            elif bmi < 25:
                classification = 'Normal weight'
            elif bmi < 30:
                classification = 'Overweight'
            else:
                classification = 'Obese'
        except:
            bmi = None
            classification = 'Error: Invalid input values'
    return render_template('index.html', bmi=bmi, classification=classification)

if __name__ == '__main__':
    app.run(debug=True)