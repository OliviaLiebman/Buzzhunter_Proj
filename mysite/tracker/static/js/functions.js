

// var Tracker = {};
//
// Tracker.start = (function () {
//
// })();
var url='127.0.0.1:8500';

document.addEventListener('click', function(event) {
   console.log("x:" + event.clientX + " y:" + event.clientY );
   // console.log(event.target.innerHTML);
   // console.log(str);

   if (event.target.id == 'welcome'){

      var a = document.getElementById('menu-item-75').getElementsByTagName('a')[0];  //will get the href of what is attached to this id
       var link = '127.0.0.1:8500/tracker/portfolio/';
       // a.href = link;
       // window.location.href = '127.0.0.1:8500/tracker/portfolio/';
       console.log(link);
       console.log(a);
       alert("buzz clicked with id = " + event.target.id);
       // window.location.href='127.0.0.1:9000/tracker/portfolio/';
   }

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
        // alert(JSON.stringify(data))
    })

});



TimeMe.callAfterTimeElapsedInSeconds(1, function(){
    console.log("The user has been using the page for 1 second. Let's prompt them with something.");

});


function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

  function getIP(json) {
    console.log("IP address: ", json.ip);
    // document.cookie = (json.ip); "expires=Thu, 18 Dec 2018 12:00:00 UTC";

    setCookie('buzz_cookie', json.ip, 365);
    console.log("inside cookie:" + json.ip);

  }

  function getCookie(cname) {//pass in key
    var name = cname + "=";
    var ca = document.cookie.split(';'); //list of key-value pairs of cookies
    for(var i = 0; i < ca.length; i++) { //loops through length of list
        var c = ca[i];
        while (c.charAt(0) == ' ') { //gets rid of leading white spcae
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length); //returns the value of the key-value pair
        }
    }
    return "";
}
(function checkCookie() {
    var user = getCookie("username");
    if (user != "") {
        alert("Welcome again " + user);
    } else {
        user = prompt("Please enter your name:", "");
        if (user != "" && user != null) {
            setCookie("username", user, 365);
        }
    }
})();
