function scoringFormToJSON() {
  var totalCount = 0;
  var hackathons_score = parseInt($('input[name="hackathons"]:checked').val());
  var projects_score = sumCategoryScore("projects");
  var resume_linkedin_score = sumCategoryScore("resume_linkedin");
  var favorite_project_score = sumCategoryScore("favorite_project");
  return hackathons_score + projects_score + resume_linkedin_score + favorite_project_score;
}

function sumCategoryScore(category){
  var elements = document.getElementsByName(category);
  console.log(category);
  var score = 0;
  for (var i = 0; i < elements.length; i++) {
    if(elements[i].checked){
      score += 1;
    }
  }
  return score;
}

function submitForm(){
  console.log("BUTTON CLICKED");
    var send = scoringFormToJSON();
    console.log(send);
    window.alert(send);
    /**$.ajax({
      url: "http://blah.feh.com/something",
      type: "POST",
      data: send,
      error: function(xhr, error) {
        alert('Error!  Status = ' + xhr.status + ' Message = ' + error);
      },
      success: function(data) {
        //have you service return the created object
        var items = [];
        items.push('<table cellpadding="4" cellspacing="4">');
        items.push('<tr><td>ID</td><td>' + data.id + '</td></tr>');
        items.push('<tr><td>Meh Feh</td><td>' + data.meh.feh + '</td></tr>');
        items.push('<tr><td>Meh Peh</td><td>' + data.meh.peh + '</td></tr>');
        //etc
        items.push('</table>');
        $('#result').html(items.join(''));
      }
    });**/
    return false;
  }
