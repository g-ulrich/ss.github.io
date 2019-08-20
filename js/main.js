var version = detectIE();
if (version === false) {
  document.getElementById('result').innerHTML = '';
  document.getElementById('msgDiv').style.display = 'none';
} else if (version >= 15) {
  document.getElementById('result').innerHTML = '';
  document.getElementById('msgDiv').style.display = 'none';
} else {
  document.getElementById('result').innerHTML = 'Internet Explorer v.' + version + ' is not supported. Please choose a different browser. <br/> &#9785;';
  document.getElementById('msgDiv').style.display = 'block';
}
function detectIE() {
  var ua = window.navigator.userAgent;
  var msie = ua.indexOf('MSIE ');
  if (msie > 0) {
    return parseInt(ua.substring(msie + 5, ua.indexOf('.', msie)), 10);
  }
  var trident = ua.indexOf('Trident/');
  if (trident > 0) {
    var rv = ua.indexOf('rv:');
    return parseInt(ua.substring(rv + 3, ua.indexOf('.', rv)), 10);
  }
  var edge = ua.indexOf('Edge/');
  if (edge > 0) {
    return parseInt(ua.substring(edge + 5, ua.indexOf('.', edge)), 10);
  }
  return false;
}
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
