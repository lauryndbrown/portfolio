//copied from https://css-tricks.com/snippets/jquery/smooth-scrolling/
$(document).on('click', 'button', function() {
    $('html,body').animate({
        scrollTop: $(".footer").offset().top},
        1000);
});
$(document).ready(function() {
   
  //hide objects 
  $("#featurette1").hide();
  $("#featurette2").hide();
  $("#featurette3").hide();

  //init scrolling event heandler
  $(document).scroll(function(){
   
        var docScroll = $(document).scrollTop(); 
       // var offset1 =  $("#featurette1").scrollTop() -100;
        var offset1 =  $("#feature1").offset().top -500;
        var offset2 =  $("#feature2").offset().top -500;
        var offset3 =  $("#feature3").offset().top -500;
 
    //when rich top of boxex than fire
    if(docScroll > offset1 ) {

      $("#featurette1").fadeIn(900)
    
    } if(docScroll > offset2 && docScroll < offset3){
     $("#featurette2").fadeIn(900)
    }
     if(docScroll > offset3){
     $("#featurette3").fadeIn(900)
    }
  })   
});
  
  

