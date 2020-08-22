

id = 40;

getName();
getExp();
getPoder();
getPoder2();

function getName(data){		
	$.getJSON("https://pokeapi.co/api/v2/pokemon/"+ id +"/", function(data){
		document.getElementById("dado").innerHTML = data['name'];
	});
}

function getExp(data){		
	$.getJSON("https://pokeapi.co/api/v2/pokemon/"+ id +"/", function(data){
		document.getElementById("xp").innerHTML = data['base_experience'];
	});
}

function getPoder(data){		
	$.getJSON("https://pokeapi.co/api/v2/pokemon/"+ id +"/", function(data){
		document.getElementById("power").innerHTML = data['types'][0]['type']['name'];
	});
}

function getPoder2(data){
	$.getJSON("https://pokeapi.co/api/v2/pokemon/"+ id +"/", function(data){
		document.getElementById("power2").innerHTML = data['types'][1]['type']['name'];
	});
}