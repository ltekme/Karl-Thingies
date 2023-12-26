//cat meme scrow
function shme() {
  m = Math.floor(Math.random() * 9);
  document.getElementById("meme").innerHTML = `
<img src="img/cat_meme/m${m}.jfif" alt="">
`;
}

function gemememe() {
  shme()
  let i = 0;
  const intervalId = setInterval(() => {
      shme();
      i++;
      if (i >= 100) {
          clearInterval(intervalId);
      }
  }, 2000);
}

//cat types scrow
function sbr(abl) {
  const breads = ["Abyssinian", "American Bobtail", "American Curl", "American Shorthair", "American Wirehair"]
  document.getElementById("breads").innerHTML = `
  <h4>${breads[abl]}:</h4>
    <img src="img/breed/${abl}.jfif" alt="">
`;
}

function sbr_b() {
  abl--;
  if (abl < 0) {
      abl = 4;
  }
  sbr(abl);
}

function sbr_s() {
  abl = 0;
  sbr(abl);
}

function sbr_f() {
  abl++;
  if (abl > 4) {
      abl = 0;
  }
  sbr(abl);
}

// for submition
function submitaction() {
  var hell = {
      name: document.getElementById("Name").value,
      sid: document.getElementById("StudentID").value,
      email: document.getElementById("Email").value,
      news: document.getElementById("News").checked
  };
  conf = confirm(`
Please check information:
Name: ${hell.name}
Student ID: ${hell.sid}
Email: ${hell.email}
`);
  if (hell.name == '') {
      alert("no Name")
      return false
  } else if  (hell.sid == '') {
      alert("no student ID")
      return false
  }else {
      if (conf == true) {
          alert('ok meow \n submitting')
          push(hell)
          return false
      } else {
          console.log("Cancaled Meow")
          return false
      }
  }
}

api_url = 'https://uy36ibbrac.execute-api.ap-east-1.amazonaws.com/signup'

function push(record) {
  var url = `${api_url}?sid=${record.sid}&name=${record.name}&email=${record.email}&news=${record.news}`;
  fetch(url)
      .then(response => response.json())
      .then(data => {
          alert(data.ok);
      })
      .then(() => {
          document.getElementById("Name").value = '';
          document.getElementById("StudentID").value = '';
          document.getElementById("Email").value = '';
          document.getElementById("News").checked = false;
      });
}