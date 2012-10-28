function submitComment() { // catch the form's submit event
    $.ajax({ // create an AJAX call...
        data: $(this).serialize(), // get the form data
        type: $(this).attr('method'), // GET or POST
        url: $(this).attr('action'), // the file to call
        success: function(response) { // on success..
            $('#DIV_CONTAINING_FORM').html(response); // update the DIV
        }
    });
    return false;
}
