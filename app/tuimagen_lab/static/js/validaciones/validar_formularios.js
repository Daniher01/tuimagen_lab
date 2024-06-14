function validarFormulario(form) {
    console.log('Formulario:', form);
    console.log('Validez inicial:', form.checkValidity());

    // Validar que los campos del formulario no estén vacíos
    if (!form.checkValidity()) {
        form.classList.add('was-validated');
    } else {
        form.classList.remove('was-validated');
    }

    // Verificar si hay algún elemento con la clase 'is-invalid'
    const invalidElements = form.querySelectorAll('.is-invalid');
    if (invalidElements.length > 0) {
        console.log('Elementos inválidos encontrados:', invalidElements);
        return false;
    }

    console.log('Validez final:', form.checkValidity());
    return form.checkValidity();
}
