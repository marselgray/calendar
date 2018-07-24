//removes calendar entry function 
function deleteCalendarEntry(entry){

    //entry variable 
    var $entry = $(entry)
    $(entry).parent().remove()
    var id = $entry.data('id')

    //ajax delete request 
    $.ajax({
        url: 'entry/delete/' + id,
        method: 'DELETE',
        beforeSend: function(xhr){
            xhr.setRequestHeader('X-CSRFToken', csrf_token)
        }
    })
};



