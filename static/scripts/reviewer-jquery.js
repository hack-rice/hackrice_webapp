/**
 * Created by AveryJordan on 1/30/17.
 */

/*
 Used to update the information on the page as a user is selected.
 */
$(function () {
    $('#users').on('click', 'tr', function () {
        //console.log(this);
        //$(this).attr("style", "")
        $('#selected_name').text($(this).find('#name').text());
        $('#redisQuota').attr("placeholder", $(this).find('#overdue').text());
        $('#reminder_email').attr("href", $(this).find("#email").text());
    });
});

/*
 Makes a post request to the application to access the mail chimp API and
 send the user who is currently selected a reminder email.
 */
var sendEmail = function () {
    //TODO make this have an app route to use the mail chimp API
    $('#reminder_email').attr("href");
};