$(document).ready(function () {

    // Handling successful query sent alert(start)
    $('.message-sent-successful-alert-cancel-btn').click(function(){
        $('.message-sent-successful-alert').fadeOut('slow')
    })

    setTimeout(function(){
        $('.message-sent-successful-alert').fadeOut('slow')
    }, 3000)
    // Handling successful query sent alert(end)

});
