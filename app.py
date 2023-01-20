from flask import Flask, request, jsonify, Response
from database.session_db import session_factory
from database.models.all_models import *


app = Flask(__name__)

@app.route('/livros', methods=['GET'])
def get_all_books():
    with session_factory() as session:
        livros = [livro.to_json() for livro in session.query(Livro).all()]
        return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def get_one_book(id):
    with session_factory() as session:
        livro = session.query(Livro).get(id)
        if livro is None:
            return Response(status=204)
        return jsonify(livro.to_json())     

@app.route('/livros', methods=['POST'])
def inserirLivros():
    id = request.form['id']
    nome = request.form['nome']
    ano = request.form['ano']
    autor = request.form['autor']

    with session_factory() as session:
        pass

if __name__ == '__main__':
    app.run(debug=True)