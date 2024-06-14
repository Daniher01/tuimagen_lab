document.getElementById('submit_impresion3d').addEventListener('click', function (e) {
    e.preventDefault();

    console.log(e);

    const form = document.getElementById('trabajoForm_impresion3d');
    if(!validarFormulario(form)){
        console.log('entra aqui');
        return;
    }
    const formData = new FormData(form);

    console.log(form);

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
            console.log(data)
            Swal.fire({
                title: 'Error',
                text: 'Hubo un problema al generar el trabajo. Por favor, inténtalo de nuevo.',
                icon: 'error',
                confirmButtonText: 'OK'
            });
        }
    })
    .catch(error => {
        Swal.fire({
            title: 'Error',
            text: 'Hubo un problema al generar el trabajo. Por favor, inténtalo de nuevo.',
            icon: 'error',
            confirmButtonText: 'OK'
        });
    });
});
