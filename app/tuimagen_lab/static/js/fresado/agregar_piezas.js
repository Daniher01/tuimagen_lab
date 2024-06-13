document.addEventListener('DOMContentLoaded', function () {
    function updateRemoveButtons() {
        const removeButtons = document.querySelectorAll('.remove-pieza');
        removeButtons.forEach(function (button) {
            button.disabled = removeButtons.length === 1;
        });
    }

    function updateFormIndices() {
        const forms = document.querySelectorAll('.pieza-form');
        const totalForms = document.getElementById('id_pieza-TOTAL_FORMS');
        forms.forEach(function (form, index) {
            form.querySelectorAll('input, select, textarea').forEach(function (input) {
                const name = input.name.replace(/pieza-\d+-/, `pieza-${index}-`);
                const id = input.id.replace(/id_pieza-\d+-/, `id_pieza-${index}-`);
                input.name = name;
                input.id = id;
            });
            form.querySelectorAll('label').forEach(function (label) {
                const newFor = label.htmlFor.replace(/id_pieza-\d+-/, `id_pieza-${index}-`);
                label.htmlFor = newFor;
            });
        });
        totalForms.value = forms.length;
    }

    document.querySelector('.add-pieza').addEventListener('click', function () {
        var piezaForm = document.querySelector('.pieza-form:last-of-type'); // Select the last pieza form
        var newPiezaForm = piezaForm.cloneNode(true);

        // Clear the values in the cloned form
        newPiezaForm.querySelectorAll('input, textarea').forEach(function (input) {
            input.value = '';
        });

        // Clear the selected values in the cloned form
        newPiezaForm.querySelectorAll('select').forEach(function (select) {
            select.selectedIndex = 0; // Set to the default value (first option)
        });

        var piezasContainer = document.getElementById('piezas-container');
        piezasContainer.appendChild(newPiezaForm);
        updateFormIndices();
        newPiezaForm.querySelector('.remove-pieza').addEventListener('click', function () {
            newPiezaForm.remove();
            updateRemoveButtons();
            updateFormIndices();
        });
        updateRemoveButtons();
    });

    document.querySelectorAll('.remove-pieza').forEach(function (button) {
        button.addEventListener('click', function () {
            if (document.querySelectorAll('.pieza-form').length > 1) {
                button.closest('.pieza-form').remove();
                updateRemoveButtons();
                updateFormIndices();
            }
        });
    });
    

    updateRemoveButtons();
    updateFormIndices();  // Ensure indices are correct on initial load
});

