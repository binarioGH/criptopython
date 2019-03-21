function translate(key, text, doe){
	var abc = "abcdefghijklmnopqrstuvwxyz";
	var bannedChars="<>%"
	var char = "";
	var translatedText = "";
	var letterIndex = 0;
	for(var index=0;index<text.length;index++){
		char = text[index]; 
		letterIndex = abc.indexOf(char);
		console.log("Inicial: "+letterIndex);
		if(char == char.toUpperCase()){
			char = char.toLowerCase();
		}
		if(letterIndex == -1){
			if(bannedChars.indexOf(char) != -1){
				continue;
			}
			else{
				translatedText += char;
			}
		}
		else{
			if(doe == "e"){
				letterIndex -= key;
				console.log("e: " + letterIndex);
			}
			else{
				letterIndex += key;
				console.log("d: " + letterIndex);
			}
			if(letterIndex<0){
				letterIndex += abc.length;
				console.log("sum: " +letterIndex);
			}
			if(letterIndex>= abc.length){
				letterIndex-=abc.length;
				console.log("mod: " + letterIndex);
			}
			translatedText += abc[letterIndex];
			console.log("Final: "+letterIndex);
		}
	}
	return translatedText;
}


var key = document.getElementById("key");
var text = document.getElementById("text");
var ecryt = document.getElementById("encrypt");
var dcrypt = document.getElementById("decrypt");
var translated = document.getElementById("translated"); 
encrypt.addEventListener("click", function(){
	k = parseInt(key.value);
	t = text.value;
	if(isNaN(k) || t == ""){
		alert("Debes de ingresar valores en todos los campos"); 
		return 0;	
	}
	else{
		translated.innerHTML = translate(k, t, "e");
	}
});
decrypt.addEventListener("click", function(){
	k = parseInt(key.value);
	t = text.value;
	if(isNaN(k) || t == ""){
		alert("Debes de ingresar valores en todos los campos"); 
		return 0;	
	}
	else{
		translated.innerHTML = translate(k, t, "d");
	}
});
