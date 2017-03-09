// document.addEventListener('click', function(event) {
//    console.log(event.target)
// })


// var Tracker = {};
//
// Tracker.start = (function () {
//
// })();


document.addEventListener('click', function(event) {
   console.log("x:" + event.clientX + " y:" + event.clientY );

    var data = new FormData();
    data.append('user_id',  1);
    data.append('current_page', '3');
    data.append('buttons_clicked', 'button');
    data.append('page_visited', '3');
    data.append('coordinates', event.clientX + ' y: ' + event.clientY);
    data.append('overall_time', '2:00');

    fetch("/tracker/api/index", {
        method: "POST",
        body: data
    })
    .then(function(res){
        return res.json();
    })
    .then(function(data){
        alert(JSON.stringify(data))
    })

});



document.addEventListener('click', function(event) {

   console.log(event.target)

   console.log("x:" + event.clientX + " y:" + event.clientY )
});



TimeMe.callAfterTimeElapsedInSeconds(15, function(){
    console.log("The user has been using the page for 15 seconds! Let's prompt them with something.");
});

  function getIP(json) {
    console.log("IP address: ", json.ip);
    document.cookie = (json.ip); "expires=Thu, 18 Dec 2018 12:00:00 UTC";
  }