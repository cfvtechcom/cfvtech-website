/* CFV Technologies – static site scripts (sliders, smooth scroll, scroll-to-top).
   Trimmed from the original theme's custom.js; contact-form, datepicker and map code removed. */
jQuery(function ($) {

  // Top banner slider
  $('.mu-top-slider').slick({
    dots: true, infinite: true, arrows: false, speed: 500,
    autoplay: true, fade: true, cssEase: 'linear'
  });

  // Certifications and client-logo carousels
  $('.mu-chef-nav').slick({
    dots: true, arrows: false, infinite: true, speed: 300,
    slidesToShow: 4, slidesToScroll: 2, autoplay: true, autoplaySpeed: 2500,
    responsive: [
      { breakpoint: 1024, settings: { slidesToShow: 3, slidesToScroll: 3, infinite: true, dots: true } },
      { breakpoint: 600,  settings: { slidesToShow: 2, slidesToScroll: 2 } },
      { breakpoint: 480,  settings: { slidesToShow: 1, slidesToScroll: 1 } }
    ]
  });

  // Smooth scrolling for in-page menu links, with active item highlight
  var topMenu = $('.mu-main-nav'),
      topMenuHeight = topMenu.outerHeight() + 13,
      menuItems = topMenu.find('a[href^="#"]'),
      lastId;

  menuItems.on('click', function (e) {
    var href = $(this).attr('href'), target = $(href);
    if (!target.length) return;
    e.preventDefault();
    $('html, body').stop().animate({ scrollTop: target.offset().top - topMenuHeight + 32 }, 1000);
    $('.navbar-collapse').removeClass('in');
    if (history.replaceState) history.replaceState(null, '', href);
  });

  $(window).on('scroll', function () {
    var fromTop = $(this).scrollTop() + topMenuHeight, id = '';
    menuItems.each(function () {
      var t = $($(this).attr('href'));
      if (t.length && t.offset().top < fromTop) id = t.attr('id');
    });
    if (id !== lastId) {
      lastId = id;
      menuItems.parent().removeClass('active');
      if (id) menuItems.filter('[href="#' + id + '"]').parent().addClass('active');
    }
    if ($(this).scrollTop() > 300) $('.scrollToTop').fadeIn(); else $('.scrollToTop').fadeOut();
  });

  $('.scrollToTop').on('click', function () {
    $('html, body').animate({ scrollTop: 0 }, 800);
    return false;
  });
});
