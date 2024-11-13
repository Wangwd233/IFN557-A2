from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Category, Book, Order
from .forms import CheckoutForm
from . import db
from datetime import datetime

bp = Blueprint('main', __name__)

#declare route index to the homepage
@bp.route('/')
def index():
    categories = Category.query.order_by(Category.name).all()
    return render_template('index.html', categories = categories)

#declare route to the booklist page
@bp.route('/category/<int:categoryid>/')
def booklist(categoryid):
    booklist = Book.query.filter(Book.category_id == categoryid)
    return render_template('booklist.html', books = booklist)

@bp.route('/books/')
def search():
    search = request.args.get('search')
    search = '%{}%'.format(search)
    booklist = Book.query.filter(Book.bookName.like(search)).all()
    return render_template('booklist.html', books = booklist) 

#declare route to the item detail page
@bp.route('/book/<int:bookid>/')
def book(bookid):  
    print(bookid)  
    item = Book.query.filter(Book.id == bookid)
    return render_template('itemDetail.html', item = item)


@bp.route('/order/', methods=['POST', 'GET'])
def order():
    book_id = request.values.get('book_id')

    #retrieve order if there is one
    if 'order_id' in session.keys():
        order = Order.query.get(session['order_id'])
    else:
        #if order_id is not exist, it means there is no order
        order = None
    
    #if there is no order, create a new one
    if order is None:
        order = Order(status = False, firstname = '', lastname = '', phoneNo = '', email = '', date=datetime.now(), shipping_addr = '', total_cost = 0)
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed to creating a new order')
            order = None
        

        #calculate the total price
    totalprice = 0
    if order is not None:
        for book in order.books:
            totalprice = totalprice + book.price

        #when the book_id is not null, it means user have trigger the button to add item into basket
    if book_id is not None and order is not None:
        book = Book.query.get(book_id)
        if book not in order.books:
            try:
                order.books.append(book)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.order'))
        else:
            flash('item already in basket')
            return redirect(url_for('main.order'))
            
    return render_template('order.html', order = order, totalprice = totalprice)

#declare a route for user to delete single item in order
@bp.route('/deleteorderitem', methods = ['POST'])
def deleteorderitem():
    id = request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        book_to_delete = Book.query.get(id)
        try:
            order.books.remove(book_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem occurs when try deleting item from order' 
    return redirect(url_for('main.order'))

@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))

@bp.route('/checkout/', methods=['POST', 'GET'])
def checkout():
    form = CheckoutForm()

    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])

        if form.validate_on_submit():
            order.status=True
            order.firstname=form.firstname.data
            order.lastname = form.lastname.data
            order.phoneNo = form.phone.data
            order.email = form.email.data
            order.shipping_addr = form.address.data
            totalcost = 0

            #add the total cost
            for book in order.books:
                totalcost = totalcost + book.price
            #assign the total cost and submit time into order
            order.total_cost = totalcost
            order.date = datetime.now()

            #try to insert data into database to complete order
            try:
                db.session.commit()
                del session['order_id']
                flash('Thank you for shopping at Link Book Store! Our staff will contact you soon...')
                return redirect(url_for('main.index'))
            except:
                return 'An issue has occured when completing your order'
    return render_template('checkout.html', form = form)