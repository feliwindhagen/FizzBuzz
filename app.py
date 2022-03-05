# from flask import FLask, render_template
# app=Flask(__name__)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    buzzfizz_list = []
    for x in range(1,1001):
        if (x%3==0 and x%5==0):
            buzzfizz_list.append("FizzBuzz")
        elif (x%3==0):
            buzzfizz_list.append("Fizz")
        elif (x%5==0):
            buzzfizz_list.append("Buzz")
        else:
            buzzfizz_list.append(x)
    return render_template("main.html", buzzfizz_list = buzzfizz_list)

@app.route('/<int:number>')
def hello_world2(number):
    buzzfizz_list = []
    for x in range(1,number+1):
        if (x%3==0 and x%5==0):
            buzzfizz_list.append("FizzBuzz")
        elif (x%3==0):
            buzzfizz_list.append("Fizz")
        elif (x%5==0):
            buzzfizz_list.append("Buzz")
        else:
            buzzfizz_list.append(x)
    return render_template("main.html", buzzfizz_list = buzzfizz_list)

# @app.route("/")
# def index():
#     buzzfizz_list = []
#     for x in range(1,1001):
#         if (x%3==0 and x%5==0):
#             buzzfizz_list.append("FizzBuzz")
#         elif (x%3==0):
#             buzzfizz_list.append("Fizz")
#         elif (x%5==0):
#             buzzfizz_list.append("Buzz")
#         else:
#             buzzfizz_list.append(x)

