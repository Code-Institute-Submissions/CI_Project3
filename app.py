from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipeDB'
app.config[
    "MONGO_URI"] = 'mongodb+srv://db_admin:klop9000@cluster0.18nsj.azure.mongodb.net/recipeDB?retryWrites=true&w=majority'

mongo = PyMongo(app)


# Route to home page
@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')


# Route to recipes page
@app.route('/recipes/')
def get_recipes():
    return render_template('recipes.html', recipes=mongo.db.recipes.find())


# Route to single recipe
@app.route('/recipe/<recipe_id>')
def single_recipe(recipe_id):
    this_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=this_recipe)


# Route to recipes in a single category
@app.route("/category/<selected_category>")
def category(selected_category):
    all_recipes = mongo.db.recipes.find()
    return render_template("category.html",
                           recipes=all_recipes,
                           selected_category=selected_category)


# Route for adding recipes.
@app.route('/addrecipe/')
def add_recipe():
    categories = list(mongo.db.categories.find().sort('category_name', pymongo.ASCENDING))
    return render_template('addrecipe.html', categories=categories)


@app.route('/insert_recipe/', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run()
