$(document).ready(function(){
    $('.left-panel-tab').click(function(){
        const tabValue = $(this).data('tab');

        $('.left-panel-tab').removeClass('active');

        $(this).addClass('active');
        
        $('.tab-content').hide();

        $(`#tab-content-${tabValue}`).fadeIn('slow');
    })

    $('.order-details-btn').click(function(){
        const productID = $('.product-id').val();
        const orderID = $('.order-id').val();

        const data = {
            productID,
            orderID
        }

        $.post('/product-details-ajax', data, function(response){
            const res = JSON.parse(response);
            if(res.code){
                const productData = res.data;
                $('.order-product-title').text(productData.product_name);
                $('.product-main-image img').attr('src', `/web/image/product.template/${productData.product_id}/image_1920`)
                $('.modal-order-name').text(productData.order_name);
                $('.modal-order-date').text('test');
                $('.modal-order-amount').text(productData.product_price);
            }
        })

        $('.order-details-modal-parent-container').fadeIn('slow');
        $("body").css("overflow", "hidden");
    })

    $('.modal-close-btn').click(function(){
        $("body").css("overflow", "auto");
        $('.order-details-modal-parent-container').fadeOut('slow');
    })
})