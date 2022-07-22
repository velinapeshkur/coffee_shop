jQuery(document).ready(function(){
    $(".qty-input").blur(function(){
        var product = this.dataset.product;
        $("form[name="+product+"]").submit()
    });
});
