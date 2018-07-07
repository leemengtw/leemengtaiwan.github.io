// Credit: https://codepen.io/k33k00/pen/ByeyVB
jQuery(document).ready(function($){
    $(window).on('load', function(){
      $(window).scroll(function() {
        var wintop = $(window).scrollTop(), docheight = $('article').height(), winheight = $(window).height();
        // console.log(wintop);
        var totalScroll = (wintop/(docheight-winheight))*100;
        // console.log("total scroll" + totalScroll);
        $(".KW_progressBar").css("width",totalScroll+"%");
      });
    });
});