console.log(roleList);

$(".panel").fadeOut(0.01);

function showSetupInfo() {
	console.log("poop");
}

$("a").click(function() { 
    $(".panel-heading").empty();
    $(".panel-body").empty();
    $(".panel").fadeIn(200);

    for (var i = 0; i < roleList.length; i++) {
        if (roleList[i].fields.name == $(this).attr('id'))
        {
            $(".panel-heading").append(roleList[i].fields.name);
            $(".panel-body").append("<p>" + roleList[i].fields.description + "</p>");   
            $("panel-body").append("POOP");
            if(roleList[i].fields.action != "n/a") {
            	$(".panel-body").append("<p>" + roleList[i].fields.action + "</p>");
            } 
            $("panel-body").append("<a href=roles/" + roleList[i].pk + "><p>Click here to see more details!</p></a>");
            $("panel-body").append("POOP");
        }
    }
});