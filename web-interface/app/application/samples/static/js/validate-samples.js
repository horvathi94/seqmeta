async function fetchNamesList(url){
	
	const resp = await fetch("/samples/registered/"+url);
	if (resp.ok){
		promise = await resp.json();
	} else {
		alert("Error fetching names.");
	}
	return promise;
}


function disableSave(inps, names, ommits=[], emptyAllowed=false){
	const subButton = document.querySelectorAll("input[type=submit]")[0];

	disabled = false;
	Array.from(inps).forEach( (inp, i) => {
		errorCode = "";
		if (names.includes(inp.value)) {
			disabled = true;
			errorCode = "Registered in db";
		} else if ((!inp.value) && (!emptyAllowed)){
			disabled = true;
			errorCode = "Empty string not allowed.";
		} else if (!ommits.includes(inp.value)){
			Array.from(inps).slice(0,i).forEach( (inp2) => {
				if (inp.value == inp2.value){
					disabled=true; 
					errorCode="Duplicate name."
				}
			});
		}
				
		let err = inp.parentElement.getElementsByClassName("error")[0];
		err.style.visibility = "visible";

		if (errorCode) {
			inp.style.backgroundColor = "orangeRed";
			err.innerHTML = errorCode;
		} else {
			inp.style.backgroundColor = "#fff";
			err.innerHTML = "";
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
		disableSave(inps, names, ommits=[""], emptyAllowed=true);
	});

}
