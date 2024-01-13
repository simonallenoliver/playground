from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index2/<times>/')
def index2(times):
    return render_template("index2.html", times = int(times))	# notice the 2 new named arguments!

@app.route('/index2/<times>/<color>')
def index2(times):
    return render_template("index3.html", times = int(times), color = "color")	# notice the 2 new named arguments!


if __name__=="__main__":
    app.run(debug=True)

