function sendPost(){
    const data = JSON.stringify({
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        position: document.getElementById("position").value
      });
      
      navigator.sendBeacon('http://127.0.0.1:5000/addData/', data);
      console.log(data);
    }