from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return "Hello World, my name is Chimezie OGBUU"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80