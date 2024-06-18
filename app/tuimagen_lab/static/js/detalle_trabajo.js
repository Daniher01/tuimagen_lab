document.addEventListener('DOMContentLoaded', function() {
    // Captura todos los botones con la clase dinámica trabajo-{tipo_trabajo}
    document.querySelectorAll('.btn-icon-split').forEach(function(button) {
        button.addEventListener('click', function(event) {
            const trabajoId = button.getAttribute('data-id');
            const trabajoTipo = button.className.split(' ').find(cls => cls.startsWith('trabajo-')).replace('trabajo-', '');
            console.log(trabajoTipo);
            if (trabajoTipo === 'fresado') {
                verDetallesTrabajoFresado(trabajoId);
            }else if (trabajoTipo === 'impresion_3d'){
                verDetallesTrabajoImpresion3D(trabajoId);
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
            document.getElementById('fresado-idTrabajo').innerText = data.id_trabajo;
            document.getElementById('fresado-detallePaciente').innerText = data.paciente_nombre;
            document.getElementById('fresado-detalleRut').innerText = data.paciente_rut;
            document.getElementById('fresado-detalleDoctor').innerText = data.doctor_nombre;
            document.getElementById('fresado-detalleFechaIngreso').innerText = data.fecha_ingreso;
            document.getElementById('fresado-detalleFechaEntrega').innerText = data.fecha_entrega;

            // Asignar estado con clases de Bootstrap
            const estadoSpan = document.getElementById('fresado-detalleEstado');
            estadoSpan.innerText = data.estado;
            estadoSpan.className = 'badge ' + (data.estado === 'completado' ? 'bg-success' : 'bg-warning');

            // Asignar ícono de maquillaje
            const maquillajeIcon = document.getElementById('fresado-detalleConMaquillaje');
            maquillajeIcon.className = 'fa ' + (data.con_maquillaje ? 'fa-check-circle text-success' : 'fa-times-circle text-danger');

            // Llenar la tabla de piezas
            const piezasTableBody = document.getElementById('fresado-detallePiezas');
            piezasTableBody.innerHTML = '';
            data.piezas.forEach(pieza => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${pieza.tipo}</td>
                    <td>${pieza.material}</td>
                    <td>${pieza.bloque}</td>
                `;
                piezasTableBody.appendChild(row);
            });

            // Mostrar el modal
            const modal = new bootstrap.Modal(document.getElementById('fresado'));
            modal.show();
        })
        .catch(error => console.error('Error:', error));
}

function verDetallesTrabajoImpresion3D(trabajoId) {
    fetch(`${window.location.origin}/detalle/impresion3d/${trabajoId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('impresion3d-idTrabajo').innerText = data.trabajo_id;
            document.getElementById('impresion3d-detallePaciente').innerText = data.paciente_nombre;
            document.getElementById('impresion3d-detalleRut').innerText = data.paciente_rut;
            document.getElementById('impresion3d-detalleDoctor').innerText = data.doctor_nombre;
            document.getElementById('impresion3d-detalleFechaIngreso').innerText = data.fecha_ingreso;
            document.getElementById('impresion3d-detalleFechaEntrega').innerText = data.fecha_entrega;
            //document.getElementById('impresion3d-detalleEstado').innerText = data.estado;
            document.getElementById('impresion3d-detalleTipo').innerText = data.detalles.tipo;
            document.getElementById('impresion3d-detalleDescripcion').innerText = data.detalles.descripcion;

            // Asignar estado con clases de Bootstrap
            const estadoSpan = document.getElementById('impresion3d-detalleEstado');
            estadoSpan.innerText = data.estado;
            estadoSpan.className = 'badge ' + (data.estado === 'completado' ? 'bg-success' : 'bg-warning');
            
            
            if (data.detalles.tipo === 'Modelo') {
                document.getElementById('impresion3d-detalleModeloTipoContainer').style.display = 'block';
                document.getElementById('impresion3d-detalleModeloTipo').innerText = data.detalles.modelo_tipo;
            } else {
                document.getElementById('impresion3d-detalleModeloTipoContainer').style.display = 'none';
                document.getElementById('impresion3d-detalleModeloTipo').innerText = '';
            }

            const modal = new bootstrap.Modal(document.getElementById('impresion_3d'));
            modal.show();
        })
        .catch(error => console.error('Error:', error));
}


