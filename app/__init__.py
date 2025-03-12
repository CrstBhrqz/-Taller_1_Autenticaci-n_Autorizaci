from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from app.models.user import User, users_db


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

app = Flask(__name__, template_folder='views') 

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
        username = request.form['username']
        password = request.form['password']
        
       
        if username in users_db and users_db[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('success'))
        
        flash('Credenciales inválidas')
    return render_template('login.html')

@app.route('/success')
@login_required
def success():
    return render_template('success.html', username=current_user.id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
