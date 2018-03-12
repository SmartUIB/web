$(document).ready(function(){
    
    //save idea form
    var frm = $('form');
    frm.submit(function(e){
        e.preventDefault();
        $.ajax({
            type: frm.attr('method'),
            // url: frm.attr('action'),
            data: frm.serialize(),
            dataType: 'json',
            success: function (data) {
                alert(data['message']);
                frm.trigger('reset');
            },
            error: function(data) {
                alert(data['responseJSON']['message']);
            }
        });
    });
    
})
