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



function seqfileRow(seqfile, label){

	if (seqfile.filename == "") {
		string = "None";
	} else {
		string = seqfile.filename;
		if (seqfile.is_assembly){
			if (seqfile.assembly_method){
				string += " (assembled with: " + seqfile.assembly_method + ")";
			}
		} else {
			if (seqfile.is_forward_read){
				string += " (forward read)";
			}
			else{
				string += " (reverse read)";
			}
		}
	}

	addRow(label, string);
}


function updateTable(sample){

	addRow("Sample name", sample.sample_name);
	addRow("Sample comment", sample.sample_comment);
	addRow("Patient", sample.patient_details);
	addRow("Collection date", sample.collection_date);
	addRow("GISAID virusname", sample.gisaid_details);
	addRow("Isolate name", sample.isolate);
	addRow("Location", sample.location_details);
	addRow("Collector name", sample.collector_name);

	addRow("Originating laboratory", sample.originating_lab_details);
	addRow("Submitting laboratory", sample.submitting_lab_details);
	addRow("Authors", sample.authors_details);


	addRow("Ilness", sample.ilness_details);
	addRow("Antiviral treatment", sample.antiviral_treatment_details);
	addRow("Hospitalisation", sample.hospitalization);
	addRow("Disease outcome", sample.host_disease_outcome);
	addRow("Vaccination details", sample.vaccination_details);
	addRow("Prior SARS-CoV-2 infection", sample.prior_infection_details);


	addRow("Sampling strategy", sample.sampling_strategy);
	addRow("Purpose of sampling", sample.purpose_of_sampling);
	addRow("Purpose of sequencing", sample.purpose_of_sequencing);

	addRow("Sequencing instrument", sample.instrument_details);
	addRow("Coverage", sample.coverage);
	

	addRow("Library ID", sample.library_id);
	addRow("Library", sample.library_details);

	seqfileRow(sample.seqbunch.consensus, "Consensus");
	seqfileRow(sample.seqbunch.contigs, "Contigs");
	seqfileRow(sample.seqbunch.scaffolds, "Scaffolds");
	sample.seqbunch.reads.forEach( (r) => {
		seqfileRow(r, "Reads");
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
};


function hideDetails(){
	closePrompt();
	clearTable();
};
