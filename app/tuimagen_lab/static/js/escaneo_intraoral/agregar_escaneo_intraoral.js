
const form = document.getElementById('trabajoForm_escaneo_intraoral');
const submitBtn = document.getElementById('submit_escaneo_intraoral');

submitBtn.addEventListener('click', function (e) {
    e.preventDefault();

    if (!validarFormulario(form)) {
        return;
    }

    const formData = new FormData(form);

    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.success) {
            Swal.fire({
                title: 'Trabajo generado',
                text: 'El trabajo ha sido generado exitosamente.',
                icon: 'success',
                confirmButtonText: 'OK'
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = `${window.location.origin}/trabajos`;
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
});
