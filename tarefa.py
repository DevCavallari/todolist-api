from flask import jsonify

def buscar_tarefas():
        tarefas = [
        {
           'id' : 1,
           'nome' : 'Vamos aumentar o zoom para nao errar a digitacao',
           'status' : 'Pendente'
        },
        {
            'id' : 2,
            'nome' : 'Aprender python para programar apis',
            'status' : 'Pendente'
        }
        
    ]
        return jsonify(tarefas)
def buscar_tarefa():
        tarefa = {
            'id' : 1,
           'nome' : 'Vamos aumentar o zoom para nao errar a digitacao',
           'status' : 'Pendente'
        }
        return jsonify(tarefa)