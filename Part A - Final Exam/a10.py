Student={123:"Sneha",124:"Shri",125:"Shashu",126:"Swathi",127:"Venky"}
print(Student)

for key in Student.keys():
	if key%2==0:
		print(key,Student[key])
