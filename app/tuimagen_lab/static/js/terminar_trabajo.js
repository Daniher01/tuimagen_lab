$(document).ready(function() {
    $('.btn-terminar-trabajo').on('click', function() {
        var trabajoId = $(this).data('id');
        
        $.ajax({
            url: `${window.location.origin}/terminar_trabajo/`,
            method: 'POST',
            data: {
                id: trabajoId,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val() // Asegúrate de enviar el token CSRF
            },
            success: function(response) {
                if (response.success) {
                    // Actualizar el estado en la tabla
                    var row = $('button[data-id="' + trabajoId + '"]').closest('tr');
                    row.find('.badge').removeClass('bg-warning text-dark').addClass('bg-success').text('Terminado');
                    // Mostrar alerta de éxito
                    Swal.fire({
                        title: 'Trabajo terminado',
                        text: 'El trabajo ha sido marcado como terminado.',
                        icon: 'success',
                        confirmButtonText: 'OK'
                    });
                } else {
                    Swal.fire({
                        title: 'Error',
                        text: 'Hubo un error al intentar terminar el trabajo.',
                        icon: 'error',
                        confirmButtonText: 'OK'
                    });
                }
            },
            error: function() {
                Swal.fire({
                    title: 'Error',
                    text: 'Hubo un error al intentar terminar el trabajo.',
                    icon: 'error',
                    confirmButtonText: 'OK'
                });
            }
        });
    });
});
