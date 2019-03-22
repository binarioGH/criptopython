function antiXSS(text){
	finalText = "";
	var banned = "<>"
	for(var char = 0;char<text.length;char++){
		if(banned.indexOf(text[char]) != -1){
			continue;
		}
		finalText += text[char];
	}
	return finalText;
}

function decode(key, text){
	var decoded = "";
	var abc = "abcdefghijklmnopqrstuvwxyz";
	var banned = "<>";
	var char = "";
	var index = 0;
	for(var i = 0;i<text.length;i++){
		char = text[i].toLowerCase();
		if(abc.indexOf(char) == -1){
			if(banned.indexOf(char) != -1){
				decoded += char;
			}
		}
		else{
			index = abc.indexOf(char) + key;
			if(index >= abc.length){
				index -= abc.length;
			}
			if(index < 0){
				index += abc.length;
			}
			decoded += abc[index];
		}
	}
	return decoded;
}
function hack(msj){
	text.innerHTML = "";
	var abc = "abcdefghijklmnopqrstuvwxyz";
	for(var i = 0; i<=26;i++){
		text.innerHTML += "<p class='hck'>"+ decode(abc.indexOf(i), msj) +"</p>";
	}
}
var cracked = document.getElementById("hackedTexts");
var text = document.getElementById("text");
var b = document.getElementById("send");
b.addEventListener("click", function(){
	t = text.value;
	t = antiXSS(t);
	hack(t);
})