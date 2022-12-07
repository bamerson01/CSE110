
most_chapters = 0
largest_book = ''

cannon_books = []
bom_books = []
ot_books = []

with open('books_and_chapters.txt') as file:
    for line in file:
        line = line.strip()
        line = line.split(':')
    
        book = line[0]
        chapter = int(line[1])
        cannon = line[2]
        
        if cannon not in cannon_books:
            cannon_books.append(cannon)
        if cannon == 'Book of Mormon':
             bom_books.append(book)

   
print('\nWhich Cannon are you interested in?')
for i, item in enumerate(cannon_books):
    print(f'{i+1}. {item}')
which_cannon = int(input('Type the number to learn more: '))
if book == cannon_books[which_cannon - 1]:
    print('yes')






























#         # print(f'Scripture: {cannon}, {book}: Chapters: {chapter}')

#         if chapter > most_chapters:
#             most_chapters = chapter
#             largest_book = book
#         if cannon == 'Book of Mormon':
#             bom_books.append(book)

# print(f'\nThe book of {largest_book} has the most chapters: {most_chapters} chapters.')


# books = ', '.join(bom_books)
# print(f'\nThe books in the Book of Mormon listed on one line: {books}')

# print(f'\nThe books of the Book of Mormon listed numerically:')
# for i, book in enumerate(bom_books):
#     print(f'{i+1}. {book}')

# print('\nWhich Cannon are you interested in?')
# for i, item in enumerate(cannon):
#     print(f'{i+1}. {cannon}')
# # which_cannon = input('Type the number to learn more: ')
# print(cannon)