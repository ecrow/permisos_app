$(document).ready(function() {

    function startChange() {
        var startDate = start.value(),
        endDate = end.value();

        if (startDate) {
            startDate = new Date(startDate);
            startDate.setDate(startDate.getDate());
            end.min(startDate);
        } else if (endDate) {
            start.max(new Date(endDate));
        } else {
            endDate = new Date();
            start.max(endDate);
            end.min(endDate);
        }
    }

    function endChange() {
        var endDate = end.value(),
        startDate = start.value();

        if (endDate) {
            endDate = new Date(endDate);
            endDate.setDate(endDate.getDate());
            start.max(endDate);
        } else if (startDate) {
            end.min(new Date(startDate));
        } else {
            endDate = new Date();
            start.max(endDate);
            end.min(endDate);
        }
    }

    var start = $("#fecha_ini").kendoDatePicker({
        change: startChange,
        format: "dd/MM/yyyy"
    }).data("kendoDatePicker");

    var end = $("#fecha_fin").kendoDatePicker({
        change: endChange,
        format: "dd/MM/yyyy"
    }).data("kendoDatePicker");

    start.max(end.value());
    end.min(start.value());

    /*Binds selects*/
    var tipo_vehiculo=$("#tipo_vehiculo").kendoDropDownList({
        optionLabel: "Todos los tipos",
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
        optionLabel: "Todas las marcas",
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
        optionLabel: "Todas las lineas",
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
});