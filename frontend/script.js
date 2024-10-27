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
            code_1 = console.log(data[i+1], data[i+1]["rank"]);
            code_1 = console.log(data[i+2], data[i+2]["rank"]);
            code_1 = console.log(data[i+3], data[i+3]["rank"]);
    
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });