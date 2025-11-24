from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Your Flask App is Deployed on Render Cloud Successfully!"

if __name__ == "__main__":
    app.run()
