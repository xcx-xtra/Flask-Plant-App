from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from models import db, Plant

app = Flask(__name__)
Bootstrap(app)

# SQLite database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    plants = Plant.query.all()
    return render_template('index.html', plants=plants)

@app.route('/add', methods=['POST'])
def add_plant():
    title = request.form.get('title')
    status = request.form.get('status', 'Incomplete')
    date = request.form.get('date')
    rating = request.form.get('rating', 0)

    new_plant = Plant(title=title, status=status, date=date, rating=rating)
    db.session.add(new_plant)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>')
def update_plant(id):
    plant = Plant.query.get_or_404(id)
    plant.status = 'Complete' if plant.status == 'Incomplete' else 'Incomplete'
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_plant(id):
    plant = Plant.query.get_or_404(id)
    db.session.delete(plant)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)