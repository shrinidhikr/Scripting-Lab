from flask import Flask, redirect, render_template, request, url_for
import time #time and date related functions
import re  #regular expressions

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def indexJS():
	if request.method == "GET":
		return render_template("indexJS.html")

	if request.method == "POST":

		#Check if form fields are empty
		if request.form["usn"] == "" or request.form["dob"] == "" :
			msg = "***All form fields are required***"
			return render_template("indexJS.html", msg=msg)

		#Check if date entered in dd/mm/yyyy format and is not an invalid date Eg. 31/11/2016
		#Use strptime() function which raises an exception if date is invalid
		try:
			time.strptime(request.form["dob"],"%d/%m/%Y")
		except ValueError:
			msg = "***Date is invalid***"
			return render_template("indexJS.html", msg=msg)

		#Regex for USN
		usn_pattern = "^[1][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$"

		#Check if entered USN matches Regex
		if not re.match(usn_pattern, request.form["usn"]) :
			msg = "***USN format invalid***"
			return render_template("indexJS.html", msg=msg)

		#If form fields are valid return success HTML page
		return render_template("success.html")

if __name__ == '__main__':
	app.run()
