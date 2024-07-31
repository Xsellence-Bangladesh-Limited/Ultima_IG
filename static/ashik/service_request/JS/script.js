$(document).ready(function () {
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
