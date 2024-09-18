$(document).ready(function () {

    // Cart counter
    let cart_counter_int = 0;
    let current_selected_shipping_cost = 0;
    const productOriginalPrice = parseFloat($('.product-original-price').text());

    $('#btn_cart_in').click(function () {
        let cart_counter = $('#cart_counter').text();
        console.log(cart_counter);
        cart_counter_int = parseInt(cart_counter);
        $('#cart_counter').text(cart_counter_int + 1);

        $('#number-of-product-input').val($('#cart_counter').text());

        $('.product-total-price').text(productOriginalPrice * parseInt($('#cart_counter').text()) + current_selected_shipping_cost);

        $('#cart_total').text(productOriginalPrice * parseInt($('#cart_counter').text()) + current_selected_shipping_cost);

        $('#product-total-price-input').val(productOriginalPrice * parseInt($('#cart_counter').text()) + current_selected_shipping_cost);
        $('#cart-total-price-input').val(productOriginalPrice * parseInt($('#cart_counter').text()) + current_selected_shipping_cost);
    })

    $('#btn_cart_de').click(function () {
        let cart_counter = $('#cart_counter').text();
        cart_counter_int = parseInt(cart_counter);
        if(cart_counter == 1){
            return;
        }
        $('#cart_counter').text(cart_counter_int - 1);

        $('#number-of-product-input').val($('#cart_counter').text())

        $('.product-total-price').text(productOriginalPrice * parseInt($('#cart_counter').text()) + current_selected_shipping_cost);

        $('#cart_total').text(productOriginalPrice * parseInt($('#cart_counter').text()) + current_selected_shipping_cost);

        $('#product-total-price-input').val(productOriginalPrice * parseInt($('#cart_counter').text()));
        $('#cart-total-price-input').val(productOriginalPrice * parseInt($('#cart_counter').text()));
    })

    $('#b_input').on('change', function(){
        $('.product-total-price').text(parseFloat($('.product-total-price').text()) - current_selected_shipping_cost);
        $('#cart_total').text(parseFloat($('#cart_total').text()) - current_selected_shipping_cost);

        const selectedOptionCost = $(this).find('option:selected').data('shipping-cost');
        // console.log(parseFloat($('.product-total-price').text()), selectedOptionCost);
        $('.product-total-price').text(parseFloat($('.product-total-price').text()) + parseFloat(selectedOptionCost));
        $('#cart_total').text(parseFloat($('#cart_total').text()) + parseFloat(selectedOptionCost));

        $('#product-total-price-input').val(parseFloat($('.product-total-price').text()));
        $('#cart-total-price-input').val(parseFloat($('#cart_total').text()));
        $('#shipping-cost').val(selectedOptionCost);

        current_selected_shipping_cost = parseFloat(selectedOptionCost);
    })

});