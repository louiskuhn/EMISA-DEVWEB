var canvas = document.querySelector('#canvas');
var ctx = canvas.getContext('2d');
var mouse = {x: 0, y: 0};
var last_mouse = {x: 0, y: 0};
var canvas_size = 800

/* Mouse Capturing Work */
canvas.addEventListener('mousemove', function(e) {
    last_mouse.x = mouse.x;
    last_mouse.y = mouse.y;
    

    if (e.offsetX) {
        mouse.x = e.offsetX;
        mouse.y = e.offsetY;
    }
    else if (e.layerX) {
        mouse.x = e.layerX;
        mouse.y = e.layerY;
    }
}, false);

window.onload = function() {
    var canvas = document.getElementById("canvas");
    var context = canvas.getContext("2d");
    context.rect(0, 0, canvas_size, canvas_size);
    context.fillStyle = 'black';
    context.fill();
}

/* Drawing on Paint App */
ctx.lineWidth = 12;
ctx.lineJoin = 'round';
ctx.lineCap = 'round';
ctx.strokeStyle = 'white';

canvas.addEventListener('mousedown', function(e) {
    canvas.addEventListener('mousemove', onPaint, false);
}, false);

canvas.addEventListener('mouseup', function() {
    canvas.removeEventListener('mousemove', onPaint, false);
}, false);

var onPaint = function() {
    ctx.beginPath();
    ctx.moveTo(last_mouse.x, last_mouse.y);
    ctx.lineTo(mouse.x, mouse.y);
    ctx.closePath();
    ctx.stroke();
};

function clearCanvas() {
    var canvas = document.getElementById("canvas");
    var context = canvas.getContext("2d");
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.rect(0, 0, canvas_size, canvas_size);
    context.fillStyle = 'black';
    context.fill();
    document.getElementById('predRF').innerHTML = "";
    document.getElementById('predCNN').innerHTML = "";
}

function uploadImage() {
    var canvas = document.getElementById("canvas");
    var dataURL = canvas.toDataURL("image/png"); // Convertit le canvas en base64
    document.getElementById('data').value = dataURL; // Met à jour l'input caché
}