console.log(setupList);
console.log(setupList.length);
console.log(setupList[0].fields.name);      

$("button").click(function() { 
    $(".setup_info").empty();

    for (var i = 0; i < setupList.length; i++) {
        if (setupList[i].fields.name == $(this).attr('id'))
        {
            $(".setup_info").append("<p>Name: " + setupList[i].fields.name + "</p>" +
                                    "<p>Description: " + setupList[i].fields.description + "</p>");    
        }
    }
});