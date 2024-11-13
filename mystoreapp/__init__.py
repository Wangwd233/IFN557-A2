#import flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
app=Flask(__name__)
#create a function that creates a web application
#a web server will run this web appliction
def create_app():
    app.debug=True
    app.secret_key='BetterSecretNeeded123'

    #set app configuration data
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///link.sqlite'

    #initialize db with flask app
    db.init_app(app)

    bootstrap = Bootstrap(app)
    #app.config['EXPLAIN_TEMPLATE_LOADING'] = True

    #register blueprints of route
    from . import views
    app.register_blueprint(views.bp)
    #from . import admin
    #app.register_blueprint(admin.bp)

    return app


# inbuilt function which takes error as parameter
app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

app.errorhandler(500)
def internal_error(e):
    return render_template("500.html")
