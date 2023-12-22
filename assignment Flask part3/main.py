from flask import Flask, jsonify, request, g
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    notes = db.relationship('Note', backref='user', lazy=True)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message='User created successfully'), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email'], password=data['password']).first()

    if user:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    else:
        return jsonify(message='Invalid credentials'), 401

@app.route('/notes', methods=['POST'])
@jwt_required()
def create_note():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    new_note = Note(title=data['title'], content=data['content'], category=data['category'], user_id=current_user_id)
    db.session.add(new_note)
    db.session.commit()
    return jsonify(message='Note created successfully'), 201

@app.route('/notes', methods=['GET'])
@jwt_required()
def get_all_notes():
    current_user_id = get_jwt_identity()
    user_notes = Note.query.filter_by(user_id=current_user_id).all()
    notes = [{'title': note.title, 'content': note.content, 'category': note.category} for note in user_notes]
    return jsonify(notes)

@app.route('/notes/<category>', methods=['GET'])
@jwt_required()
def get_notes_by_category(category):
    current_user_id = get_jwt_identity()
    user_notes = Note.query.filter_by(user_id=current_user_id, category=category).all()
    notes = [{'title': note.title, 'content': note.content, 'category': note.category} for note in user_notes]
    return jsonify(notes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(
            port=5000,
            debug=True
        )
