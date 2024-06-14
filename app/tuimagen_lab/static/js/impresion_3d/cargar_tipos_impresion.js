const tipoImpresion3DSelect = document.getElementById('tipoImpresion3D');
const guiaQuirurgicaForm = document.getElementById('guiaQuirurgicaForm');
const modeloForm = document.getElementById('modeloForm');
const biomodeloForm = document.getElementById('biomodeloForm');

// todo agregar .ignore-validation a los campos que esten con display none y quitarlo cuando se muestren

tipoImpresion3DSelect.addEventListener('change', function () {
    guiaQuirurgicaForm.style.display = 'none';
    modeloForm.style.display = 'none';
    biomodeloForm.style.display = 'none';

    if (this.value === 'guia_quirurgica') {
        guiaQuirurgicaForm.style.display = 'block';
    } else if (this.value === 'modelo') {
        modeloForm.style.display = 'block';
    } else if (this.value === 'biomodelo') {
        biomodeloForm.style.display = 'block';
    }
});