
/* expands the comments div */
function expander(div){
    $(div).toggle("fast");
    return false;
}

/* casts a plus or a down vote on a post */
function cast_vote(id, vote){

	$.ajax({
		data : { },
		url : '/vote/'+id+'/'+vote+'/',
		type : 'POST',

		success: function(data) {
        	if ( vote == 'plus') {
        		$('span.promote').html(data);
        	} else {
        		$('span.demote').html(data);
        	}
        },

        error: function(data) { }

	});

	return false;
}

/* paginator for the history */
function change_page(page){

    /* if there's no next/prev, error function will handle with empty behaviour */
    var next = parseInt(page)+1;
    var prev = parseInt(page)-1;

    $.ajax({
        data : { },
        url : '/posts/paginate/'+page+'/',
        type : 'POST',

        success: function(data){
            /* updating the history div */
            $('#history').fadeOut('slow', function() {
                $('#history').html(data);
                $('#history').fadeIn('slow', function() {});
            });

            /* updating the current page div */
            $('.curr').html(page);

            /* updating the links */
            $('#next_page').onclick = new Function(next, 'change_page("'+next+'");');
            $('#prev_page').onclick = new Function(prev, 'change_page("'+prev+'");');
        },

        error: function(data){}

    });

    return false;
}

