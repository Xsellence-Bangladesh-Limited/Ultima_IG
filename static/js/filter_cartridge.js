$(document).ready(function () {

    $('.owl-carousel').owlCarousel({
        loop: true,
        margin: 10,
        nav: false, // This disables the arrows
        stagePadding: 10,
        items: 1,
        responsive: {
            0: {
                items: 2
            },
            600: {
                items: 3
            },
            1000: {
                items: 5
            }
        }
    })

    // img_owl
    $('.img_owl').click(function () {

        let src = $(this).attr('src');
        console.log(src);

        $('#img_service_kit').attr('src', src);

    });

    /*
    pd_detail_svg
    */

    $('.pd_detail_svg').click(function () {

        $('.tab_content').hide();
        let data_tab_content_id = $(this).attr('data_tab_content_id');
        $(`#tab_content_${data_tab_content_id}`).show();

        $('.pd_detail_svg').removeClass('pd_detail_svg_active')
        $(this).toggleClass('pd_detail_svg_active');

        $('.pd_detail_svg_text').removeClass('pd_detail_svg_text_active');
        $(`#pd_detail_svg_text_${data_tab_content_id}`).addClass('pd_detail_svg_text_active');

    });

    /*
    End pd_detail_svg
    */

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
    panel_active.style.maxHeight = panel_active.scrollHeight + "px";

    /*
        End Frequently Asked Question
    */

    /*
        Testimonial Slider (start)
    */
    var swiper = new Swiper(".testimonial-slider .mySwiper", {
        cssMode: true,
        loop: true,
        autoplay: {
            delay: 5000,
            pauseOnMouseEnter: true,
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        pagination: {
            el: ".swiper-pagination",
            dynamicBullets: true,
            clickable: true,
        },
    });

    /*
        Testimonial Slider (end)
    */


});