from flask import Flask, request, jsonify, Response
from resource.connection.session_db import session_factory
from resource.models.all_models import *


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
    livro_data = request.get_json()
    livro = Livro(
        nome = livro_data.get('nome'),
        ano = livro_data.get('ano'),
        autor = livro_data.get('autor')
    )
    
    errors = []
    for key, value in livro.to_json().items():
        if value is None:
            errors.append(
                {
                    "message" : f"O atributo {key} não foi passado"
                }
            )
    
    if len(errors) == 0:
        return Response(
            response=jsonify(errors),
            status=400,
            mimetype="application/json"
        )

    with session_factory() as session:
        print(livro)
        session.add(livro)
        session.commit()
    
    return "Livro Cadastrado com Sucesso!"

if __name__ == '__main__':
    app.run(debug=True)