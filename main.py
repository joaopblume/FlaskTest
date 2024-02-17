from flask import Flask, url_for, render_template

# Inicializacao
app = Flask(__name__)

# Rotas
@app.route('/')
def index():
    titulo = 'Gestao de Usuarios'
    usuarios = [
        {'nome': 'Ana', 'membro_ativo': True},
        {'nome': 'Bruno', 'membro_ativo': False},
        {'nome': 'Carlos', 'membro_ativo': True},
        {'nome': 'Daniela', 'membro_ativo': False}
    ]

    return render_template('index.html', titulo=titulo, usuarios=usuarios) 
    #return f"<a href='{ url_for('pagina_sobre') }'>Sobre</a> <h1>"

@app.route('/sobre')
def pagina_sobre():
    return '''
    <h1>Sobre</h1>
    <p>Este é um exemplo de página sobre.</p>
    '''
# Execucao
app.run(debug=True) # debug=True, para que o servidor seja reiniciado automaticamente sempre que o código for alterado.

