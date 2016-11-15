function formToJSON() {
  var objectGraph = {};
  function add(objectGraph, name, value) {
    if(name.length == 1) {
      //if the array is now one element long, we're done
      objectGraph[name[0]] = value;
    }
    else {
      //else we've still got more than a single element of depth
      if(objectGraph[name[0]] == null) {
        //create the node if it doesn't yet exist
        objectGraph[name[0]] = {};
      }
    //recurse, chopping off the first array element
      add(objectGraph[name[0]], name.slice(1), value);
    }
  };
  //loop through all of the input/textarea elements of the form
  //this.find('input, textarea').each(function()
  var elements = document.getElementsByTagName("input");
  for (var i = 0; i < elements.length; i++) {
    add(objectGraph, elements[i].name.split('.'), elements[i].value);
  }
  $(this).children('input, textarea').each(function() {
    console.log("hi")
    //ignore the submit button
    if($(this).attr('name') != 'submit') {
      //split the dot notated names into arrays and pass along with the value
      add(objectGraph, $(this).attr('name').split('.'), $(this).val());
    }
  });
  $(this).children('select').each(function() {
    //ignore the submit button
    if($(this).attr('name') != 'submit') {
      //split the dot notated names into arrays and pass along with the value
      add(objectGraph, $(this).attr('name').split('.'), $(this).val());
    }
  });
  return JSON.stringify(objectGraph);
}

function submitForm(){
  console.log("BUTTON CLICKED");
    var send = formToJSON();
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
