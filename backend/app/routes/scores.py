from flask_smorest import Blueprint
from flask.views import MethodView
from flask import request

blp = Blueprint(
    "Scores",
    "scores",
    url_prefix="/scores",
    description="Endpoints for submitting and retrieving scores."
)

@blp.route("/", methods=["POST"])
class ScoreSubmission(MethodView):
    """
    PUBLIC_INTERFACE
    Submit a user score.

    Example request body:
    {
        "username": "player1",
        "score": 12345
    }
    """
    def post(self):
        # Placeholder logic: Do not persist, just echo back
        data = request.get_json() or {}
        # In real scenario would validate/parse data
        return {
            "message": "Score submission endpoint (not yet implemented)",
            "received": data
        }, 501
