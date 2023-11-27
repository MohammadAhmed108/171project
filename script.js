$(document).ready(function(){
    $('#text-form').on('submit', function(e){
        e.preventDefault();
        var inputData = $('#input-text').val();
        $.ajax({
            type: 'POST',
            url: '/analyze', // This is the route we will set up on our Flask backend
            data: JSON.stringify({ text: inputData }),
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            success: function(response) {
                $('#result').html('Sentiment score: ' + response.prediction);
            },
            error: function(error) {
                $('#result').html('Error: ' + error);
            }
        });
    });
});
