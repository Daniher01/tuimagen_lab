const formEscaneoIntraoral = document.getElementById('trabajoForm_escaneo_intraoral');
const submitBtnEscaneoIntraoral = document.getElementById('submit_escaneo_intraoral');

submitBtnEscaneoIntraoral.addEventListener('click', function (e) {
    e.preventDefault();

    if (!validarFormulario(formEscaneoIntraoral)) {
        return;
    }

    // Mostrar la alerta de confirmación
    Swal.fire({
        title: '¿Desea crear el trabajo?',
        text: 'Está por crear un trabajo de escaneo intraoral',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Sí, crear',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            const formData = new FormData(formEscaneoIntraoral);

            enviarFormularioEscaneoIntraoral(formEscaneoIntraoral, formData);
        }
    });
});

function enviarFormularioEscaneoIntraoral(form, formData) {
    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            Swal.fire({
                title: 'Trabajo generado',
                text: 'El trabajo ha sido generado exitosamente.',
                icon: 'success',
                confirmButtonText: 'OK',
                allowOutsideClick: false,  // Evita que el modal se cierre al hacer clic fuera
                allowEscapeKey: false      // Evita que el modal se cierre con la tecla escape
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = `${window.location.origin}/pendientes`;
                }
            });
        } else {
            Swal.fire({
                title: 'Error',
                text: 'Hubo un problema al generar el trabajo. Por favor, inténtalo de nuevo.',
                icon: 'error',
                confirmButtonText: 'OK'
            });
        }
    })
    .catch(error => {
        console.log(error);
        Swal.fire({
            title: 'Error',
            text: 'Hubo un problema al generar el trabajo. Por favor, inténtalo de nuevo.',
            icon: 'error',
            confirmButtonText: 'OK'
        });
    });
}
