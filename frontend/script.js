fetch('http://localhost:8080/get_data')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log('Data received:', data);
    for (i = 0; i < 4; i++) {
        console.log(data[i], data[i]["rank"]);
    }
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });