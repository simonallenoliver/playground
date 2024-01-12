from flask import Flask, render_template  # added render_template!
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)

# app.run(debug=True) should be the very last statement! 
if __name__=="__main__":
    app.run(debug=True)