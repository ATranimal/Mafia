// button clicking function

console.log(setupList);

$(".panel").fadeOut(1);

$("button").click(function() { 
    $(".panel-heading").empty();
    $(".panel-body").empty();
    $(".panel").fadeIn(1000);

    for (var i = 0; i < setupList.length; i++) {
        if (setupList[i].fields.name == $(this).attr('id'))
        {
            $(".panel-heading").append(setupList[i].fields.name);
            $(".panel-body").append("<p>" + setupList[i].fields.description + "</p>" + 
                                    "<a href=setups/" + setupList[i].pk + "><p>Click here to see more details!</p></a>");    
        }
    }
});