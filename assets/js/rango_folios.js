$(document).ready(function() {

    $("#rango_foliosu").kendoValidator().data("kendoValidator");
    

    $("#folioini_rango").kendoNumericTextBox({
        format: "n0",
        min:1,
        placeholder: "Introduzca un número",
        spinners: false
    });

    $("#foliofin_rango").kendoNumericTextBox({
        format: "n0",
        min:1,
        placeholder: "Introduzca un número",
        spinners: false
    });

	
    //binds tipo_vehiculo 
    $("#usuario_rango").kendoDropDownList({
    	optionLabel: "Selecciona un valor...",
        dataTextField: "descripcion",
        dataValueField: "idusuario_id",
        dataSource: {
            transport: {
                read: {
                    dataType: "json",
                    url: "/catalogo/usuarios/",
                }
            }
        },
        change:function(e){
            var value = this.value();
            if (value!=''){
                var url_folios="usuario/"+value;
                var sharedDataSource = new kendo.data.DataSource({
                    transport: {
                        read: {
                            url: url_folios,
                            dataType: "json"
                        }
                    }
                });
                var grid=$("#grid_folios_usuario").kendoGrid({
                    dataSource: sharedDataSource,
                        columns: [
                        {
                            field: "folio_ini",
                            title: "Folio inicial"
                        },
                        {
                            field: "folio_fin",
                            title: "Folio final",
                            
                    }]
                });
            } //end if 
        }

    });

    
    //save data
    $('#rango_foliosu').submit(function(e){
        
        if (validator.validate()) {
            console.log('oks');
            return;
        } else {
            console.log("error");
        }
    });

    

});