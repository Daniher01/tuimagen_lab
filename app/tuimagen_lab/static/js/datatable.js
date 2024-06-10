$(document).ready(function() {
    if (!$.fn.DataTable.isDataTable('#dataTable')) {
        $('#dataTable').DataTable({
            "paging": true,
            "searching": true,
            "ordering": true,
            "info": true,
            "language": {
                "url": `${window.location.origin}/static/vendor/datatables/Spanish.json`
            }
        });
    }
});