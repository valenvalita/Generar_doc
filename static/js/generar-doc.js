
// Al seleccionar Campo es extranjero 
// Se muestran o no campos de nacionalidad, pasaporte y cedula
const esExtranjero = document.getElementById('extranjero');

esExtranjero.addEventListener('change', function() {
    const nacionalidad = document.getElementById('campo_nacionalidad_arrendatario');
    const pasaporte = document.getElementById('campo_pasaporte_arrendatario');
    const cedula= document.getElementById('campo_cedula_arrendatario');

    if (this.checked) {
        nacionalidad.hidden = false;
        pasaporte.hidden = false;
        cedula.hidden = true;
        
    } else {
        nacionalidad.hidden = true;
        pasaporte.hidden = true;
        cedula.hidden = false;
    }
});

function generate_doc() {
    let formName = document.getElementById("form");
    formName.submit()
}
