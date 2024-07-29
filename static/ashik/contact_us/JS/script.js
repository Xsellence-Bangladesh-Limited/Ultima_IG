$(document).ready(function(){

    $('.message-sent-successful-alert-cancel-btn').click(function(){
        $('.message-sent-successful-alert').fadeOut('slow')
    })

    setTimeout(function(){
        $('.message-sent-successful-alert').fadeOut('slow')
    }, 3000)

})