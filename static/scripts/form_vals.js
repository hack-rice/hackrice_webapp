function getUniversity(formVals) {
  String univ = formVals["university"];
  if (univ.equals("Rice University (TX)") || univ.equals("University of Houston (TX)"){
  	return "auto-acpt"
  }
  else:
  	return univ
  }

function getGithub(formVals){
  return formVals["github"]
}

function getLinkedin(formVals){
  return formVals["linkedin"]
}

function getWebsite(formVals){
  return formVals["website"]
}
function getEmail(formVals){
	return formVals["email"]
}


