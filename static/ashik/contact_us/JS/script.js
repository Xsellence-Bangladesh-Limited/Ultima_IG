$(document).ready(function(){

    // Phone number validation function (start)
    function validatePhoneNumber(phoneNumber, countryCode){
        // const indiaMobileCode = '+91';
        // const bdMobileCode = '+880';

        if(phoneNumber){
            try {
                // if(countryCode == 'BD') {
                //                phoneNumber = bdMobileCode + phoneNumber
                //            }
                //
                //            else if(countryCode == 'IN'){
                //                phoneNumber = indiaMobileCode + phoneNumber
                //            }
                // console.log(phoneNumber)

                const phoneNumberObj = libphonenumber.parsePhoneNumberFromString(phoneNumber, countryCode)
                const isValid = phoneNumberObj && phoneNumberObj.isValid() && phoneNumberObj.country === countryCode

                if(!isValid){
                    $('.invalid-phone-number-warning').fadeIn('slow')
                    $('.get-in-touch-form-submission-btn').fadeOut('slow')
                }

                else{
                    $('.invalid-phone-number-warning').fadeOut('slow')
                    $('.get-in-touch-form-submission-btn').fadeIn('slow')
                }
            } catch (error) {
               console.log('Error')
            }
        }

        else{
            $('.invalid-phone-number-warning').fadeOut('slow')
            $('.get-in-touch-form-submission-btn').fadeIn('slow')
        }
    }
    // Phone number validation function (end)


    // Handling successful message sent alert(start)
    $('.message-sent-successful-alert-cancel-btn').click(function(){
        $('.message-sent-successful-alert').fadeOut('slow')
    })

    setTimeout(function(){
        $('.message-sent-successful-alert').fadeOut('slow')
    }, 3000)
    // Handling successful message sent alert(end)


    // Handling form country selection (start)
    let countryDropdownButtonClicked = false

    $('.country-select-item').click(function(){
        countryDropdownButtonClicked = !countryDropdownButtonClicked

        if(countryDropdownButtonClicked){
            $('.country-dropdown').slideDown('slow')
            $('.country-dropdown-icon').removeClass('fa-chevron-down')
            $('.country-dropdown-icon').addClass('fa-chevron-up')
        }

        else{
            $('.country-dropdown').slideUp('slow')
            $('.country-dropdown-icon').addClass('fa-chevron-down')
            $('.country-dropdown-icon').removeClass('fa-chevron-up')
        }

    })

    $('.country-dropdown-item').click(function(){
        const countryDataValue = $(this).data('value')

        $('.initial-country-code').text(countryDataValue)

        countryDropdownButtonClicked = !countryDropdownButtonClicked
        $('.country-dropdown').slideUp('slow')
        $('.country-dropdown-icon').addClass('fa-chevron-down')
        $('.country-dropdown-icon').removeClass('fa-chevron-up')

        const countryCode = $('.initial-country-code').text()
        let phoneNumber = $('#phone-number-input-id').val()

        validatePhoneNumber(phoneNumber, countryCode)
    })
    // Handling form country selection (end)


    // Extracting phone number input value and validating the number (start)
    $('#phone-number-input-id').on('input', function(e){
        const countryCode = $('.initial-country-code').text()
        let phoneNumber = e.target.value

        validatePhoneNumber(phoneNumber, countryCode)
    })
    // Extracting phone number input value and validating the number (end)

})