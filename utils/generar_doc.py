import pandas as pd
from datetime import datetime
from flask import Flask, request

from docxtpl import DocxTemplate
from docx2pdf import convert

import calendar
import os
import pythoncom


# Paths
path = "static/files/inputfiles/" 
path_output = "static/files/outputfiles/"
nombre_doc = "doc_generado.docx"
nombre_doc_pdf = "contrato.pdf" #Nombre de contrato identificado con nombre arrendador o tag

# Plantilla de Contrato
doc = DocxTemplate(path + "Contrato_copia.docx")
   
def generar_doc():
    """
    Función que obtiene los datos del formulario necesarios para generar el contrato de arriendo.
    Crea un archivo word (Contrato)
    """

    # Info Contexto
    #ciudad = request.form['ciudad']
    ciudad = ""
    dia_actual = datetime.today().strftime("%d")
    mes_actual = datetime.today().strftime("%m")
    anho_actual = datetime.today().strftime("%Y")
    dias_mes_actual = calendar.monthrange(int(anho_actual), int(mes_actual))[1]
    dias_faltantes = dias_mes_actual - int(dia_actual)
 
    # Info Arrendadorx
    nombre_arrendador = request.form['nombre_arrendador']
    profesion_arrendador = request.form['profesion_arrendador']
    cedula_arrendador = request.form['cedula_arrendador']
    calle_arrendador = request.form['calle_arrendador']
    n_calle_arrendador = request.form['n_calle_arrendador']
    depto_arrendador = request.form['depto_arrendador']
    comuna_arrendador = request.form['comuna_arrendador']
    region_arrendador = request.form['region_arrendador']

    # Info Arrendatarix
    nombre_arrendatario = request.form['nombre_arrendatario']
    nacionalidad_arrendatario = request.form['nacionalidad_arrendatario']
    profesion_arrendatario = request.form['profesion_arrendatario']
    cedula_arrendatario = request.form['cedula_arrendatario']
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
    correo_renta = request.form['correo_renta']
    correo_copia = request.form['correo_copia'] 

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

    # Diccionario con info 
    my_context = {}
    
    # Info Contexto
    info_contexto = {
        "ciudad" : ciudad,
        "fecha_hoy" : datetime.today().strftime("%A %d %B, %Y"), # Formato: Miércoles 09 Agosto, 2023
        "mes_actual" : mes_actual,
        "anho_actual" : anho_actual,
        "dias_faltantes": str(dias_faltantes)
    }
    my_context.update(info_contexto)
    
    # Info Arrendadorx
    info_arrendador = {
        "nombre_arrendadorx" : nombre_arrendador,
        "profesion_arrendadorx" : profesion_arrendador,
        "cedula_arrendadorx" : cedula_arrendador,
        "calle_arrendadorx": calle_arrendador, 
        "n_calle_arrendadorx" : n_calle_arrendador,
        "depto_arrendadorx": depto_arrendador,
        "comuna_arrendadorx" : comuna_arrendador,
        "region_arrendadorx" : region_arrendador
    }
    my_context.update(info_arrendador)
    
    # Info Arrendatarix
    info_arrendatario = {
        "nombre_arrendatarix" : nombre_arrendatario,
        "nacionalidad_arrendatarix" : nacionalidad_arrendatario,
        "cedula_arrendatarix" : cedula_arrendatario,
        "pasaporte_arrendatarix" : pasaporte_arrendatario,
        "residencia_arrendatarix" : residencia_arrendatario,
        "profesion_arrendatarix" : profesion_arrendatario,
        "calle_arrendatarix": calle_arrendatario,
        "n_calle_arrendatarix" : n_calle_arrendatario,
        "depto_arrendatarix": depto_arrendatario,
        "comuna_arrendatarix" : comuna_arrendatario,
        "region_arrendatarix" : region_arrendatario,
    }
    my_context.update(info_arrendatario)

    # Info Inmueble en arriendo
    info_arriendo = {
        "calle_arriendo" : calle_arriendo,
        "n_calle_arriendo" : n_calle_arriendo,
        "depto_arriendo" : depto_arriendo,
        "comuna_arriendo" : comuna_arriendo,
        "region_arriendo" : region_arriendo,
        "fojas_arriendo" : fojas_arriendo,
        "n_arriendo": n_arriendo,
        "bienes_raices_arriendo": bienes_raices_arriendo,
        "anho_arriendo": anho_arriendo,
        "n_dormitorios": n_dormitorios,
        "n_banhos": n_banhos,
    }
    my_context.update(info_arriendo)

    # Info Habitación en arriendo
    info_habitacion = {
        "n_habitacion" : n_habitacion,
        "nombre_habitacion" : nombre_habitacion,
        "ubicacion_habitacion" : ubicacion_habitacion,
    }
    my_context.update(info_habitacion)

    # Info Pago arriendo
    info_pago = {
        "renta_UF" : renta_UF,
        "renta_pesos" : renta_pesos,
        "nombre_banco" : nombre_banco,
        "n_cuenta" : n_cuenta,
        "receptor_renta" : receptor_renta,
        "correo_renta" : correo_renta,
        "correo_copia" : correo_copia, 
    }
    my_context.update(info_pago)

    # Info Multa
    info_multa = {
        "multa_UF" : multa_UF,
        "multa_pesos" : multa_pesos,        
    }
    my_context.update(info_multa)

    # Info Garantía
    info_garantia = {
        "garantia_UF" : garantia_UF,
        "garantia_pesos" : garantia_pesos,        
    }
    my_context.update(info_garantia)


    # Info Duración contrato
    info_duracion_contrato = {
        "duracion_dias_contrato" : duracion_dias_contrato,
        "fecha_inicio_contrato": fecha_inicio_contrato,
        "dia_inicio_contrato": dia_inicio_contrato,
        "mes_inicio_contrato": mes_inicio_contrato,
        "anho_inicio_contrato": anho_inicio_contrato,
        "fecha_termino_contrato": fecha_termino_contrato,
        "dia_termino_contrato": dia_termino_contrato,
        "mes_termino_contrato": mes_termino_contrato,
        "anho_termino_contrato": anho_termino_contrato,
        "plazo_dias_abandono_contrato" : plazo_dias_abandono_contrato, 
    }
    my_context.update(info_duracion_contrato)


    # Info Normas de convivenvia
    info_normas_convivencia = {
        "tenencia_mascotas" : tenencia_mascotas,
        "tipo_mascotas" : tipo_mascotas,  
        "fumar" : fumar,      
        "hora_descanso_inicio": hora_descanso_inicio,
        "hora_descanso_termino": hora_descanso_termino,
        "dias_descanso": dias_descanso,
        "excepcion_descanso": excepcion_descanso,
    }
    my_context.update(info_normas_convivencia)

    # Info domiclio de jurisdiccion
    info_domicilio_jurisdiccion = {
        "ciudad_jurisdiccion" : ciudad_jurisdiccion,
        "region_jurisdiccion" : region_jurisdiccion,  
    }
    my_context.update(info_domicilio_jurisdiccion)

    # Se guarda documento WORD con información agregada
    doc.render(my_context)
    doc.save(path_output + nombre_doc)
    
def wordToPdf():
    '''
    Convierte un archivo word a un archivo pdf
    '''
    try:
        pythoncom.CoInitializeEx(pythoncom.COINIT_MULTITHREADED)
    except pythoncom.com_error:
        # Ya inicializado
        pass
    # Convierte documento WORD de contrato con información ya agregada a PDF
    convert(os.path.abspath(path_output + nombre_doc), os.path.abspath(path_output + nombre_doc_pdf))


    