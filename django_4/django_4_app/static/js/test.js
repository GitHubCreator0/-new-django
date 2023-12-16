function test(){
    $('#btn').click(function(){
        $.ajax('/test/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                 'text': $('#text').val(),
                 'tasks', $('#tasks').val()
                 'name': $('#id_name').val(),
                'deadline': $('#id_deadline').val(),
                'status': $('#id_status').val(),
                'priority': $('#id_priority').val()
                 },
                 'success': function(data){
                    document.getElementById('resp').innerHTML = data['resp']
                 }
        })
    })
}


$(document).ready(function(){
    test();
})