var highlightindex = -1;

var timeoutId;

var timeMS = 500;
$(document).ready
(
	function() 
	{
	    var wordInput = $("#word");
	    var wordInputOffset = wordInput.offset();
	    
	    //Define background color and position
		$("#auto").css("background-color","white");

		$("#word").width("300px");
	    
	    $("#auto").hide().css("border","1px black solid").css("position","absolute")
	            .css("top",wordInputOffset.top + wordInput.height() + 20 + "px")
	            .css("left",wordInputOffset.left + "px").width(wordInput.width());

	    wordInput.keyup
	    (
	    function(event) 
	    {
	        
	        
            //get input
            var wordText = $("#word").val();
            var autoNode = $("#auto");
            if (wordText != "") 
            {
            	//empty last request
            	clearTimeout(timeoutId);
            	//Delay by 0.5 second
            	timeoutId = setTimeout(function()
            	{
            		//send the input to backend
	               	$.ajax(
	               		{
               				type: "GET",
						    url: "/autocomplete",
						    data: {"word":wordText},
						    dataType:"json",
			                success:function(result)
			                {		                	
			                			                    
			                    autoNode.html("");
			                    
			                    if(result!=null)
								{
									$("#auto").show("slow");
									for (i in result){
										var newDivNode=$("<div>").attr("id",i);
										var record = result[i];
										var type;
										switch(record.type)
										{case "nc": type="Drug NamesCode";
										break;
										case "nb": type="Drug NamesBrand";
										break;
										case "ng": type="Drug NamesGeneric";
										break;
										case "nm": type="Drug NameMain";
										break;
										case "mc": type="Mechanism";
										break;
										}

										newDivNode.html(record.name+' ('+type+')').appendTo(autoNode);

										newDivNode.prepend('<div id="new_div"></div>');
										$("#new_div").html(record.id)
										$("#new_div").hide()




										newDivNode.mouseover
					                        (
					                        function(){
					                        	//remove the highlight
					                        	if(highlightindex != -1){
					                        		$("#auto").children("div").eq(highlightindex)
					                        		.css("background-color","white");
					                        	}
					                        	//record the highlight index
					                        	highlightindex = $(this).attr("id");
					                        	//highlight the mouseover
					                        	$(this).css("background-color","#6699CC");
					                        });
					                        //remove the highlight
					                        newDivNode.mouseout(
						                        function(){
						                        	$(this).css("background-color","white");
						                        }
					                        );
				                        				                        
				                        //mouse click event
				                        newDivNode.click(
				                        function (){
							                var text = $(this).text();
							                
							                document.getElementById('auto').style.display='none';
							                
							                highlightindex= -1;
							                $("#word").val(text);//put the clicked text inside the input

											                        }
											                        );
										
									}
								}
							                  
			                                    

				                }
		               		}
		               	);
	            	},timeMS);
	            }
	            else{
	            	autoNode.hide("slow");
	            } 	         	        
	    });
	}
)