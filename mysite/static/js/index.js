//copied from https://css-tricks.com/snippets/jquery/smooth-scrolling/
 //$("button").click(function() {
$(document).on('click', 'button', function() {
    $('html,body').animate({
        scrollTop: $(".footer").offset().top},
        1000);
});
