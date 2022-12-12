jQuery(document).ready(function(){
    $(".plus").click(function(e){
        e.preventDefault();
        field = "input[name=" + $(this).attr("field") + "]";
        var currentVal = parseInt($(field).val());
        if (currentVal < 10) {
            $(field).val(currentVal + 1);
        }
    });

    $(".minus").click( function(e) {
        e.preventDefault();
        field = "input[name=" + $(this).attr("field") + "]";
        var currentVal = parseInt($(field).val());
        if (currentVal > 1){
            $(field).val(currentVal - 1);
        }
    });
});
