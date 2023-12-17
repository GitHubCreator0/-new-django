function test(){
    $('#btn').click(function(){
        $.ajax('/test/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                 'text': $('#text').val()
                 },
                 'success': function(data){
                    document.getElementById('resp').innerHTML = data['resp']
                 }
        })
    })
}


$(function(){
    $('#btn1').click(function(){
    var button = $(this)
        $.ajax(button.data('url'), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                 'name': $('#id_name').val(),
                'deadline': $('#id_deadline').val(),
                'status': $('#id_status').val(),
                'priority': $('#id_priority').val()
            },
            'success': function(data){
               document.getElementById('tasks').innerHTML += data
            }
        })
    })
})

$(function(){
    $(document).click(function(event){
        var element = $(event.target);
        if (element.attr('class') == 'edit_task') {
            $.ajax(element.data('url'), {
                'type' : 'POST',
                'async' : true,
                'dataType' : 'json',
                'data' : {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'id' : element.attr('id')
                },
                'success': function(data){
               document.getElementById('edit').innerHTML += data
               }
            })
        }
    })
})

$(document).ready(function(){
    test();
})