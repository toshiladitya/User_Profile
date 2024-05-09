from flask import Flask,redirect,url_for,render_template,request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *

app=Flask(__name__)
app.secret_key = 'my_super_secret_key_123456789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        existing_user = User.query.filter((User.username == username) | (User.email == email) | (User.phone == phone)).first()
        if existing_user:
            flash('Username or email or phone already exists', 'error')
            return redirect(url_for('register'))
        new_user = User(username=username, email=email, phone=phone)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            return redirect(url_for('profile'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        new_username = request.form['username']
        new_email = request.form['email']
        new_phone = request.form['phone']
    
        existing_username = User.query.filter((User.id != current_user.id) & (User.username == new_username)).first()
        if existing_username:
            flash('Username already exists', 'error')
            return redirect(url_for('edit_profile'))
        
        existing_email = User.query.filter((User.id != current_user.id) & (User.email == new_email)).first()
        if existing_email:
            flash('Email already exists', 'error')
            return redirect(url_for('edit_profile'))
        
        existing_phone = User.query.filter((User.id != current_user.id) & (User.phone == new_phone)).first()
        if existing_phone:
            flash('Phone number already exists', 'error')
            return redirect(url_for('edit_profile'))
        current_user.username = request.form['username']
        current_user.email = request.form['email']
        current_user.phone = request.form['phone']
        db.session.commit()
        flash('Profile updated successfully', 'success')
        return redirect(url_for('profile'))
    return render_template('edit_profile.html', user=current_user)

@app.route('/profile/delete', methods=['POST'])
@login_required
def delete_account():
    if request.method == 'POST':
        db.session.delete(current_user)
        db.session.commit()
        flash('Your account has been deleted', 'success')
        return redirect(url_for('register'))
    return redirect(url_for('profile'))

                    
if __name__ == '__main__':
    app.run(port=5000,debug=True)