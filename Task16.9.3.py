class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.'
    def get_info(self):
        return f'{self.name} {self.surname}, г.{self.city}'

client_1 = Client('Иван', 'Петров', 'Москва', 50)
client_2 = Client('Сергей', 'Кожин', 'Иркутск', 27)
client_3 = Client('Анатолий', 'Иванов', 'Сургут', 65)

print(client_1)

all_clients = [client_1, client_2, client_3]
for client in all_clients:
    print(client.get_info())