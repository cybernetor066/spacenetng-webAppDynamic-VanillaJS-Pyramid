var slideIndexb2 = 0;
showSlidesb2();

function showSlidesb2() {
  
  var slidesb2 = document.getElementsByClassName("mySlidesb2");
  var dotsb2 = document.getElementsByClassName("dotb2");
  for (let i = 0; i < slidesb2.length; i++) {
    slidesb2[i].style.display = "none";
  }
  slideIndexb2++;
  if (slideIndexb2 > slidesb2.length) slideIndexb2 = 1;
  slidesb2[slideIndexb2-1].style.display = "block";
  for (let i = 0; i < dotsb2.length; i++) {
    dotsb2[i].className = dotsb2[i].className.replace("activeb2", "");
  }  
  dotsb2[slideIndexb2-1].className += " activeb2"; //Remove the space and see its consequence.
  setTimeout(showSlidesb2, 4000); // Change image every 5 seconds for each Recursive function
}