
from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipeDB'
app.config["MONGO_URI"] = 'mongodb+srv://db_admin:klop9000@cluster0.18nsj.azure.mongodb.net/recipeDB?retryWrites=true&w=majority'

mongo = PyMongo(app)

# Route to home page
@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

#Route to recipes page
@app.route('/recipes/')
def get_recipes():
    return render_template('recipes.html', recipes=mongo.db.recipes.find())

if __name__ == '__main__':
    app.run()
