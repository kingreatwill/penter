from flask import Flask
# flask run
app = Flask(__name__)

# import config
# app.config.from_object(config)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run() # app.run(debug=True)