from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# Configurer la connexion à la base de données MySQL
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://user:password@mysql:3306/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# Définir le modèle de données pour le formulaire de contact
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.Text)
# Route pour la page d'accueil (formulaire de contact)
@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST': 
        name = request.form['name'] 
        email = request.form['email']
        message = request.form['message']
        new_contact = Contact(name=name, email=email, message=message)
        db.session.add(new_contact)
        db.session.commit()
        return redirect(url_for('thank_you'))
    return render_template('contact.html')
# Route pour la page de remerciement
@app.route('/thank-you')
def thank_you():
    return "Thank you for your message!"
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(host='0.0.0.0')