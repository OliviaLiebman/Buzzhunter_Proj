/**
 * Created by olivialiebman on 3/13/17.
 */
console.log('i am in dashboard js');

// var finalArray;
/*var retVal = null;*/

// $(document).ready(function() {
    // function createTable(datagrabbed) {
    //
    //       finalArray = datagrabbed.map(function (obj) {
    //           return [obj.buttons_clicked, obj.coordinates, obj.current_page];
    //       });

        // console.log(datagrabbed);


    //     $('#example').DataTable({
    //     //            "processing": true,
    //     // "serverSide": true,
    //         ajax: "tracker/api/index/",
    //         // "type": "POST",
    //         // data:datagrabbed,
    //         // data: [{buttons_clicked:3, coordinates: 4, current_page:5}, {buttons_clicked:3, coordinates: 4, current_page:5}, {buttons_clicked:3, coordinates: 4, current_page:5}],
    //         columns: [
    //             { "data": "buttons_clicked" },
    //             { "data": "coordinates" },
    //             { "data": "current_page" },
    //             { "data": "date_time_of_access" },
    //              { "data": "id" },
    //             { "data": "overall_time" },
    //             { "data": "page_visited" },
    //             { "data": "user_id" }
    //              ]
    //     });
    // });


     // $.ajax({
     //        type: 'GET',
     //        url: "http://127.0.0.1:8500/tracker/api/index/",
     //  success: function(datagrabbed) {
     //      console.log(datagrabbed);
     //      // var data = datagrabbed;
     //      console.log(datagrabbed);
     //      createTable(datagrabbed);
     //  }});

    // console.log(data);
  //   function createTable(datagrabbed) {
  //
  //       $('#example').DataTable({
  //           data: datagrabbed,
  //           columns: [
  //               { data: "buttons_clicked" },
  //               { data: "coordinates" },
  //               { data: "current_page" },
  //               { data: "date_time_of_access" },
  //               { data: "id" },
  //               { data: "overall_time" },
  //               { data: "page_visited" },
  //               { data: "user_id" }
  //               ]
  //       });
  //   }
  //
  // });

  function createTable(data) {

        $('#example').DataTable({
            "data": data,
            columns: [
                { "data": "buttons_clicked" },
                { "data": "coordinates" },
                { "data": "current_page" },
                { "data": "date_time_of_access" },
                { "data": "id" },
                { "data": "overall_time" },
                { "data": "page_visited" },
                { "data": "user_id" }
                 ]
        });
    }

     $.ajax({
            type: 'GET',
            url: "http://127.0.0.1:8500/tracker/api/index/",
      success: function(datagrabbed) {
          console.log(datagrabbed);
          createTable(datagrabbed);
      }});











