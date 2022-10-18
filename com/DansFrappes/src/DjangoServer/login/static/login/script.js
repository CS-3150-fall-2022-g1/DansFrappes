document.title = "Dan's Frapp's - Login";

const loginDiv = document.createElement("div");
loginDiv.id = "loginDiv";
document.body.appendChild(loginDiv);

const loginIntro = document.createElement('H1');
loginIntro.innerHTML = "Login";
loginIntro.id = 'loginIntro';
loginDiv.appendChild(loginIntro);

const username = document.createElement('input');
username.setAttribute("placeholder", "Username");
username.id = 'username';
loginDiv.appendChild(username);

const password = document.createElement('input');
password.setAttribute('placeholder', 'Password')
password.setAttribute('type','password')
password.id = 'password';
loginDiv.appendChild(password);

const button = document.createElement('input');
button.setAttribute('type','button')
button.setAttribute('value', "Login");
button.id = 'button';
loginDiv.appendChild(button);


const createAccountText = document.createElement("p");
createAccountText.innerHTML = "New here? Let's get <a href=\"/login/createaccount\"> started!</a>";
loginDiv.appendChild(createAccountText);