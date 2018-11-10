// References: https://codepen.io/lehollandaisvolant/pen/ryrrGx
var scrollPos = 0;
var hdr = $('header');
window.addEventListener('scroll', function(){
  // detects new state and compares it with the new one
  if ((document.body.getBoundingClientRect()).top > scrollPos) {
     hdr.addClass('scrolling');
  }
  else {
     hdr.removeClass('scrolling');
  }
  scrollPos = (document.body.getBoundingClientRect()).top;
});