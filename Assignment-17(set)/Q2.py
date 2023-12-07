# Write a python program to store your own information {name, age, gender, so on..}

personal_info=[
    {'name':'utkarsh','age':21, 'gender':'Male'},
    {'name':'pandey','age':21, 'gender':'Male'},
]

for person in personal_info:
    print("Name :", person['name'])
    print("Age :", person['age'])
    print("Gender :", person['gender'])
    print()