$(document).ready(function() {

    var validator = $("#datos_propietario").kendoValidator().data("kendoValidator");
	
    //binds sexo del propietario
    $("#sexo_propietario").kendoDropDownList({
    	optionLabel: "Selecciona un valor...",
        dataTextField: "descripcion",
        dataValueField: "idsexo_id",
        dataSource: {
            transport: {
                read: {
                    dataType: "json",
                    url: "/catalogo/sexo/",
                }
            }
        }
    });

    //binds estado
    var estado=$("#estado_propietario").kendoDropDownList({
    	optionLabel: "Selecciona un valor ...",
        dataTextField: "descripcion",
        dataValueField: "idestado_id",
        dataSource: {
            transport: {
                read: {
                    dataType: "json",
                    url: "/catalogo/estado/",
                }
            }
        }
    });

    //binds municipio con estado
    var municipio=$("#municipio_propietario").kendoDropDownList({
        autoBind:false,
        cascadeFrom:'estado_propietario',
        optionLabel: "Selecciona un valor ...",
        dataTextField: "descripcion",
        dataValueField: "idmunicipio_id",
        dataSource: {
            transport: {
                read: {
                    dataType: "json",
                    url: "/catalogo/municipio/",
                }
            }
        }
    });

    //masked telefono
    $("#telefono_propietario").kendoMaskedTextBox({
        mask: "(999) 000-0000",
        unmaskOnPost: true
    });



    //save data
    $('#datos_propietario').submit(function(e){
        
        if (validator.validate()) {
            console.log('oks');
            return;
        } else {
            console.log("error");
        }
    })


    function guarda(url,dataString){
        $.ajax(
            url,
            {
                type : "POST",
                data : dataString,
                dataType: "json",
            }
        ).done(function(data){
            if(parseInt(data.status)==1)
            {
              console.log(data.msg);
                
            }
            else if(parseInt(data.status)==0)
            {
              console.log(data.msg);
            }
            console.log("ok")
        }).fail(function(jqXHR, textStatus, tipoError){
            console.log(jq);
        }); //end ajax
    }


});