$(document).ready(function () {

    // Faq toggle button
    // data_faq_desc_id
    // id="faq_desc_3"

    $('.con_arrow').click(function () {

        $('.faq .desc').hide();

        let data_faq_desc_id = $(this).attr('data_faq_desc_id');
        let data_state = $(this).attr('data_state');
        $(`#faq_desc_${data_faq_desc_id}`).slideDown(500);

        // Active faq color
        $('.faq .head').removeClass('active');
        $(`#faq_head_${data_faq_desc_id}`).addClass('active');

        // Change icon
        if (data_state == 'open') {

            // $(`#arrow_content_${data_faq_desc_id}`).text('-');
            // $(this).attr('data_state', 'close');

        } else {

            // $(`#arrow_content_${data_faq_desc_id}`).text('+');
            // $(this).attr('data_state', 'open');

        }

    });

    /*
        Frequently Asked Question
    */
    var acc = document.getElementsByClassName("accordion");
    var i;

    for (i = 0; i < acc.length; i++) {

        acc[i].addEventListener("click", function () {

            this.classList.toggle("active");
            var panel = this.nextElementSibling;

            if (panel.style.maxHeight) {
                panel.style.maxHeight = null;

            } else {
                panel.style.maxHeight = panel.scrollHeight + "px";

            }

        });

    }

    // panel_active
    var panel_active = document.getElementById("panel_active");
    if (panel_active){
        panel_active.style.maxHeight = panel_active.scrollHeight + "px";
    }

    /*
        End Frequently Asked Question
    */

    /*
        Introduce
    */
    let padding = 0;
    let status = 'in';
    function introduce_play_animate() {

        if (status == 'in') {
            padding++;

            if (padding >= 9) {
                status = 'de'
            }

        } else if (status == 'de') {
            padding--;

            if (padding <= 0) {
                status = 'in'
            }
        }

        // 'background-color': `rgba(0, 0, 0, 0.${padding * 100})`,

        $('#introduce_play').css({
            'padding': `${padding}px`,
        })

    }

    setInterval(introduce_play_animate, 90);

    $("#modal_introduce_video").on('hide.bs.modal', function () {
        var iframe = $('#introduce_iframe');
        var src = iframe.attr('src');
        iframe.attr('src', ''); // Temporarily set the src to an empty string
        iframe.attr('src', src); // Reset the src back to the original value
    });

    /*
        End Introduce
    */

    // Product buy button for logged out user (start)

        $('#product-buy-btn').click(function(){
            $('.login-form-container').fadeIn('slow');
        })

    // Product buy button for logged out user (end)

});