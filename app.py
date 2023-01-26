from flask import Flask, request, jsonify, Response
from resource.models.all_models import *
from resource.database import livraria_repository


app = Flask(__name__)


@app.route('/livros', methods=['GET'])
def get_all_books():
    livros = livraria_repository.get_all()
    return livros if livros is not None else Response(status=204)

@app.route('/livros/<int:id>', methods=['GET'])
def get_one_book(id):
    livro = livraria_repository.get_by_id(id)
    if livro is None:
        return Response(status=204)
    return jsonify(livro.to_json())     

@app.route('/livros', methods=['POST'])
def cadastrar_livro():
    livro_data = request.get_json()
    livro = Livro(
        nome = livro_data.get('nome'),
        ano = livro_data.get('ano'),
        autor = livro_data.get('autor')
    )

    try:
        livraria_repository.inserir_livro(livro)
    except:
        return Response(
                response = {"message" : "Erro ao cadastrar o livro"},
                status = 500
            )

    return Response (
            response = {"message" : "Livro Cadastrado com Sucesso"},
            status = 200
        )

@app.route('/livros/<int:id>', methods=['PUT'])
def alterar_livro(id):
    pass

if __name__ == '__main__':
    app.run(debug=True)