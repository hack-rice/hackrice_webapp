
function nextPageFocus(cur_page) {
	var pages = ["university", "experience", "resume", "linkedin", "other"];
    window.alert(pages);
    window.alert(cur_page);
	for (var page in pages){
    window.alert(page);
		if page.equals(cur_page){
		document.getElementById(page).style.display="block";
	}
	else{
   	    document.getElementById(page).style.display="none";
   	}
  	}


}


function page2Focus() {
   document.getElementById("university").style.display="none";
   document.getElementById("experience").style.display="block"
   document.getElementById("resume").style.display="none"
   document.getElementById("linkedin").style.display="none"
   document.getElementById("other").style.display="none";
}