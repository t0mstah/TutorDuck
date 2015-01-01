//AJAX search functions - requires 'result' tagged div

$(document).ready(function(){

    $("input").on('input',function(){
        var query = $('input').val();
        if(query===""){
            $('.tutor-card').each(function(i, obj){
                $(this).fadeIn('fast');
            });
        }
        var department = $('.page-header').first().attr('id');

        $.ajax({
            url:"/search/",
            type: "GET",
            data: {'query' : query, 'dept' : department},

            success: function(json){
                $('.tutor-card').each(function(i, obj){
                    if($.inArray($(this).attr('id'),json.results) == -1)
                        $(this).fadeOut('fast');
                    else $(this).fadeIn('fast');
                });
            },

            error: function(){
                alert("An error occurred while searching.");
            }
        });
    });
});


