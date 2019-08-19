$(document).ready(function(){
  $("#web-header").load("common/header.html");
  $("#web-footer").load("common/footer.html");
});
function dropdown() {
    var x = document.getElementById("dropdown-content");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }