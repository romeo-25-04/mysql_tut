from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


class Example(db.Model):
    __tablename__ = 'examples'
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Unicode)


def main():
    examples = Example.query.all()
    for ex in examples:
        print(ex.id, ex.data)


if __name__ == '__main__':
    main()
