import time
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")  # we can pass routes
@app.route("/home")
def home():
    return "<h1>Welcome to home page</h1>"


# --------- dynamic URL concept ---------
# here the name parameter is dynamic parameter
@app.route("/welcome/<name>")  # path parameter
def welcome(name):
    # whatever we will pass in endpoint, it'll be reflected here
    return f"<h1>Hi {name.title()}, welcome to the page!</h1>"


# ------- URL Redirection --------
# why URL redirection?
# if page is deleted, user need to redirected to another page
# if maintainance of page is going on
# if website gets renamed, so user should be redirectd to appropriate URL
@app.route("/score/<name>/<int:score>")
def score(name, score):
    if score < 30:
        time.sleep(1)
        # redirect to failed page
        # here we can pass full url while redirecting like https://** but to reduce manual efforts use url_for, it'll do this for us
        return redirect(
            # as passed is expecting name parameter so pass parameter in url_for function itself
            url_for("failed", name=name)
        )  # pass function name, not endpoint
    else:
        time.sleep(1)
        # redirect to passed page
        # as passed is expecting name parameter so pass parameter in url_for function itself
        return redirect(url_for("passed", name=name))


# redrirected to passed
@app.route("/pass/<name>")
def passed(name):
    return f"<h1>Congrats {name.title()}, you've cleared the xm.</h1>"


# redirected to failed
@app.route("/failed/<name>")
def failed(name):
    return f"<h1>Sorry {name.title()}, better luck next time.</h1>"


if __name__ == "__main__":
    app.run(debug=True)
