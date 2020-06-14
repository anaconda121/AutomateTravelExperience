		init()
			function init() {
				var url = "https://api.covid19api.com/summary";
				var data = "";
				$.get(url, function(data){
					console.log(data.Global); //cleans out bad parts of data
					data = `

						<td> ${data.Global.TotalConfirmed}</td>
						<td> ${data.Global.TotalDeaths}</td>
						<td> ${data.Global.TotalRecovered}</td>

					` // `` allow people to write multiple lines of html in jquery
					$("#data").html(data);
				})
			}


		function refreshData() {
			clearData() //clears out previous entry
			init()
		}

		function clearData() {
			$("#data").empty()
			init()
		}