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


	editor.appendChild(newAuthor);

};
