const agTable = document.getElementById("author-group-editor").tBodies[0];
const agTemplate = agTable.getElementsByClassName("editor template")[0];

function addAuthorToGroup(){

	const cloned = agTemplate.cloneNode(true);
	
	let newIndx = 0;
	let indx;
	for (let i=1; i<agTable.rows.length; i++){
		indx = Number(agTable.rows[i].getElementsByClassName("orderindx")[0].value);
		if (indx > newIndx){ newIndx = indx; }
	}

	newIndx += 1;
	const rowIndx = agTable.rows.length-1;
	const oIndx = cloned.cells[0].getElementsByTagName("input")[0];
	oIndx.setAttribute("name", "author+"+String(rowIndx)+"+order_index");
	oIndx.value = newIndx;
	cloned.cells[1].getElementsByTagName("select")[0].setAttribute("name", "author+"+String(rowIndx)+"+author_id");

	agTable.appendChild(cloned);
	cloned.style.visibility	= "visible";

};

