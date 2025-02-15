def classify_books(*book_genres, **isbn_data):
    fiction_books = {}
    non_fiction_books = {}
    for genre, title in book_genres:
        if genre == "fiction":
            if title not in fiction_books.keys():
                fiction_books[title] = ""
        elif genre == "non_fiction":
            if title not in non_fiction_books.keys():
                non_fiction_books[title] = ""
    for isbn, title in isbn_data.items():
        if title in fiction_books.keys():
            fiction_books[title] = isbn
        elif title in non_fiction_books.keys():
            non_fiction_books[title] = isbn

    fiction_books_sorted = dict(sorted(fiction_books.items(), key=lambda x: x[1]))
    non_fiction_books_sorted = dict(sorted(non_fiction_books.items(), key=lambda x: x[1], reverse=True))
    result = []

    if fiction_books_sorted:
        result.append("Fiction Books:")
        for title, isbn in fiction_books_sorted.items():
            result.append(f"~~~{isbn}#{title}")
    if non_fiction_books_sorted:
        result.append("Non-Fiction Books:")
        for title, isbn in non_fiction_books_sorted.items():
            result.append(f"***{isbn}#{title}")

    return "\n".join(result)


# print(classify_books(
#     ("fiction", "Brave New World"),
#     ("non_fiction", "The Art of War"),
#     NF3421NN="The Art of War",
#     FF1234UU="Brave New World"
# ))
# print(classify_books(
#     ("non_fiction", "The Art of War"),
#     ("fiction", "The Great Gatsby"),
#     ("non_fiction", "A Brief History of Time"),
#     ("fiction", "Brave New World"),
#     FF1234HH="The Great Gatsby",
#     NF3845UU="A Brief History of Time",
#     NF3421NN="The Art of War",
#     FF1234UU="Brave New World"
# ))
# print(classify_books(
#     ("fiction", "Brave New World"),
#     ("fiction", "The Catcher in the Rye"),
#     ("fiction", "1984"),
#     FICCITRZZ="The Catcher in the Rye",
#     FIC1984XX="1984",
#     FICBNWYYY="Brave New World"
# ))
print(classify_books(
    ("non_fiction", "Sapiens"),
    ("non_fiction", "Homo Deus"),
    ("non_fiction", "The Selfish Gene"),
    NF123ABC="Sapiens",
    NF987XYZ="Homo Deus",
    NF456DEF="The Selfish Gene"
))
