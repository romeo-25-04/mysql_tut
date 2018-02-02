from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


class Example(db.Model):
    __tablename__ = 'examples'
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Unicode)

    def __init__(self, id, data):
        self.id = id
        self.data = data


def get_all_examples():
    examples = Example.query.all()
    for ex in examples:
        print(ex.id, ex.data)
    return examples


def main():
    examples = get_all_examples()
    # # Insert Data
    # new_id = max([ex.id for ex in examples]) + 1
    # new_example = Example(new_id, "from python")
    # db.session.add(new_example)

    # Update data
    update_row = Example.query.filter_by(id=3).first()
    update_row.data = "updated 3"


    # Delete data
    # delete_row = Example.query.filter_by(id=2).first()
    # db.session.delete(delete_row)

    db.session.commit() # commit to db
    examples = get_all_examples()


if __name__ == '__main__':
    main()
