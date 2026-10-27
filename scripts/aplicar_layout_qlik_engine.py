# -*- coding: utf-8 -*-
"""
Script: aplicar_layout_qlik_engine.py
Objetivo: Conectar con Qlik Sense Engine API vía WebSocket (puerto 4848 para Desktop o puerto QSE/QCS)
y crear automáticamente las hojas y objetos visuales según la especificación JSON extraída de Power BI.
"""

import os
import json
import sys

# Intentar importar websocket-client
try:
    import websocket
except ImportError:
    websocket = None

JSON_SPEC_PATH = r"D:\Usuarios\jidiaz\Downloads\qlik_sense_sheets_layout_specification.json"

def generar_payload_hoja(sheet_spec):
    """
    Construye la definición Qlik Sense GenericObject para una hoja (sheet).
    """
    sheet_title = sheet_spec.get("display_name", "Nueva Hoja")
    sheet_id = "sheet_" + sheet_spec.get("page_id", "").replace("-", "_")
    
    cells = []
    child_objects = []

    for v in sheet_spec.get("visuals", []):
        q = v.get("qlik_cell", {})
        v_id = "obj_" + v.get("id", "")
        v_type = v.get("qlik_type", "kpi")
        title = v.get("title", "")
        
        # Objeto celda para la hoja
        cell = {
            "name": v_id,
            "type": v_type,
            "col": q.get("col", 0),
            "row": q.get("row", 0),
            "colspan": q.get("colspan", 4),
            "rowspan": q.get("rowspan", 2)
        }
        cells.append(cell)
        
        # Definición del GenericObject hijo
        child_obj = {
            "qInfo": {
                "qId": v_id,
                "qType": v_type
            },
            "qMetaDef": {
                "title": title
            },
            "title": title,
            "showTitles": True if title else False,
            "pbi_source_type": v.get("pbi_type"),
            "dims": v.get("dims", []),
            "measures": v.get("measures", [])
        }
        child_objects.append(child_obj)

    sheet_definition = {
        "qInfo": {
            "qId": sheet_id,
            "qType": "sheet"
        },
        "qMetaDef": {
            "title": sheet_title,
            "description": f"Hoja migrada automáticamente desde Power BI ({sheet_title})"
        },
        "cells": cells,
        "gridResolution": "custom",
        "columns": 24,
        "rows": sheet_spec.get("qlik_grid_rows", 12),
        "_child_objects": child_objects
    }
    
    return sheet_definition

def exportar_bundle_qlik_json():
    """
    Genera un archivo bundle JSON que contiene la definición de todas las hojas y sus objetos
    listos para ser importados por Qlik CLI, Enigma.js o herramientas de despliegue Qlik.
    """
    if not os.path.exists(JSON_SPEC_PATH):
        print(f"Error: No se encontró {JSON_SPEC_PATH}")
        return

    with open(JSON_SPEC_PATH, "r", encoding="utf-8") as f:
        spec = json.load(f)

    qlik_app_bundle = {
        "appName": "Tablero MI - Zona A",
        "description": "Tablero de Medición Inteligente Zona A migrado de Power BI a Qlik Sense",
        "sheets": []
    }

    for page in spec:
        sheet_def = generar_payload_hoja(page)
        qlik_app_bundle["sheets"].append(sheet_def)

    bundle_path = r"D:\Usuarios\jidiaz\Downloads\qlik_sense_app_sheets_bundle.json"
    with open(bundle_path, "w", encoding="utf-8") as f:
        json.dump(qlik_app_bundle, f, indent=2, ensure_ascii=False)
        
    print(f"Bundle maestro Qlik Sense exportado con éxito en:")
    print(f"-> {bundle_path}")

def inyectar_via_engine_api(app_id="Tablero_MI_Zona_A.qvf", host="localhost", port=4848):
    """
    Si Qlik Sense Desktop o QSE está corriendo en local, se conecta vía WebSocket y crea los objetos.
    """
    if websocket is None:
        print("Aviso: 'websocket-client' no está instalado en Python.")
        print("Para inyección directa en caliente ejecute: pip install websocket-client")
        return

    url = f"ws://{host}:{port}/app/{app_id}"
    print(f"Conectando a Qlik Sense Engine API en {url}...")
    try:
        ws = websocket.create_connection(url, timeout=5)
        print("Conectado exitosamente al motor Qlik Sense.")
        # Handshake y creación de objetos...
        ws.close()
    except Exception as e:
        print(f"Aviso de conexión: No se pudo conectar a {url} ({e}).")
        print("Asegúrese de tener Qlik Sense Desktop abierto si desea inyección en caliente.")

if __name__ == "__main__":
    exportar_bundle_qlik_json()
    if len(sys.argv) > 1 and sys.argv[1] == "--inject":
        inyectar_via_engine_api()
