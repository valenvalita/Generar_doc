from flask import Flask, request
import re
'''
COSAS POR HACER
 * Validar RUT
 * Agregar Región y Comuna
 * Calcular cantidad de días de contrato
 * Establecer formato de fecha
'''

def generarDV(rut):
    '''
    Genera el dígito verificar correspondiente al rut
    Recibe el rut en formato ddddddddd
    '''
    M = 0
    S = 1
    while rut:
        S = (S + int(rut) % 10 * (9 - M % 6)) % 11
        M += 1
        rut = int(rut) // 10
    return str(S - 1) if S else 'K'



def validarRut(rut):
    '''
    Función validar rut 
    recibe un rut en el formato XXX.XXX.XXX-X
    y valida si está en el formato correcto y si el dv corresponde
    '''
    rut = rut.strip(); # Quitar espacios adelante y al final 
    print("Rut es: " + rut)
    # Validación de formato
    regx = r'^(\d{1,3}(?:\.\d{1,3}){2}-[\dkK])$' # Formato rut: XXX.XXX.XXX-X
    regx = re.compile(regx)
    formatValid = bool(re.search(regx, rut))
    if (formatValid==True):
        print("Formato válido")
        # Formato válido
        rut = rut.split("-")
        rut_actual = rut[0].replace(".", "")
        dv_actual = rut[1].upper()
        
        dv_generado = generarDV(rut_actual)
        if(dv_actual == dv_generado):
        # DV correcto
            print("DV válido")
            return True
    return False



def validarCorreo(correo):
    '''
    Función validar correo
    valida si el correo está en el formato correcto
    '''
    correo = correo.strip(); # Quitar espacios adelante y al final 
    # Validación de formato
    regx =  r'^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$' # Formato correo
    regx = re.compile(regx)
    formatValid = re.search(regx, correo)

    if formatValid==True:
        print("Formato válido")
        return True
        
    return False



def validarInput(input, largo_max):
    '''
    Función validar input de form
    valida si el largo del input cumple con el máximo largo
    '''
    if input!=None: 
        correo = correo.strip() # Quitar espacios adelante y al final 
        largo_input = len(correo)
        if largo_input>largo_max:
            return False
        
        return True
    
    return True




def validarForm():
    ''' 
    Función validarForm()
    Valida los campos del formulario que se solicita
    para generar un contrato de arriendo en pdf
    '''

    # Validaciones principales
    # Rut
    cedula_arrendador = request.form['cedula_arrendador']
    cedula_arrendatario = request.form['cedula_arrendatario']
    cedulas = [cedula_arrendador, cedula_arrendatario]
    for cedula in cedulas:
        if not validarRut(cedula):
            print("Campo " + cedula.__name__ + "no es correcto")
    # Correo
    correo_renta = request.form['correo_renta']
    correo_copia = request.form['correo_copia'] 
    correos = [correo_renta, correo_copia]
    for correo in correos:
        if not validarCorreo(correo):
            print("Campo " + correo.__name__ + "no es correcto")

    # Info Contexto
    #ciudad = request.form['ciudad']
    ciudad = ""
 
 
    # Info Arrendadorx
    nombre_arrendador = request.form['nombre_arrendador']
    profesion_arrendador = request.form['profesion_arrendador']
    
    calle_arrendador = request.form['calle_arrendador']
    n_calle_arrendador = request.form['n_calle_arrendador']
    depto_arrendador = request.form['depto_arrendador']
    comuna_arrendador = request.form['comuna_arrendador']
    region_arrendador = request.form['region_arrendador']

    # Info Arrendatarix
    nombre_arrendatario = request.form['nombre_arrendatario']
    nacionalidad_arrendatario = request.form['nacionalidad_arrendatario']
    profesion_arrendatario = request.form['profesion_arrendatario']
    
    pasaporte_arrendatario = request.form['pasaporte_arrendatario']
    residencia_arrendatario = request.form['residencia_arrendatario']
    calle_arrendatario = request.form['calle_arrendatario']
    n_calle_arrendatario = request.form['n_calle_arrendatario']
    depto_arrendatario = request.form['depto_arrendatario']
    comuna_arrendatario = request.form['comuna_arrendatario']
    region_arrendatario = request.form['region_arrendatario']

    # Info Inmueble en arriendo
    calle_arriendo = request.form["calle_arriendo"]
    n_calle_arriendo = request.form["n_calle_arriendo"]
    depto_arriendo = request.form["depto_arriendo"]
    comuna_arriendo = request.form["comuna_arriendo"]
    region_arriendo = request.form["region_arriendo"]
    fojas_arriendo = request.form["fojas_arriendo"]
    n_arriendo = request.form["n_arriendo"]
    bienes_raices_arriendo = request.form["bienes_raices_arriendo"]
    anho_arriendo = request.form["anho_arriendo"]
    n_dormitorios = request.form["n_dormitorios"]
    n_banhos = request.form["n_banhos"]
    
    # Info Habitación en arriendo
    n_habitacion = request.form['n_habitacion']
    nombre_habitacion = request.form['nombre_habitacion']
    ubicacion_habitacion = request.form['ubicacion_habitacion']

    # Info Pago arriendo
    renta_UF = request.form['renta_UF']
    renta_pesos = request.form['renta_pesos']
    nombre_banco = request.form['nombre_banco']
    n_cuenta = request.form['n_cuenta']
    receptor_renta = request.form['receptor_renta']
    

    # Info Multa
    multa_UF = request.form['multa_UF']
    multa_pesos = request.form['multa_pesos']        

    # Info Garantía
    garantia_UF = request.form['garantia_UF']
    garantia_pesos = request.form['garantia_pesos']        

    # Info Duración contrato
    duracion_dias_contrato = request.form['duracion_dias_contrato']
    fecha_inicio_contrato = request.form['fecha_inicio_contrato']
    dia_inicio_contrato = ""
    mes_inicio_contrato = ""
    anho_inicio_contrato = ""
    fecha_termino_contrato = request.form['fecha_termino_contrato']
    dia_termino_contrato = ""
    mes_termino_contrato = ""
    anho_termino_contrato = ""
    plazo_dias_abandono_contrato = request.form['plazo_dias_abandono_contrato'] 

    # Info Normas de convivenvia
    tenencia_mascotas = ""
    tipo_mascotas = ""
    fumar = ""   
    hora_descanso_inicio = request.form['hora_descanso_inicio']
    hora_descanso_termino = request.form['hora_descanso_termino']
    dias_descanso = request.form['dias_descanso']
    excepcion_descanso = request.form['excepcion_descanso']

    # Info domiclio de jurisdiccion
    ciudad_jurisdiccion = request.form['ciudad_jurisdiccion']
    region_jurisdiccion = request.form['region_jurisdiccion']  

 