mystrings=["I am going home at 12","I am tired","I live 12kms away","Give me 1 packet","Rs14 for 1 dosa"]
print(mystrings)

for i in range(len(mystrings)):
	if i%2==0:
		print("At index", i ,mystrings[i])

for i in range(len(mystrings)):
	if i%3==0:
		mystrings[i]=mystrings[i].upper()
print(mystrings)

for i in range(len(mystrings)):
	mystrings[i]=" ".join(reversed(mystrings[i].split()))
print("On reversal",mystrings)

num=[]
for i in range(len(mystrings)):
	for s in mystrings[i].split():
		 if s.isdigit():
		 	num.append(s)
		 	
print(num)
