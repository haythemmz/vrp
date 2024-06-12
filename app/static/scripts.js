document.getElementById('dataForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const data = {
        // Collect form data
    };
    fetch('/submit_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(results => {
        // Handle results
    });
});
