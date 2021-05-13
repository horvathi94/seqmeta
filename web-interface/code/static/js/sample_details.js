const apiUrlBase = "/sample/details?id=";
const promptWrap = document.getElementsByClassName("prompt", "wrap")[0];
const detailsDiv = document.getElementById("sample-details");
const detailsTable = document.getElementById("sample-details-table");

function closePrompt(){
	promptWrap.style.display = "none";
}

async function fetchDetails(sampleID){
	
	let apiUrl = apiUrlBase + sampleID;
	const response = await fetch(apiUrl);

	if (response.ok){
		promise = await response.json();
	} else {
		alert("Error fetching details.");
	}

	return promise;

}


function updateTable(data){
	
	Object.entries(data).forEach(([key, value]) => {
		
		let row = detailsTable.insertRow();

		let propCell = row.insertCell(0);
		propCell.classList.add("prop");
		propCell.innerHTML = key + ":";

		let valueCell = row.insertCell(1);
		valueCell.innerHTML = value;

	});


};



function displayDetails(sampleID){

	promptWrap.style.display = "block";
	
	let promise = fetchDetails(sampleID);
	promise.then( res => {updateTable(res);} );

};



function clearTable(){

	rowsCount = detailsTable.rows.length;
	for (let i = 0; i < rowsCount; i++ ) {
		detailsTable.deleteRow(0);
	}

}

function hideDetails(){
	closePrompt();
	clearTable();
}
