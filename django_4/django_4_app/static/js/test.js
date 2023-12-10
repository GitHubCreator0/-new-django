function test(){
    $('#btn').click(function(){
        $.ajaz('/test/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json'
            'data': {
                'csrfmiddlewaretoken':
                 $('input[name="csrfm
                 iddlewaretoken"]').val(),
            }
        })
    })
}


$(document).ready(function(){
    test();
})
}