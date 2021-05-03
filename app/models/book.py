from app import db


# (inheritance)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

    # CHANGE TABLE IN POSTGRES CALLED BOOKS (plural tables + singular CLASSES ???)
    __tablenames__ = "books"

    # optional
    # def to_string(self):
    #     return f"{self.id}: {self.title} Description: {self.description}"
