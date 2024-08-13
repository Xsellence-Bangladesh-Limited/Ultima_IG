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

});