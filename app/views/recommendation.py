from flask import Flask, request, jsonify
from app.views import recommendation_blueprint

from app import db, client, loaded_model


def recommend_items(user_id, listCourseId, numOfRecommend):
    # print("xxxxxx>>>>>>", listCourseId)
    arr = []
    for courseId in listCourseId:
        x = loaded_model.predict(int(user_id), int(courseId))
        arr.append(x)
    arr.sort(key=lambda x: x[3], reverse=True)
    return arr[:numOfRecommend]


@recommendation_blueprint.route("/predict", methods=["POST"])
def post_predict():
    item = request.get_json()
    user_id = item.get("id")
    courseId = item.get("courseId")

    if loaded_model is None or courseId is None or user_id is None:
        return jsonify({"error": "Dont have user_id , courseId or algo"}), 400

    predict = loaded_model.predict(int(user_id), int(courseId))
    return jsonify({"predict": predict})


@recommendation_blueprint.route("/recommend", methods=["POST"])
def get_recommendations():
    item = request.get_json()
    user_id = item.get("user_id")
    listCourseId = item.get("listCourseId")
    numOfRecommend = item.get("numOfRecommend")
    print("user_id", user_id)
    print("listCourseId", listCourseId)
    print("numOfRecommend", numOfRecommend)

    if user_id is None:
        return jsonify({"error": "Please provide a user_id parameter"}), 400

    if numOfRecommend is None:
        numOfRecommend = 5

    recommendations = recommend_items(int(user_id), listCourseId, int(numOfRecommend))
    return jsonify({"recommendations": recommendations})


@recommendation_blueprint.route("/", methods=["GET"])
def get_homepage():
    home = "well come to website!"
    return jsonify({"data": home})


# @recommendation_blueprint.route("/getBranch", methods=["GET"])
# def get_branch():
#     branches = db.items.find()
#     data = {"success": True, "message": "All Branches Loaded!", "branches": branches}
#     return jsonify(data)


# def get_all_courses():
#     if db is not None and client is not None:
#         courses_collection = db["scores"]
#         # Retrieve all documents (courses) from the 'courses' collection
#         courses = courses_collection.find({})
#         # Convert MongoDB cursor to list of dictionaries
#         course_list = list(courses)
#         return course_list
#     else:
#         return "None"
