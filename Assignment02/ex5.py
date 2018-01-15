name = 'Zed A. Shaw'
inches_to_cm = 2.74
lbs_to_kg = 0.453592
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
#This converts height from inches to cm
height_metric = height * inches_to_cm

#This converts weight from lbs to kg
weight_metric = weight * lbs_to_kg

eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {height_metric} cm tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {weight_metric} kilograms heavy.")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
