from flask import Flask, request
from database.models.__all_models import *


app = Flask(__name__)

@app.route('/livros', methods=['GET'])
def get_all_books():
    pass

@app.route('/livros/<int:id>', methods=['GET'])
def get_one_book():
    pass

@app.route('/livros', methods=['POST'])
def inserirLivros():
    id = request.form['id']
    nome = request.form['id']
    ano = request.form['id']
    autor = request.form['id']

if __name__ == '__main__':
    app.run(debug=True)