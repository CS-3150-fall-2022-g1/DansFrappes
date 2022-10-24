document.title = "Dan's Frapp's - Login";

const createAccountDiv = document.createElement("div");
createAccountDiv.id = "createAccountDiv";
createAccountDiv.className= "textEntryDiv";
document.body.appendChild(createAccountDiv);

const createIntro = document.createElement('H1');
createIntro.innerHTML = "Create Account";
createIntro.id = 'loginIntro';
createAccountDiv.appendChild(createIntro);

var form_create = document.getElementById("createform");
createAccountDiv.appendChild(form_create);

const firstname = document.getElementById('firstname');
firstname.setAttribute("placeholder", "First Name");
firstname.className = "textEntry"
form_create.appendChild(firstname);

const fntxt = document.getElementById("fnerr");
form_create.appendChild(fntxt);

const lastname = document.getElementById('lastname');
lastname.setAttribute("placeholder", "Last Name");
lastname.className = "textEntry"
form_create.appendChild(lastname);

const lntxt = document.getElementById("lnerr");
form_create.appendChild(lntxt);

const username = document.getElementById('username');
username.setAttribute("placeholder", "Username");
username.className = "textEntry"
form_create.appendChild(username);

const untxt = document.getElementById("unerr");
form_create.appendChild(untxt);

const email = document.getElementById('email');
email.setAttribute("placeholder", "Email");
email.className = "textEntry"
email.setAttribute("type","email")
form_create.appendChild(email);

const emtxt = document.getElementById("emerr");
form_create.appendChild(emtxt);

const password = document.getElementById('password');
password.setAttribute('placeholder', 'Password');
password.setAttribute('type','password');
password.className = "textEntry"
form_create.appendChild(password);

const pwdtxt = document.getElementById("pwderr");
form_create.appendChild(pwdtxt);

const cpassword = document.getElementById('confirmpassword');
cpassword.setAttribute('placeholder', 'Confirm Password');
cpassword.setAttribute('type','password');
cpassword.className = "textEntry"
form_create.appendChild(cpassword);

const cpwdtxt = document.getElementById("cpwderr");
form_create.appendChild(cpwdtxt);

const button = document.getElementById('createaccountbutton');
button.setAttribute('type','submit')
button.setAttribute('value', "Create Account");
button.id = 'loginbutton';
button.className = "submitbutton";
form_create.appendChild(button);



