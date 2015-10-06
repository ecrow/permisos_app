$(document).ready(function() {

    $("#folio_permiso").kendoDropDownList({
        filter:"contains",
        optionLabel: "Selecciona un valor...",
        dataTextField: "folio",
        dataValueField: "idfolio_id",
        template: '<h3 class="templateDropdown"><i class="fa fa-car"></i> #: folio #</h3>',
        dataSource: {
            transport: {
                dataType: "json",
                serverFiltering: true,
                read: {
                    url: "/catalogo/folios/",
                }
            }
        }
    });
});