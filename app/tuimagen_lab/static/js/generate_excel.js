document.getElementById('generateExcel').addEventListener('click', function () {
    // Obtener la tabla y crear un nuevo array de datos
    var table = document.getElementById('dataTable');
    var data = [];
    
    // Obtener encabezados
    var headers = [];
    for (var i = 0; i < table.rows[0].cells.length; i++) {
        headers[i] = table.rows[0].cells[i].innerHTML;
    }
    headers.push('Monto'); // Añadir la nueva columna
    data.push(headers);
    
    // Obtener datos de filas
    for (var i = 1; i < table.rows.length; i++) {
        var row = [];
        for (var j = 0; j < table.rows[i].cells.length; j++) {
            row[j] = table.rows[i].cells[j].innerHTML;
        }
        row.push(''); // Añadir celda vacía para "Monto"
        data.push(row);
    }
    
    // Crear libro de trabajo y hoja
    var wb = XLSX.utils.book_new();
    var ws = XLSX.utils.aoa_to_sheet(data);
    
    // Añadir hoja al libro de trabajo
    XLSX.utils.book_append_sheet(wb, ws, "Trabajos Doctores");
    
    // Generar archivo Excel
    var wbout = XLSX.write(wb, {bookType: 'xlsx', type: 'binary'});

    // Obtener el nombre del doctor
    const doctorName = document.getElementById('nombreDoctor').innerText;
    const formattedDate = new Date().toISOString().split('T')[0];

    function s2ab(s) {
        var buf = new ArrayBuffer(s.length);
        var view = new Uint8Array(buf);
        for (var i = 0; i < s.length; i++) view[i] = s.charCodeAt(i) & 0xFF;
        return buf;
    }

    saveAs(new Blob([s2ab(wbout)], {type: "application/octet-stream"}), `cuenta_de_cobro_${doctorName}_${formattedDate}.xlsx`);
});

function saveAs(blob, fileName) {
    var url = window.URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.style.display = "none";
    a.href = url;
    a.download = fileName;
    document.body.appendChild(a);
    a.click();
    window.URL.revokeObjectURL(url);
}
