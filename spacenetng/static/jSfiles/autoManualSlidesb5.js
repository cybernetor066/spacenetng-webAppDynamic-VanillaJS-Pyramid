var slideIndexb5 = 0;
showSlidesb5();

function showSlidesb5() {
  
  var slidesb5 = document.getElementsByClassName("mySlidesb5");
  var dotsb5 = document.getElementsByClassName("dotb5");
  for (let i = 0; i < slidesb5.length; i++) {
    slidesb5[i].style.display = "none";
  }
  slideIndexb5++;
  if (slideIndexb5 > slidesb5.length) slideIndexb5 = 1;
  slidesb5[slideIndexb5-1].style.display = "block";
  for (let i = 0; i < dotsb5.length; i++) {
    dotsb5[i].className = dotsb5[i].className.replace("activeb5", "");
  }  
  dotsb5[slideIndexb5-1].className += " activeb5"; //Remove the space and see its consequence.
  setTimeout(showSlidesb5, 7000); // Change image every 5 seconds for each Recursive function
}