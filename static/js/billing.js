$(document).ready(function () {

    // Cart counter
    $('#btn_cart_in').click(function () {
        let cart_counter = $('#cart_counter').text();
        console.log(cart_counter);
        let cart_counter_int = parseInt(cart_counter);
        $('#cart_counter').text(cart_counter_int + 1);
    })

    $('#btn_cart_de').click(function () {
        let cart_counter = $('#cart_counter').text();
        let cart_counter_int = parseInt(cart_counter);
        $('#cart_counter').text(cart_counter_int - 1);
    })

});