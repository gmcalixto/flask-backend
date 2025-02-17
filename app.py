import os
import datetime
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import json
import sqlite3


app = Flask(__name__)
CORS(app)



@app.route('/pessoas', methods=['GET'])
def pessoas():
    try:
        with sqlite3.connect('crud.db') as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''SELECT nome, sobrenome, cpf, data_nascimento FROM pessoa''')
            result = cursor.fetchall()
            return json.dumps([dict(ix) for ix in result]), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/pessoa/<cpf>', methods=['GET', 'DELETE'])
def pessoa_por_cpf(cpf):

    try:
        with sqlite3.connect('crud.db') as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            if request.method == 'GET':
                cursor.execute('''SELECT nome, sobrenome, cpf, data_nascimento FROM pessoa WHERE cpf=?''', [cpf])
                result = cursor.fetchall()
                if result:
                    return json.dumps([dict(ix) for ix in result]), 200
                return jsonify(error="Pessoa não encontrada"), 404
            elif request.method == 'DELETE':
                cursor.execute('DELETE FROM pessoa WHERE cpf = ?', (cpf,))
                if cursor.rowcount == 0:
                    return jsonify(error="Pessoa não encontrada"), 404
                conn.commit()
                return jsonify(success="Pessoa deletada com sucesso"), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/pessoa', methods=['POST'])
def insere_atualiza_pessoa():


    data = request.get_json(force=True)
    nome = data.get('nome')
    sobrenome = data.get('sobrenome')
    cpf = data.get('cpf')
    datanascimento = data.get('data_nascimento')

    try:
        with sqlite3.connect('crud.db') as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT 1 FROM pessoa WHERE cpf = ?', (cpf,))
            exists = cursor.fetchone()
            if exists:
                cursor.execute('UPDATE pessoa SET nome=?, sobrenome=?, data_nascimento=? WHERE cpf=?', (nome, sobrenome, datanascimento, cpf))
                conn.commit()
                return jsonify(success="Pessoa atualizada com sucesso"), 200
            cursor.execute('INSERT INTO pessoa (nome, sobrenome, cpf, data_nascimento) VALUES (?, ?, ?, ?)', (nome, sobrenome, cpf, datanascimento))
            conn.commit()
            return jsonify(success="Pessoa inserida com sucesso"), 201
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)