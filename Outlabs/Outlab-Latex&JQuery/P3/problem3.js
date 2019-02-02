$(document).ready(function(){
	$("nav[role='navigation']").children("ul").find("ul:first").css("background-color","red");
	$("nav[role='navigation']").children("ul").find("ul:first").css("color","blue");
	$("#text").find("ol").find("li").append(" in the list");
	$("body").css("background-color","#eee");
	$("a").click(function(){
    	alert("You clicked some link");
	});
});