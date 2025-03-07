//Listening for the page to load
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const firstName = document.getElementById("first-name");
    const lastName = document.getElementById("last-name");
    const rating = document.getElementById("rating");
    const resultsContainer = document.getElementById("results");

    //Fetch and display existing results
    fetchResults();

    //Form submission
    form.addEventListener("submit", function (event) {  
        event.preventDefault();

        //Validating User Input
        if (validateInputs()) {
            //Making sure a response is selected
            const selectedResponse = document.querySelector('input[name="response"]:checked');
            if (!selectedResponse) {
                alert("Please select a response.");
                return;
            }

            //Create JavaScript ojbect called userData
            const userData = {
                firstName: firstName.value.trim(),
                lastName: lastName.value.trim(),
                response: selectedResponse.value,
                rating: rating.value,
            };

            //Send data to Flask backend
            fetch("/submit", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(userData),
            })
            //Handling server response
            .then(response => response.json())
            .then(result => {
                alert(result.message);
                fetchResults(); //Refresh displayed results after submission
            })
            .catch(error => console.error("Error:", error));
        }
    });

    //Validating user's inputs
    function validateInputs() {
        let isValid = true;
        if (!firstName.value.trim()) {
            alert("First name is required.");
            isValid = false;
        }
        if (!lastName.value.trim()) {
            alert("Last name is required.");
            isValid = false;
        }
        if (!rating.value.trim()) {
            alert("Rating is required.");
            isValid = false;
        }
        return isValid;
    }

    //Fetching and displaying previous submissions
    function fetchResults() {
        fetch("/get_data")
            .then(response => response.json())
            .then(data => {
                resultsContainer.innerHTML = "";

                if (data.length === 0) {
                    resultsContainer.innerHTML = "<p>No Records</p>";
                    return;
                }

                //Calculate percentage of "Yes" responses
                const percentageYes = calculateTruePercentage(data);

                data.forEach((entry, index) => {
                    const resultItem = document.createElement("div");
                    resultItem.innerHTML = `
                        <strong>${index + 1}. ${entry.firstName} ${entry.lastName}</strong> - 
                        <strong>Warming quicker: ${entry.response === "true" ? "Yes" : "No"}</strong> - 
                        <strong>Rating: ${entry.rating}</strong>
                    `;
                    resultsContainer.appendChild(resultItem);
                });

                //Add "Did you know?" paragraph
                const didYouKnow = document.createElement("p");
                didYouKnow.innerHTML = `Did you know? <strong>${percentageYes}%</strong> of users responded "Yes: Their country is warming quicker than average"`;
                resultsContainer.appendChild(didYouKnow);
            })
            .catch(error => console.error("Error loading results:", error));
    }

    //Function to calculate the percentage of "true" responses
    function calculateTruePercentage(data) {
        if (!data || data.length === 0) {
            return 0; //No data available
        }

        const totalEntries = data.length;
        const trueCount = data.filter(entry => entry.response === "true").length;
        return ((trueCount / totalEntries) * 100).toFixed(2); //Round to 2 decimal places
    }
});
