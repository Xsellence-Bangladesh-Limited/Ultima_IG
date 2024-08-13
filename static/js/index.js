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

});