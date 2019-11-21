$(document).ready(function(){
    $("#web-header").load("../common/post-header.html");
    $("#web-rightSideBar").load("../common/search.html");
    $("#web-resources").load("../common/post-resources.html");
    $("#web-footer").load("../common/post-footer.html");
    $("#articleSearch").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#articleList li").filter(function() {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
     });
});