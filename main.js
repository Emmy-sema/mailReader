// var login = document.getElementById('submit')

// login.addEventListener('click', ()=>{
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            console.log("User data received!");
                   // Set current data text
            sessionStorage.setItem('data',xhttp.responseText);
            location.href= '/account.html'
        }
    }
    xhttp.open("GET", "http://localhost:6969/gmail", true);
    xhttp.send(null);

// })
