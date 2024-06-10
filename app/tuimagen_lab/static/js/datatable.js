$(document).ready(function() {
    if (!$.fn.DataTable.isDataTable('#dataTable')) {
        $('#dataTable').DataTable({
            "paging": true,
            "searching": true,
            "ordering": true,
            "info": true,
            "language": {
                "url": `${window.location.href}static/vendor/datatables/Spanish.json`
            }
        });
    }
});