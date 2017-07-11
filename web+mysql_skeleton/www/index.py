import os
from flask import Flask
from flask import Markup
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure MySQL connection.
db = SQLAlchemy()
db_uri = 'mysql://{0}:{1}@db:3306/information_schema'.format(
    'my_user',#os.environ('MYSQL_USER'),
    'my_password',#os.environ('MYSQL_PASSWORD'),
)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def index():
    return "<html><h1>Hello</h1></html>"

@app.route("/bb")
def test_basic_sql():
    res = db.engine.execute("SHOW TABLES;")
    result = []
    for row in res:
        result.append(row[0])

    return "<html><h1>Describe tables</h1><p>{0}</p></html>".format(str(result))

    
@app.route("/aa")
def test():
    mysql_result = False
    # TODO REMOVE FOLLOWING LINE AFTER TESTING COMPLETE.
    db.session.query("1").from_statement("SELECT 1").all()
    try:
        if db.session.query("1").from_statement("SELECT 1").all():
            mysql_result = True
    except:
        pass

    if mysql_result:
        result = Markup('<span style="color: green;">PASS</span>')
    else:
        result = Markup('<span style="color: red;">FAIL</span>')

    # Return the page with the result.
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
