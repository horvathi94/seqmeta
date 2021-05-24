function updateIndices(){
   
   const listItems = document.querySelectorAll("#virusname .piece:not(.hidden)");
         
   listItems.forEach((li, index) => {
      let indxInput = li.querySelectorAll(".wrap .indx")[0];
      indxInput.value = index + 1;
      console.log(li);
   });

}



$( function() {
   $( "#virusname" ).sortable({
      update: function(e, ui){updateIndices()}
   });

   $( "#virusname" ).disableSelection();
} );



function removeItem(e) {
   const li = e.parentElement.parentElement;
   const indxInput = li.querySelectorAll(".wrap .indx")[0];
   indxInput.value = 0;
   li.classList.add("hidden");
   updateIndices();
}

function addVirusnamePiece(){
   const ul = document.getElementById("virusname");
   const empty = document.getElementsByClassName("piece")[0];
   newPiece = empty.cloneNode(true);
   newPiece.classList.remove("hidden");

   ul.appendChild(newPiece);
   $(document).find("form").trigger("create")
}
