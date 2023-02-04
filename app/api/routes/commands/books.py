from flask import current_app as app
from flask import make_response, request, jsonify
from app.server.database.models.all_models import Livro
from app.server.resource import livraria_repository
import http.client as HTTP_STATUS


# Read all
@app.route('/livros', methods=['GET'])
def get_all_books():
    livros = livraria_repository.get_all()
    return livros if livros is not None else make_response(status=204)

# Read One
@app.route('/livros/<int:id>', methods=['GET'])
def get_one_book(id):
    livro = livraria_repository.get_by_id(id)
    if livro is None:
        return make_response(status = HTTP_STATUS.NO_CONTENT)
    return jsonify(livro.to_json())     

# Create
@app.route('/livros/adicionar', methods=['POST'])
def cadastrar_livro():
    livro_data = request.get_json()
    livro = Livro (
        nome = livro_data.get('nome'),
        ano = livro_data.get('ano'),
        autor = livro_data.get('autor')
    )

    try:
        livraria_repository.inserir_livro(livro)
    except Exception as err:
        return make_response(status = HTTP_STATUS.BAD_REQUEST)

    return make_response(status = HTTP_STATUS.CREATED)

# Update
@app.route('/livros/alterar/<int:id>', methods=['PATCH'])
def alterar_livro(id):
    livro_data = request.get_json()
    livro_to_update = livraria_repository.get_by_id(id)
    
    if livro_to_update is None:
        return make_response(status = HTTP_STATUS.NO_CONTENT)
    
    try:
        new_livro = Livro(
            nome= livro_data['nome'],
            ano= livro_data['ano'],
            autor= livro_data['autor']
        )
        livraria_repository.alterar_livro(id, new_livro)
    except:
        return make_response(status = HTTP_STATUS.BAD_REQUEST)
    
    return make_response(status = HTTP_STATUS.CREATED)

# Delete
@app.route('/livros/deletar/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    try:
        livraria_repository.deletar_livro(id)
    except Exception as err:
        return make_response('Não foi possivel deletar o livro', HTTP_STATUS.BAD_REQUEST)
   
    return make_response('Livro deletado com sucesso!', HTTP_STATUS.ACCEPTED)