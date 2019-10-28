var slideIndexb4 = 0;
showSlidesb4();

function showSlidesb4() {
  
  var slidesb4 = document.getElementsByClassName("mySlidesb4");
  var dotsb4 = document.getElementsByClassName("dotb4");
  for (let i = 0; i < slidesb4.length; i++) {
    slidesb4[i].style.display = "none";
  }
  slideIndexb4++;
  if (slideIndexb4 > slidesb4.length) slideIndexb4 = 1;
  slidesb4[slideIndexb4-1].style.display = "block";
  for (let i = 0; i < dotsb4.length; i++) {
    dotsb4[i].className = dotsb4[i].className.replace("activeb4", "");
  }  
  dotsb4[slideIndexb4-1].className += " activeb4"; //Remove the space and see its consequence.
  setTimeout(showSlidesb4, 6000); // Change image every 5 seconds for each Recursive function
}