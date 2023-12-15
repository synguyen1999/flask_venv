from flask import Blueprint

recommendation_blueprint = Blueprint("recommendation", __name__)
branch_blueprint = Blueprint("branch", __name__)

# Import the views
from app.views.recommendation import get_recommendations
from app.views.recommendation import get_homepage
from app.views.recommendation import post_predict

# from app.views.recommendation import get_branch


from app.views.branch import get_branch
