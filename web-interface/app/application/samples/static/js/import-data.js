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



			if (inp.type == "select"){

				inp.options.forEach( (opt) => {
					if (opt.value == sampleData[className]) {
						opt.setAttribute("selected", "selected")
					}
				});

			} else if (inp.type == "select-one") {
				
				Array.from(templateRow.getElementsByClassName(className)).forEach(e => {
					if (e.value == sampleData[className]) {e.checked=true;};
				});
				
			} else {
				
				console.log(className, sampleData[className]);
				inp.value = sampleData[className];

			}

		});

	});


}
