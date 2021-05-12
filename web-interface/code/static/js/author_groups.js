console.log("Hello Fucker!");

function addAuthorToGroup(){
	
	const empty = document.getElementById("editor-empty");
	const editor = document.getElementById("editor");
	let entries = document.getElementsByClassName("editor-entry");

	newAuthor = empty.cloneNode(true);


	maxOrder = 0;
	[...entries].forEach(entry => {
		let order = entry.getElementsByClassName("order")[0].value;
		if ( order > maxOrder ){
			maxOrder = parseInt(order);
		}
	});

	console.log("Max. order: " + maxOrder);

	newAuthor.style.display = "block";
	newAuthor.style.color = "red";
	newAuthor.classList.add("editor-entry");
	newAuthor.classList.remove("editor-empty");
	
	newOrder = newAuthor.getElementsByClassName("order")[0];
	newOrder.value = maxOrder + 1;
	newOrder.classList.remove("empty");

	newName = newAuthor.getElementsByClassName("authorid")[0];
	newName.classList.remove("empty");
	elementName = "author+" + String(entries.length+1) + "+author_id";
	newName.setAttribute("name", elementName);

	editor.appendChild(newAuthor);

};


function sendData(){

	let xhr = new XMLHttpRequest();
	let url = "/authors/groups/submit";
	xhr.open("POST", url, true);
	xhr.setRequestHeader("Content-Type", "apliccation/json");
	xhr.onreadystatechange = function() {
		if ( xhr.readyState == 4  && xhr.status == 200 ){
			console.log("State ok");
		}
	}

	let data = JSON.stringify({"test": "value"});
	xhr.send(data);

};



