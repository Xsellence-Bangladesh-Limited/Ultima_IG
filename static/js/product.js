$(document).ready(function () {
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