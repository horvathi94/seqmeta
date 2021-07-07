const hostsTable = document.getElementById("hosts-table").tBodies[0];
const hostsTemplate = hostsTable.getElementsByClassName("template")[0];

function addNewHost(){

	let indx = 0;
	let newIndx = 0;
	for ( let i=1; i<hostsTable.rows.length; i++){
		indx = Number(hostsTable.rows[i].cells[0].getElementsByTagName("input")[0].getAttribute("name").split("+")[1]);
		if ( indx > newIndx ){ newIndx = indx; }
	}

	let cloned = hostsTemplate.cloneNode(true);
	const rowIndx = hostsTable.rows.length - 1;
	cloned.style.visibility = "visible";
	const indxCell = cloned.cells[0].getElementsByTagName("input")[0];
	indxCell.setAttribute("name", "hosts+"+rowIndx+"+indx");
	indxCell.value = newIndx+1;
	cloned.cells[1].getElementsByTagName("input")[0].setAttribute("name", "hosts+"+rowIndx+"+label");
	cloned.cells[2].getElementsByTagName("input")[0].setAttribute("name", "hosts+"+rowIndx+"+latin");

	hostsTable.appendChild(cloned);


}
