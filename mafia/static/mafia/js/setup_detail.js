console.log(roleList);
console.log(setup);
console.log(alignments);

// Setup
$(".panel").fadeOut(0.01);
var intialPlayerNumber = $(".players").val();
for (var i = 0; i < intialPlayerNumber; i++) {
	if(alignments[i] == "Mafia") {
		$(".role_list").append("<li><a href=# class="+ alignments[i] +" id='"+ setup[i] +"'>"+ setup[i] +"</a>"
            );	
	}
}
for (var i = 0; i < intialPlayerNumber; i++) {
	if(alignments[i] == "Town") {
		$(".role_list").append("<li><a href=# class="+ alignments[i] +" id='"+ setup[i] +"'>"+ setup[i] +"</a>"
          );
	}
}

// Code for showing role info
function bindClick() {
    $("a").click(function() {
        $(".panel-heading").empty();
        $(".panel-body").empty();
        $(".panel").fadeIn(200);
        console.log($(this).attr('id'));

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
}


// Recreating the role list based on slider
$(".players").change(function() {
	var playerNumber = $(this).val();
    $(".number_players").text("Number of players: " + playerNumber );


    // Emptying and refilling
    $(".role_list").empty();

    for (var i = 0; i < playerNumber; i++) {
        if(alignments[i] == "Mafia") {
            $(".role_list").append("<li><a href=# class="+ alignments[i] +" id='"+ setup[i] +"''>"+ setup[i] +"</a>"
                );  
        }
    }
    for (var i = 0; i < playerNumber; i++) {
        if(alignments[i] == "Town") {
            $(".role_list").append("<li><a href=# class="+ alignments[i] +" id='"+ setup[i] +"''>"+ setup[i] +"</a>"
                );
        }
    }

    $("a").click(function() {

        $(".panel-heading").empty();
        $(".panel-body").empty();
        $(".panel").fadeIn(200);
        console.log($(this).attr('id'));

        for (var i = 0; i < roleList.length; i++) {
            if (roleList[i].fields.name == $(this).attr('id'))
            {
                $(".panel-heading").append(roleList[i].fields.name);
                $(".panel-body").append("<p>" + roleList[i].fields.description + "</p>");   
                $("panel-body").append("POOP");
                if(roleList[i].fields.action != "n/a") {
                    $(".panel-body").append("<p>" + roleList[i].fields.action + "</p>");
                } 
                console.log("nothing happens");
                $("panel-body").append("<a href=roles/" + roleList[i].pk + "><p>Click here to see more details!</p></a>");
                $("panel-body").append("POOP");
            }
        }
    });
});
