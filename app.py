from flask import Flask, render_template

app = Flask(__name__)



@app.route('/home')
def home():
        return render_template("index1.html") 

@app.route('/')
def hello():
        return render_template("index.html", name = "salman") 



# to run app on specific port here we can add port = 8080

if __name__ == '__main__':
    app.run(debug=True, port = 8080)