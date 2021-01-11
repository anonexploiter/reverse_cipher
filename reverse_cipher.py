message = input("what is the message which you want to encrypt: ")

translate = ""

x=len(message) - 3

while x >=0:
	translate = translate +message[x]
	x = x - 1

	
print(translate)
