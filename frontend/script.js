fetch('http://localhost:8080/get_data')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log('Data received:', data);
            i = 0;
            let code_1 = data[0]["hangup_count"]; // Assuming "rank" holds the number you want to display for code_1
            let code_2 = data[1]["hangup_count"];
            let code_3 = data[2]["hangup_count"];

            document.querySelector('.podium-label_1').textContent = code_1;
            document.querySelector('.podium-label_2').textContent = code_2;
            document.querySelector('.podium-label_3').textContent = code_3;
    
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });