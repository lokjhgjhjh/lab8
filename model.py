class Category(db.Model):
    __tablename__ = 'Categories'
    CategoryID = db.Column(db.Integer, primary_key=True)
    CategoryName = db.Column(db.String(50))

class Post(db.Model):
    __tablename__ = 'Posts'
    PostID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100))
    Content = db.Column(db.Text)
    CategoryID = db.Column(db.Integer, db.ForeignKey('Categories.CategoryID'))
    ImageURL = db.Column(db.String(255))

    category = db.relationship('Category', backref=db.backref('posts', lazy=True))
