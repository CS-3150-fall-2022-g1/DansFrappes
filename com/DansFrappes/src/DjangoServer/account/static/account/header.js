function sendToMenu() {
    location.href = '/menu/';
}


const header = document.createElement("div");
header.id = "headerDiv";
document.body.appendChild(header);

h1_1 = document.createElement("h1");
h1_1.innerHTML = "Dan's Frappes";
header.appendChild(h1_1);

bufferDiv = document.createElement("div");
bufferDiv.id = "bufferdiv";
document.body.appendChild(bufferDiv);

header.onclick = sendToMenu;