// Parse product names and stock quantities passed from the backend as JSON strings
const names = JSON.parse('{{ names_json | safe }}');        // Array of product names
const quantities = JSON.parse('{{ quantities_json | safe }}');  // Corresponding array of stock quantities

// Get the 2D drawing context of the canvas element with ID 'stockChart'
const ctx = document.getElementById('stockChart').getContext('2d');

// Create a new bar chart using Chart.js
new Chart(ctx, {
    type: 'bar',  // Chart type: bar chart
    data: {
        labels: names,  // X-axis labels (product names)
        datasets: [{
            label: 'Stock Quantity',           // Legend label
            data: quantities,                  // Y-axis data (stock quantities)
            backgroundColor: 'rgba(52, 152, 219, 0.6)',  // Bar fill color
            borderColor: 'rgba(52, 152, 219, 1)',        // Bar border color
            borderWidth: 1                    // Border thickness
        }]
    },
    options: {
        responsive: true,  // Make the chart responsive to window size
        scales: {
            y: {
                beginAtZero: true,  // Start Y-axis at zero
                ticks: {
                    stepSize: 1    // Use a step of 1 unit for Y-axis labels
                }
            }
        }
    }
});