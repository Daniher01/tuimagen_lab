const rutInputs = document.getElementsByClassName('is-rut');

Array.from(rutInputs).forEach(function (input) {
    input.addEventListener('keyup', function () {
        input.value = formatearRut(input.value);
        validarRut(input.value, input);

        console.log(input.value);
        // limpiar el input
        if(input.value === ''){
            input.classList.remove('is-invalid');
        }
    });

});

function validarRut(rutValue, inputElement) {
    let rutSinFormato = rutValue.replace(/[.-]/g, '');
    let digitoVerificador = rutSinFormato.slice(-1).toUpperCase();
    let rutNumerico = parseInt(rutSinFormato.slice(0, -1), 10);

    let suma = 0;
    let multiplicador = 2;

    while (rutNumerico > 0) {
        suma += (rutNumerico % 10) * multiplicador;
        rutNumerico = Math.floor(rutNumerico / 10);
        multiplicador = multiplicador === 7 ? 2 : multiplicador + 1;
    }

    let resto = suma % 11;
    let digitoVerificadorCalculado = 11 - resto;

    if (digitoVerificadorCalculado === 11) {
        digitoVerificadorCalculado = '0';
    } else if (digitoVerificadorCalculado === 10) {
        digitoVerificadorCalculado = 'K';
    } else {
        digitoVerificadorCalculado = digitoVerificadorCalculado.toString();
    }

    if (digitoVerificador !== digitoVerificadorCalculado) {
        inputElement.classList.add('is-invalid');
        inputElement.classList.remove('is-valid');
    } else {
        inputElement.classList.remove('is-invalid');
        inputElement.classList.add('is-valid');
    }
}

function formatearRut(rut) {
    let rutSinFormato = rut.replace(/\./g, '').replace('-', '');
    let rutFormateado = '';
    let contador = 0;

    for (let i = rutSinFormato.length - 1; i >= 0; i--) {
        if (contador === 1 && i === rutSinFormato.length - 2) {
            rutFormateado = '-' + rutFormateado;
            contador = 0;
        } else if (contador === 3) {
            rutFormateado = '.' + rutFormateado;
            contador = 0;
        }
        rutFormateado = rutSinFormato.charAt(i) + rutFormateado;
        contador++;
    }

    return rutFormateado;
}