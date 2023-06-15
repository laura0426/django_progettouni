document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('menu_form_id').addEventListener('submit', function(e) {
        e.preventDefault()
        window.location = this.target.value
    })
    })









var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}





