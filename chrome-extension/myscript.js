// var reportURL = function (url) {
//     var response;
//     if (!httpRequest) {
//         httpRequest = new XMLHttpRequest();
//         httpRequest.open("GET", url, true);
//         //httpRequest.setRequestHeader('Access-Control-Allow-Methods', 'GET');
//         response.setHeader('access-control-allow-origin', '*');
//         httpRequest.send(null);
//     } else if (httpRequest.readyState === 4) {
//         response = httpRequest.responseText;
//         httpRequest = null;
//         return response;
//     }
//     return reportURL(url);
// };

// var script = document.createElement('script');
// script.src = 'http://jqueryjs.googlecode.com/files/jquery-1.2.6.min.js';
// script.type = 'text/javascript';
// document.getElementsByTagName('head')[0].appendChild(script);

setTimeout(function() { document.getElementsByClassName('thumbUpButton')[0].onclick =
    function () {
        alert("sup");
        var trackData = document.getElementsByClassName("trackData")[0];
        var song = trackData.firstElementChild;
        var song_name = song.textContent;
        var data = {
            "name": song_name,
            "artist": "",
        }
        $.ajax({
          type: "POST",
          dataType: "json",
          contentType: 'application/json;charset=UTF-8',
          url: "http://127.0.0.1:5000/downloads/",          
          data: JSON.stringify(data),
          success: function(result) {
            alert(result['url']);
          }
        });        
    };
}, 6000);