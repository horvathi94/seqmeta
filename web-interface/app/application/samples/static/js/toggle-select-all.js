function toggleSelectAll(e){

	Array.from(document.getElementsByName("selected-samples")).forEach( (cb) => {
		cb.checked = e.checked;
	});

}
