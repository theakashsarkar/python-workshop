import csv
field_name = ["Name", "Author", "Publisher", "Price", "Category"]
book1 = {"Name":"Computer Programming part 1", "Author": "Tamim Shahriar Subeen", "Publisher": "Onnorokom Prokashoni", "Price": "240.00", "Category": "Programming"}
book2 = {"Name":"Computer Programming part 2", "Author": "Tamim Shahriar Subeen", "Publisher": "Onnorokom Prokashoni", "Price": "250.00", "Category": "Programming"}
book3 = {"Name":"Computer Programming part 3", "Author": "Tamim Shahriar Subeen", "Publisher": "Onnorokom Prokashoni", "Price": "200.00", "Category": "Programming"}

book_list = [book1, book2, book3]
with open("book_list.csv", "w") as csvf:
    csv_writer = csv.DictWriter(csvf, fieldnames=field_name)
    # csv_writer.writeheader()
    csv_writer.writeheader()
    csv_writer.writerows(book_list)


with open('books.csv', newline='') as csvf:
    csv_reader = csv.reader(csvf)
    for row in csv_reader:
        print(row)