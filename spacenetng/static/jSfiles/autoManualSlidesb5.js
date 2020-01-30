  // Auto slide
  // var slideIndexb5 = 0;
  // showSlidesb5();
  
  // function showSlidesb5() {
    
  //   var slidesb5 = document.getElementsByClassName("mySlidesb5");
  //   var dotsb5 = document.getElementsByClassName("dotb5");
  //   for (let i = 0; i < slidesb5.length; i++) {
  //     slidesb5[i].style.display = "none";
  //   }
    
  //   slideIndexb5++;
  //   if (slideIndexb5 > slidesb5.length) slideIndexb5 = 1;
  //   slidesb5[slideIndexb5-1].style.display = "block";
  //   for (let i = 0; i < dotsb5.length; i++) {
  //     dotsb5[i].className = dotsb5[i].className.replace("activeb5", "");
  //   }  
  //   dotsb5[slideIndexb5-1].className += " activeb5"; //Remove the space and see its consequence.
  //   setTimeout(showSlidesb5, 3000); // Change image every 5 seconds for each Recursive function
  // }



  
  // manual slide
  var slideIndexb5 = 1;
  showSlidesb5(slideIndexb5);
  
  function plusSlidesb5(n) {
    showSlidesb5(slideIndexb5 += n);
  }
  

  function showSlidesb5(n) {
    var i;
    var slidesb5 = document.getElementsByClassName("mySlidesb5");
    var dotsb5 = document.getElementsByClassName("dotb5");
    if (n > slidesb5.length) {slideIndexb5 = 1}    
    if (n < 1) {slideIndexb5 = slidesb5.length}
    for (i = 0; i < slidesb5.length; i++) {
        slidesb5[i].style.display = "none";  
    }
    for (i = 0; i < dotsb5.length; i++) {
        dotsb5[i].className = dotsb5[i].className.replace(" activeb5", "");
    }
    slidesb5[slideIndexb5-1].style.display = "block";  
    dotsb5[slideIndexb5-1].className += " activeb5";
  }




function nextSlideb5() {
  plusSlidesb5(1);
}

function prevSlideb5() {
  plusSlidesb5(-1);
}

document.querySelector(".prevb5").addEventListener("click", prevSlideb5);
document.querySelector(".nextb5").addEventListener("click", nextSlideb5);