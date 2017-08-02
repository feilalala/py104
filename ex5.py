my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about {}".format(my_name))
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line in tricky, try to get in exectly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, {my_weight} I get {total}.")
# foget f f for "format" tell python3,"Hey ,this string needs to be formatted.Put these variables in there"
