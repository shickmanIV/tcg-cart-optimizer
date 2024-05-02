document.getElementById("searchForm").addEventListener("submit", function(event) {
    event.preventDefault(); 

    // Get the search query from the html file
    var query = document.getElementById("searchInput").value;

    // Send query to py file
    fetch("http://localhost:5000/search?query=" + encodeURIComponent(query))
        .then(response => response.json())
        .then(data => {
        
            var resultsDiv = document.getElementById("results");
            resultsDiv.innerHTML = ""; // Clear previous result

            for (let i = 0; i < data.length; i += 2) {
                // Create a div element to contain the name and ID
                var cardContainer = document.createElement("div");

                // // Create a span element for the card ID
                // var idElement = document.createElement("span");
                // idElement.textContent = data[i + 1]; // ID
                // cardContainer.appendChild(idElement);
    
                // // Add a separator between name and ID
                // cardContainer.appendChild(document.createTextNode(" - "));
    
                // Create an anchor element for the card name
                var nameElement = document.createElement("a");
                nameElement.textContent = data[i]; // Name
                nameElement.href = 'cardPage.html?query=' + encodeURIComponent(data[i+1]);
                cardContainer.appendChild(nameElement);
    
                // Append the card container to the resultsDiv
                resultsDiv.appendChild(cardContainer);
    
                // Add a line break after each card container
                resultsDiv.appendChild(document.createElement("br"));
            }
        })
        .catch(error => console.error('Error:', error));
        
});