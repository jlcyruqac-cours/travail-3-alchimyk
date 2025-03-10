$(document).ready(function()
{
	$( "#inputDOB" ).datepicker();

	$("button").click(function(event)
	{
		event.preventDefault();

	    // Serialize the data in the form
	    var serializedData = $("#bullshitRequestForm").serialize();

	    $.post("./horoscope", serializedData,
		    function(data,status)
		    {
		      console.log("Data:" + data + "\nStatus: " + status);
		      var obj = JSON.parse(data);
		      if ((obj.ErrorCodes).length > 0)
		      {
		      	window.alert((obj.ErrorCodes).join(""));
		      	return;
		      }
		      $("#myform").toggle();
		      $("#response").toggle();
		      $("#theSign").html(obj.sign);
		      $("#theName").html(obj.name);
		      $("#theFirstName").html(obj.fstName);
		      $("#theDOB").html(obj.bthDate);
		      $("#thePred").html(obj.horoscope);
		    });
	});
});