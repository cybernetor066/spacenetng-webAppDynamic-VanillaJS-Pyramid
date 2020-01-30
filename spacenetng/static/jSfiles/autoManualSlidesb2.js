  // Auto slide
  // var slideIndexb2 = 0;
  // showSlidesb2();
  
  // function showSlidesb2() {
    
  //   var slidesb2 = document.getElementsByClassName("mySlidesb2");
  //   var dotsb2 = document.getElementsByClassName("dotb2");
  //   for (let i = 0; i < slidesb2.length; i++) {
  //     slidesb2[i].style.display = "none";
  //   }
    
  //   slideIndexb2++;
  //   if (slideIndexb2 > slidesb2.length) slideIndexb2 = 1;
  //   slidesb2[slideIndexb2-1].style.display = "block";
  //   for (let i = 0; i < dotsb2.length; i++) {
  //     dotsb2[i].className = dotsb2[i].className.replace("activeb2", "");
  //   }  
  //   dotsb2[slideIndexb2-1].className += " activeb2"; //Remove the space and see its consequence.
  //   setTimeout(showSlidesb2, 3000); // Change image every 5 seconds for each Recursive function
  // }



  
  // manual slide
  var slideIndexb2 = 1;
  showSlidesb2(slideIndexb2);
  
  function plusSlidesb2(n) {
    showSlidesb2(slideIndexb2 += n);
  }
  

  function showSlidesb2(n) {
    var i;
    var slidesb2 = document.getElementsByClassName("mySlidesb2");
    var dotsb2 = document.getElementsByClassName("dotb2");
    if (n > slidesb2.length) {slideIndexb2 = 1}    
    if (n < 1) {slideIndexb2 = slidesb2.length}
    for (i = 0; i < slidesb2.length; i++) {
        slidesb2[i].style.display = "none";  
    }
    for (i = 0; i < dotsb2.length; i++) {
        dotsb2[i].className = dotsb2[i].className.replace(" activeb2", "");
    }
    slidesb2[slideIndexb2-1].style.display = "block";  
    dotsb2[slideIndexb2-1].className += " activeb2";
  }




function nextSlideb2() {
  plusSlidesb2(1);
}

function prevSlideb2() {
  plusSlidesb2(-1);
}

document.querySelector(".prevb2").addEventListener("click", prevSlideb2);
document.querySelector(".nextb2").addEventListener("click", nextSlideb2);