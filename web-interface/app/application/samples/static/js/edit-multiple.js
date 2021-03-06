const editor = document.getElementById("samples-editor").tBodies[0];
const templateRow = editor.getElementsByClassName("template")[0];


function addNewRow(){
	let newIndx = editor.rows.length - 2;
	let cloned = templateRow.cloneNode(true);
	cloned.classList.remove("template");
	cloned.style.visibility = "visible";
	let inp;
	Array.from(cloned.cells).forEach( (cell) => {
		Array.from(cell.querySelectorAll("input, select, textarea")).forEach( (inp) => {
			newName = inp.getAttribute("name").replace("0", newIndx);
			inp.setAttribute("name", newName);
		});
	});
	editor.appendChild(cloned);

	checkSampleNames();
}


function updateColumn(e){
	className = e.className;
	Array.from(editor.rows).slice(2).forEach( (row) => {
		row.getElementsByClassName(className)[0].setAttribute("value", e.value);
		row.getElementsByClassName(className)[0].innerHTML = e.value;
	});
}

function updateColumnSelect(e){
	className = e.className;
	Array.from(editor.rows).slice(2).forEach( (row) => {
		Array.from(row.getElementsByClassName(className)[0].options).forEach( (opt) => {
			if (opt.value == e.value) {opt.selected="selected";}
		} );
	});
}


function updateColumnRadio(e){
	className = e.className;
	Array.from(editor.rows).slice(2).forEach( (row) => {
		Array.from(row.getElementsByClassName(className)).forEach( (rb) => {
			if (rb.value == e.value) {rb.checked="checked";}
		});
	});
	
}


function removeRow(e){
	e.parentElement.parentElement.remove();
	checkSampleNames();
	if (!document.querySelectorAll("input[type=submit]")[0].disabled){
		checkLibraryNames();
	}
}
