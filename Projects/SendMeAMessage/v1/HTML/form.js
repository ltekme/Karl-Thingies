function push(record) {
    var url = `https://apigw.aws.ltek.me/dev/Messages/Submit?name=${record.Name}&msg=${record.Message}`;
    
    fetch(url)
      .then(response => response.json())
      .then(data => {
        document.getElementById('maincontent').innerHTML = `
          <a>${data.ok}</a><br>
          <a>Time(UTC): ${data.time}</a><br>
          <a>Name: ${record.Name}</a><br>
          <a>Message: ${record.Message}</a><br>
        `;
      })
      .catch(error => {
        document.getElementById('maincontent').innerHTML = `
          <a>${error}</a>
        `
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
