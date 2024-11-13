from . import db

class Category(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    image = db.Column(db.String(60), nullable=False, default = 'defaultcategory.png')
    description = db.Column(db.String(500), nullable=False)
    books = db.relationship('Book', backref='Category', cascade="all, delete-orphan")

    def __repr__(self):
            str = "id: {}, name: {}, image: {}, description: {}"
            str = str.format(self.id, self.name, self.image, self.description)
            return str

orderdetails = db.Table('orderdetails', 
        db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), nullable=False),
        db.Column('book_id', db.Integer, db.ForeignKey('books.id'), nullable=False),
        db.PrimaryKeyConstraint('order_id', 'book_id'))    
   
    
class Book(db.Model):
    __tablename__='books'
    id = db.Column(db.Integer, primary_key=True)
    bookName = db.Column(db.String(100), unique=True)
    image = db.Column(db.String(60), nullable=False, default = 'defaultbook.png')
    author = db.Column(db.String(100))
    isbn = db.Column(db.String(20), unique=True)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __repr__(self):
        str = "id: {}, bookName: {}, image: {}, author: {}, ISBN: {}, price: {}, description: {}, category: {} \n"
        str = str.format(self.id, self.bookName, self.image, self.author, self.isbn, self.price, self.description, self.category_id)
        return str
    
class Order(db.Model):
    __tablename__='orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default = False)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    phoneNo = db.Column(db.String(32))
    email = db.Column(db.String(128))
    date = db.Column(db.DateTime)
    shipping_addr = db.Column(db.String(200))
    total_cost = db.Column(db.Float)
    books = db.relationship("Book", secondary=orderdetails, backref="orders")

    def __repr__(self):
            str = "id: {}, status: {}, firstname: {}, lastname: {}, phoneNo: {}, email: {}, date: {}, shipping_addr: {}, books: {}, total_cost: {}"
            str = str.format(self.id, self.status, self.firstname, self.lastname, self.phoneNo, self.email, self.date, self.shipping_addr, self.books, self.total_cost)
            return str