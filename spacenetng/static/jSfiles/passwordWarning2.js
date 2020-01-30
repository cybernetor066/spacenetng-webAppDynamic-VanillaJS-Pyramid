document.addEventListener("DOMContentLoaded", init, false); // Initialise the DOM Environment
	
function init() {
    window.addEventListener("load", warnUser, false);
}
// Function to remove warning after 6secs
function warnUser() {
    setTimeout(() => {document.getElementById('userWarning').setAttribute('hidden', '')}, 6000);
}