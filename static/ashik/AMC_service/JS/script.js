$(document).ready(function () {
  // Main Banner Slider (start)

  var swiper = new Swiper(".main-banner-slider .mySwiper", {
    loop: true,
    autoplay: {
      delay: 5000,
      pauseOnMouseEnter: true,
    },
    pagination: {
      el: ".swiper-pagination",
      dynamicBullets: true,
      clickable: true,
    },
  });

  // Main Banner Slider (end)

  // Testimonial Slider (start)

  var swiper = new Swiper(".testimonial-slider .mySwiper", {
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

  //   Testimonial Slider (end)
});
