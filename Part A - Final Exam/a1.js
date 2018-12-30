function check1(){
			var x = document.getElementById("num").value;
			if(x%3==0 && x%7==0)
				document.getElementById("res").innerHTML =  "Divisible by 3 and 7";
			else if(x%3==0 && x%7!=0)
				document.getElementById("res").innerHTML =  "Divisible by only 3 and not 7";
			else if(x%3!=0 && x%7==0)
				document.getElementById("res").innerHTML =  "Divisible by only 7 and not 3";
			else
				document.getElementById("res").innerHTML =  "Not divisible by both 3 or 7";
		}
