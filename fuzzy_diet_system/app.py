from flask import Flask, render_template, request
from fuzzy import classify_user

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        age      = int(request.form['age'])
        height   = float(request.form['height'])
        weight   = float(request.form['weight'])
        diet     = request.form['diet']
        activity = request.form['activity']

        # Get full-day plan
        plan = classify_user(age, height, weight, diet, activity)

        return render_template('result.html',
                               age=age,
                               bmi=round(plan['bmi'],2),
                               category=plan['category'],
                               day_plan=plan['day_plan'])
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
