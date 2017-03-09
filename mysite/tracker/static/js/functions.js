

// var Tracker = {};
//
// Tracker.start = (function () {
//
// })();


document.addEventListener('click', function(event) {
   console.log("x:" + event.clientX + " y:" + event.clientY );
    console.log(event.target.innerHTML);
    console.log(str);

    if(event.target instanceof SVGElement) {
        var s = new XMLSerializer();
        var d = document;
        var str = s.serializeToString(d);
        var data = new FormData();
        data.append('user_id',  1);
        data.append('current_page', '3');
        data.append('buttons_clicked', str);
        data.append('page_visited', '3');
        data.append('coordinates', event.clientX + ' y: ' + event.clientY);
        data.append('overall_time', '2:00');
    }

    else {
        var data = new FormData();
        data.append('user_id',  1);
        data.append('current_page', '3');
        data.append('buttons_clicked', event.target.innerHTML);
        data.append('page_visited', '3');
        data.append('coordinates', event.clientX + ' y: ' + event.clientY);
        data.append('overall_time', '2:00');
    }


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






TimeMe.callAfterTimeElapsedInSeconds(15, function(){
    console.log("The user has been using the page for 15 seconds! Let's prompt them with something.");
});
