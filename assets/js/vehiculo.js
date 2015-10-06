$(document).ready(function() {

    var validator = $("#datos_vehiculo").kendoValidator().data("kendoValidator");
	
    //binds tipo_vehiculo 
    var tipo_vehiculo=$("#tipo_vehiculo").kendoDropDownList({
    	optionLabel: "Selecciona un valor...",
        dataTextField: "descripcion",
        dataValueField: "idtipo_vehiculo_id",
        dataSource: {
            transport: {
                read: {
                    dataType: "json",
                    url: "/catalogo/tipo_vehiculo/",
                }
            }
        }
    });

    //binds marca_vehiculo con tipo_vehiculo
    var marca_vehiculo=$("#marca_vehiculo").kendoDropDownList({
        autoBind:false,
        cascadeFrom:'tipo_vehiculo',
    	optionLabel: "Selecciona un valor ...",
        dataTextField: "descripcion",
        dataValueField: "idmarca_vehiculo_id",
        dataSource: {
            transport: {
                read: {
                    dataType: "json",
                    url: "/catalogo/marca_vehiculo/",
                }
            }
        }
    });

    //binds linea_vehiculo con marca_vehiculo
    var linea_vehiculo=$("#linea_vehiculo").kendoDropDownList({
        autoBind:false,
        cascadeFrom:'marca_vehiculo',
        optionLabel: "Selecciona un valor ...",
        dataTextField: "descripcion",
        dataValueField: "idlinea_vehiculo_id",
        dataSource: {
            transport: {
                read: {
                    dataType: "json",
                    url: "/catalogo/linea_vehiculo/",
                }
            }
        }
    });

    
    //save data
    $('#datos_vehiculo').submit(function(e){
        
        if (validator.validate()) {
            console.log('oks');
            return;
        } else {
            console.log("error");
        }
    });

    //binds sexo del propietario
    $("#modelo_vehiculo").kendoDropDownList({
        optionLabel: "Selecciona un valor...",
        dataTextField: "descripcion",
        dataValueField: "idmodelo_vehiculo_id",
        dataSource: {
            transport: {
                read: {
                    dataType: "json",
                    url: "/catalogo/modelo_vehiculo/",
                }
            }
        }
    });

});