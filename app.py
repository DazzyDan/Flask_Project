from distutils.log import debug
from numbers import Integral
from urllib import request
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# //// => absolute path; /// => relative path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    
    def __repr__(self) -> str:
        return '<Task %r>' % self.id
    

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content = task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "Issue happens during inserting"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        #No need to precise the path, it will find the file under templates folder
        return render_template('index.html', tasks = tasks)

if __name__ == "__main__":
    app.run(debug=True)