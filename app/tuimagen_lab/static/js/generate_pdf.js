document.getElementById('generatePDF').addEventListener('click', function () {

    // Obtener el nombre del doctor
    const doctorName = document.getElementById('nombreDoctor').innerText //document.getElementById('doctor-name').innerText;

    // Obtener el SVG como cadena
    fetch(`${window.location.origin}/static/images/logo grande.svg`)
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
                generatePDF(doctorName, imgData);
                URL.revokeObjectURL(url);
            };

            img.onerror = function () {
                console.warn('No se pudo cargar la imagen. Generando PDF sin la imagen.');
                generatePDF(doctorName, null);
            };

            img.src = url;
        })
        .catch(() => {
            console.warn('No se pudo cargar la imagen. Generando PDF sin la imagen.');
            generatePDF(doctorName, null);
        });
});


function generatePDF(doctorName, imgData = null) {
    const { jsPDF } = window.jspdf;

    // Obtener el color de la variable CSS
    const color_tuimagen = getComputedStyle(document.documentElement)
        .getPropertyValue('--color-tuimagen').trim();

    // Crear un nuevo documento PDF
    const doc = new jsPDF();

    // Si la imagen se carga correctamente, agregarla al PDF
    if (imgData) {
        doc.addImage(imgData, 'PNG', 150, 10, 40, 20); // Ajusta las coordenadas y tamaño según sea necesario
    }

    // Agregar el título y la tabla
    doc.setFontSize(22);
    doc.setTextColor(color_tuimagen); // Establecer el color del texto del título
    doc.text('Tu Imagen Lab', 20, 20);

    doc.setFontSize(12);
    doc.setTextColor(0, 0, 0); // Restablecer el color del texto a negro
    doc.text(`Trabajos de ${doctorName}`, 20, 40);

    const rows = [];
    document.querySelectorAll('#dataTable tbody tr').forEach(tr => {
        const row = [];
        tr.querySelectorAll('td').forEach(td => row.push(td.innerText));
        rows.push(row);
    });

    doc.autoTable({
        head: [['N°', 'Nombre del Paciente', 'Fecha de Entrega', 'Tipo de Trabajo', 'Estado', 'Pagado']],
        body: rows,
        startY: 50,
        headStyles: { // Estilos para el encabezado de la tabla
            fillColor: color_tuimagen, // Color de fondo del encabezado
            textColor: '#ffffff', // Color del texto del encabezado
            fontStyle: 'bold' // Estilo de la fuente del encabezado
        },
    });

    // Guardar el PDF
    doc.save(`trabajos_${doctorName}`);
}

