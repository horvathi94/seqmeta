async function fetchSampleData(sampleID){

	const resp = await fetch("/samples/view/import?id="+sampleID);
	if (resp.ok){
		promise = await resp.json();
	} else {
		alert("Error fetching sample data!");
	}
	return promise;

}



const importer = document.getElementById("import-from-sample");


function importDataFromOtherSample(){

	let inp;

	fetchSampleData(importer.value).then( (sampleData) => {

		Object.keys(sampleData).filter( (className) => className != "sample_id" ).forEach( (className) => {
		
			inp = templateRow.getElementsByClassName(className)[0];
			console.log(className);
			console.log(inp.type);

		});

	});


	/*
	const selector = document.getElementById("import-from-sample");
	const templateRow = document.getElementById("samples-editor").getElementsByClassName("template row")[0];
	const selectorClasses = ["collector-name", "continent", "country", "geo-loc-exposure",
		"host", "patient-status", "host-behaviour-id", "host-habitat-id",
		"collection-device", "host-anatomical-material", "host-body-product",
		"prior-sars-cov-2-vaccination-id", "host-health-state", "ilness-disease-outcome",
		"sars-cov-2-diag-gene-name-1", "sars-cov-2-diag-gene-name-2",
		"originating-lab", "submitting-lab", "sequencing-lab", "author-group",
		"purpose-of-sampling", "purpose-of-sequencing", "sampling-strategy",
		"sample-capture-status", "specimen-source", "sequencing-instrument", "assembly-method",
		"library-strategy", "library-source", "library-selection"];
	
	const radioClasses = ["patient-gender", "prior-sars-cov-2-infection", "prior-sars-cov-2-antiviral-treat", "hospitalisation", "library-layout"];
	let inp;
	

	fetchSampleData(selector.value).then( (sampleData) => {

		Object.keys(sampleData).filter( (className) => className != "sample_id" ).forEach( (className) => {
	
			inp = templateRow.getElementsByClassName(className)[0];

			if ( selectorClasses.includes(className) ){
				inp.options[sampleData[className]].setAttribute("selected", "selected");
			} else if ( radioClasses.includes(className) ) {
				Array.from(templateRow.getElementsByClassName(className)).forEach(e => {
					if (e.value == sampleData[className]) {e.checked=true;};
				});
			} else {
				inp.value = sampleData[className];
			}
		
		});

	});
	*/

}
