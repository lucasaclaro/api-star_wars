import requests
import tkinter
from tkinter import *



##### Code


#print(character_name)
#print(character_height)
#print(character_mass)
#print(character_hair_color)
#print(character_skin_color)
#print(character_eye_color)
#print(character_homeworld)
#print(character_birthyear)

#if owns_vehicle == 0:
#    print('Vehicle: unknown')
#else:
#    character_vehicle = f"Vehicle: {requests.get(request_json['vehicles'][0]).json()['name']}"
#    print(character_vehicle)



##### Windows
master = Tk()
master.title('Star Wars')
master.geometry('1260x800+250+100')
master.minsize(1260, 800)
master.maxsize(1260, 800)
background = PhotoImage(file='images/background.png')
background_master = Label(master, image=background)
background_master.pack()

entry_number = Entry(master, font=('Verdana', 8, 'bold'), bg='#B8B4B4', fg='#000000', justify=CENTER)
entry_number.insert(0, '10')
entry_number.place(width=100, height=30, x=175, y=250)

character_id = str((entry_number).get())
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

if owns_ship == 0:
    print('Starship: unknown')
else:
    character_starship = f"Starship: {requests.get(request_json['starships'][0]).json()['name']}"
    print(character_starship)
######



if owns_ship == 0:
    result = Label(master, text=f'{character_name}\n\n\n {character_height}\n\n {character_mass}\n\n {character_hair_color}\n\n {character_skin_color}\n\n {character_eye_color}\n\n {character_homeworld}\n\n {character_birthyear}\n\n Starship: unknown', font=('Verdana', 14, 'bold'), fg='white', background='black')
    result.place(width=780, height=600, x=240, y=150)
else:
    result = Label(master, text=f'{character_name}\n\n\n {character_height}\n\n {character_mass}\n\n {character_hair_color}\n\n {character_skin_color}\n\n {character_eye_color}\n\n {character_homeworld}\n\n {character_birthyear}\n\n {character_starship}',font=('Verdana', 14, 'bold'), fg='white', background='black')
    result.place(width=780, height=600, x=240, y=150)










master.mainloop()






