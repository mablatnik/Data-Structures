# python3
# direct access hash table scheme


class PhoneBook:
    def __init__(self):
        self.contacts = [None] * 10000000

    def add(self, number, name):
        self.contacts[number] = name

    def delete(self, number):
        if self.contacts[number] is not None:
            self.contacts[number] = None

    def find(self, number):
        if self.contacts[number] is None:
            return "not found"
        return self.contacts[number]


def process_queries(x):
    for query in x:
        request = query.split()
        cmd = request[0]
        number = int(request[1])
        if cmd == "add":
            phone_book.add(number, request[2])
        if cmd == "find":
            print(phone_book.find(number))
        if cmd == "del":
            phone_book.delete(number)


if __name__ == '__main__':
    phone_book = PhoneBook()

    n = int(input())
    queries = [input() for i in range(n)]
    process_queries(queries)
