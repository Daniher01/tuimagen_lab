document.getElementById('submitBtn').addEventListener('click', function (e) {
    e.preventDefault();

    const form = document.getElementById('trabajoForm');
    if(!validarFormulario(form)){
        return;
    }


    const formData = new FormData(form);

    // Ensure all select values are included in the form data
    document.querySelectorAll('.pieza-form').forEach(function (piezaForm) {
        piezaForm.querySelectorAll('input, select, textarea').forEach(function (input) {
            formData.append(input.name, input.value);
        });
    });

    // Log the form data to the console for debugging
    /*
    for (let pair of formData.entries()) {
        console.log(pair[0] + ': ' + pair[1]);
    }
    */

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
