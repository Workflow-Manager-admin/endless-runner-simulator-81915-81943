from flask_smorest import Blueprint
from flask.views import MethodView

blp = Blueprint(
    "Users",
    "users",
    url_prefix="/users",
    description="Endpoints for user account management and retrieval."
)

@blp.route("/<string:username>", methods=["GET"])
class UserProfile(MethodView):
    """
    PUBLIC_INTERFACE
    Retrieve a user profile by username.
    """
    def get(self, username):
        # Placeholder: Not implemented
        return {
            "message": "User profile endpoint (not yet implemented)",
            "username": username
        }, 501
