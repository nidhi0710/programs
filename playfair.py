import string
#build matrix
def matrix(key):
	matrix=[]

	#adding key
	for i in key.lower():
		if i not in matrix: 
			matrix.append(i)

	add = string.ascii_lowercase[:26]
	add = add.replace(exclude,"")
	#adding remaining alphabets
	for i in add:
		if i not in matrix:
			matrix.append(i)
	if " " in matrix:
		matrix.remove(" ")

	split=[]
	for i in range(5):
		split.append("")
	#can exclude any letter in range of 5. excluding z here!
	split[0]=matrix[0:5]
	split[1]=matrix[5:10]
	split[2]=matrix[10:15]
	split[3]=matrix[15:20]
	split[4]=matrix[20:25]

	return split

def message_split(message):
	message_split=[]

	for i in message.lower():
		message_split.append(i)
		if " " in message_split:
			message_split.remove(" ")

	if (len(message_split) == 0):
		message_split.append("x")

	k = 0
	for i in range(len(message_split)-1):
		if(message_split[i] == message_split[i+1]):
			message_split.insert(i+1,"x")
		k = k+2

	if len(message_split)%2 == 1:
			message_split.append("x")

	return message_split

def enycrypt(message):
	final=[]
	a = matrix(key)
	e = message_split(message)
	m = int((len(e))/2)
	print(a)
	k=0
	for i in range(m):
		first = e[k]
		second = e[k+1]

		for i in range(5):
			for j in range(5):
				if(a[i][j] == first):
					x1=i
					y1=j
				if(a[i][j] == second):
					x2=i
					y2=j

		if(x1 == x2):
			if(y1 == 4):
				y1= -1
			if(y2 == 4):
				y2=-1
			final.append(a[x1][y1+1])
			final.append(a[x1][y2+1])

		elif(y1 == y2):
			if(x1 == 4):
				x1= -1
			if(x2 == 4):
				x2=-1
			final.append(a[x1+1][y1])
			final.append(a[x2+1][y1])

		else:
			final.append(a[x1][y2])
			final.append(a[x2][y1])

		k=k+2

	z=''.join(final)
	return z

def decrypt(message):
	final=[]
	a = matrix(key)
	e = []
	for i in message:
		e.append(i)
	m = int((len(e))/2)
	k=0
	for i in range(m):
		first = e[k]
		second = e[k+1]

		for i in range(5):
			for j in range(5):
				if(a[i][j] == first):
					x1=i
					y1=j
				if(a[i][j] == second):
					x2=i
					y2=j

		if(x1 == x2):
			if(y1 == 0):
				y1 = 5
			if(y2 == 0):
				y2 = 5
			final.append(a[x1][y1-1])
			final.append(a[x1][y2-1])

		elif(y1 == y2):
			if(x1 == 0):
				x1= 5
			if(x2 == 0):
				x2= 5
			final.append(a[x1-1][y1])
			final.append(a[x2-1][y1])

		else:
			final.append(a[x1][y2])
			final.append(a[x2][y1])

		k=k+2

	z=''.join(final)
	return z

key = input("Input your key")
message= input("Type message")
exclude= input("Input the letter you want to exclude(should not be a part of key or message!)")
e_text = enycrypt(message)
print("Key is: \t" + key)
print("Plain Text is:\t" + message)
print("Encrypted text:\t" +e_text)
print("Decrypted text:\t" +decrypt(e_text))
