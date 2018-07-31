import string
import os

key_matrix=[]

#build matrix
def matrix(key):
	matrix=[]

	#adding key
	for i in key.lower():
		if i not in matrix: 
			matrix.append(i)

	add = string.ascii_lowercase[:26]
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

	m = int((len(message_split))/2)
	k = 0
	for i in range(m):
		if(message_split[k] == message_split[k+1]):
			message_split.insert(k+1,"x")
		k = k+2

		if len(message_split)%2 == 1:
			message_split.append("x")

	return message_split

def enycrypt(message):
	final=[]
	a = matrix(key)
	print(a)
	e = message_split(message)
	print(e)
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

		print(x1,x2,y1,y2)

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

	print(final)

def decrypt(message):
	final=[]
	a = matrix(key)
	print(a)
	e = message_split(message)
	print(e)
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

		print(x1,x2,y1,y2)

		if(x1 == x2):
			if(y1 == 0):
				y1= 5
			if(y2 == 0):
				y2= 5
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

	print(final)


select= input("enter 1 to enycrypt and 2 to decrypt")
print(select)

key = input("input your key")
message= input("type message")

if select == "1":
	enycrypt(message)
elif select == "2":
	decrypt(message)
else:
	print("wrong option")



