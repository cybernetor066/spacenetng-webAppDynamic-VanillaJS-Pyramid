  var slideIndexb1 = 0;
  showSlidesb1();
  
  function showSlidesb1() {
    
    var slidesb1 = document.getElementsByClassName("mySlidesb1");
    var dotsb1 = document.getElementsByClassName("dotb1");
    for (let i = 0; i < slidesb1.length; i++) {
      slidesb1[i].style.display = "none";
    }
    slideIndexb1++;
    if (slideIndexb1 > slidesb1.length) slideIndexb1 = 1;
    slidesb1[slideIndexb1-1].style.display = "block";
    for (let i = 0; i < dotsb1.length; i++) {
      dotsb1[i].className = dotsb1[i].className.replace("activeb1", "");
    }  
    dotsb1[slideIndexb1-1].className += " activeb1"; //Remove the space and see its consequence.
    setTimeout(showSlidesb1, 3000); // Change image every 5 seconds for each Recursive function
  }