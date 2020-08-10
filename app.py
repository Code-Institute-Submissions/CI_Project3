from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipeDB'
app.config["MONGO_URI"] = 'mongodb+srv://db_admin:<password>@cluster0.18nsj.azure.mongodb.net/<dbname>?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
