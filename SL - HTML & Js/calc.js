function multiply()
		{
		     var num1 = parseFloat(document.getElementById("first").value);
		    var num2 = parseFloat(document.getElementById("second").value);
		    if(num1 && num2){
			document.getElementById("result").innerHTML = num1 * num2;
			}
		    else{
			document.getElementById("result").innerHTML = "INVALID";
  			}
 		}

		function add()
		{
		    var num1 = parseFloat(document.getElementById("first").value);
		    var num2 = parseFloat(document.getElementById("second").value);
		    if(num1 && num2){
			document.getElementById("result").innerHTML = num1 + num2;
			}
		    else{
			document.getElementById("result").innerHTML = "INVALID";
  			}
		}
		
		function divide()
		{
		     var num1 = parseFloat(document.getElementById("first").value);
		    var num2 = parseFloat(document.getElementById("second").value);
		    if(num1 && num2){
			document.getElementById("result").innerHTML = num1 / num2;
			}
		    else if(num2 == 0){
			document.getElementById("result").innerHTML = "INVALID-Division by zero error";
  			}
		    else{
			document.getElementById("result").innerHTML = "INVALID";
  			}

 		}

		function subtract()
		{
		      var num1 = parseFloat(document.getElementById("first").value);
		    var num2 = parseFloat(document.getElementById("second").value);
		    if(num1 && num2){
			document.getElementById("result").innerHTML = num1 - num2;
			}
		    else{
			document.getElementById("result").innerHTML = "INVALID";
  			}
		}
