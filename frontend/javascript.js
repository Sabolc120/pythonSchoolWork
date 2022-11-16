var url = "http://127.0.0.1:5000/";

async function generator(url) {
    var request = await new XMLHttpRequest()

request.open('GET', url, true)
request.onload = function () {
  // Begin accessing JSON data here
  var data = JSON.parse(this.response)
view(data, request);

}

request.send()
  }

  function view(data, request){
    if (request.status >= 200 && request.status < 400) {
         data.forEach((query) => {
          console.log(request.status);
          var div = document.createElement("tr");
            var mainContainer = document.getElementById("view");
          div.innerHTML = "<td><input id='id"+query.id+"' placeholder = '"+query.id+"' value = '"+query.id+"'/>"+
          "<td><input id='name"+query.id+"' placeholder = '"+query.name+"' value = '"+query.name+"'/>"+
          "<td><input id='email"+query.id+"' placeholder = '"+query.email+"' value = '"+query.email+"'/>"+
          "<td><input id='phone"+query.id+"' placeholder = '"+query.phone+"' value = '"+query.phone+"'/>"+
          "<td><input id='position"+query.id+"' placeholder = '"+query.position+"' value = '"+query.position+"'/>"+
          "<button onclick = 'deleteData("+query.id+")' type = 'submit' value='Submit'>Delete</button>"+
          "<button onclick = 'updateData("+query.id+")' type = 'submit' value='Submit'>Update</button>"
          mainContainer.appendChild(div)
        })
      } else {
        console.log('error')
      }
  }

async function generate_html(){
await generator(url);
}

function deleteData(id){
  console.log("Funtion called")
  const data = JSON.stringify({
    id: parseInt(id)
  });
  
  navigator.sendBeacon('http://127.0.0.1:5000/deleteData/'+id, data);
  console.log(data);
}

function updateData(id){
  console.log("function calleeeeeeeeeeeeeeeeeeeeeeeeeeed")
  const data = JSON.stringify({
    id: document.getElementById("id"+id).value,
    name: document.getElementById("name"+id).value,
    email: document.getElementById("email"+id).value,
    phone: document.getElementById("phone"+id).value,
    position: document.getElementById("position"+id).value
  });
  navigator.sendBeacon('http://127.0.0.1:5000/updateData/'+id, data);
  console.log(data);
}

generate_html();
