import os
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user
from app.models.user import User, users_db

app = Flask(__name__, template_folder='views') 
app.secret_key= os.urandom(24)

login_manager = LoginManager(app)



@login_manager.user_loader
def load_user(user_id):
    return users_db.get(int(user_id))


# Rutas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Buscar usuario en la base de datos
        user = next((u for u in users_db.values() if u.username == username and u.password == password), None)

        if user:
            login_user(user)  # Iniciar sesión
            flash('Inicio de sesión exitoso', 'success')
            print('Inicio de sesión exitoso')
            return redirect(url_for('success', username=user.username, es_admin=user.es_admin)) 
        else:
            flash('Usuario o contraseña incorrectos', 'danger')

    return render_template('login.html')  # Página de login


@app.route('/success/<username>/<es_admin>')
def success(username, es_admin):

    print('Inicio de sesión exitoso')
    print(username)
    print(es_admin)
    if es_admin == 'True':
        return render_template('admin.html', username=username, es_admin=es_admin)
    return render_template('sucess.html', username=username,)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))