"""#basic Flask code 
from flask import Flask
app=Flask(__name__)

@app.route('/')

def home():
    return "Hello"

if __name__=='__main__':
    app.run(debug=True) """

"""
#using variables
from flask import Flask

app=Flask(__name__)

@app.route("/home/<name>")

def home(name):
    return "Hello "+name

if __name__=='__main__':
    app.run(debug=True)

#here you need to type in url /home/name 
"""

#using multiple variables

from flask import Flask

app=Flask(__name__)

@app.route('/home/<name>')

def home(name):
    return "Hello "+ name

@app.route('/home/<int:age>')

def home_age(age):
    return "I am "+ str(age)+ "years old"

@app.route('/home/<float:salary>')

def home_salary(salary):
    return f"My salary is {str(salary)}"

if __name__=="__main__":
    app.run(debug=True)