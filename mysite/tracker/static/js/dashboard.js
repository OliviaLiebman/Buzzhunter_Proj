/**
 * Created by olivialiebman on 3/13/17.
 */

$(document).ready(function() {
    $('#example').DataTable( {
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "scripts/post.php",
            "type": "POST"
        },
        "columns": [
            { "data": "user_id" },
            { "data": "current_page" },
            { "data": "buttons_clicked" },
            { "data": "pages_visited" },
            { "data": "coordinates" },
            { "data": "overall_time" },
            { "data": "date_time_of_access" }
        ]
    } );
} );