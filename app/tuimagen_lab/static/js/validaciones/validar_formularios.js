function validarFormulario(form) {
    // Inicializar la validez del formulario como verdadera
    let isValid = false;

    // Validar que los campos del formulario no estén vacíos
    if (!form.checkValidity()) {
        form.classList.add('was-validated');
        return false;
    }
    form.classList.remove('was-validated');
    return true;
}