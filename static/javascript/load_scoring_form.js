function loadScoringForm(serverJSON){
  document.getElementById("email").innerHTML = serverJSON["email"];
  document.getElementById("university").innerHTML = serverJSON["university"];
}

window.onload = function(){
  loadScoringForm({"email":"email","password":"pass","confirmed_password":"word","first_name":"first","last_name":"last","date_of_birth":"0001-01-01","github":"gh","personal_website":"my","linkedin":"li","university":"Rice University (TX)"});
};
