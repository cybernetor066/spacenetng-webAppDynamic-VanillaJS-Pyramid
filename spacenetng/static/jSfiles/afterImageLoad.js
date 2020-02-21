// /* eslint-disable no-unused-vars */
// import imagesloaded from 'imagesloaded';

// Code1
document.addEventListener("DOMContentLoaded", init, false); // Initialise the DOM Environment
function init() {
    window.addEventListener("load", reAlignImage, false);
}

// specific function to rectify the images
function reAlignImage() {
    var list0 = document.getElementsByTagName('img');
    for(let i=0; i<list0.length; i++) {
        list0[i].setAttribute('hidden', '');
        list0[i].removeAttribute('hidden');
    }
}





// Alternative code2
// // imagesloaded(reAlignImage);

// imagesloaded(rectifyImages);

// function rectifyImages () {
//     document.addEventListener("DOMContentLoaded", init, false); // Initialise the DOM Environment
//     function init() {
//         window.addEventListener("load", reAlignImage, false);
//     }
//     // specific function to rectify the images
//     function reAlignImage() {
//         var list0 = document.getElementsByTagName('img');
//         for(let i=0; i<list0.length; i++) {
//             list0[i].setAttribute('hidden', '');
//             // list0[i].removeAttribute('hidden');
//         }
//     }
// }



// // Alternative code3
// // specific function to rectify the images
// function reAlignImage() {
//     var list0 = document.getElementsByTagName('img');
//     list0.innerHTML(alert("Hello Cyber!!"));
//     // for(let i=0; i<list0.length; i++) {
//     //     list0[i].setAttribute('hidden', '');
//     //     // list0[i].removeAttribute('hidden');
//     // }
// }








