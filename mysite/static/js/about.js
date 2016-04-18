function changeAbout(img_url){
    document.getElementById('about-img').src = img_url;
    if(img_url.indexOf("img/hands.jpg")!==-1)
            document.getElementById('about-text').innerHTML = '<h3 class="text-center" >Family</h3><p class="lead">I grew up in Oklahoma and am the oldest of four girls. My sisters and I grew up without a lot of luxuries and an idea that if we got our educations we\'d be setting ourselve up for a better life. My blog chronicals my journey to see if this is true.</p>';
 if(img_url.indexOf("img/keyboard.jpg")!==-1)
            document.getElementById('about-text').innerHTML = '<h3 class="text-center" >Overview</h3><p class="lead">I am a software engineer from Oklahoma and currently based in Philedephia. I have a wide number of experiences spanning artificial intelligence and computer vision to video game development. I\'m also a self taught artist. When I\'m not coding or drawing, you\'ll find me practicing the violin or working towards becoming more competitive at Hearthstone Heroes of Warcraft. </p>';
  if(img_url.indexOf("img/books.jpg")!==-1)
            document.getElementById('about-text').innerHTML = '<h3 class="text-center" >Books</h3><p class="lead"> I grew up with a love of books, reading, and education. After being an advid lover of books, I\'ve decided to work on some of my own. I\'m currently working on a series of young adult novels. More details yet to come.</p>';
if(img_url.indexOf("img/colored_pencils.jpg")!==-1)
            document.getElementById('about-text').innerHTML = '<h3 class="text-center" >Art</h3><p class="lead">I am a self taught artist and work with a variety of styles. My most well versed medium is pencil and colored pencil. I look forward to showcasing my art on my website soon.</p>';
if(img_url.indexOf("img/beach.jpg")!==-1)
            document.getElementById('about-text').innerHTML = '<h3 class="text-center" >Community</h3><p class="lead">Volunteering and advocating for the rights of others is something deeply important to me. I have a particular soft spot for education, LGBTQA issues, and animal causes.</p>';
if(img_url.indexOf("img/rotary.jpg")!==-1)
            document.getElementById('about-text').innerHTML = '<h3 class="text-center" >Social</h3><p class="lead">I love the exchange of ideas and interesting tidbits that come from conversing with others. Feel free to contact me or find me on social media. :)</p>';
}
