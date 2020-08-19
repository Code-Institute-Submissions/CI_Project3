import os
from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

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


# Route for editing recipe
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    this_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = list(mongo.db.categories.find())
    return render_template('editrecipe.html', recipe=this_recipe,
                           categories=categories)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    # Update the article after editing it using JSON
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)}, {
        'recipe_name': request.form.get('recipe_name'),
        'user_name': request.form.get('user_name'),
        'category_name': request.form.get('category_name'),
        'photo_url': request.form.get('photo_url'),
        'preparation_time': request.form.get('preparation_time'),
        'brief_description': request.form.get('brief_description'),
        'ingredients': request.form.get('ingredients'),
        'preparation': request.form.get('preparation')})
    return redirect(url_for('get_recipes'))


# Route for deleting recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


# Error Handling
@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404


@app.errorhandler(500)
def something_wrong():
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
