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


function addRow(){
	const row = detailsTable.insertRow();
	const propCell = row.insertCell(0);
	propCell.classList.add("prop");
	const valCell = row.insertCell(1);
	valCell.classList.add("value");
	return [propCell, valCell];
}

function updateTable(sample){

	let cells = [];

	cells = addRow();
	cells[0].innerHTML = "Sample ID:";
	cells[1].innerHTML = sample.sample_id;

	cells = addRow();
	cells[0].innerHTML = "Sample name:";
	cells[1].innerHTML = sample.sample_name;

	cells = addRow();
	cells[0].innerHTML = "Collection date:";
	cells[1].innerHTML = sample.collection_date;

	cells = addRow();
	cells[0].innerHTML = "Originating laboratory:";
	cells[1].innerHTML = sample.originating_lab_name;

	cells = addRow();
	cells[0].innerHTML = "Submitting laboratory:";
	cells[1].innerHTML = sample.submitting_lab_name;

	cells = addRow();
	cells[0].innerHTML = "Passage details:";
	cells[1].innerHTML = sample.passage_details;

	cells = addRow();
	cells[0].innerHTML = "Sampling strategy:";
	cells[1].innerHTML = sample.sampling_strategy;

	cells = addRow();
	cells[0].innerHTML = "Location:";
	cells[1].innerHTML = sample.location;

	cells = addRow();
	cells[0].innerHTML = "Additional location information:";
	cells[1].innerHTML = sample.additional_location_info;

	cells = addRow();
	cells[0].innerHTML = "Author group:";
	cells[1].innerHTML = sample.author_group_name + " ("+sample.authors_list+")";

	cells = addRow();
	cells[0].innerHTML = "Host:";
	cells[1].innerHTML = sample.host;

	cells = addRow();
	cells[0].innerHTML = "Additional host information";
	cells[1].innerHTML = sample.additional_host_info;

	cells = addRow();
	cells[0].innerHTML = "Patient age:";
	cells[1].innerHTML = sample.patient_age;

	cells = addRow();
	cells[0].innerHTML = "Patient gender:";
	cells[1].innerHTML = sample.patient_gender;

	cells = addRow();
	cells[0].innerHTML = "Patient status:";
	cells[1].innerHTML = sample.patient_status;

	cells = addRow();
	cells[0].innerHTML = "Sequencing technology:";
	cells[1].innerHTML = sample.sequencing_technology;

	cells = addRow();
	cells[0].innerHTML = "Assembly method:";
	cells[1].innerHTML = sample.assembly_method;
	
	cells = addRow();
	cells[0].innerHTML = "Coverage:";
	cells[1].innerHTML = sample.coverage;

}


function updateTableOld(data){
	
	Object.entries(data).forEach(([key, value]) => {
		
		let row = detailsTable.insertRow();

		let propCell = row.insertCell(0);
		propCell.classList.add("prop");
		propCell.innerHTML = key + ":";

		let valueCell = row.insertCell(1);
		valueCell.classList.add("value");
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
