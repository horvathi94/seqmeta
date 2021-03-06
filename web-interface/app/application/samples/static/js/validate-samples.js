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

	isDisabled = false;

	inps.forEach( (inp, i) => {
		errorCode = "";
		if (names.includes(inp.value)) {
			isDisabled = true;
			errorCode = "Registered in db";
		} else if ((!inp.value) && (!emptyAllowed)){
			isDisabled = true;
			errorCode = "Empty string not allowed.";
		} else if (!ommits.includes(inp.value)){
			Array.from(inps).slice(0,i).forEach( (inp2) => {
				if (inp.value == inp2.value){
					isDisabled=true; 
					errorCode="Duplicate name."
				}
			});
		}
				
		let err = inp.parentNode.getElementsByClassName("error-box")[0];
		if ( err ) { err.remove(); }

		if (errorCode) {
			inp.style.backgroundColor = "orangeRed";
			let err = document.createElement("p");
			err.classList.add("error-box");
			err.innerHTML = errorCode;
			err.style.fontWeight = "bold";
			inp.parentNode.appendChild(err);
		} else {
			inp.style.backgroundColor = "#fff";
		}

	});

	subButton.disabled = isDisabled;

}


function checkSampleNames(){

	const inps = Array.from(document.getElementsByClassName("sample-name")).slice(1);

	fetchNamesList("sample-names").then( (names) => {
		disableSave(inps, names);
	});

}


function checkLibraryNames(){

	const inps = Array.from(document.getElementsByClassName("library-id")).slice(1);
	
	fetchNamesList("library-names").then( (names) => {
		disableSave(inps, names, ommits=[""], emptyAllowed=true);
	});

}


