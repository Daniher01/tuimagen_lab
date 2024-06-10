$(document).ready(function() {
    $('.btn-terminar-trabajo').on('click', function() {
        var trabajoId = $(this).data('id');

        Swal.fire({
            title: '¿Está seguro que desea terminar el trabajo?',
            text: "¡Esta acción no se puede deshacer!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, terminar',
            cancelButtonText: 'No, cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                // Realizar la solicitud AJAX para terminar el trabajo
                $.ajax({
                    url: `${window.location.origin}/terminar_trabajo/`,
                    method: 'POST',
                    data: {
                        id: trabajoId,
                        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val() // Asegúrate de enviar el token CSRF
                    },
                    success: function(response) {
                        if (response.success) {
                            // Mostrar alerta de éxito
                            Swal.fire({
                                title: 'Trabajo terminado',
                                text: 'El trabajo ha sido marcado como terminado.',
                                icon: 'success',
                                confirmButtonText: 'OK',
                                html: "Esta ventana se cerrará en <b></b> millisegundos.",
                                timer: 2000,
                                timerProgressBar: true,
                                didOpen: () => {
                                  Swal.showLoading();
                                  const timer = Swal.getPopup().querySelector("b");
                                  timerInterval = setInterval(() => {
                                    timer.textContent = `${Swal.getTimerLeft()}`;
                                  }, 100);
                                },
                                allowOutsideClick: false, // No permitir clics fuera del modal
                                willClose: () => {
                                    location.reload(); // Recargar la página al cerrar el modal
                                },
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
            }
        });
    });
});

