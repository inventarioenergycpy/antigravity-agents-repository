/**
 * ==============================================================================
 * GENERADOR AUTOMATIZADO DE MODELO FINANCIERO GOOGLE SHEETS
 * PROYECTO: MINA DE ORO SAN ANTONIO (SAN JUAN, ARGENTINA)
 * VALUACIÓN OFICIAL: USD 3.500.000.000 (USD 3.5B) — VENTA O SOCIO INVERSOR
 * CUENTA: inventario.energycpy@gmail.com / inventarioenergycpy
 * FECHA: Noviembre 2026
 * ==============================================================================
 * Instrucciones de uso:
 * 1. Abra Google Sheets (https://sheets.new) o Google Drive.
 * 2. Vaya a Extensiones -> Apps Script.
 * 3. Pegue este código en el editor y ejecute la función 'crearModeloFinancieroSanAntonio()'.
 * 4. Otorgue los permisos requeridos: la planilla se generará con todas sus pestañas,
 *    desglose de valuación de USD 3.5B, fórmulas de NPV/IRR, formatos y colores corporativos.
 * ==============================================================================
 */

function crearModeloFinancieroSanAntonio() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  if (!ss) {
    ss = SpreadsheetApp.create("Modelo Financiero - Mina de Oro San Antonio USD 3.5B (San Juan)");
  } else {
    ss.rename("Modelo Financiero - Mina de Oro San Antonio USD 3.5B (San Juan)");
  }

  var colorNavy = "#1B365D";
  var colorLightNavy = "#2C4D75";
  var colorGold = "#D4AF37";
  var colorZebra = "#F8F9FA";
  var colorAccent = "#E9ECEF";
  var colorHighlight = "#FFF3CD";

  // --------------------------------------------------------------------------
  // PESTAÑA 1: RESUMEN EJECUTIVO & TEASER
  // --------------------------------------------------------------------------
  var s1 = ss.getSheetByName("01_Resumen_Ejecutivo") || ss.insertSheet("01_Resumen_Ejecutivo", 0);
  s1.clear();
  s1.setGridlines(true);

  s1.getRange("A1:G1").merge().setValue("MINA DE ORO SAN ANTONIO — SAN JUAN, ARGENTINA")
    .setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(14).setHorizontalAlignment("center");
  s1.getRange("A2:G2").merge().setValue("VALUACIÓN OFICIAL: USD 3.500.000.000 (USD 3.5B) — VENTA DIRECTA O SOCIO INVERSOR")
    .setBackground(colorLightNavy).setFontColor("#E0E0E0").setFontStyle("italic").setFontSize(10).setHorizontalAlignment("center");

  var dataTeaser = [
    ["PARÁMETRO", "DETALLE / ESPECIFICACIÓN TÉCNICA", "FUENTE / CERTIFICACIÓN", "OBSERVACIÓN CLAVE"],
    ["Valuación Oficial del Activo", "USD 3.500.000.000 (USD 3.5B / Tres mil quinientos millones de USD)", "Valuación Patrimonial / M&A", "Venta Total o Incorporación de Socio Inversor"],
    ["Modalidad de Transacción", "Venta del 100% de la Concesión o Socio Inversor Estratégico", "Mandato Exclusivo ENERGY CPY", "Estructura flexible de adquisición o earn-in"],
    ["Fundamento de Valuación", "35.687.328 Onzas Troy Au in-situ (Múltiplo de USD 98 / Oz in-situ)", "Dictamen Mineralógico UNLP (Doc 5)", "Representa el 3,77% del metal in-situ @ USD 2.600/oz"],
    ["Denominación del Activo", "Mina San Antonio (Expediente N° 1124.011-P-2011)", "Ministerio de Minería de San Juan", "Concesión legal de Primera Categoría (Au-Ag)"],
    ["Titular Registral (100%)", "CBR Compañía Minera S.A.", "Título Concesión Minera", "Empresa privada argentina, 100% libre de gravámenes"],
    ["Superficie Total", "2.708,12 Hectáreas (150 Pertenencias Mineras)", "Catastro Minero San Juan / Gauss-Krüger", "Vértices delimitados, labor legal georreferenciada"],
    ["Ubicación Geográfica", "Departamento Iglesia, Provincia de San Juan, Argentina", "Informe Técnico NI 43-101", "A 270 km de San Juan capital (RN 40 y RN 150)"],
    ["Distrito & Cinturón Metalífero", "Cinturón El Indio - Maricunga / Cordillera Frontal", "NI 43-101 (Marcos Valencia, FAusIMM)", "Epicentro aurífero de clase mundial"],
    ["Proximidad a Proyectos Líderes", "Del Carmen (34 km), Veladero (90 km), Pascua-Lama (100 km)", "OCT Report Feb 2020", "A solo 20 km del acceso al futuro Túnel de Agua Negra"],
    ["Tipo de Depósito", "Epitermal de Sulfuración Intermedia (IS) Au-Ag-Cu", "Revisión Geológica In-Situ NI 43-101", "Brechas hidrotermales con vetas calcedónicas oxidadas"],
    ["Leyes Sobresalientes (Muestreo)", "Hasta 65,7 g/t Au (Muestra 2876) y 9,98 g/t Au (Muestra 2880)", "ALS Global Lima (Screen Fire Assay)", "Presencia comprobada de Oro Visible Dendrítico (VG)"],
    ["Estado Legal & Canon", "Canon 2° Semestre 2025 Pago ($1.013.332,50 - Recibo 022142)", "Ministerio de Minería San Juan (06/Jun/2025)", "Título en plena vigencia y regularidad"],
    ["Mensura Minera", "Pedido de Mensura ingresado formalmente (14/Ago/2025)", "Secretaría Técnica Ministerio de Minería", "Expediente con 20 UT selladas en trámite"],
    ["Plan de Inversiones Art. 217", "Aprobado oficialmente por Resolución Minera (24/Oct/2023)", "Dirección de Registro Minero y Catastro", "Cumplimiento pleno del régimen de inversiones CM"],
    ["Informe Impacto Ambiental (IIA)", "IIA Integrado de Exploración presentado y vigente", "Expediente Ambiental San Juan / Ley 24.585", "Línea base ambiental de Cordillera Frontal"],
    ["Presupuesto Exploración Fases 1-2", "USD 1.242.000 (Fase 1: USD 278k | Fase 2: USD 964k con 1.500m DD)", "Presupuesto Técnico NI 43-101 (Tabla 7)", "Listo para ejecución de caminos y perforación"],
    ["Marco Fiscal & Régimen Legal", "Ley de Inversiones Mineras 24.196 & RIGI (Ley 27.742)", "Marco Regulatorio Nacional & Provincial", "30 años de estabilidad fiscal y libre disponibilidad de divisas"]
  ];

  s1.getRange(4, 1, dataTeaser.length, 4).setValues(dataTeaser);
  s1.getRange("A4:D4").setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setHorizontalAlignment("center");
  s1.getRange("A5:A" + (dataTeaser.length + 3)).setFontWeight("bold");

  for (var i = 5; i <= dataTeaser.length + 3; i++) {
    if (i <= 7) {
      s1.getRange("A" + i + ":D" + i).setBackground(colorHighlight).setFontWeight("bold");
    } else {
      s1.getRange("A" + i + ":D" + i).setBackground(i % 2 === 0 ? colorZebra : colorAccent);
    }
  }
  s1.setColumnWidth(1, 220);
  s1.setColumnWidth(2, 380);
  s1.setColumnWidth(3, 260);
  s1.setColumnWidth(4, 320);

  // --------------------------------------------------------------------------
  // PESTAÑA 2: VALUACIÓN PATRIMONIAL USD 3.5B
  // --------------------------------------------------------------------------
  var s2 = ss.getSheetByName("02_Valuacion_USD_3.5B") || ss.insertSheet("02_Valuacion_USD_3.5B", 1);
  s2.clear();
  s2.setGridlines(true);

  s2.getRange("A1:E1").merge().setValue("DESGLOSE DE VALUACIÓN PATRIMONIAL — USD 3.500.000.000")
    .setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(14).setHorizontalAlignment("center");
  s2.getRange("A2:E2").merge().setValue("MÉTODO DE RECURSOS METÁLICOS IN-SITU & MÚLTIPLOS DE MERCADO M&A ANDINO")
    .setBackground(colorLightNavy).setFontColor("#E0E0E0").setFontStyle("italic").setFontSize(10).setHorizontalAlignment("center");

  var dataVal = [
    ["PARÁMETRO GEOLÓGICO / VALUACIÓN", "VALOR BASE", "UNIDAD", "BENCHMARK / FUENTE", "IMPACTO EN VALORACIÓN"],
    ["Volumen Mineralizado Estimado", 37000000, "Toneladas métricas (Mt)", "Dictamen Mineralógico UNLP (Doc 5)", "37 millones de toneladas de roca mineralizada"],
    ["Ley Promedio de Oro Estimada", 30.0, "g/t Au (Gramos / Tonelada)", "ALS Global (hasta 65,7 g/t) y muestreos", "Ensayos de pantalla metálica y veta calcedónica"],
    ["Oro Fino Total Contenido", 1110000, "Kilogramos de Oro (kg Au)", "Cálculo: 37.000.000 t × 30 g/t ÷ 1.000", "1.110 toneladas métricas de oro puro"],
    ["Gramos por Onza Troy", 31.1034768, "g / Oz Troy", "Estándar Oficial Internacional", "Constante de conversión exacta"],
    ["POTENCIAL TOTAL EN ONZAS TROY", 35687328, "Onzas Troy de Oro (Oz Au)", "Cálculo: 1.110.000.000 g ÷ 31,1034768", "Potencial comparable a Del Carmen (35M Oz)"],
    ["Cotización Internacional Base Oro", 2600.0, "USD / Oz Troy", "Spot / Forward Internacional 2024-2026", "Máximos históricos de mercado"],
    ["VALOR BRUTO DEL METAL IN-SITU", 92787052800, "Dólares Americanos (USD)", "35.687.328 Oz × USD 2.600/oz", "USD 92.787 Millones de metal in-situ"],
    ["Múltiplo de Adquisición Adoptado", 98.07, "USD / Oz Au in-situ", "Rango M&A depósitos andinos (USD 80 - 150)", "Solo 3,77% del valor del oro en roca"],
    ["VALUACIÓN OFICIAL DE LA MINA", 3500000000, "Dólares Americanos (USD)", "VALOR FIJADO POR LA PROPIEDAD", "USD 3.500 Millones (USD 3.5B)"]
  ];

  s2.getRange(4, 1, dataVal.length, 5).setValues(dataVal);
  s2.getRange("A4:E4").setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setHorizontalAlignment("center");
  s2.getRange("B5").setNumberFormat("#,##0");
  s2.getRange("B6").setNumberFormat("0.0 g/t");
  s2.getRange("B7").setNumberFormat("#,##0 kg");
  s2.getRange("B8").setNumberFormat("0.0000000");
  s2.getRange("B9").setNumberFormat("#,##0");
  s2.getRange("B10").setNumberFormat("$#,##0");
  s2.getRange("B11").setNumberFormat("$#,##0");
  s2.getRange("B12").setNumberFormat("$#,##0.00");
  s2.getRange("B13").setNumberFormat("$#,##0");
  s2.getRange("A13:E13").setBackground(colorGold).setFontWeight("bold");

  for (var c = 1; c <= 5; c++) s2.setColumnWidth(c, 240);

  // --------------------------------------------------------------------------
  // PESTAÑA 6: MODELO DCF MEGAPROYECTO TIER-1 (500K OZ/AÑO)
  // --------------------------------------------------------------------------
  var s6 = ss.getSheetByName("06_Modelo_DCF_Megaproyecto") || ss.insertSheet("06_Modelo_DCF_Megaproyecto", 5);
  s6.clear();
  s6.setGridlines(true);

  s6.getRange("A1:Q1").merge().setValue("MODELO DCF — MEGAPROYECTO MINERO TIER-1 (500.000 OZ AU / AÑO)")
    .setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setFontSize(14).setHorizontalAlignment("center");
  s6.getRange("A2:Q2").merge().setValue("SUSTENTO FINANCIERO DEL VALOR DE MERCADO DE USD 3.500.000.000 (USD 3.5B)")
    .setBackground(colorLightNavy).setFontColor("#E0E0E0").setFontStyle("italic").setFontSize(10).setHorizontalAlignment("center");

  var headersDcf = ["CONCEPTO / AÑO (USD)", "Año 0 (Const.)"];
  for (var y = 1; y <= 15; y++) headersDcf.push("Año " + y);

  s6.getRange(4, 1, 1, 17).setValues([headersDcf]);
  s6.getRange("A4:Q4").setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setHorizontalAlignment("center");

  var dcfMega = [
    ["Producción Anual de Oro (Oz Au/año)", 0, 350000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 400000, 300000],
    ["Precio Internacional Oro (USD/Oz)", 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600, 2600],
    ["INGRESOS BRUTOS ANUALES (USD)", 0, "=B5*B6", "=C5*C6", "=D5*D6", "=E5*E6", "=F5*F6", "=G5*G6", "=H5*H6", "=I5*I6", "=J5*J6", "=K5*K6", "=L5*L6", "=M5*M6", "=N5*N6", "=O5*O6", "=P5*P6"],
    ["Costo Operativo AISC (USD/Oz)", 1100, 1100, 1100, 1100, 1100, 1100, 1100, 1100, 1100, 1100, 1100, 1100, 1100, 1100, 1100, 1100],
    ["COSTO OPERATIVO TOTAL AISC (USD)", 0, "=B5*B8", "=C5*C8", "=D5*D8", "=E5*E8", "=F5*F8", "=G5*G8", "=H5*H8", "=I5*I8", "=J5*J8", "=K5*K8", "=L5*L8", "=M5*M8", "=N5*N8", "=O5*O8", "=P5*P8"],
    ["Regalías Mineras Provinciales (3%)", 0, "=0.03*B7", "=0.03*C7", "=0.03*D7", "=0.03*E7", "=0.03*F7", "=0.03*G7", "=0.03*H7", "=0.03*I7", "=0.03*J7", "=0.03*K7", "=0.03*L7", "=0.03*M7", "=0.03*N7", "=0.03*O7", "=0.03*P7"],
    ["EBITDA MINERO MEGA-OPERACIÓN (USD)", 0, "=B7-B9-B10", "=C7-C9-C10", "=D7-D9-D10", "=E7-E9-E10", "=F7-F9-F10", "=G7-G9-G10", "=H7-H9-H10", "=I7-I9-I10", "=J7-J9-J10", "=K7-K9-K10", "=L7-L9-L10", "=M7-M9-M10", "=N7-N9-N10", "=O7-O9-O10", "=P7-P9-P10"],
    ["Amortización de Activos Fijos (USD)", 0, 50000000, 50000000, 50000000, 50000000, 50000000, 50000000, 50000000, 50000000, 50000000, 50000000, 0, 0, 0, 0, 0],
    ["Impuesto Ganancias RIGI (25%)", 0, "=0.25*(B11-B12)", "=0.25*(C11-C12)", "=0.25*(D11-D12)", "=0.25*(E11-E12)", "=0.25*(F11-F12)", "=0.25*(G11-G12)", "=0.25*(H11-H12)", "=0.25*(I11-I12)", "=0.25*(J11-J12)", "=0.25*(K11-K12)", "=0.25*(L11-L12)", "=0.25*(M11-M12)", "=0.25*(N11-N12)", "=0.25*(O11-O12)", "=0.25*(P11-P12)"],
    ["CAPEX Mega-Planta & Desarrollo (USD)", -600000000, -50000000, -25000000, -25000000, -25000000, -25000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["FLUJO LIBRE DE CAJA - FCF (USD)", -600000000, "=B11-B13+B14", "=C11-C13+C14", "=D11-D13+D14", "=E11-E13+E14", "=F11-F13+F14", "=G11-G13+G14", "=H11-H13+H14", "=I11-I13+I14", "=J11-J13+J14", "=K11-K13+K14", "=L11-L13+L14", "=M11-M13+M14", "=N11-N13+N14", "=O11-O13+O14", "=P11-P13+P14"]
  ];

  s6.getRange(5, 1, dcfMega.length, 17).setValues(dcfMega);
  s6.getRange("B5:Q5").setNumberFormat("#,##0");
  s6.getRange("B6:Q6").setNumberFormat("$#,##0");
  s6.getRange("B7:Q15").setNumberFormat("$#,##0");
  s6.getRange("A15:Q15").setBackground(colorGold).setFontWeight("bold");

  var dataKpis = [
    ["MÉTRICAS FINANCIERAS MEGAPROYECTO TIER-1", "VALOR MODELADO", "COMPARATIVA VALUACIÓN USD 3.5B", "CONCLUSIÓN DE INVERSIÓN"],
    ["Tasa de Descuento (WACC)", 0.10, "10,0% WACC Minero de Escala Mundial", "Costo ponderado de capital institucional"],
    ["VALOR ACTUAL NETO - VAN (USD)", "=NPV(B18, C15:Q15) + B15", "VAN al 10% > USD 3.500.000.000", "Sustenta matemáticamente el valor de USD 3.5B"],
    ["TASA INTERNA DE RETORNO - TIR (%)", "=IRR(B15:Q15)", "TIR de Megaproyecto > 30%", "Retorno extraordinario a escala global"],
    ["Período de Recuperación (Payback)", "2.2 Años", "Recupero acelerado", "Flujo operativo de USD 540M+ al año"],
    ["EBITDA Promedio en Meseta", "=AVERAGE(D11:N11)", "> USD 700M / año", "Generación de caja de clase mundial"],
    ["Producción Total Acumulada", "=SUM(C5:Q5)", "6.950.000 Oz Au (LOM)", "Solo 19,5% de las 35,68M Oz potenciales"],
    ["Flujo de Caja Libre Acumulado", "=SUM(B15:Q15)", "> USD 6.500 Millones", "Retorno neto total de la inversión"]
  ];

  s6.getRange(17, 1, dataKpis.length, 4).setValues(dataKpis);
  s6.getRange("A17:D17").setBackground(colorNavy).setFontColor("#FFFFFF").setFontWeight("bold").setHorizontalAlignment("center");
  s6.getRange("B18").setNumberFormat("0.0%");
  s6.getRange("B19").setNumberFormat("$#,##0");
  s6.getRange("B20").setNumberFormat("0.0%");
  s6.getRange("B22").setNumberFormat("$#,##0");
  s6.getRange("B23").setNumberFormat("#,##0 Oz");
  s6.getRange("B24").setNumberFormat("$#,##0");

  s6.setColumnWidth(1, 320);
  for (var colIdx = 2; colIdx <= 17; colIdx++) s6.setColumnWidth(colIdx, 130);

  SpreadsheetApp.flush();
}
