from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics #1
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#PrometheusMetrics(app)
metrics = PrometheusMetrics(app) #2
#response_data, content_type = metrics.generate_metrics()
with app.app_context(): #дописал
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    db = SQLAlchemy(app)

    class Todo(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        text = db.Column(db.String(200))
        complete = db.Column(db.Boolean)
    db.create_all() #дописал
    
    #@app.route('/metrics') #проверка статус ок
    #def main():
    #  return 'OK'
    @app.route("/")
    def index():
        todos = Todo.query.all()
        return render_template("index.html", todos=todos)
     
    @app.route('/add', methods=["POST"])
    def add():
        data = request.form["todo_item"]
        todo = Todo(text=data, complete=False)
        db.session.add(todo)
        db.session.commit()
        # return data # DEBUG REQUEST
        return redirect(url_for("index"))


    @app.route('/update', methods=["POST"])
    def update():
        # return request.form # DEBUG REQUEST
        return redirect(url_for("index"))

    if __name__ == '__main__':
        app.run("0.0.0.0", 5000, threaded=True)