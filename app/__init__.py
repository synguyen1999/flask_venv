from flask import Flask
from pymongo import MongoClient
import pickle
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)


# Load the model during app initialization
def load_model():
    try:
        with open("app/models/model.pkl", "rb") as file:
            loaded_model = pickle.load(file)

        return loaded_model

    except Exception as e:
        print(f"Model loading error: {str(e)}")
        return None


# Make the model accessible to the application
loaded_model = load_model()


# MongoDB connection
def connect_to_mongodb():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["test_database"]  # Change this to your DB name
        return db, client
    except Exception as e:
        print(f"Failed to connect to MongoDB: {str(e)}")
        return None, None


# Establish MongoDB connection during app initialization
db, client = connect_to_mongodb()

if db is not None and client is not None:
    print("Successfully connected to MongoDB!")
else:
    print("Failed to connect to MongoDB. Check your connection settings.")

# Import views to register blueprints
from app.views import recommendation_blueprint, branch_blueprint

# Register the blueprints
app.register_blueprint(recommendation_blueprint)
app.register_blueprint(branch_blueprint)
