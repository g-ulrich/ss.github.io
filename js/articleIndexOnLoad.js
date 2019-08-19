$(document).ready(function(){
    // $("#web-header").load("common/header.html");
    $("#web-rightSideBar").load("common/search.html");
    // $("#web-articlesIndex").load("common/articlesIndex.html");
    $("#web-resources").load("common/resources.html");
    $("#web-footer").load("common/footer.html");
    $("#articleSearchInput").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#articleList li").filter(function() {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
     });
     $("#articleSearch").on("keyup", function() {
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
