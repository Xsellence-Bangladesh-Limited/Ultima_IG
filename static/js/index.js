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

    $('.expert-form-container').click(function(){
        $(this).fadeOut('slow');
    })

    $('.talk-with-expert-form').click(function(e){
        e.stopPropagation();
    })

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

    // Toggling login form (start)

    $('.user-sign-in-button').click(function(){
        $('.login-form-container').fadeIn('slow');

        // Clicking login buttons pressing enter key (start)

        $(document).keypress(function(e){
            if(e.which === 13){
                $('.ultima_login_form_btn:visible').click();
            }
        })

        // Clicking login buttons pressing enter key (end)
    })

    $('.login-form-container').click(function(){
        $(this).fadeOut('slow');
    })

    $('.login-form').click(function(e){
        e.stopPropagation();
    })

    // Toggling login form (end)

    // Login form validating phone number (start)

    function validatePhoneNumber(phoneNumber, countryCode){
        if(phoneNumber){
            try {

                const phoneNumberObj = libphonenumber.parsePhoneNumberFromString(phoneNumber, countryCode)
                const isValid = phoneNumberObj && phoneNumberObj.isValid() && phoneNumberObj.country === countryCode

                if(!isValid){
                    $('.invalid-phone-number-warning').fadeIn('slow')
                    $('#login-form-proceed-btn').fadeOut('slow')
                }

                else{
                    $('.invalid-phone-number-warning').fadeOut('slow')
                    $('#login-form-proceed-btn').fadeIn('slow')
                }
            } catch (error) {
               console.log('Error')
            }
        }

        else{
            $('.invalid-phone-number-warning').fadeOut('slow')
            $('#login-form-proceed-btn').fadeIn('slow')
        }
    }

    $('#login-form-phone-number-input').on('input', function(e){
        const countryCode = 'BD'
        let phoneNumber = e.target.value.trim()

        validatePhoneNumber(phoneNumber, countryCode)
    })

    // Login form validating phone number (end)

    // AJAX for sending OTP (start)

    $('#login-form-proceed-btn').click(function(){
        const phoneNumber = $('#login-form-phone-number-input').val().trim();
        if (phoneNumber){

            const data = {phoneNumber}

            $(this).hide();

            $('.login-form-proceed-loading-btn').show();

            $.post('/create-otp', data, function(response){
                const res = JSON.parse(response);
                if(res.code === 200){
                    console.log('ok')
                    $('#login-form-proceed-btn-otp').show();
                    $('.login-form-proceed-loading-btn').hide();
                }
            })

            $('#login-form-otp-input').fadeIn('slow')
        }
    })

    $('#login-form-proceed-btn-otp').click(function(){
        const otp = $('#login-form-otp-input').val().trim();
        const phoneNumber = $('#login-form-phone-number-input').val().trim();

        if(otp){
            const data = {otp, phoneNumber};

            $(this).hide();

            $('.login-form-proceed-loading-btn').show();

            $.post('/check-otp', data, function(response){
                const res = JSON.parse(response);
                if(res.code === 200){
                    console.log('Matched');
                    $('.invalid-otp-warning').fadeOut('slow');
                    $('#login-form-proceed-btn-otp').hide();
                    $('#login-form-otp-input').hide();
                    $('.login-form-proceed-loading-btn').hide();
                    $('.login-form-personal-info').show();
                }

                else if(res.code === 201){
                    $('.invalid-otp-warning').fadeOut('slow');
                    $('#login-form-proceed-btn-otp').hide();
                    $('#login-form-otp-input').hide();
                    $('.login-form-proceed-loading-btn').hide();
                    window.location.href = res.current_page;
                }

                else if(res.code === 400){
                    console.log('Not matched');
                    $('.invalid-otp-warning').fadeIn('slow');
                    $('#login-form-proceed-btn-otp').show();
                    $('.login-form-proceed-loading-btn').hide();
                }
            })
        }
    })

    // Register a user (start)

    $('#create-account-btn').click(function(){
        const firstName = $('#personal-info-first-name-input').val().trim();
//        const lastName = $('#personal-info-last-name-input').val().trim();
        const emailAddress = $('#personal-info-email-input').val().trim();
        const phoneNumber = $('#login-form-phone-number-input').val().trim();

        if(!firstName){
            $('.invalid-first-name-warning').fadeIn('slow');
        }

        else{
            $('.invalid-first-name-warning').fadeOut('slow');
        }

//        if(!lastName){
//            $('.invalid-last-name-warning').fadeIn('slow');
//        }
//
//        else{
//            $('.invalid-last-name-warning').fadeOut('slow');
//        }

        if(!emailAddress){
            $('.invalid-email-warning').fadeIn('slow');
        }

        else{
            $('.invalid-email-warning').fadeOut('slow');
        }

        const data = {
            firstName, emailAddress, phoneNumber
        }

        $(this).hide();

        $('.create-user-login-form-proceed-loading-btn').show();

        $.post('/register-user', data, function(response){
            const res = JSON.parse(response);

            if(res.code === 200){
                window.location.href = res.current_page;
                $('.existing-email-warning').fadeOut('slow');
                $('#create-account-btn').show();
                $('.create-user-login-form-proceed-loading-btn').hide();
            }

            if (res.code === 400){
                $('.existing-email-warning').fadeIn('slow');
                $('#create-account-btn').show();
                $('.create-user-login-form-proceed-loading-btn').hide();
            }
        })
    })

    // Register a user (end)

    // AJAX for sending OTP (end)

});