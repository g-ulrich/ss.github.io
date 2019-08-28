$(document).ready(function(){
    $("#web-rightSideBar").load("common/articlesHomeSearch.html");
    $("#web-resources").load("common/resources.html");
    $("#articleSearchInput").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#articleList li").filter(function() {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
     });
});

var cards = $(".lightBorder");
for(var i = 0; i < cards.length; i++){
    var target = Math.floor(Math.random() * cards.length -1) + 1;
    var target2 = Math.floor(Math.random() * cards.length -1) +1;
    cards.eq(target).before(cards.eq(target2));
}

$("#articleSearchInput").click(function() {
  document.getElementById("articles-li").style.display = "block";
  $( "#search" ).prop( "checked", true );
 });

 $("#searchBurger").click(function() {
  var x = document.getElementById("articles-li");
      if (x.style.display === "block") {
        x.style.display = "none";
      } else {
        x.style.display = "block";
      }
 });
