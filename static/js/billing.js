$(document).ready(function () {

    // Cart counter
    let cart_counter_int = 0;
    const productOriginalPrice = parseFloat($('.product-original-price').text());

    $('#btn_cart_in').click(function () {
        let cart_counter = $('#cart_counter').text();
        console.log(cart_counter);
        cart_counter_int = parseInt(cart_counter);
        $('#cart_counter').text(cart_counter_int + 1);

        $('#number-of-product-input').val($('#cart_counter').text());

        $('.product-total-price').text(productOriginalPrice * parseInt($('#cart_counter').text()));

        $('#cart_total').text(productOriginalPrice * parseInt($('#cart_counter').text()));

        $('#product-total-price-input').val(productOriginalPrice * parseInt($('#cart_counter').text()));
        $('#cart-total-price-input').val(productOriginalPrice * parseInt($('#cart_counter').text()));
    })

    $('#btn_cart_de').click(function () {
        let cart_counter = $('#cart_counter').text();
        cart_counter_int = parseInt(cart_counter);
        if(cart_counter == 1){
            return;
        }
        $('#cart_counter').text(cart_counter_int - 1);

        $('#number-of-product-input').val($('#cart_counter').text())

        $('.product-total-price').text(productOriginalPrice * parseInt($('#cart_counter').text()));

        $('#cart_total').text(productOriginalPrice * parseInt($('#cart_counter').text()));

        $('#product-total-price-input').val(productOriginalPrice * parseInt($('#cart_counter').text()));
        $('#cart-total-price-input').val(productOriginalPrice * parseInt($('#cart_counter').text()));
    })

});