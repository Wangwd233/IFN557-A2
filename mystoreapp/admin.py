#Create data seeding for test web application
#Data will be insert into database 'link.sqlite'
#admin has been defined in __init__.py as a blueprint and has been hidden as it should only be insert one time after the database is creating

from flask import Blueprint
from . import db
from .models import Category, Book, Order

bp = Blueprint('admin', __name__, url_prefix='/admin/')

#function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():
    category1 = Category(name='fiction', image='fiction.png', description='A work of fiction is one that is derived from the imagination. ')
    category2 = Category(name='history', image='history.png', description='Books about history')
    category3 = Category(name='science', image='science.png', description='Books relevant to science')

    #try to insert data into database
    try:
        db.session.add(category1)
        db.session.add(category2)
        db.session.add(category3)
        db.session.commit()
    except:
        return 'There was an issue when adding the categories in dbseed function'
    
    
    book1 = Book(category_id= category2.id, bookName='Secret History', image='4%LL}IVCO6BK$IL{87%DYQP.png', author='Donna Tartt', isbn='1400031702', price='28.75', description='Under the influence of a charismatic classics professor, a group of clever, eccentric misfits at a New England college discover a way of thought and life a world away from their banal contemporaries. But their search for the transcendent leads them down a dangerous path, beyond human constructs of morality.')
    book2 = Book(category_id= category1.id, bookName='Harry Potter and the Order of the Phoenix', image='FIIB7K(`TNO0$U`G]OB]FFK.png', author='Rowling, J. K', isbn='0439358078', price='7.76', description='A popular fiction')
    book3 = Book(category_id= category1.id, bookName='Gone With the Wind', image='OQQ34NIBJSC@`4A8)W9GAOY.png', author='Bartel, Pauline', isbn='1493036130', price='16.99', description='Classic romantic fiction')
    book4 = Book(category_id= category3.id, bookName='The Science Book', image='OICAPKXM~18T0V8H$J3MIXL.png', author='DK', isbn='9781409350156', price='32.75', description='Discover 80 trail-blazing scientific ideas, which underpin our modern world, giving us everything from antibiotics to gene therapy, electricity to space rockets and batteries to smart phones.')
    book5 = Book(category_id= category3.id, bookName='Pearson Science 8', image='$GM$MQL8{9T5ZI]1G$~2BXI.png', author='Greg Rickard, Warwick Clarke, Jacinta Devlin', isbn='9781488615061', price='17.75', description='The Pearson Science Second Edition Activity Book is a write-in resource designed to develop and consolidate students’ knowledge and understanding of science by providing a variety of activities and questions to apply skills, reinforce learning outcomes and extend thinking.')
    book6 = Book(category_id= category2.id, bookName='History', image='JOR3)9(_@BAGE@FQKR5KT48.png', author='DK', isbn='9780241515266', price='35.75', description='A comprehensive, up-to-date, world history reference book for families')
    
    try:
        db.session.add(book1)
        db.session.add(book2)
        db.session.add(book3)
        db.session.add(book4)
        db.session.add(book5)
        db.session.add(book6)
        db.session.commit()
    except:
        return 'There was an issue when adding the books in dbseed function'
    
    return 'DATA LOADED'