
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