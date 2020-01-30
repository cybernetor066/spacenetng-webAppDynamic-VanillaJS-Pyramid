  // Auto slide
  // var slideIndexb3 = 0;
  // showSlidesb3();
  
  // function showSlidesb3() {
    
  //   var slidesb3 = document.getElementsByClassName("mySlidesb3");
  //   var dotsb3 = document.getElementsByClassName("dotb3");
  //   for (let i = 0; i < slidesb3.length; i++) {
  //     slidesb3[i].style.display = "none";
  //   }
    
  //   slideIndexb3++;
  //   if (slideIndexb3 > slidesb3.length) slideIndexb3 = 1;
  //   slidesb3[slideIndexb3-1].style.display = "block";
  //   for (let i = 0; i < dotsb3.length; i++) {
  //     dotsb3[i].className = dotsb3[i].className.replace("activeb3", "");
  //   }  
  //   dotsb3[slideIndexb3-1].className += " activeb3"; //Remove the space and see its consequence.
  //   setTimeout(showSlidesb3, 3000); // Change image every 5 seconds for each Recursive function
  // }



  
  // manual slide
  var slideIndexb3 = 1;
  showSlidesb3(slideIndexb3);
  
  function plusSlidesb3(n) {
    showSlidesb3(slideIndexb3 += n);
  }
  

  function showSlidesb3(n) {
    var i;
    var slidesb3 = document.getElementsByClassName("mySlidesb3");
    var dotsb3 = document.getElementsByClassName("dotb3");
    if (n > slidesb3.length) {slideIndexb3 = 1}    
    if (n < 1) {slideIndexb3 = slidesb3.length}
    for (i = 0; i < slidesb3.length; i++) {
        slidesb3[i].style.display = "none";  
    }
    for (i = 0; i < dotsb3.length; i++) {
        dotsb3[i].className = dotsb3[i].className.replace(" activeb3", "");
    }
    slidesb3[slideIndexb3-1].style.display = "block";  
    dotsb3[slideIndexb3-1].className += " activeb3";
  }




function nextSlideb3() {
  plusSlidesb3(1);
}

function prevSlideb3() {
  plusSlidesb3(-1);
}

document.querySelector(".prevb3").addEventListener("click", prevSlideb3);
document.querySelector(".nextb3").addEventListener("click", nextSlideb3);