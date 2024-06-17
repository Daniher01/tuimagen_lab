const tipoImpresion3DSelect = document.getElementById('tipoImpresion3D');
const guiaQuirurgicaForm = document.getElementById('guiaQuirurgicaForm');
const modeloForm = document.getElementById('modeloForm');
const biomodeloForm = document.getElementById('biomodeloForm');

// todo agregar .ignore-validation a los campos que esten con display none y quitarlo cuando se muestren

tipoImpresion3DSelect.addEventListener('change', function () {
    guiaQuirurgicaForm.style.display = 'none';
    modeloForm.style.display = 'none';
    biomodeloForm.style.display = 'none';

    // quitar el atributo required en los form que no se usan
    let required_guiaquirurgica = guiaQuirurgicaForm.querySelectorAll('input, textarea, select')
    required_guiaquirurgica.forEach(function(element) {
        element.removeAttribute('required');
    });

    let required_modelo = modeloForm.querySelectorAll('input, textarea, select')
    required_modelo.forEach(function(element) {
        element.removeAttribute('required');
    });

    let required_biomodelo = biomodeloForm.querySelectorAll('input, textarea, select')
    required_biomodelo.forEach(function(element) {
        element.removeAttribute('required');
    });

    if (this.value === 'guia_quirurgica') {
        guiaQuirurgicaForm.style.display = 'block';
        //agregar el required
        required_guiaquirurgica.forEach(function(element) {
            element.setAttribute('required', '');
        });
    } else if (this.value === 'modelo') {
        modeloForm.style.display = 'block';
        //agregar el required
        required_modelo.forEach(function(element) {
            element.setAttribute('required', '');
        });
    } else if (this.value === 'biomodelo') {
        biomodeloForm.style.display = 'block';
        //agregar el required
        required_biomodelo.forEach(function(element) {
            element.setAttribute('required', '');
        });
    }
});