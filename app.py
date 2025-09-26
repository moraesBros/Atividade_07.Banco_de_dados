from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']
        
        # Aqui você pode adicionar lógica para enviar email
        # ou salvar no banco de dados
        
        flash('Mensagem enviada com sucesso!', 'success')
        return redirect(url_for('contato'))
    
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
