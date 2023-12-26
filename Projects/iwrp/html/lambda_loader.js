const api_url = 'https://7yll41tdl8.execute-api.ap-east-1.amazonaws.com/prod/iwrp-func';

function submit() {
  let sid = document.getElementById('sid').value;
  let name = document.getElementById('name').value;
  let msg = document.getElementById('msg').value;
  let confirmation = confirm(`
    Do you want to submit this response?
    Session: ${sid}
    Name: ${name}
    Response: ${msg}
  `);
  if (confirmation) {
    let request_url = `${api_url}/post?sid=${encodeURIComponent(sid)}&name=${encodeURIComponent(name)}&msg=${encodeURIComponent(msg)}`;
    // {time: '2023-12-15 13-26-11', name: 'anonmus', msg: 'test', ok: 'Your Response Has Been Submited'}
    fetch(request_url)
      .then(response => response.json())
      .then(data => {
        alert(data.ok);
        document.getElementById('msg').value = '';
      })
      .catch(error => {
        console.log(error);
        alert('Something went wrong');
      });
  }
}

function apiGet() {
  let request_url = `${api_url}/view?sid=${encodeURIComponent(sid)}`;
  fetch(request_url)
    .then(response => response.json())
    .then(data => {
      var response_items = '';
      data.forEach(item => {
        var time_htm = '';
        var name_htm = '';
        var msg_htm = '';
        if (document.getElementsByName('shw_item')[0].checked) 
          time_htm = `<a>Time: ${item.time}</a><br>`;
        if (document.getElementsByName('shw_item')[1].checked) 
          name_htm = `<a>Name: ${item.name}</a><br>`;
        if (document.getElementsByName('shw_item')[2].checked) 
          msg_htm = `<a>Response: ${item.msg}</a><br>`;
        console.log
        response_items += `<div class="response_item">
          ${time_htm}
          ${name_htm}
          ${msg_htm}
        </div>`;
      });
      document.getElementById('session_items').innerHTML = response_items;
    })
    .catch(error => {
      console.log(error);
      alert('Something went wrong');
    });
}

function getResponse() {
  apiGet()
  let nd = new Date();
  let cd = `Last Updated: ${nd.getHours()}:${nd.getMinutes()}:${nd.getSeconds()}`;
  document.getElementById('last_updated').innerHTML = cd;
}
