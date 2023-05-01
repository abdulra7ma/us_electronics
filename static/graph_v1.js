const ctx = document.getElementById('myChart');

function updateChart() {
    console.log('updating chart');
    const url = "http://127.0.0.1:8000/api/data";
  // Make a request to your backend
  fetch(url)
    .then(response => response.json())
    .then(data => {
        console.log(data);
      // Use the response to update the chart
      const labels = data.map(item => item.end_time);
      const values = data.map(item => item.distance);

      const chartData = {
        labels: labels,
        datasets: [{
          label: '# of Votes',
          data: values,
          borderWidth: 1
        }]
      };

      new Chart(ctx, {
        type: 'line',
        data: chartData,
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    });
}

// Call the function to initially update the chart
updateChart();