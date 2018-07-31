enyc = input("your message")
key = input("enter key")
enycarray = list(enyc)
new = []
for i in range(0,len(enycarray)):
	if(enycarray[i].isupper()):
		new.append(chr((ord(enycarray[i]) + int(key) - 65) % 26 + 65))

	elif(enycarray[i].isdigit()):
		new.append(chr(((ord(enycarray[i])+int(key)) - 48) % 10 + 48))
	
	elif(enycarray[i].isalpha()):
		new.append(chr((ord(enycarray[i]) + int(key)-97) % 26 + 97))

	else:
		new.append(" ")

final_enyc1 = ''.join(new)

print(final_enyc1)

final_enyc = list(final_enyc1)
new1 = []

for i in range(0,len(final_enyc)):
	if(final_enyc[i].isupper()):
		new1.append(chr((ord(final_enyc[i]) - int(key) - 65) % 26 + 65))

	elif(final_enyc[i].isdigit()):
		new1.append(chr(((ord(final_enyc[i])-int(key)) - 48) % 10 + 48))
	
	elif(final_enyc[i].isalpha()):
		new1.append(chr((ord(final_enyc[i]) - int(key) - 97) % 26 + 97))

	else:
		new1.append(" ")

final_dec = ''.join(new1)
print(final_dec)