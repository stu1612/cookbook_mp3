import os
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


# recipes = [{
#         'title': 'Italien Lasagna with chorizo, feta cheese and spinach',
#         'ingredients': 'Mince, Onion, Pasta sheets',
#         'instructions': 'Cook carefully',
#         'categories': 'Meat, Italien, Lasagna, Pasta',
#         'cook_time': '1.5 hrs',
#         'preperation_time': '30 mins',
#         'date_posted': 'December 03, 2019'
#     },
#     {
#         'title': 'Sausage Pasta',
#         'ingredients': 'Sausage, pasta, white sauce',
#         'instructions': 'Cook carefully',
#         'categories': 'Meat, Pasta',
#         'cook_time': '30 mins',
#         'preperation_time': '5 mins',
#         'date_posted': 'December 02, 2019'
#     },
#     {
#         'title': 'Sausage Pasta',
#         'ingredients': 'Sausage, pasta, white sauce',
#         'instructions': 'Cook carefully',
#         'categories': 'Meat, Pasta',
#         'cook_time': '30 mins',
#         'preperation_time': '5 mins',
#         'date_posted': 'December 02, 2019'
#     },
#     {
#         'title': 'Salad',
#         'ingredients': 'Sausage, pasta, white sauce',
#         'instructions': 'Cook carefully',
#         'categories': 'Meat, Pasta',
#         'cook_time': '30 mins',
#         'preperation_time': '5 mins',
#         'date_posted': 'December 02, 2019'
#     }
# ]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/recipes')
def recipes_page():
    return render_template('recipes.html', recipes=mongo.db.recipes.find(), title='Recipes')
    
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', title='Create Recipe', recipes=mongo.db.recipes.find())
    
    
@app.route('/post_recipe', methods=['POST'])
def post_recipe():
    if request.method == 'POST':
        recipes = mongo.db.recipes
        recipes.insert({
            'title':request.form.get('title'),
            'tag_1':request.form.get('tag_1'),
            'tag_2':request.form.get('tag_2'),
            'tag_3':request.form.get('tag_3'),
            'prep_time':request.form.get('prep_time'),
            'cook_time':request.form.get('cook_time'),
            'serving':request.form.get('serving'),
            'image':request.form.get('image'),
            'ing_1':request.form.get('ing_1'),
            'qty_1':request.form.get('qty_1'),
            'method_1':request.form.get('method_1')
        })
        flash('Great - your recipe has been added to our collection !', 'success')
        return redirect(url_for('recipes_page'))
    return render_template('add_recipe.html', title='Create Recipe')    


if __name__ == '__main__':
    app.run(host = os.environ.get('IP'),
        port = int(os.environ.get('PORT')),
        debug = True)