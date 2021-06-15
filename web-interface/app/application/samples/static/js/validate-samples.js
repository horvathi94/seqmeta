async function fetchNamesList(url){
	
	const resp = await fetch("/samples/registered/"+url);
	if (resp.ok){
		promise = await resp.json();
	} else {
		alert("Error fetching names.");
	}
	return promise;
}


function disableSave(inps, names, ommits=[]){
	const subButton = document.querySelectorAll("input[type=submit]")[0];

	disabled = false;
	Array.from(inps).forEach( (inp, i) => {
		ok = true;
		if (names.includes(inp.value)) {
			disabled = true;
			ok = false;
		} else {
			if (!ommits.includes(inp.value)){
				Array.from(inps).slice(0,i).forEach( (inp2) => {
					if (inp.value == inp2.value){disabled=true; ok=false;}
				});
			}
		}

		if (!ok) {
			inp.style.backgroundColor = "orangeRed";

		} else {
			inp.style.backgroundColor = "#fff";
		}
		subButton.disabled = disabled;

	});

}


function checkSampleNames(){

	const inps = document.getElementsByClassName("sample-name");
	
	fetchNamesList("sample-names").then( (names) => {
		disableSave(inps, names);
	});

}


function checkLibraryNames(){

	const inps = document.getElementsByClassName("library-id");
	
	fetchNamesList("library-names").then( (names) => {
		disableSave(inps, names, ommits=[""]);
	});

}
