the_book = input()
current_book = ''
amount_books = 0

while current_book != the_book:
    current_book = input()
    if current_book == 'No More Books':
        print(f'''The book you search is not here! 
You checked {amount_books} books.''');
        break
    amount_books += 1
if current_book == the_book:
    print(f'You checked {amount_books - 1} books and found it.')
