//AJAX search functions - requires 'result' tagged div

$(document).ready(function(){

    $("input").on('input',function(){
        var query = $('input').val();
        var result_target = $("#result");
        if(query===""){
            result_target.text("");
            return;
        }

        $.ajax({
            url:"/search/",
            type: "GET",
            data: {'query' : query},

            success: function(json){
                result_target.empty();
                for(var i=0; i<json.results.length; i++){
                    result_target.append("<b>"+json.results[i]+"</b><br>");
                }
            },

            error: function(){
                result_target.text("An error occurred");
            }
        });
    });
});


