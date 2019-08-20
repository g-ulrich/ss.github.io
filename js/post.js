$(document).ready(function(){
    $("#web-rightSideBar").load("common/search.html");
    $("#web-resources").load("common/resources.html");
    $("#articleSearch").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#articleList li").filter(function() {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
     });
});