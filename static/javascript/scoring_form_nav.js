
function nextPageFocus(cur_page) {
	var pages = ["university", "experience", "resume", "linkedin", "other"];
    window.alert(cur_page);
    window.alert(pages);
	for (idx = 0; idx < pages.length; idx++){
    window.alert(pages[idx]);
		if (pages[idx] == (cur_page)){
		document.getElementById(pages[idx]).style.display="block";
	}
	else{
   	    document.getElementById(pages[idx]).style.display="none";
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