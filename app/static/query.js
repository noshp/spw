
// Read input content
// ... send it to spwguesser
// ... receive reply
function input_to_db() {
		var entries = document.getElementById("search_bar_input").value
		console.log("Sending: "+entries)

		$.getJSON($SCRIPT_ROOT + "/guesser", {
			entries: entries
		}, function(data){
			$("#input_result").text(data)
		})
	}