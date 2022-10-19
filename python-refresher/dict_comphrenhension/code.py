users = [
    (0, 'Yogeshwar', 'password'),
    (1, 'Danush', 'user'),
    (2, 'Uma', 'Admin'),
    (3, 'Prathyu', 'MD')
]
# dict comphrehension with username key[position]: values
username_mapping = {user[1]: user for user in users}
print(username_mapping)

user_name_input = input('Enter your username :')
password_input = input('Enter your password :')


# passing username from user as key to dict - login functionality
_, username, password = username_mapping[user_name_input]

if password_input == password:
    print('Authenticated !')
else:
    print('Invalid user!')
