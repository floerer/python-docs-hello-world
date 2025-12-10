from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/floerer")
def poc():
    return "Hello, this is floerer! This is the PoC for subdomain takeover"
if __name__ == '__main__':
    app.run(debug=True)
