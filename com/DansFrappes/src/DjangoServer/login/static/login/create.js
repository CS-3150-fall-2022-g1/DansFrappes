document.title = "Dan's Frapp's - Login";

const loginDiv = document.createElement("div");
loginDiv.id = "loginDiv";
document.body.appendChild(loginDiv);

const loginIntro = document.createElement('H1');
loginIntro.innerHTML = "Login";
loginIntro.id = 'loginIntro';
loginDiv.appendChild(loginIntro);

var form = document.createElement("form");
form.id = "loginform";
form.method="post";
loginDiv.appendChild(form);

const username = document.getElementById('username');
username.setAttribute("placeholder", "Username");
username.className = "textEntry"
form.appendChild(username);

const password = document.getElementById('password');
password.setAttribute('placeholder', 'Password');
password.setAttribute('type','password');
password.className = "textEntry"
form.appendChild(password);

const button = document.getElementById('loginbutton');
button.setAttribute('type','submit')
button.setAttribute('value', "Login");
button.id = 'loginbutton';
form.appendChild(button);

const warningText = document.getElementById("invalidLoginText");
warningText.innerHTML = "Incorrect Username and/or Password."
loginDiv.appendChild(warningText);

const createAccountText = document.createElement("p");
createAccountText.innerHTML = "New here? Let's get <a href=\"/login/createaccount\"> started!</a>";
loginDiv.appendChild(createAccountText);

