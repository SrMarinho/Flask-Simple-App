from flask import Blueprint, Response
import controllers.books_controller as books_controller


bp = Blueprint('routes', __name__)

@bp.route('/api/books', methods=["GET"])
def get_books():
    return Response(books_controller.getBooks(), mimetype='application/json', status=200)