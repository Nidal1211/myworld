const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

// password validation function 
function matchPassword() {  
  var pw2='';
  var pw1 = document.getElementById("pswd1").value;
   pw2 = document.getElementById("pswd2").value;
  if ( (pw1 !== pw2 )|| (pw2 === ''))
  {   
    alert("Passwörter stimmen nicht überein");  
  } else {  
    alert("Passwort erfolgreich erstellt");  
  }
}

