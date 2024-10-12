from flask import Flask

app = Flask(__name__)


@app.route("/")  # we can pass routes
@app.route("/home")
def home():
    return "<h1>Welcome to home page</h1>"


# here the name parameter by default taking string
@app.route("/welcome/<name>")  # path parameter
def welcome(name):
    # whatever we will pass in endpoint, it'll be reflected here
    return f"<h1>Hi {name.title()}, welcome to the page!</h1>"


# lets pass num and chage its data type
@app.route("/addition/<int:num>")  # path parameter
def addition(num):
    return f"<h1>Num is {num}, Addition is {num+10}</h1>"


@app.route("/addition_two/<int:num1>/<int:num2>")  # path parameter
def addition_two(num1, num2):
    return f"<h1>{num1} + {num2} = {num1 + num2}</h1>"


@app.route("/about")
def about():
    return "<h1>This is about page</h1>"


if __name__ == "__main__":
    app.run(debug=True)
