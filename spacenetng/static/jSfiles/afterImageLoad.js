/* eslint-disable no-unused-vars */
import imagesloaded from 'imagesloaded';

imagesloaded(rectifyImages);

function rectifyImages () {
    document.addEventListener("DOMContentLoaded", init, false); // Initialise the DOM Environment
    function init() {
        window.addEventListener("load", reAlignImage, false);
    }
    // specific function to rectify the images
    function reAlignImage() {
        document.getElementsByClassName('views-left1').setAttribute('hidden', '');
        document.getElementsByClassName('views-left1').removeAttribute('hidden');
    }
}