
// Read input content
// ... send it to spwguesser
// ... receive reply
function input_to_db()
	{
		var entries = document.getElementById("search_bar_input").value
		console.log("Sending: "+entries)

		$.ajax({
			url: '../static/guesser.py',
			data: {param: entries},
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	}