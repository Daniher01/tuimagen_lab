$(document).ready(function() {
    // Manejar la apertura del modal y llenar los datos
    $('#verTrabajoModal').on('show.bs.modal', function(event) {
        var button = $(event.relatedTarget); // Botón que disparó el modal
        var trabajoId = button.data('id'); // Extraer información del atributo data-id
        // Realizar una solicitud AJAX para obtener los detalles del trabajo
        $.ajax({
            url: `${window.location.origin}/detalle_trabajo`, // URL para obtener los detalles del trabajo
            data: {id: trabajoId},
            success: function(data) {
                // Llenar los datos en el modals
                $('#verTrabajoModalLabel').text(`Detalle del trabajo N°${trabajoId}`)
                $('#detallePaciente').text(data.paciente_nombre);
                $('#detalleRut').text(data.paciente_rut);
                $('#detalleDentista').text(data.dentista_nombre);
                $('#detalleFechaIngreso').text(data.fecha_ingreso);
                $('#detalleFechaEntrega').text(data.fecha_entrega);
                $('#detalleEstado').text(data.estado);
                var piezasList = $('#detallePiezas');
                piezasList.empty();
                data.piezas.forEach(function(pieza) {
                    piezasList.append('<li>Pieza: ' + pieza.pieza_nombre + ', Material: ' + pieza.material_nombre + '</li>');
                });
            }
        });
    });
});