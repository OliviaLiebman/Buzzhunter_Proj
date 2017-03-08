// document.addEventListener('click', function(event) {
//    console.log(event.target)
// })

// function printMousePos(event) {
//   console.log =("clientX: " + event.clientX + " - clientY: " + event.clientY);
// }
//
// document.addEventListener("click", printMousePos(event));

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