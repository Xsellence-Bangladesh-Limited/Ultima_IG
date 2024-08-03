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
});
