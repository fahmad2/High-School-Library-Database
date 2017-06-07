from track.models import Borrower, Book

#Initialize Borrowers:
ali = Borrower(name='Ali')
ali.save()

#Initialize Books:
hp1 = Book(title='Harry Potter1', author='JK Rowling',ISBN='9788499301511')
hp1.save()
hp2 = Book(title='Harry Potter2', author='JK Rowling',ISBN='9788499301512')
hp2.save()
hp3 = Book(title='Harry Potter3', author='JK Rowling',ISBN='9788499301513')
hp3.save()
hp4 = Book(title='Harry Potter4', author='JK Rowling',ISBN='9788499301514')
hp4.save()
hp5 = Book(title='Harry Potter5', author='JK Rowling',ISBN='9788499301515')
hp5.save()
hp6 = Book(title='Harry Potter6', author='JK Rowling',ISBN='9788499301516')
hp6.save()
hp7 = Book(title='Harry Potter7', author='JK Rowling',ISBN='9788499301517')
hp7.save()
