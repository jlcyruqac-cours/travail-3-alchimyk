$(document).ready(function()
{
	$( "#inputDOB" ).datepicker();

	/*$("#getHoroscope").click(function()
	{
	    $.post("./horoscope", /*$("inputName"), $("inputFstName"), $("inputDOB"), 
	    	{
	    		name: $("#inputName"),
		    	firstname: $("#inputFstName"),
		    	dbirth: $("#inputDOB")
		    },
	    function(data,status)
	    {
	      alert("Data: " + data + "\nStatus: " + status);
	    });
	});*/
});

$("button").click(function(event)
{
	event.preventDefault();

    // Serialize the data in the form
    var serializedData = $("#bullshitRequestForm").serialize();

    $.post("./horoscope", serializedData,
	    function(data,status)
	    {
	      alert("data:" + data + "\nStatus: " + status);
	      var obj = JSON.parse(data);
	      window.alert(obj);
	      $("#theName").html(obj.name)
	      $("#theFirstName").html(obj.fstName)
	      $("#theDOB").html(obj.bthDate)

	    /*$("#titre").html = data.titre;*/
	    });
	    /*function(responseText)
	    {
	    	window.alert(responseText)
	    	var parsed_data = JSON.parse(responseText);
	    	$('#result').html(JSON.stringify(parsed_data));
	    });*/
});
