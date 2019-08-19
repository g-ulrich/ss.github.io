$(document).ready(function(){
                $("#web-header").html("common/header.html");
                $("#web-rightSideBar").html("common/search.html");
                $("#web-articlesForIndex").html("common/articlesIndex.html");
                $("#web-footer").html("common/footer.html");
              $("#articleSearch").on("keyup", function() {
                var value = $(this).val().toLowerCase();
                $("#articleList li").filter(function() {
                  $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
                });
             });
	});