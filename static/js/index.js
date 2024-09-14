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

    $('.talk-with-expert-button').click(function(){
        $('.talk-with-expert-form').fadeIn("slow");
    })

    $('.expert-form-close-icon').click(function(){
        $('.talk-with-expert-form').fadeOut("slow");
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
            console.log(res);

            if(res.code === 200){
                $('.expert-form-submit-btn').show();
                $('.expert-form-submit-loading-btn').hide();

                $('.talk-with-expert-form').fadeOut("slow");
                $('.talk-with-expert-form-submission-done').fadeIn('slow');

                setTimeout(function(){
                    $('.talk-with-expert-form-submission-done').fadeOut('slow');
                }, 3000);
            }
        })
    })

    // Sending expert message (end)

    // Handling expert form submission done (start)

    $('.talk-with-expert-form-submission-done-btn').click(function(){
        $('.talk-with-expert-form-submission-done').fadeOut('slow');
    });

    // Handling expert form submission done (end)

});