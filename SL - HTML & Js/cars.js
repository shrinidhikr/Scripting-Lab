function call(i) {
var cars = JSON.parse(x);	
//document.getElementById("head1").addEventListener("click", headclickFunction(i));
	//function headclickFunction(i) {
		document.getElementById("label1").removeAttribute("hidden");
		var n = cars[i];
		//console.log(n.name);
		var k 
		for(k=0;k<3;k++)
		{
			document.getElementById("image"+(k+1)).setAttribute("hidden",true);
			document.getElementById("head"+(k+1)).innerHTML = "Car "+(k+1);
			//document.getElementById("image3").setAttribute("hidden",true);
	        }
		document.getElementById("head"+(i+1)).innerHTML = n.name;		
		document.getElementById("image"+(i+1)).removeAttribute("hidden");
		document.getElementById("image"+(i+1)).innerHTML = '<img src="'+n.image+'.jpg">';
		var l 
		for(l=0;l<3;l++)
		{
			document.getElementById("name"+(l+1)).innerHTML = " ";
		}
	//}
}
function ImgHover(i){
	var cars = JSON.parse(x);	
	var n = cars[i];
	document.getElementById("name"+(i+1)).innerHTML = "Car Model: "+n.model+"  "+"Price of Car: "+n.price+"  "+"Year of Production: "+n.year;
}
