$(document).ready(function() {

    var validator = $("#nuevo_usuario").kendoValidator().data("kendoValidator");
	
    
    //save data
    $('#nuevo_usuario').submit(function(e){
        if (validator.validate()) {
            console.log('oks');
            return;
        } else {
            console.log("error");
        }
    })

});