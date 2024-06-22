from flask import Flask, render_template

app = Flask(__name__)



@app.route('/home')
def home():
        return render_template("index1.html") 

@app.route('/')
def hello():
        return render_template("index.html", name = "salman") 





if __name__ == '__main__':
    app.run(debug=True)