const apiUrlBase = "/samples/details?id=";
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


function addRow(propHTML="", valueHTML=""){
	const row = detailsTable.insertRow();
	const propCell = row.insertCell(0);
	propCell.classList.add("prop");

	if (propHTML){
		propCell.innerHTML = propHTML + ":";
	}

	const valCell = row.insertCell(1);
	valCell.classList.add("value");
	valCell.innerHTML = valueHTML;
	
	return [propCell, valCell];
}




function updateTable(sample){

	let cells = [];

	cells = addRow("Sample name", sample.sample_name);
	cells = addRow("Sample comment", sample.sample_comment);
	cells = addRow("Patient", sample.patient_details);
	cells = addRow("Collection date", sample.collection_date);
	cells = addRow("GISAID virusname", sample.gisaid_details);
	cells = addRow("Isolate name", sample.isolate);
	cells = addRow("Location", sample.location_details);
	cells = addRow("Collector name", sample.collector_name);

	cells = addRow("Originating laboratory", sample.originating_lab_details);
	cells = addRow("Submitting laboratory", sample.submitting_lab_details);
	cells = addRow("Authors", sample.authors_details);


	cells = addRow("Ilness", sample.ilness_details);
	cells = addRow("Antiviral treatment", sample.antiviral_treatment_details);
	cells = addRow("Hospitalisation", sample.hospitalization);
	cells = addRow("Disease outcome", sample.host_disease_outcome);
	cells = addRow("Vaccination details", sample.vaccination_details);
	cells = addRow("Prior SARS-CoV-2 infection", sample.prior_infection_details);


	cells = addRow("Sampling strategy", sample.sampling_strategy);
	cells = addRow("Purpose of sampling", sample.purpose_of_sampling);
	cells = addRow("Purpose of sequencing", sample.purpose_of_sequencing);

	cells = addRow("Sequencing instrument", sample.instrument_details);
	cells = addRow("Assembly method", sample.assembly_method);
	cells = addRow("Coverage", sample.coverage);
	
	

	cells = addRow("Library ID", sample.library_id);
	cells = addRow("Library", sample.library_details);

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
};


function hideDetails(){
	closePrompt();
	clearTable();
};
