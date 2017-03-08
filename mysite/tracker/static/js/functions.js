// document.addEventListener('click', function(event) {
//    console.log(event.target)
// })




var Tracker = {};

Tracker.start = (function () {

})();
//


document.addEventListener('click', function(event) {
   console.log("x:" + event.clientX + " y:" + event.clientY )
});



TimeMe.callAfterTimeElapsedInSeconds(15, function(){
    console.log("The user has been using the page for 15 seconds! Let's prompt them with something.");
});
