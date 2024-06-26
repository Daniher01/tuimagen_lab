document.getElementById('generatePDF').addEventListener('click', function () {

    // Obtener el nombre del doctor
    const doctorName = document.getElementById('nombreDoctor').innerText //document.getElementById('doctor-name').innerText;
    const totalTrabajos = document.querySelectorAll('#dataTable tbody tr').length;

    // Obtener el SVG como cadena
    fetch(`${window.location.origin}/static/images/logotipo.svg`)
        .then(response => response.text())
        .then(svgText => {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            const img = new Image();
            const svgBlob = new Blob([svgText], { type: 'image/svg+xml;charset=utf-8' });
            const url = URL.createObjectURL(svgBlob);

            img.onload = function () {
                ctx.drawImage(img, 0, 0);
                const imgData = canvas.toDataURL('image/png');
                generatePDF({doctorName, totalTrabajos}, imgData);
                URL.revokeObjectURL(url);
            };

            img.onerror = function () {
                console.warn('No se pudo cargar la imagen. Generando PDF sin la imagen.');
                generatePDF({doctorName, totalTrabajos}, null);
            };

            img.src = url;
        })
        .catch(() => {
            console.warn('No se pudo cargar la imagen. Generando PDF sin la imagen.');
            generatePDF({doctorName, totalTrabajos}, null);
        });
});


function generatePDF({ doctorName, totalTrabajos }, imgData = null) {
    const { jsPDF } = window.jspdf;
    const date = new Date().toLocaleDateString();
    const formattedDate = new Date().toISOString().split('T')[0];

    // Obtener el color de la variable CSS
    const color_tuimagen = getComputedStyle(document.documentElement)
        .getPropertyValue('--color-tuimagen').trim();

    // Crear un nuevo documento PDF
    const doc = new jsPDF();

    // Si la imagen se carga correctamente, agregarla al PDF en el lado derecho
    if (imgData) {
        doc.addImage(imgData, 'PNG', 150, 10, 40, 20); // Ajusta las coordenadas y tamaño según sea necesario
    }

    // Agregar el título y la tabla
    doc.setFontSize(22);
    doc.setTextColor(0, 0, 0); // Establecer el color del texto del título
    doc.text('Cuenta de cobro', 20, 20);

    // Agregar la fecha actual
    doc.setFontSize(12);
    doc.setTextColor(0, 0, 0); // Establecer el color del texto de la fecha
    doc.text(`Fecha: ${date}`, 20, 30);

    // Agregar la información de la empresa
    doc.setFontSize(14);
    doc.text('Tu Imagen Lab', 20, 40);

    // Agregar el destinatario
    doc.setFontSize(12);
    doc.text('Dirigido a:', 20, 50);
    doc.setTextColor(0, 0, 0); // Establecer el color del texto del nombre del doctor
    doc.text(45, 50, doctorName);

    // Agregar el total de trabajos
    doc.setFontSize(12);
    doc.setTextColor(0, 0, 0); // Establecer el color del texto "Total de trabajos:"
    doc.text('La suma de:', 20, 60);
    const trabajoText = totalTrabajos === 1 ? 'trabajo' : 'trabajos';
    doc.setTextColor(0, 0, 0); // Establecer el color del número total de trabajos
    doc.text(45, 60, `${totalTrabajos.toString()} ${trabajoText}`);

    // Dibujar una línea horizontal
    doc.setLineWidth(0.1); // Línea más fina
    doc.line(20, 65, 190, 65);

    const rows = [];
    document.querySelectorAll('#dataTable tbody tr').forEach(tr => {
        const row = [];
        tr.querySelectorAll('td').forEach(td => row.push(td.innerText));
        rows.push(row);
    });

    doc.autoTable({
        head: [['N°', 'Nombre del Paciente', 'Fecha de Entrega', 'Tipo de Trabajo', 'Estado', 'Pagado']],
        body: rows,
        startY: 70,
        headStyles: { // Estilos para el encabezado de la tabla
            fillColor: color_tuimagen, // Color de fondo del encabezado
            textColor: '#ffffff', // Color del texto del encabezado
            fontStyle: 'bold' // Estilo de la fuente del encabezado
        },
    });

    // Agregar el pie de página
    doc.setFontSize(10);
    doc.text('Este es un documento de referencia, no es válido como Factura.', 105, doc.internal.pageSize.height - 10, { align: 'center' });

    // Guardar el PDF con el nombre `trabajos_nombredoctor_fecha`
    doc.save(`trabajos_${doctorName}_${formattedDate}.pdf`);
}




