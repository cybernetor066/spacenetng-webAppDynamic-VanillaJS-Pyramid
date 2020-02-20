// /* eslint-disable no-unused-vars */
// import imagesloaded from 'imagesloaded';

// imagesloaded(rectifyImages);

// function rectifyImages () {
//     document.addEventListener("DOMContentLoaded", init, false); // Initialise the DOM Environment
//     function init() {
//         window.addEventListener("load", reAlignImage, false);
//     }
//     // specific function to rectify the images
//     function reAlignImage() {
//         var list1 = document.getElementsByClassName('views-left1');
//         for(let item=0; item<list1.length; item++) {
//             item.setAttribute('hidden', '');
//             item.removeAttribute('hidden');
//         }
//     }
// }



document.addEventListener("DOMContentLoaded", init, false); // Initialise the DOM Environment
function init() {
    window.addEventListener("load", reAlignImage, false);
}

// specific function to rectify the images
function reAlignImage() {
    var list1 = document.getElementsByClassName('views-left1');
    for(let item=0; item<list1.length; item++) {
        item.setAttribute('hidden', '');
        // item.removeAttribute('hidden');
    }
}

