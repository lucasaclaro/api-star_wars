import requests


print('Star Wars characters\n')
character_id = int(input('Choose a number between 1 and 82 for a character: '))
while character_id > 82:
    character_id = int(input('Choose a number between 1 and 82 for a character: '))

link = f'https://swapi.dev/api/people/{character_id}'
request = requests.get(link)
request_json = request.json()
character_name = f"{request_json['name']}"
character_height = f"Height: {request_json['height']}"
character_mass = f"Mass: {request_json['mass']}"
character_hair_color = f"Hair color: {request_json['hair_color']}"
character_skin_color = f"Skin color: {request_json['skin_color']}"
character_eye_color = f"Eye color: {request_json['eye_color']}"
character_homeworld = f"Home World: {requests.get(request_json['homeworld']).json()['name']}"
character_birthyear = f"Birth year: {request_json['birth_year']}"
owns_ship = len(request_json['starships'])
owns_vehicle = len(request_json['vehicles'])

print(character_name)
print(character_height)
print(character_mass)
print(character_hair_color)
print(character_skin_color)
print(character_eye_color)
print(character_homeworld)
print(character_birthyear)

if owns_ship == 0:
    print('Starship: unknown')
else:
    character_starship = f"Starship: {requests.get(request_json['starships'][0]).json()['name']}"
    print(character_starship)























