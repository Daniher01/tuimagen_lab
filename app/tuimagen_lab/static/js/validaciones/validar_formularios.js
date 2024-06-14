function validarFormulario(form) {

    // Validar que los campos del formulario no estén vacíos
    if (!form.checkValidity()) {
        form.classList.add('was-validated');
        return false;
    }
    form.classList.remove('was-validated');
    return true;
}