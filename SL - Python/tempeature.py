def celciustofarenhiet(c):
	return (c*(9/5) + 32)

def farenhiettocelcius(p):
	return ((p-32)*(5/9))
	
def celciustokelvin(x):
	return (x+273.15)
	
def kelvintocelcius(y):
	return (y-273.15)

def farenhiettokelvin(a):
	return celciustokelvin(farenhiettocelcius(a))
	
def kelvintofarenhiet(b):
	return celciustofarenhiet(kelvintocelcius(b))
	
