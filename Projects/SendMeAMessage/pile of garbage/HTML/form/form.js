function push(record) {
    var url = `https://api.aws.ltek.me/form/submit?name=${record.Name}&msg=${record.Message}`;
    
    fetch(url)
      .then(response => response.json())
      .then(data => {
        document.getElementById('respons').innerHTML = `
          <h2>${data.ok}</h2>
          <h2>${data.time}
          <p>Name: ${record.Name}</p>
          <p>Message: ${record.Message}</p>
        `;
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }
  
  function sumbit() {
    var name = document.getElementById('name').value;
    var msg = document.getElementById('message').value;
    
    var record = {
      Name: name,
      Message: msg
    };
    
    push(record);
  }
