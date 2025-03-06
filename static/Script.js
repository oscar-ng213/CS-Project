document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const firstName = document.getElementById("first-name");
    const lastName = document.getElementById("last-name");
    const rating = document.getElementById("rating");
    const resultsContainer = document.getElementById("results");
    
    fetchResults();

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        if (validateInputs()) {
            const selectedResponse = document.querySelector('input[name="response"]:checked');
            if (!selectedResponse) {
                alert("Please select a response.");
                return;
            }
    
            const userData = {
                firstName: firstName.value.trim(),
                lastName: lastName.value.trim(),
                response: selectedResponse.value,
                rating: rating.value.trim(),
            };
        
            fetch("/submit", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(userData),
            })
            .then(response => response.json())
            .then(result => {
                alert(result.message);
                fetchResults();
            })
            .catch(error => console.error("Error:", error));
        }
    });

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

    function fetchResults() {
        fetch("/get_data")
            .then(response => response.json())
            .then(data => {
                resultsContainer.innerHTML = "";
                if (data.length === 0) {
                    resultsContainer.innerHTML = "<p>No Records</p>";
                    return;
                }
                data.forEach((entry, index) => {
                    const resultItem = document.createElement("div");
                    resultItem.innerHTML = `
                        <strong>${index + 1}. ${entry.firstName} ${entry.lastName}</strong> -
                        <strong>Warming quicker: ${entry.response === "true" ? "Yes" : "No"}</strong> -
                        <strong>Rating: ${entry.rating}</strong>
                    `;
                    resultsContainer.appendChild(resultItem);
                });
            })
            .catch(error => console.error("Error loading results:", error));
    }
});
