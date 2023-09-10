/**
 * Validar RUT
 * Agregar Región y Comuna
 * Calcular cantidad de días de contrato
 * Establecer formato de fecha
 */

/**
 * Genera el dígito verificar correspondiente al rut
 * Recibe el rut en formato ddddddddd
 * @param {*} T 
 * @returns 
 */
const generarDV = (rut) => {
    const M = 0,
        S = 1;
    for (; rut; rut = Maruth.floor(rut / 10))
        S = (S + rut % 10 * (9 - M++ % 6)) % 11;
    return S ? S - 1 : 'K';
};

/**
 * Función validar rut 
 * recibe un rut en el formato XXX.XXX.XXX-X
 * y valida si está en el formato correcto y si el dv corresponde
 */
const validarRut = (rut) => {
    rut = rut.trim(); // Quitar espacios adelante y al final 
    // Validación de formato
    let re = /^(\d{1,3}(?:\.\d{1,3}){2}-[\dkK])$/; // Formato rut: XXX.XXX.XXX-X
    let formatValid = re.test(rut);
    if (formatValid==true) {
    // Formato válido
    rut = rut.split("-");
    rut_actual = rut[0].replaceAll(".", "");
    dv_actual = rut[1].toUpperCase();
    dv_generado = generarDV(rut_actual);
    if(dv_actual == dv_generado) {
        // DV correcto
        return true;
    }  
    }
    return false;
};

/**
 * Función validar correo
 * valida si el correo está en el formato correcto
 */
const validarCorreo = (correo) => {
    correo = correo.trim(); // Quitar espacios adelante y al final 
    // Validación de formato
    let re =  /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/; // Formato correo
    let formatValid = re.test(correo);
      if (formatValid==true) {
        return true;  
      }
      return false;
};

/**
 * Función validar input de form
 * valida si el largo del input cumple con el máximo largo
 */
const validarInput = (input, largo_max) => {
    if (input!=null) {
        correo = correo.trim();
        largo_input = correo.length;
        if (largo_input>largo_max) {
            return false;
        }
        return true;
    }
    return true;
}


/** 
 * Función validarForm()
 * Valida los campos del formulario que se solicita
 * para generar un contrato de arriendo en pdf
 */
const validarForm = () => {

    // Se acceden a los campos del formulario
    
    // Info Contexto
    //const ciudad = document.getElementById('ciudad')
    const ciudad = ""
    
  
     // Info Arrendadorx
    const nombre_arrendador = document.getElementById('nombre_arrendador')
    const profesion_arrendador = document.getElementById('profesion_arrendador')
    const cedula_arrendador = document.getElementById('cedula_arrendador')
    const calle_arrendador = document.getElementById('calle_arrendador')
    const n_calle_arrendador = document.getElementById('n_calle_arrendador')
    const depto_arrendador = document.getElementById('depto_arrendador')
    const comuna_arrendador = document.getElementById('comuna_arrendador')
    const region_arrendador = document.getElementById('region_arrendador')
 
     // Info Arrendatarix
    const nombre_arrendatario = document.getElementById('nombre_arrendatario')
    const nacionalidad_arrendatario = document.getElementById('nacionalidad_arrendatario')
    const profesion_arrendatario = document.getElementById('profesion_arrendatario')
    const cedula_arrendatario = document.getElementById('cedula_arrendatario')
    const pasaporte_arrendatario = document.getElementById('pasaporte_arrendatario')
    const residencia_arrendatario = document.getElementById('residencia_arrendatario')
    const calle_arrendatario = document.getElementById('calle_arrendatario')
    const n_calle_arrendatario = document.getElementById('n_calle_arrendatario')
    const depto_arrendatario = document.getElementById('depto_arrendatario')
    const comuna_arrendatario = document.getElementById('comuna_arrendatario')
    const region_arrendatario = document.getElementById('region_arrendatario')
 
     // Info Inmueble en arriendo
    const calle_arriendo = document.getElementById("calle_arriendo")
    const n_calle_arriendo = document.getElementById("n_calle_arriendo")
    const depto_arriendo = document.getElementById("depto_arriendo")
    const comuna_arriendo = document.getElementById("comuna_arriendo")
    const region_arriendo = document.getElementById("region_arriendo")
    const fojas_arriendo = document.getElementById("fojas_arriendo")
    const n_arriendo = document.getElementById("n_arriendo")
    const bienes_raices_arriendo = document.getElementById("bienes_raices_arriendo")
    const anho_arriendo = document.getElementById("anho_arriendo")
    const n_dormitorios = document.getElementById("n_dormitorios")
    const n_banhos = document.getElementById("n_banhos")
     
     // Info Habitación en arriendo
    const n_habitacion = document.getElementById('n_habitacion')
    const nombre_habitacion = document.getElementById('nombre_habitacion')
    const ubicacion_habitacion = document.getElementById('ubicacion_habitacion')
 
     // Info Pago arriendo
    const renta_UF = document.getElementById('renta_UF')
    const renta_pesos = document.getElementById('renta_pesos')
    const nombre_banco = document.getElementById('nombre_banco')
    const n_cuenta = document.getElementById('n_cuenta')
    const receptor_renta = document.getElementById('receptor_renta')
    const correo_renta = document.getElementById('correo_renta')
    const correo_copia = document.getElementById('correo_copia') 
 
     // Info Multa
    const multa_UF = document.getElementById('multa_UF')
    const multa_pesos = document.getElementById('multa_pesos')        
 
     // Info Garantía
    const garantia_UF = document.getElementById('garantia_UF')
    const garantia_pesos = document.getElementById('garantia_pesos')        
 
     // Info Duración contrato
    const duracion_dias_contrato = document.getElementById('duracion_dias_contrato')
    const fecha_inicio_contrato = document.getElementById('fecha_inicio_contrato')
    const dia_inicio_contrato = ""
    const mes_inicio_contrato = ""
    const anho_inicio_contrato = ""
    const fecha_termino_contrato = document.getElementById('fecha_termino_contrato')
    const dia_termino_contrato = ""
    const mes_termino_contrato = ""
    const anho_termino_contrato = ""
    const plazo_dias_abandono_contrato = document.getElementById('plazo_dias_abandono_contrato') 
 
     // Info Normas de convivenvia
    const tenencia_mascotas = ""
    const tipo_mascotas = ""
    const fumar = ""   
    const hora_descanso_inicio = document.getElementById('hora_descanso_inicio')
    const hora_descanso_termino = document.getElementById('hora_descanso_termino')
    const dias_descanso = document.getElementById('dias_descanso')
    const excepcion_descanso = document.getElementById('excepcion_descanso')
 
     // Info domiclio de jurisdiccion
    const ciudad_jurisdiccion = document.getElementById('ciudad_jurisdiccion')
    const region_jurisdiccion = document.getElementById('region_jurisdiccion')  
}; 
 