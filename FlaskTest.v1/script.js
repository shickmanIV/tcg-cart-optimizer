
document.getElementById("searchForm").addEventListener("submit", function(event) {
    event.preventDefault(); 

    // Get the search query from the html file
    var query = document.getElementById("searchInput").value;

    // Send query to py file
    fetch("http://localhost:5000/search?query=" + encodeURIComponent(query))
        .then(response => response.json())
        .then(data => {
        
            var resultsDiv = document.getElementById("results");
            resultsDiv.innerHTML = ""; // Clear previous results

            data.forEach(result => { // Text
                var resultElement = document.createElement("div");
                resultElement.textContent = result;
                resultsDiv.appendChild(resultElement);
            });

            // data.forEach(result => { // Image URL
            //     var imgElement = document.createElement("img");
            //     imgElement.src = result;
            //     resultsDiv.appendChild(imgElement);
            // });
        })
        .catch(error => console.error('Error:', error));
        
});
