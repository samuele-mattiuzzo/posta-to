function submitComment() { 
    $.ajax({ 
        data: $(this).serialize(), 
        type: $(this).attr('method'), 
        url: $(this).attr('action'), 
        success: function(response) { 
            $('.sub_comments').html(response);
        }
    });
    return false;
}
