async function fetchSampleNames(){
	
	const resp = await fetch("/samples/registered-names");
	if (resp.ok){
		promise = await resp.json();
	} else {
		alert("Error fetching names.");
	}
	return promise;
}


function disableSave(){
	const subButton = document.querySelectorAll("input[type=submit]")[0];
	const inps = document.getElementsByClassName("sample-name");
	fetchSampleNames().then( (sampleNames) => {
		disabled = false;
		Array.from(inps).forEach( (inp) => {
			if (sampleNames.includes(inp.value)) {
				disabled=true;
				inp.style.backgroundColor = "orangeRed";
			} else {
				inp.style.backgroundColor = "#fff";
			}
			subButton.disabled = disabled;
		});
	});
}


