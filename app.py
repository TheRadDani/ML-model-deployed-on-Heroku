from flask import Flask,render_template,request
from values_ import prediction

app = Flask(__name__)
@app.route("/")
def values():
        
    return render_template("index.html")


@app.route("/sub",methods = ['POST'])
def submit():
    # HTML -> .py
    if request.method == "POST":
        value = request.form['CO2']
        values_pred = prediction(value)
    # .py -> HTML
    return render_template("submit.html",name = values_pred)

if __name__ == "__main__":
    app.run(debug=True)