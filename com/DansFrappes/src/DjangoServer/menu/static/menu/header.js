
const header = document.createElement("div");
header.id = "headerDiv";
document.body.appendChild(header);

var h1_1 = document.createElement("h1");
h1_1.innerHTML = "Dan's Frapps";
header.appendChild(h1_1);

var useraccountimage = new Image(35, 35);;
useraccountimage.src = "/static/menu/userAccountIcon.png"
useraccountimage.id = "uaimg";
useraccountimage.style.position="absolute";
useraccountimage.style.left = "90%";
useraccountimage.onclick = function() {
    window.location.href = '/account/view';
};
header.appendChild(useraccountimage);

var menuicon = new Image(35, 35);;
menuicon.src = "/static/menu/menuIcon.png"
menuicon.id = "menuimg";
menuicon.style.position = "absolute";
menuicon.style.left="2%";
menuicon.onclick = function() {
    alert("TODO: Implement Menu");
};
header.appendChild(menuicon);

var homeicon = new Image(35, 35);;
homeicon.src = "/static/menu/homeIcon.png"
homeicon.id = "menuimg";
homeicon.style.position = "absolute";
homeicon.style.left = "95%";
homeicon.onclick = function() {
    window.location.href = '/menu';
};
header.appendChild(homeicon);

bufferDiv = document.createElement("div");
bufferDiv.id = "bufferdiv";
document.body.appendChild(bufferDiv);

