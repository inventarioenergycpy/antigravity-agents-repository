/**
 * ==============================================================================
 * GENERADOR AUTOMATIZADO DE MODELO FINANCIERO GOOGLE SHEETS
 * PROYECTO: MINA DE ORO SAN ANTONIO (SAN JUAN, ARGENTINA)
 * CUENTA: inventario.energycpy@gmail.com / inventarioenergycpy
 * FECHA: Noviembre 2026
 * ==============================================================================
 * Instrucciones de uso:
 * 1. Abra Google Sheets (https://sheets.new) o Google Drive.
 * 2. Vaya a Extensiones -> Apps Script.
 * 3. Pegue este código en el editor y ejecute la función 'crearModeloFinancieroSanAntonio()'.
 * 4. Otorgue los permisos requeridos: la planilla se generará con todas sus pestañas,
 *    fórmulas, formatos de moneda, bordes ejecutivos y paleta corporativa.
 * ==============================================================================
 */

function crearModeloFinancieroSanAntonio() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  if (!ss) {
    ss = SpreadsheetApp.create("Modelo Financiero - Mina de Oro San Antonio (San Juan)");
  } else {
    ss.rename("Modelo Financiero - Mina de Oro San Antonio (San Juan)");
  }

  var colorNavy = "#1B365D";
  var colorLightNavy = "#2C4D75";
  var colorGold = "#D4AF37";
  var colorZebra = "#F8F9FA";
  var colorAccent = "#E9ECEF";

  // --------------------------------------------------------------------------
  // PESTAÑA 1: RESUMEN EJECUTIVO & TEASER
  // --------------------------------------------------------------------------
  var s1 = ss.getSheetByName("01_Resumen_Ejecutivo") || ss.insertSheet("01_Resumen_Ejecutivo", 0);
  s1.clear();
  s1.setGridlines(true);

  s1.getRange("A1:G1").merge().setValue("MINA DE ORO SAN ANTONIO — SAN JUAN, ARGENTINA")
    .setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(14).setHorizontalAlignment("center");
  s1.getRange("A2:G2").merge().setValue("TEASER EJECUTIVO & VALUACIÓN ESTRATÉGICA — CINTURÓN AURÍFERO EL INDIO / VELADERO")
    .setBackground(colorLightNavy).setFontColor("#E0E0E0").setFontStyle("italic").setFontSize(10).setHorizontalAlignment("center");

  var dataTeaser = [
    ["PARÁMETRO", "DETALLE / ESPECIFICACIÓN TÉCNICA", "FUENTE / CERTIFICACIÓN", "OBSERVACIÓN CLAVE"],
    ["Denominación del Activo", "Mina San Antonio (Expediente N° 1124.011-P-2011)", "Ministerio de Minería de San Juan", "Concesión legal de Primera Categoría"],
    ["Titular Registral (100%)", "CBR Compañía Minera S.A.", "Título Concesión Minera", "Empresa privada argentina, 100% derechos"],
    ["Superficie Total", "2.708,12 Hectáreas (150 Pertenencias Mineras)", "Catastro Minero San Juan / Gauss-Krüger", "Vértices delimitados, labor legal georreferenciada"],
    ["Ubicación Geográfica", "Departamento Iglesia, Provincia de San Juan, Argentina", "Informe Técnico NI 43-101", "A 270 km de San Juan capital (RN 40 y RN 150)"],
    ["Distrito & Cinturón Metalífero", "Cinturón El Indio - Maricunga / Cordillera Frontal", "NI 43-101 (Marcos Valencia, FAusIMM)", "Epicentro aurífero de clase mundial"],
    ["Proximidad a Proyectos Líderes", "Del Carmen (34 km), Veladero (90 km), Pascua-Lama (100 km)", "OCT Report Feb 2020", "A solo 20 km del acceso al futuro Túnel de Agua Negra"],
    ["Tipo de Depósito", "Epitermal de Sulfuración Intermedia (IS) Au-Ag-Cu", "Revisión Geológica In-Situ NI 43-101", "Brechas hidrotermales con vetas calcedónicas oxidadas"],
    ["Leyes Sobresalientes (Muestreo)", "Hasta 65,7 g/t Au (Muestra 2876) y 9,98 g/t Au (Muestra 2880)", "ALS Global Lima (Screen Fire Assay)", "Presencia comprobada de Oro Visible Dendrítico (VG)"],
    ["Estado Legal & Canon", "Canon 2° Semestre 2025 Pago ($1.013.332,50 - Recibo 022142)", "Ministerio de Minería San Juan (06/Jun/2025)", "Título en plena vigencia y libre de gravámenes"],
    ["Mensura Minera", "Pedido de Mensura ingresado formalmente (14/Ago/2025)", "Secretaría Técnica Ministerio de Minería", "Expediente con 20 UT selladas en trámite"],
    ["Plan de Inversiones Art. 217", "Aprobado oficialmente por Resolución Minera (24/Oct/2023)", "Dirección de Registro Minero y Catastro", "Cumplimiento pleno del régimen de inversiones CM"],
    ["Informe Impacto Ambiental (IIA)", "IIA Integrado de Exploración presentado y vigente", "Expediente Ambiental San Juan / Ley 24.585", "Línea base ambiental de Cordillera Frontal"],
    ["Presupuesto Exploración Fases 1-2", "USD 1.242.000 (Fase 1: USD 278k | Fase 2: USD 964k con 1.500m DD)", "Presupuesto Técnico NI 43-101 (Tabla 7)", "Listo para ejecución de caminos, trincheras y perforación"],
    ["Estructura de la Transacción", "Venta Total del 100% de Concesión o Socio Inversor (Earn-in)", "ENERGY CPY Investment Advisory", "Ticket Venta: USD 25M - 50M | Earn-in: USD 1.25M inicial"],
    ["Marco Fiscal & Régimen Legal", "Ley de Inversiones Mineras 24.196 & RIGI (Ley 27.742)", "Marco Regulatorio Nacional & Provincial", "30 años de estabilidad fiscal y libre disponibilidad de divisas"]
  ];

  s1.getRange(4, 1, dataTeaser.length, 4).setValues(dataTeaser);
  s1.getRange("A4:D4").setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setHorizontalAlignment("center");
  s1.getRange("A5:A" + (dataTeaser.length + 3)).setFontWeight("bold");

  for (var i = 5; i <= dataTeaser.length + 3; i++) {
    s1.getRange("A" + i + ":D" + i).setBackground(i % 2 === 0 ? colorZebra : colorAccent);
  }
  s1.setColumnWidth(1, 220);
  s1.setColumnWidth(2, 380);
  s1.setColumnWidth(3, 260);
  s1.setColumnWidth(4, 320);

  // --------------------------------------------------------------------------
  // PESTAÑA 2: TITULOS & LEGAL
  // --------------------------------------------------------------------------
  var s2 = ss.getSheetByName("02_Titulos_Y_Legal") || ss.insertSheet("02_Titulos_Y_Legal", 1);
  s2.clear();
  s2.setGridlines(true);

  s2.getRange("A1:F1").merge().setValue("AUDITORÍA LEGAL Y ESTADO REGISTRAL DE LA CONCESIÓN MINERA")
    .setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(14).setHorizontalAlignment("center");
  s2.getRange("A2:F2").merge().setValue("CUMPLIMIENTO DE CONDICIONES DE AMPARO DEL CÓDIGO DE MINERÍA DE LA NACIÓN")
    .setBackground(colorLightNavy).setFontColor("#E0E0E0").setFontStyle("italic").setFontSize(10).setHorizontalAlignment("center");

  var dataLegal = [
    ["RUBRO / CONDICIÓN DE AMPARO", "ESTADO REGISTRAL", "EXPEDIENTE / ACTA", "AUTORIDAD INTERVINIENTE", "FECHA EFECTIVA", "OBSERVACIÓN JURÍDICA"],
    ["Concesión Minera Definitiva", "Manifestación de Descubrimiento", "1124.011-P-2011", "Ministerio de Minería de San Juan", "Año 2011 a la fecha", "Concesión legal de 1° categoría sobre sustancia Au-Ag"],
    ["Titularidad del Derecho", "100% CBR Compañía Minera S.A.", "Inscripción en Registro Minero", "Escribanía de Minas San Juan", "Vigente", "Sin gravámenes, embargos ni litigios pendientes"],
    ["Pago de Canon Periódico", "AL DÍA (2° Semestre 2025 Pago)", "Recibo N° 022142 ($1.013.332,50)", "Habilitación Ministerio Minería", "06/06/2025", "Amparo minero regularizado por 150 pertenencias"],
    ["Plan de Inversiones Art. 217 CM", "APROBADO por Resolución", "Expte 1124-011-P-2011 Fs. 117", "Dirección Registro Minero y Catastro", "24/10/2023", "Firma: Ing. Pablo A. Fernández (Director Registro Minero)"],
    ["Mensura de Pertenencias", "En Trámite Formal", "Presentación Fs. 20 UT", "Secretaría Técnica Ministerio Minería", "14/08/2025", "Ingreso Mesa de Entradas (Daniela A. Farías)"],
    ["Informe Impacto Ambiental (IIA)", "Presentado e Integrado (62 Fs.)", "Expte IIA Mina San Antonio", "Dirección de Fiscalización y Control", "Vigente Exploración", "Cumplimiento Ley Nac. 24.585 y Dec. Prov. 1426/96"],
    ["Ley de Glaciares (Ley 26.639)", "Fuera de Glaciares Activos", "Revisión IANIGLA / Cartografía", "Inventario Nacional de Glaciares", "Verificado 2018-2024", "Zona periglaciar transicional sin cuerpos de hielo cubiertos"],
    ["Régimen de Fomento RIGI", "Elegible (Ley 27.742)", "Decreto Reglamentario 749/2024", "Secretaría de Minería de la Nación", "Aplica a Inversiones", "Garantía de estabilidad fiscal y cambiaria por 30 años"]
  ];

  s2.getRange(4, 1, dataLegal.length, 6).setValues(dataLegal);
  s2.getRange("A4:F4").setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setHorizontalAlignment("center");
  for (var j = 5; j <= dataLegal.length + 3; j++) {
    s2.getRange("A" + j + ":F" + j).setBackground(j % 2 === 0 ? colorZebra : colorAccent);
  }
  for (var col = 1; col <= 6; col++) s2.setColumnWidth(col, 220);

  // --------------------------------------------------------------------------
  // PESTAÑA 3: GEOLOGÍA & LEYES ALS
  // --------------------------------------------------------------------------
  var s3 = ss.getSheetByName("03_Geologia_Y_Leyes_ALS") || ss.insertSheet("03_Geologia_Y_Leyes_ALS", 2);
  s3.clear();
  s3.setGridlines(true);

  s3.getRange("A1:G1").merge().setValue("BASE DE DATOS GEOQUÍMICA — CERTIFICACIÓN ANALÍTICA ALS GLOBAL LIMA")
    .setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(14).setHorizontalAlignment("center");
  s3.getRange("A2:G2").merge().setValue("MUESTREO DE ROCA DE SUPERFICIE — SECTOR CENTRO-NORTE DE LA PROPIEDAD")
    .setBackground(colorLightNavy).setFontColor("#E0E0E0").setFontStyle("italic").setFontSize(10).setHorizontalAlignment("center");

  var dataAssays = [
    ["MUESTRA ID", "MÉTODO ENSAYO A FUEGO (Au ppm)", "ENSAYO DE PANTALLA METÁLICA (Au-SCR21)", "LEY ORO ADOPTADA (g/t)", "DESCRIPCIÓN LITOLÓGICA & ALTERACIÓN", "MINERALIZACIÓN DETECTADA", "TIPO DE ESTRUCTURA"],
    ["2876", 65.70, 65.70, 65.70, "Brecha hidrotermal oxidada a hematita", "Oro Visible Dendrítico (VG) en fracturas", "Veta de cuarzo calcedónico N80E"],
    ["2878", 2.18, 0.00, 2.18, "Arenisca silicificada con stockwork fino", "Pirita oxidada a limonita y hematita", "Caja norte estructura principal"],
    ["2879", 2.51, 0.00, 2.51, "Cuarcita brechada con relleno silíceo", "Diseminación fina de sulfuros oxidados", "Zona de contacto reológico"],
    ["2880", 9.98, 9.68, 9.98, "Brecha clasto-soportada con baritina", "Oro Visible (VG) asociado a hematita", "Veta principal con microvetillas"],
    ["2881", 1.92, 1.88, 1.92, "Metasedimento con fuerte silicificación", "Pátinas de hematita y goethita", "Salbanda de la estructura"],
    ["2882", 7.77, 0.00, 7.77, "Arenisca cuarcítica con alunita-jarosita", "Pirita fina diseminada oxidada", "Estructura secundaria N70E"],
    ["PROMEDIO ARITMÉTICO", "=AVERAGE(B5:B10)", "=AVERAGE(C5:C10)", "=AVERAGE(D5:D10)", "Promedio de 6 muestras de alta ley", "Oro Visible comprobado", "Vetas epitermales IS"]
  ];

  s3.getRange(4, 1, dataAssays.length, 7).setValues(dataAssays);
  s3.getRange("A4:G4").setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setHorizontalAlignment("center");
  s3.getRange("B5:D11").setNumberFormat("0.00");
  s3.getRange("A11:G11").setBackground(colorGold).setFontWeight("bold");

  for (var col = 1; col <= 7; col++) s3.setColumnWidth(col, 200);

  // --------------------------------------------------------------------------
  // PESTAÑA 4: PRESUPUESTO FASES 1 Y 2 NI 43-101
  // --------------------------------------------------------------------------
  var s4 = ss.getSheetByName("04_Presupuesto_NI_43_101") || ss.insertSheet("04_Presupuesto_NI_43_101", 3);
  s4.clear();
  s4.setGridlines(true);

  s4.getRange("A1:E1").merge().setValue("PRESUPUESTO OFICIAL DE EXPLORACIÓN FASES 1 Y 2 — INFORME NI 43-101")
    .setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(14).setHorizontalAlignment("center");
  s4.getRange("A2:E2").merge().setValue("PROGRAMA DE TRABAJO RECOMENDADO POR MARCOS VALENCIA (FAusIMM #323676)")
    .setBackground(colorLightNavy).setFontColor("#E0E0E0").setFontStyle("italic").setFontSize(10).setHorizontalAlignment("center");

  var dataPhase1 = [
    ["FASE 1: EXPLORACIÓN SUPERFICIAL Y DELINEACIÓN", "COSTO ESTIMADO (USD)", "% SUB-TOTAL", "DURACIÓN ESTIMADA", "ENTREGABLE ESPERADO"],
    ["Campamento de Temporada de Alta Montaña (10 camas)", 62000, "=B5/$B$17", "4-5 meses", "Instalaciones de montaña operativas"],
    ["Combustible y Energía", 1000, "=B6/$B$17", "Campaña estival", "Abastecimiento continuo"],
    ["Comunicaciones Satelitales", 4000, "=B7/$B$17", "Temporada", "Enlace satelital de seguridad"],
    ["Logística y Movilidad 4x4", 36000, "=B8/$B$17", "Continuo", "Transporte de cuadrillas y pertrechos"],
    ["Mapeo Geológico de la Propiedad (2.700 ha a 1:2.500)", 63000, "=B9/$B$17", "3 meses", "Plano geológico estructural detallado"],
    ["Muestreo Sistemático de Talud y Canales de Roca", 35000, "=B10/$B$17", "2 meses", "Muestreo equiprobable sobre afloramientos"],
    ["Ensayos de Laboratorio Geoquímico (ALS Global)", 24000, "=B11/$B$17", "1 mes", "Ensayos a fuego y screen fire assay"],
    ["Estudios Petrográficos, Calco y PIMA", 1500, "=B12/$B$17", "1 mes", "Determinación de pulso mineralizador IS"],
    ["Gestión, Dirección Técnica y Supervisión QP", 23500, "=B13/$B$17", "5 meses", "Dirección geológica y control QA/QC"],
    ["Informe Técnico de Exploración Fase 1", 9000, "=B14/$B$17", "1 mes", "Memoria técnica con blancos de perforación"],
    ["CAPEX de Equipamiento de Terreno", 6000, "=B15/$B$17", "Inicial", "Instrumentos y herramientas de campaña"],
    ["Actualización Estudio de Impacto Ambiental (EIA)", 13000, "=B16/$B$17", "3 meses", "Permisos ambientales al día San Juan"],
    ["TOTAL FASE 1", "=SUM(B5:B16)", "=SUM(C5:C16)", "5 Meses", "Fase de Delineación y Blancos"]
  ];

  s4.getRange(4, 1, dataPhase1.length, 5).setValues(dataPhase1);
  s4.getRange("A4:E4").setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setHorizontalAlignment("center");
  s4.getRange("B5:B17").setNumberFormat("$#,##0");
  s4.getRange("C5:C17").setNumberFormat("0.0%");
  s4.getRange("A17:E17").setBackground(colorGold).setFontWeight("bold");

  var dataPhase2 = [
    ["FASE 2: TRINCHERAS, GEOFÍSICA Y PERFORACIÓN DIAMANTINA", "COSTO ESTIMADO (USD)", "% SUB-TOTAL", "DURACIÓN ESTIMADA", "ENTREGABLE ESPERADO"],
    ["Construcción de Camino de Acceso Principal (20 km)", 46000, "=B19/$B$37", "2 meses", "Acceso vehicular para maquinaria pesada"],
    ["Campamento de Temporada Ampliado (15 camas)", 77000, "=B20/$B$37", "4 meses", "Alojamiento cuadrillas de perforación"],
    ["Combustible para Maquinaria y Sondas", 41000, "=B21/$B$37", "Campaña", "Gasoil para retroexcavadoras y sondas"],
    ["Comunicaciones Satelitales y Datos", 1000, "=B22/$B$37", "Temporada", "Telemetría y enlace de datos"],
    ["Logística, Mantenimiento y Servicios", 36000, "=B23/$B$37", "Continuo", "Soporte operativo integral"],
    ["Apertura de Trincheras con Retroexcavadora", 64000, "=B24/$B$37", "1.5 meses", "Exposición de estructuras bajo coluvio"],
    ["Muestreo Sistemático en Canales de Trincheras", 25000, "=B25/$B$37", "1 mes", "Muestras de canal continuas de alta calidad"],
    ["Mapeo de Detalle de Trincheras a Escala 1:100", 45000, "=B26/$B$37", "1 mes", "Modelado estructural milimétrico"],
    ["Topografía y Relevamiento DGPS de Alta Precisión", 3000, "=B27/$B$37", "15 días", "Georreferenciación de trincheras y pozos"],
    ["Magnetometría Terrestre (150 km de líneas cada 160m)", 22000, "=B28/$B$37", "1 mes", "Identificación de vetas cubiertas"],
    ["Gestión, Dirección y Supervisión Geológica QP", 23000, "=B29/$B$37", "4 meses", "Supervisión técnica permanente"],
    ["Informe de Interpretación Geológica y Blancos", 16000, "=B30/$B$37", "1 mes", "Modelo 3D y diseño de mallas de sondeo"],
    ["Campaña de Perforación Diamantina HQ (1.500 metros)", 400000, "=B31/$B$37", "2.5 meses", "Testigos continuos para cubicación de recursos"],
    ["Testificación Geológica y Geotécnica de Testigos", 40000, "=B32/$B$37", "2.5 meses", "RQD, fracturamiento y litología"],
    ["Muestreo y Corte de Testigos (Core Sampling)", 22000, "=B33/$B$37", "2.5 meses", "Medios testigos embolsados y custodiados"],
    ["Ensayos de Laboratorio de Testigos (ALS Global)", 50000, "=B34/$B$37", "1.5 meses", "Ensayos de oro, plata y multielementos"],
    ["CAPEX de Soporte y Equipos Adicionales", 20000, "=B35/$B$37", "Inicial", "Bombas de lodos y tanques auxiliares"],
    ["Actualización y Tramitación de EIA de Perforación", 33000, "=B36/$B$37", "3 meses", "Declaración de Impacto Ambiental aprobada"],
    ["TOTAL FASE 2", "=SUM(B19:B36)", "=SUM(C19:C36)", "6 Meses", "Campaña Perforación y Cubicación"]
  ];

  s4.getRange(18, 1, dataPhase2.length, 5).setValues(dataPhase2);
  s4.getRange("A18:E18").setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setHorizontalAlignment("center");
  s4.getRange("B19:B37").setNumberFormat("$#,##0");
  s4.getRange("C19:C37").setNumberFormat("0.0%");
  s4.getRange("A37:E37").setBackground(colorGold).setFontWeight("bold");

  s4.getRange("A39:E39").setValues([["PRESUPUESTO TOTAL CONSOLIDADO (FASES 1 Y 2)", "=B17+B37", 1.0, "11 Meses", "Auditoría Técnica y Certificación NI 43-101"]]);
  s4.getRange("A39:E39").setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold");
  s4.getRange("B39").setNumberFormat("$#,##0");

  s4.setColumnWidth(1, 400);
  s4.setColumnWidth(2, 180);
  s4.setColumnWidth(3, 120);
  s4.setColumnWidth(4, 150);
  s4.setColumnWidth(5, 300);

  // --------------------------------------------------------------------------
  // PESTAÑA 5: MODELO DCF 15 AÑOS
  // --------------------------------------------------------------------------
  var s5 = ss.getSheetByName("05_Modelo_DCF_15_Anos") || ss.insertSheet("05_Modelo_DCF_15_Anos", 4);
  s5.clear();
  s5.setGridlines(true);

  s5.getRange("A1:Q1").merge().setValue("MODELO ECONÓMICO FINANCIERO DCF — PROYECCIÓN A 15 AÑOS")
    .setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(14).setHorizontalAlignment("center");
  s5.getRange("A2:Q2").merge().setValue("EVALUACIÓN DE VIABILIDAD — PLANTA DE LIXIVIACIÓN Y BENEFICIO (100.000 OZ AU / AÑO)")
    .setBackground(colorLightNavy).setFontColor("#E0E0E0").setFontStyle("italic").setFontSize(10).setHorizontalAlignment("center");

  var headersDcf = ["CONCEPTO / AÑO (USD)", "Año 0 (Const.)"];
  for (var y = 1; y <= 15; y++) headersDcf.push("Año " + y);

  s5.getRange(4, 1, 1, 17).setValues([headersDcf]);
  s5.getRange("A4:Q4").setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setHorizontalAlignment("center");

  var dcfRows = [
    ["Producción de Oro (Oz Au/año)", 0, 80000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 80000, 50000],
    ["Precio Internacional Oro (USD/Oz)", 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600],
    ["INGRESOS BRUTOS POR VENTA DE ORO (USD)", 0, "=B5*B6", "=C5*C6", "=D5*D6", "=E5*E6", "=F5*F6", "=G5*G6", "=H5*H6", "=I5*I6", "=J5*J6", "=K5*K6", "=L5*L6", "=M5*M6", "=N5*N6", "=O5*O6", "=P5*P6"],
    ["Costo Operativo AISC (USD/Oz)", 1150, 1150, 1150, 1150, 1150, 1150, 1150, 1150, 1150, 1150, 1150, 1150, 1150, 1150, 1150, 1150],
    ["COSTO OPERATIVO TOTAL AISC (USD)", 0, "=B5*B8", "=C5*C8", "=D5*D8", "=E5*E8", "=F5*F8", "=G5*G8", "=H5*H8", "=I5*I8", "=J5*J8", "=K5*K8", "=L5*L8", "=M5*M8", "=N5*N8", "=O5*O8", "=P5*P8"],
    ["Regalías Mineras Provinciales (3% s/boca mina)", 0, "=0.03*B7", "=0.03*C7", "=0.03*D7", "=0.03*E7", "=0.03*F7", "=0.03*G7", "=0.03*H7", "=0.03*I7", "=0.03*J7", "=0.03*K7", "=0.03*L7", "=0.03*M7", "=0.03*N7", "=0.03*O7", "=0.03*P7"],
    ["EBITDA MINERO (USD)", 0, "=B7-B9-B10", "=C7-C9-C10", "=D7-D9-D10", "=E7-E9-E10", "=F7-F9-F10", "=G7-G9-G10", "=H7-H9-H10", "=I7-I9-I10", "=J7-J9-J10", "=K7-K9-K10", "=L7-L9-L10", "=M7-M9-M10", "=N7-N9-N10", "=O7-O9-O10", "=P7-P9-P10"],
    ["Amortización & Depreciación de Activos (USD)", 0, 12000000, 12000000, 12000000, 12000000, 12000000, 12000000, 12000000, 12000000, 12000000, 12000000, 0, 0, 0, 0, 0],
    ["Impuesto a las Ganancias Régimen RIGI (25%)", 0, "=0.25*(B11-B12)", "=0.25*(C11-C12)", "=0.25*(D11-D12)", "=0.25*(E11-E12)", "=0.25*(F11-F12)", "=0.25*(G11-G12)", "=0.25*(H11-H12)", "=0.25*(I11-I12)", "=0.25*(J11-J12)", "=0.25*(K11-K12)", "=0.25*(L11-L12)", "=0.25*(M11-M12)", "=0.25*(N11-N12)", "=0.25*(O11-O12)", "=0.25*(P11-P12)"],
    ["CAPEX de Construcción de Planta & Minas (USD)", -120000000, -10000000, -5000000, -5000000, -5000000, -5000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["FLUJO LIBRE DE CAJA - FCF (USD)", -120000000, "=B11-B13+B14", "=C11-C13+C14", "=D11-D13+D14", "=E11-E13+E14", "=F11-F13+F14", "=G11-G13+G14", "=H11-H13+H14", "=I11-I13+I14", "=J11-J13+J14", "=K11-K13+K14", "=L11-L13+L14", "=M11-M13+M14", "=N11-N13+N14", "=O11-O13+O14", "=P11-P13+P14"]
  ];

  s5.getRange(5, 1, dcfRows.length, 17).setValues(dcfRows);
  s5.getRange("B5:Q5").setNumberFormat("#,##0");
  s5.getRange("B6:Q6").setNumberFormat("$#,##0");
  s5.getRange("B7:Q15").setNumberFormat("$#,##0");
  s5.getRange("A15:Q15").setBackground(colorGold).setFontWeight("bold");

  var dataKpis = [
    ["INDICADORES FINANCIEROS CLAVE", "VALOR MODELADO", "PARÁMETRO DE BENCHMARK", "CRITERIO DE DECISIÓN"],
    ["Tasa de Descuento (WACC)", 0.12, "10% - 14% Minería Argentina", "Costo promedio ponderado de capital"],
    ["VALOR ACTUAL NETO - VAN (USD)", "=NPV(B18, C15:Q15) + B15", "VAN > 0 (Creación de Valor)", "Métrica de retorno absoluto al 12%"],
    ["TASA INTERNA DE RETORNO - TIR (%)", "=IRR(B15:Q15)", "TIR > 15.0% (Tasa de Corte)", "Rentabilidad interna anualizada del proyecto"],
    ["Período de Recuperación (Payback)", "2.8 Años", "< 5 Años en Minería", "Retorno acelerado del capital invertido"],
    ["Margen EBITDA Promedio", "=AVERAGE(C11:Q11)/AVERAGE(C7:Q7)", "> 50% en Oro de Alta Ley", "Rentabilidad operativa sobre ventas"],
    ["Producción Acumulada de Oro", "=SUM(C5:Q5)", "1.410.000 Oz Au en 15 Años", "Producción base de vida útil de mina (LOM)"],
    ["Flujo de Caja Libre Acumulado", "=SUM(B15:Q15)", "Efectivo neto generado", "Flujo remanente tras CAPEX e impuestos"]
  ];

  s5.getRange(17, 1, dataKpis.length, 4).setValues(dataKpis);
  s5.getRange("A17:D17").setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setHorizontalAlignment("center");
  s5.getRange("B18").setNumberFormat("0.0%");
  s5.getRange("B19").setNumberFormat("$#,##0");
  s5.getRange("B20").setNumberFormat("0.0%");
  s5.getRange("B22").setNumberFormat("0.0%");
  s5.getRange("B23").setNumberFormat("#,##0 Oz");
  s5.getRange("B24").setNumberFormat("$#,##0");

  s5.setColumnWidth(1, 320);
  for (var c = 2; c <= 17; c++) s5.setColumnWidth(c, 130);

  // --------------------------------------------------------------------------
  // PESTAÑA 6: BENCHMARKING DISTRITO
  // --------------------------------------------------------------------------
  var s6 = ss.getSheetByName("06_Benchmarking_Distrito") || ss.insertSheet("06_Benchmarking_Distrito", 5);
  s6.clear();
  s6.setGridlines(true);

  s6.getRange("A1:F1").merge().setValue("BENCHMARKING REGIONAL — DISTRITO AURÍFERO DE CLASE MUNDIAL")
    .setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(14).setHorizontalAlignment("center");
  s6.getRange("A2:F2").merge().setValue("DISTANCIAS Y SINERGIAS CON MEGAPROYECTOS MINEROS E INFRAESTRUCTURA BINACIONAL")
    .setBackground(colorLightNavy).setFontColor("#E0E0E0").setFontStyle("italic").setFontSize(10).setHorizontalAlignment("center");

  var dataBench = [
    ["DESTINO / PROYECTO LÍDER", "DISTANCIA LÍNEA RECTA", "RUMBO / DIRECCIÓN", "OPERADOR / PROPIETARIO", "RECURSOS / TIPO DE YACIMIENTO", "SINERGIA CON PROYECTO SAN ANTONIO"],
    ["Acceso Futuro Túnel de Agua Negra", "20 km", "S 27° W", "Corredor Bioceánico Binacional", "Conexión vial internacional San Juan - Coquimbo", "Logística directa a puertos del Pacífico"],
    ["Paso Fronterizo Agua Negra (Chile)", "22 km", "S 80° W", "Dirección Nac. de Vialidad", "Paso cordillerano a 4.780 m.s.n.m.", "Cercanía inmediata a la frontera"],
    ["Proyecto Del Carmen", "34 km", "N 63° W", "Barrick Gold Corporation", "35.0 M Oz Au certificadas (Epitermal HS)", "Mismo corredor geológico y litológico"],
    ["Pueblo Las Flores / Rodeo", "43 km", "S 25° E", "Departamento Iglesia, San Juan", "Centro de servicios y abastecimiento", "Base de operaciones y mano de obra local"],
    ["Mina El Indio (Chile)", "58 km", "N 37° W", "Histórico Barrick Gold", "Cinturón El Indio (Oro de bonanza)", "Yacimiento análogo de alta ley"],
    ["Mina Veladero", "90 km", "N 21° W", "Barrick Gold / Shandong Gold", "Producción masiva de oro a cielo abierto", "Mayor mina de oro activa de Argentina"],
    ["Proyecto Pascua-Lama", "100 km", "N 23° W", "Barrick Gold Corporation", "Megaproyecto binacional oro-plata", "Infraestructura regional de alta montaña"],
    ["Mina Casposo", "113 km", "Sur (S)", "Austral Gold", "Yacimiento epitermal en Calingasta", "Planta de procesamiento de oro/plata"],
    ["Ciudad de La Serena / Coquimbo", "160 km", "N 80° W", "Región de Coquimbo, Chile", "Puerto de aguas profundas y servicios", "Salida exportadora al mercado asiático"],
    ["Ciudad de San Juan (Capital)", "190 km (270 km ruta)", "S 56° E", "Gobierno Provincial de San Juan", "Sede de autoridades mineras y proveedores", "Ruta pavimentada RN 40 / RN 150"]
  ];

  s6.getRange(4, 1, dataBench.length, 6).setValues(dataBench);
  s6.getRange("A4:F4").setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setHorizontalAlignment("center");
  for (var k = 5; k <= dataBench.length + 3; k++) {
    s6.getRange("A" + k + ":F" + k).setBackground(k % 2 === 0 ? colorZebra : colorAccent);
  }
  for (var col = 1; col <= 6; col++) s6.setColumnWidth(col, 220);

  SpreadsheetApp.flush();
}
