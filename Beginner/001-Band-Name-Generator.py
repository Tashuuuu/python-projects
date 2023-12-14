print("Welcome to the Band Name Generator.")

# This funtion is completely optional.
def capitalize(a):
  capital = a[0:1].upper() + a[1:]
  return capital

city_name = input("Name of the city you grew up in? \n")
pet_name = input("What's your pet's name? \n")

print("Your band name could be " + capitalize(city_name) + capitalize(pet_name))

# Without using funtion we can use below code:
# print("Your band name could be " + city_name + pet_name)