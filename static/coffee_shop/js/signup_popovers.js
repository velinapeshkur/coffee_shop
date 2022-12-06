$(document).ready(function(){
    $('#password1').popover({
        html:true,
        placement: 'right',
        content: '<ul class="popoverContent">\
            <li>Your password can’t be too similar to your other personal information.</li>\
            <li>Your password must contain at least 8 characters.</li>\
            <li>Your password can’t be a commonly used password.</li>\
            <li>Your password can’t be entirely numeric.</li>\
                </ul>',
        trigger: 'focus'
    }
    );
});

$(document).ready(function(){
    $('#password2').popover({
        html:true,
        placement: 'right',
        content: '<p class="popoverContent">Enter the same password as before, for verification.</p>',
        trigger: 'focus'
    }
    );
});
