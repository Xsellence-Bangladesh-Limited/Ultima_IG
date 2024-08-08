$(document).ready(function () {

   // Handling successful message sent alert(start)
   $('.message-sent-successful-alert-cancel-btn').click(function(){
       $('.message-sent-successful-alert').fadeOut('slow')
   })

   setTimeout(function(){
       $('.message-sent-successful-alert').fadeOut('slow')
   }, 3000)
   // Handling successful message sent alert(end)

  // Testimonial Slider (start)

  var swiper = new Swiper(".mySwiper", {
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
    },
  });

  //   Testimonial Slider (end)

    /* FAQ (start) */

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

  /* FAQ (end) */
});
