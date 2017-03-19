/**
 * Created by olivialiebman on 3/13/17.
 */
console.log('i am in dashboard js');

  function createUserInteractionTable(data) {

        $('#user-interaction-table').DataTable({
            "data": data,
            columns: [
                { "data": "user_id" },
                { "data": "user_name" },
                { "data": "user_email" },
                { "data": "session_id" },
                { "data": "overall_time" },
                { "data": "date_time_of_access" },
                { "data": "percentage_scroll" }
            ]
        });
    }

         $.ajax({
            type: 'GET',
            url: "http://127.0.0.1:8000/tracker/api/index/1/",
      success: function(datagrabbed) {
          console.log(datagrabbed);
          createUserInteractionTable(datagrabbed);
      }});

   function createPageInteractionTable(data) {

        $('#page-interaction-table').DataTable({
            "data": data,
            columns: [
                { "data": "user_id" },
                { "data": "session_id" },
                { "data": "current_page" },
                { "data": "buttons_clicked" },
                { "data": "coordinates" }
                 ]
        });
    }

     $.ajax({
            type: 'GET',
            url: "http://127.0.0.1:8000/tracker/api/index/2/",
      success: function(datagrabbed) {
          console.log(datagrabbed);
          createPageInteractionTable(datagrabbed);
      }});
