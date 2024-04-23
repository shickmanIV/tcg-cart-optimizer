// // Code to execute when the document is loaded
// document.addEventListener("DOMContentLoaded", function() {
//     // Get the query parameter from the URL
//     const urlParams = new URLSearchParams(window.location.search);
//     const query = urlParams.get('query');

//     // Check if the current page is cardPage.html
//     if (window.location.pathname.includes("cardPage.html")) {
//         // Fetch card-specific information using the query parameter
//         fetch("http://localhost:5000/search?query=" + encodeURIComponent(query))
//             .then(response => response.json())
//             .then(data => {
//                 displayCardInfo(data);
//             })
//             .catch(error => console.error('Error:', error));
//     }
// });



// function displayCardInfo(cardData) {
//     // Get the elements where the information will be displayed
//     var nameElement = document.getElementById("cardName");
//     var imageElement = document.getElementById("cardImage");
//     var idElement = document.getElementById("cardId");

//     // Set the text content or attributes of the elements with the fetched data
//     nameElement.textContent = "Name: " + cardData[0];
//     imageElement.src = cardData[1];
//     idElement.textContent = "ID: " + cardData[2];
// }