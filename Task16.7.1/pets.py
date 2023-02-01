from pet_class import Pet
import json

with open('all_pets.json', encoding='utf8') as file:
    pets_json = json.load(file)

pets_list = pets_json['results']
print(pets_list)

i = 1
for pet_dict in pets_list:
    name = pet_dict.get('name')
    gender = pet_dict.get('gender').get('name')
    age = pet_dict.get('age')
    breed = pet_dict.get('breed').get('name')
    pet = Pet(name, gender, age, breed)
    print(f'''Животное {i}''')
    print(f'''Имя: {pet.name}\nПол: {pet.gender}\nВозраст: {pet.age}\nПорода: {pet.breed} \n''')
    i += 1