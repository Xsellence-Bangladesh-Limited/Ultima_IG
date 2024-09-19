$(document).ready(function () {
  // Main slider (start)
  var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },

    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
  // Main slider (end)

  // Category Slider(start)
  var splide = new Splide(".splide", {
    gap: "0.625rem",
    fixedWidth: "auto",
    fixedHeight: "auto",
    pagination: false,
    perMove: 1,
    breakpoints: {
      640: {
        perPage: 1,
        gap: "0.625rem",
      },
      480: {
        perPage: 1,
        gap: "0.625rem",
      },
    },
  });

  splide.mount();
  // Category Slider(end)
});
