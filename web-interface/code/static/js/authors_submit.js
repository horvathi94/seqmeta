console.log("Hello Fucker!");

// const authorForm = document.querySelector("#edit-authors");
const authorForm = document.getElementById("edit-authors");

if (authorForm) {

	authorForm.addEventListener("submit", function(e){
		submitForm(e, this);
	});

}


async function submitForm(e, form){

	e.preventDefault();

	//const submitButton = document.getElementById("submit-authors");
	//submitButton.disabled = true;
	//setTimeout(() => submitButton.disabled = false, 2000);

	const data = new FormData(e.target);

	const value = Object.fromEntries(data.entries());
	console.log(value);

	const parsed = JSON.pa);
	console.log(parsed);

//	console.log(form.getAll("authors"));

//	const jsonData = buildJsonFormData(form);
//	console.log(jsonData);


}	
