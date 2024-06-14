function validarFormulario(form) {
    // Validar que los campos del formulario no estén vacíos
    if (!form.checkValidity()) {
        form.classList.add('was-validated');
    } else {
        form.classList.remove('was-validated');
    }

    // Verificar si hay algún elemento con la clase 'is-invalid'
    const invalidElements = form.querySelectorAll('.is-invalid');
    if (invalidElements.length > 0) {
        return false;
    }

    return form.checkValidity();
}
