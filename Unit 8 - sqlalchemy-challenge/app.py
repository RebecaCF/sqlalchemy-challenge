from flask import Flask

# Create an app
app = Flask(__name__)


# -----
#"/api/country/"
#"/"
@app.route("/")
def home():
    print("Server received a GET request for 'Home'")
    return "Welcome to my home page!"

@app.route("/about")
def about():
    print("Server received a GET request for 'About'")
    return "Welcome to my about page!"

if __name__=="__main__":
    app.run(debug=True)