function openNav() {
    console.log("Attempt open sidenav");
    document.getElementById("sideNav").style.width = "250px";
  }
  
/* Set the width of the side navigation to 0 */
function closeNav() {
document.getElementById("sideNav").style.width = "0";
}


const header = document.createElement("div");
header.id = "headerDiv";
document.body.appendChild(header);

var h1_1 = document.createElement("h1");
h1_1.innerHTML = "Inventory";
header.appendChild(h1_1);

var useraccountimage = new Image(35, 35);;
useraccountimage.src = "/static/menu/userAccountIcon.png"
useraccountimage.id = "uaimg";
useraccountimage.style.position = "absolute";
useraccountimage.style.left = "95%";
useraccountimage.style.bottom = "5%";
useraccountimage.onclick = function() {
    window.location.href = '/account/view';
};
header.appendChild(useraccountimage);

var menuicon = new Image(35, 35);;
menuicon.src = "/static/menu/menuIcon.png"
menuicon.id = "menuimg";
menuicon.style.position = "absolute";
menuicon.style.left = "2%";
menuicon.style.bottom = "5%";
menuicon.onclick = openNav;
header.appendChild(menuicon);

var homeicon = new Image(35, 35);;
homeicon.src = "/static/menu/homeIcon.png"
homeicon.id = "menuimg";
homeicon.style.position = "absolute";
homeicon.style.left = "90%";
homeicon.style.bottom = "5%";
homeicon.onclick = function() {
    window.location.href = '/menu';
};
header.appendChild(homeicon);

bufferDiv = document.createElement("div");
bufferDiv.id = "bufferdiv";
document.body.appendChild(bufferDiv);


var sideNav = document.createElement('div');
sideNav.id = "sideNav";
sideNav.className = "sidenav";
document.body.appendChild(sideNav);

var closeNavbttn = document.createElement("a");
closeNavbttn.href="javascript:void(0)";
closeNavbttn.className ="closebtn"
closeNavbttn.onclick = closeNav;
closeNavbttn.innerHTML = "&times;";
sideNav.appendChild(closeNavbttn);

var queueLink = document.createElement("a");
queueLink.href= "/employee/queue/";
queueLink.innerHTML = "Queue";
sideNav.appendChild(queueLink);

var inventoryLink = document.createElement("a");
inventoryLink.href= "/employee/inventory/";
inventoryLink.innerHTML = "Inventory";
sideNav.appendChild(inventoryLink);

var employeeLink = document.createElement("a");
employeeLink.href= "/employee/";
employeeLink.innerHTML = "Employees"
sideNav.appendChild(employeeLink);
