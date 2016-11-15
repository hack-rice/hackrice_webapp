function page1Focus() {
   document.getElementById("form_page_1").style.display="block";
   document.getElementById("form_page_2").style.display="none";
   document.getElementById("form_page_3").style.display="none";
}
function page2Focus() {
   document.getElementById("form_page_1").style.display="none";
   document.getElementById("form_page_2").style.display="block";
   document.getElementById("form_page_3").style.display="none";
}
function page3Focus() {
   document.getElementById("form_page_1").style.display="none";
   document.getElementById("form_page_2").style.display="none";
   document.getElementById("form_page_3").style.display="block";
}
