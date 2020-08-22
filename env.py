import os

# Create a secret key1
os.environ["SECRET_KEY"] = "Dyzio"
# Storing the MONGO_URI environment variable
os.environ[
    "MONGO_URI"] = 'mongodb+srv://db_admin:kakao9000@cluster0.18nsj.azure.mongodb.net/recipeDB?retryWrites=true&w=majority'
os.environ["MONGO_DBNAME"] = 'recipeDB'
