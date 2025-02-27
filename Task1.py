#Part1 Personal Information
name="Umme Habiba"
gender="Female"
age=20
address="Sangla Hill"
degree="BSCS"
dob="07October2004"
email="habiba@gmail.com"
print("Name: ", name)
print("Gender: ", gender)
print("Age: ", age)
print("Address: ", address)
print("Degree: ", degree)
print("Date-of-Birth: ", dob)
print("Email: ", email)

#Part2 Type casting while swaping two variables
val1=10
val2="15"
print(type(val1))
print(type(val2))

# we cannot add string and integer so changing the type of val2
val2=int("15")
print(type(val2))

print(val1+val2)

#Part3 Variables with different DataTypes
name=str("Habiba")
age=int(20)
height=float(5)
male=bool(False)
print(type(name))
print(type(age))
print(type(height))
print(type(male))