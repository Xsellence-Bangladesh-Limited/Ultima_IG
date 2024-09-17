$(document).ready(function () {

    // Show / Hide md menu
    $('#menu_control_icon_bars').click(function () {

        $('#menu_control_icon_times').show();
        $('#menu_control_icon_bars').hide();
        $('.sm_menu').slideDown();

    });

    // Show / Hide md menu
    $('#menu_control_icon_times').click(function () {

        $('#menu_control_icon_bars').show();
        $('#menu_control_icon_times').hide();
        $('.sm_menu').slideUp();

    });

    // lang
    $('.select_lang').change(function () {

        let code = $(this).val();
        $(`.flag_image`).hide();
        $(`#flag_image_${code}`).show();
        alert('This feature is upcoming');

    });

        /*
        Testimonial Slider (start)
    */
    var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 20,
    loop: true,
    autoplay: {
      delay: 5000,
      pauseOnMouseEnter: true,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    breakpoints: {
      640: {
        slidesPerView: 2,
      },

      992:{
        slidesPerView: 3,
      }
    },
  });

    /*
        Testimonial Slider (end)
    */

    // Handling talk with expert form toggling (start)

    $('.talk-with-expert-button').click(function(e){
        $('body').css('overflow', 'hidden');
        $('.expert-form-container').fadeIn("slow");
        $('.no-user-name-warning').hide();
        $('.no-phone-number-warning').hide();
        $('.talk-with-expert-form').show();
    })

    $('.talk-to-expert-icon-mobile').click(function(){
        $('body').css('overflow', 'hidden');
        $('.expert-form-container').fadeIn("slow");
        $('.no-user-name-warning').hide();
        $('.no-phone-number-warning').hide();
        $('.talk-with-expert-form').show();
    })

    $('.expert-form-close-icon').click(function(){
        $('body').css('overflow', 'auto');
        $('.expert-form-container').fadeOut("slow");
    })

    // Handling talk with expert form toggling (end)

    // Sending expert message (start)

    $('.expert-form-submit-btn').click(function(){
        if($('#expert-form-name-input').val().trim() === ''){
            $('.no-user-name-warning').fadeIn('slow');
            $('#expert-form-name-input').focus();
            return;
        }

        else {
            $('.no-user-name-warning').fadeOut('slow');
        }

        if($('#expert-form-number-input').val().trim() === ''){
            $('.no-phone-number-warning').fadeIn('slow');
            $('#expert-form-number-input').focus();
            return;
        }

        else {
            $('.no-phone-number-warning').fadeOut('slow');
        }

        $('.expert-form-submit-btn').hide();

        $('.expert-form-submit-loading-btn').show();

        const userName = $('#expert-form-name-input').val().trim();
        const phoneNumber = $('#expert-form-number-input').val().trim();

        const formData = {
            userName, phoneNumber
        }

        $('#expert-form-name-input').val('');
        $('#expert-form-number-input').val('');

        $.post('/send-expert-message', formData, function(response){
            const res = JSON.parse(response);
            if(res.code === 200){
                $('.expert-form-submit-btn').show();
                $('.expert-form-submit-loading-btn').hide();

                $('.talk-with-expert-form').hide();
                $('.talk-with-expert-form-submission-done').show();

                setTimeout(function(){
                    $('body').css('overflow', 'auto');
                    $('.expert-form-container').fadeOut('slow');
                    $('.talk-with-expert-form-submission-done').hide();
                }, 3000);
            }
        })
    })

    // Sending expert message (end)

    // Handling expert form submission done (start)

    $('.talk-with-expert-form-submission-done-btn').click(function(e){
        $('body').css('overflow', 'auto');
        $('.expert-form-container').fadeOut('slow');
        $('.talk-with-expert-form-submission-done').hide();
    });

    // Handling expert form submission done (end)

});