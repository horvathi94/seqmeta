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

	newAuthor.style.display = "block";
	newAuthor.style.color = "red";
	newAuthor.classList.add("editor-entry");
	newAuthor.classList.remove("editor-empty");
	
	newOrder = newAuthor.getElementsByClassName("order")[0];
	newOrder.value = maxOrder + 1;
	newOrder.classList.remove("empty");
	newOrderName = "author+" + String(entries.length+1) + "+order_index";
	newOrder.setAttribute("name", newOrderName);

	newName = newAuthor.getElementsByClassName("authorid")[0];
	newName.classList.remove("empty");
	elementName = "author+" + String(entries.length+1) + "+author_id";
	newName.setAttribute("name", elementName);

	editor.appendChild(newAuthor);

};

