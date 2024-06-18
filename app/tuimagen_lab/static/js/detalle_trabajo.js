document.addEventListener('DOMContentLoaded', function() {
    // Captura todos los botones con la clase dinámica trabajo-{tipo_trabajo}
    document.querySelectorAll('.btn-icon-split').forEach(function(button) {
        button.addEventListener('click', function(event) {
            const trabajoId = button.getAttribute('data-id');
            const trabajoTipo = button.className.split(' ').find(cls => cls.startsWith('trabajo-')).replace('trabajo-', '');

            if (trabajoTipo === 'fresado') {
                verDetallesTrabajoFresado(trabajoId);
            }
            // Agregar condiciones para otros tipos de trabajos si es necesario
        });
    });
});

function verDetallesTrabajoFresado(trabajoId) {
    
    // Suponiendo que tienes una API que devuelve los detalles del trabajo
    fetch(`${window.location.origin}/detalle/fresado/${trabajoId}`)
        .then(response => response.json())
        .then(data => {

            // Asignar los valores recuperados a los elementos del DOM
            document.getElementById('fresado-detallePaciente').innerText = data.paciente_nombre;
            document.getElementById('fresado-detalleRut').innerText = data.paciente_rut;
            document.getElementById('fresado-detalleDoctor').innerText = data.doctor_nombre;
            document.getElementById('fresado-detalleFechaIngreso').innerText = data.fecha_ingreso;
            document.getElementById('fresado-detalleFechaEntrega').innerText = data.fecha_entrega;
            document.getElementById('fresado-detalleEstado').innerText = data.estado;
            document.getElementById('fresado-detalleConMaquillaje').innerText = data.con_maquillaje ? 'Sí' : 'No';

            const piezasList = document.getElementById('fresado-detallePiezas');
            piezasList.innerHTML = '';
            data.piezas.forEach(pieza => {
                const li = document.createElement('li');
                li.innerText = `Tipo: ${pieza.tipo}, Material: ${pieza.material}, Bloque: ${pieza.bloque}`;
                piezasList.appendChild(li);
            });

            // Mostrar el modal
            const modal = new bootstrap.Modal(document.getElementById('fresado'));
            modal.show();
        })
        .catch(error => console.error('Error:', error));
}


