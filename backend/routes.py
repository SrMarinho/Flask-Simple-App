from flask import Blueprint, Response
import controllers.books_controller as books_controller

bp = Blueprint('routes', __name__)

@bp.route('/api/books', methods=["GET"])
def get_books():
    def generate():
        yield '['  # Início da lista
        first = True
        for book in books_controller.getBooks():
            if not first:
                yield ','  # Adiciona uma vírgula entre os objetos
            first = False
            yield book  # Streama o JSON do livro
        yield ']'  # Fim da lista
    return Response(generate(), mimetype='application/json', status=200)
