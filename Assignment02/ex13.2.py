from sys import argv
script, name, job, university = argv

print(f"""So your name is {name}, you are a {job},
and you work at {university}!
good job, you are doing great!
""")

age = int(input(f"How old are you {name}?"))

Test_age = age < 100
print(f"This means that it is {Test_age} that you are younger than 100!")
