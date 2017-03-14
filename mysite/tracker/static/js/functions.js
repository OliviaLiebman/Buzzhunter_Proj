// var Tracker = {};
//
// Tracker.start = (function () {
//
// })();

// var url='127.0.0.1:8500'; //change the port to whichever port is being used for runserver, default is 8000


// if (event.target.id == 'welcome'){
//         var a = document.getElementById('menu-item-75').getElementsByTagName('a')[0];  //will get the href of what is attached to this id
//         var link = '127.0.0.1:8500/tracker/portfolio/';
//         // a.href = link;
//         // window.location.href = '127.0.0.1:8500/tracker/portfolio/';
//         console.log(link);
//         console.log(a);
//         alert("buzz clicked with id = " + event.target.id);
//         // window.location.href='127.0.0.1:9000/tracker/portfolio/';
//    }


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
    user_interaction_table(json.ip)

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
// (function checkCookie() {
//     var user = getCookie("username");
//     if (user != "") {
//         alert("Welcome again " + user);
//     } else {
//         user = prompt("Please enter your name:", "");
//         if (user != "" && user != null) {
//             setCookie("username", user, 365);
//         }
//     }
// })();

    function user_interaction_table(user_id) {
        var data = new FormData();
        data.append('user_id', user_id);
        data.append('overall_time', '4:00');

        // data.append('session_id', '5.40');


        fetch("/tracker/api/index/1", {
            method: "POST",
            body: data
        })
            .then(function (res) {
                return res.json();
            })
            .then(function (data) {
                // alert(JSON.stringify(data))
            })
    }



document.addEventListener('click', function(event) { //add a click event listener on the whole doc


    console.log("x:" + event.clientX + " y:" + event.clientY );//returns x- and y-pos
    // if(event.target instanceof SVGElement) {
    //     var s = new XMLSerializer();
    //     var d = event.target;
    //     var str = s.serializeToString(d);
    //     console.log(str);
    //     var data = new FormData();
    //     data.append('user_id',  1);
    //     data.append('current_page', '3');
    //     data.append('buttons_clicked', str);
    //     data.append('page_visited', '3');
    //     data.append('coordinates', event.clientX + ' y: ' + event.clientY);
    //     data.append('overall_time', '2:00');
    //     // data.append('session_id', '5.40');
    // }
    // else {
    //     console.log(event.target.innerHTML);
    //     var data = new FormData();
    //     data.append('user_id', 1);
    //     data.append('current_page', '3');
    //     data.append('buttons_clicked', event.target.innerHTML);
    //     data.append('page_visited', '3');
    //     data.append('coordinates', event.clientX + ' y: ' + event.clientY);
    //     data.append('overall_time', '2:00');
    //     // data.append('session_id', '5.40');
    //
    // }
 if(event.target instanceof SVGElement) {
        var s = new XMLSerializer();
        var d = event.target;
        var str = s.serializeToString(d);
        console.log(str);
        var data = new FormData();
        data.append('user_id',  1);
        data.append('current_page', '3');
        data.append('buttons_clicked', str);
        data.append('coordinates', event.clientX + ' y: ' + event.clientY);
        // data.append('session_id', '5.40');
    }
    else {
        console.log(event.target.innerHTML);
        var data = new FormData();
        data.append('user_id',  1);
        data.append('current_page', '3');
        data.append('buttons_clicked', str);
        data.append('coordinates', event.clientX + ' y: ' + event.clientY);
        // data.append('session_id', '5.40');

    }
    fetch("/tracker/api/index/2", {
        method: "POST",
        body: data
    })
    .then(function(res){
        return res.json();
    })
    .then(function(data){
        // alert(JSON.stringify(data))
    })




//     TimeMe.callAfterTimeElapsedInSeconds(1, function(){
//     console.log("The user has been using the page for 1 second. Let's prompt them with something.");
//     });
//
//     TimeMe.callWhenUserLeaves(function(){
//     console.log("The user is not currently viewing the page!");
// }, 5);
//
// // Executes every time a user returns
// TimeMe.callWhenUserReturns(function(){
//     console.log("The user has come back!");
// });
//
// window.onbeforeunload = function (event) {
//     xmlhttp=new XMLHttpRequest();
//     xmlhttp.open("POST","ENTER_URL_HERE", true);
//     xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//     var timeSpentOnPage = TimeMe.getTimeOnCurrentPageInSeconds();
//     xmlhttp.send(timeSpentOnPage);
// };



});

