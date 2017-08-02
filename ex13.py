from sys import argv #没理解什么意思 sys是系统默认的模块 argv（argument varibles）
#
script, first, second, third = argv #unpack

print("The script is called:", script)
age = input("How old are you?")
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
