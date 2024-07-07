# variabel can used
""" firstname
    lastname
    age
    country
    city
    first_name
    last_name
    capital_city
    _if # if we want to use reserved word as a variable
    year_2021
    year2021
    current_year_2021
    birth_year
    num1
    num2 """

# Variables in Python
first_name = "Adam"
last_name = "Hidayat"
country = "Indonesia"
city = "wonowowo"
age = 1800
is_married = False
skills = ['Machine Learning', 'Tensorflow', 'Python', 'Pytorch', 'Keras']
person_info = {
    'name': "Adam",
    'country': 'Indonesia',
    'city' : 'Purwokerto',
    'age' : 18
}

# print with 2 argument or more
# 1. with comma to separated
print("hasil dari 3 + 4 adalah", 3 + 4)
# 2. using f string
print(f"hasil dari 3 + 4 adalah {3 + 4}")

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)