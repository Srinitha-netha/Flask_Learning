#using multiple variables

from flask import Flask

app=Flask(__name__)

@app.route('/home/<name>')

def home(name):
    return "Hello "+ name

@app.route('/home/<int:age>')

def home_age(age):
    return "I am "+ str(age)+ " years old"

@app.route('/home/<float:salary>')

def home_salary(salary):
    return f"My salary is {str(salary)}"

if __name__=="__main__":
    app.run(debug=True)