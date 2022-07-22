$(function () {
    $(document).scroll(function () {
      var $nav = $(".navbar");
      $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
});

jQuery(document).ready(function(){
    $("#search-form").focusin(function(){
        $("#results").show()
    });
    $("#search-form").blur(function(){
        if (!$('#results').is(':hover')) {
            $("#results").hide();
    }});
});