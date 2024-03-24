
const body = document.getElementById('contain')

let data = JSON.parse(sessionStorage.getItem('data'))
let audioText = {}
let count = 0
let values = Object.values(data)
for( let j = 0; j<values.length;j++){
    for(let i=0; i < Object.keys(values[j]).length ; i++){
            first = 
        `
            <div class="from">Gmail: ${Object.values(values[j])[i]['From']}</div>
        `
    }
    body.insertAdjacentHTML('beforeEnd',first)
    for(let i=0; i < Object.keys(values[j]).length ; i++){
        audioText[count++] = Object.values(values[j])[i]['email/text']
        email = Object.values(values[j])[i]['email/text']
        text = `
                    <div class="card" onclick="get_audio_file('${count-1}')">
                        <div class="info">
                            <div class="date">${Object.values(values[j])[i]['date']}</div>
                            <div class="label">${Object.keys(values[j])[i]}</div>
                            <div class="from">From:${Object.values(values[j])[i]['nameOfSender']}</div>
                        </div>
                        <div class="email">${Object.values(values[j])[i]['email/text']}</div>
                        
                        <audio class="audio">
                            <source src="" type="audio/mp3">
                        </audio>
                    </div>
                `
        body.insertAdjacentHTML('beforeEnd',text)
    }
    sessionStorage.setItem('audioText',JSON.stringify(audioText))
}



function get_audio_file(self){
    text = JSON.parse(sessionStorage.getItem('audioText'))[self]
    xhttp = new XMLHttpRequest()
    xhttp.open('POST','http://localhost:6969/audio')
    xhttp.responseType = 'arraybuffer'

    xhttp.onreadystatechange = function(){
        if(xhttp.readyState == 4 && xhttp.status == 200){
            arrayBuffer = xhttp.response
            const blob = new Blob([arrayBuffer], { type: "audio/mp3" });
            const url = window.URL.createObjectURL(blob);
            var audio = new Audio(url)
            audio.play()
        }
        
    }
    xhttp.send(text)   
}
    
        


// get_audio_file('this works')
// .then (response =>{
//     console.log(response)
// })

// var BASE64_MARKER = ';base64,';

// function convertDataURIToBinary(dataURI) {
//     var base64Index = dataURI.indexOf(BASE64_MARKER) + BASE64_MARKER.length;
//     var base64 = dataURI.substring(base64Index);
//     var raw = window.atob(base64);
//     var rawLength = raw.length;
//     var array = new Uint8Array(new ArrayBuffer(rawLength));
  
//     for(i = 0; i < rawLength; i++) {
//       array[i] = raw.charCodeAt(i);
//     }
//     return array;
//   }
