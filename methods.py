from flask import Flask, render_template, redirect, session,request
app = Flask(__name__)
#set a secrest key for encrypting session data
app.secret_key = 'my_secret_key'

# dictionary to store username and password
users = {
    'imran' : '1234',
    'user2' : 'password2'
}

# to render a login form 
@app.route('/')
def view_form():
    return render_template('login.html')

# for handling get request form we can get
# the form input value by using the args attribute.
# this values after submitting u can see in the urls
# eg. http://127.0.0.1:5000/handle_get?username=kunal&password=1234
# these exploits our credentials so that's
# why develepers prefer post request.

@app.route('/handle_get', methods =['GET'])
def handle_get():
    if request.method == 'GET':
        username = request.args['username']
        password = request.args['password']
        print(username, password)
        if username in users and users[username] == password:
            return '<h1>Welcome</h1>'
        else :
            return "<h1>Invalid Credentials</h1>"
    else:
        return render_template('login.html')
    
# for handling the post request form we can get the form 
# input values by using POST attribute.
# these values after submitting u will never see in the urls
@app.route('/handle_post', methods =['POST'])
def handle_post():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if username in users and users[username] == password:
            return '<h1>Welcome</h1>'
        else :
            return "<h1>Invalid Credentials</h1>"
    else:
        return render_template('login.html')
    
if __name__ == '__main__':
    app.run(debug=True)
