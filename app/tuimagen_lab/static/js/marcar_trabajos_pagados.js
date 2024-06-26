document.getElementById('marcarPagado').addEventListener('click', function () {
    const doctorName = document.getElementById('nombreDoctor').innerText;
    const trabajosIds = Array.from(document.querySelectorAll('#dataTable tbody tr')).map(tr => tr.querySelector('td').innerText);

    Swal.fire({
        title: '¿Estás seguro?',
        text: 'Se marcarán como pagados estos trabajos. Esta acción no se puede deshacer.',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, marcar como pagados',
        cancelButtonText: 'No, cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            const formData = new FormData();
            formData.append('doctorName', doctorName);
            trabajosIds.forEach(id => formData.append('trabajosIds[]', id));

            fetch(`${window.location.origin}/marcar-pagado/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'), // Solo si estás utilizando CSRF token en Django
                },
                body: formData
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Error al marcar los trabajos como pagados');
                }
            })
            .then(data => {
                Swal.fire({
                    title: 'Trabajos Pagados',
                    text: 'Los trabajos se han marcado como pagados.',
                    icon: 'success',
                    confirmButtonText: 'OK',
                    html: "Esta ventana se cerrará en <b></b> segundos.",
                    timer: 2000,
                    timerProgressBar: true,
                    didOpen: () => {
                        Swal.showLoading();
                        const timer = Swal.getPopup().querySelector("b");
                        timerInterval = setInterval(() => {
                            timer.textContent = (Swal.getTimerLeft() / 1000).toFixed(0); // Convertir a segundos y redondear
                        }, 100);
                    },
                    allowOutsideClick: false, // No permitir clics fuera del modal
                    willClose: () => {
                        clearInterval(timerInterval); // Asegurarse de limpiar el intervalo
                        location.reload(); // Recargar la página al cerrar el modal
                    },
                });
            })
            .catch(error => {
                Swal.fire({
                    title: 'Error',
                    text: 'Ocurrió un error al marcar los trabajos como pagados.',
                    icon: 'error',
                    confirmButtonText: 'OK'
                });
                console.error('Error:', error);
            });
        }
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
