from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route('/home')
def homepage():
    return render_template('home.html')
    #return "<h1>hello from homepage !!!<br> bye</h1>"

@app.route('/about')
def aboutus():
    return render_template('about.html')

@app.route('/home/test')
def testpage():
    return redirect(url_for("homepage"))
    # return redirect(url_for("hello_world"))
    # return "hello from testpage !!!"

@app.route("/<name>")
def user(name):
    return f"hello {name}!"

if __name__ == '__main__':
    app.run(debug = True)
