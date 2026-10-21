/**
 * =========================================================================================
 * GOOGLE APPS SCRIPT: PRESUPUESTO EJECUTIVO 1 HOJA CON TOTALES PESOS Y DÓLARES (BNA)
 * Proyecto: Sistema Solar Fotovoltaico On-Grid 10 kW (SFERCO)
 * Cotización Dólar Oficial Banco Nación (BNA) Vendedor Billete: $ 1.535,00
 * Cuenta Google Workspace: inventario.energycpy@gmail.com
 * Formato: Optimizado para ingresar exactamente en UNA SOLA HOJA (A4 / Carta)
 * =========================================================================================
 */

function generarPresupuesto1HojaSfercoConTotales() {
  var docTitle = "Presupuesto 10 kW On-Grid - SFERCO (Totales ARS y USD)";
  var doc = DocumentApp.create(docTitle);
  var body = doc.getBody();
  body.clear();

  // Márgenes compactos de 30 pt (~1.05 cm) para garantizar 1 sola página
  body.setMarginTop(30);
  body.setMarginBottom(30);
  body.setMarginLeft(38);
  body.setMarginRight(38);

  // Parámetros y Conversiones
  var tc = 1535.0; // Dólar BNA Billete Vendedor
  var matUsd = 5500.0;
  var moArs = 4800000.0;

  var matArs = matUsd * tc;          // $ 8.442.500,00
  var moUsd = moArs / tc;            // USD 3.127,04
  var totalArs = matArs + moArs;     // $ 13.242.500,00
  var totalUsd = matUsd + moUsd;     // USD 8.627,04

  // Estilos
  var styleTitle = {};
  styleTitle[DocumentApp.Attribute.FONT_FAMILY] = 'Calibri';
  styleTitle[DocumentApp.Attribute.FONT_SIZE] = 14;
  styleTitle[DocumentApp.Attribute.BOLD] = true;
  styleTitle[DocumentApp.Attribute.FOREGROUND_COLOR] = '#0F172A';

  var styleSubtitle = {};
  styleSubtitle[DocumentApp.Attribute.FONT_FAMILY] = 'Calibri';
  styleSubtitle[DocumentApp.Attribute.FONT_SIZE] = 10.5;
  styleSubtitle[DocumentApp.Attribute.BOLD] = true;
  styleSubtitle[DocumentApp.Attribute.FOREGROUND_COLOR] = '#0284C7';

  var styleMeta = {};
  styleMeta[DocumentApp.Attribute.FONT_FAMILY] = 'Calibri';
  styleMeta[DocumentApp.Attribute.FONT_SIZE] = 8.5;
  styleMeta[DocumentApp.Attribute.FOREGROUND_COLOR] = '#475569';

  var styleSectionHeader = {};
  styleSectionHeader[DocumentApp.Attribute.FONT_FAMILY] = 'Calibri';
  styleSectionHeader[DocumentApp.Attribute.FONT_SIZE] = 10;
  styleSectionHeader[DocumentApp.Attribute.BOLD] = true;
  styleSectionHeader[DocumentApp.Attribute.FOREGROUND_COLOR] = '#0F172A';

  var styleBody = {};
  styleBody[DocumentApp.Attribute.FONT_FAMILY] = 'Calibri';
  styleBody[DocumentApp.Attribute.FONT_SIZE] = 8.5;
  styleBody[DocumentApp.Attribute.LINE_SPACING_LINES] = 1.1;
  styleBody[DocumentApp.Attribute.FOREGROUND_COLOR] = '#1F2937';

  // 1. Título y Encabezado
  var p1 = body.appendParagraph("PRESUPUESTO TÉCNICO-COMERCIAL");
  p1.setAttributes(styleTitle);
  p1.setAlignment(DocumentApp.HorizontalAlignment.CENTER);

  var p2 = body.appendParagraph("SISTEMA SOLAR FOTOVOLTAICO ON-GRID 10 kW (10,44 kWp)");
  p2.setAttributes(styleSubtitle);
  p2.setAlignment(DocumentApp.HorizontalAlignment.CENTER);

  var pMeta = body.appendParagraph("Cliente: SFERCO | Córdoba | Fecha: 14/10/2026 | TC Referencia BNA Venta: $ 1.535,00 | Validez: 5 días");
  pMeta.setAttributes(styleMeta);
  pMeta.setAlignment(DocumentApp.HorizontalAlignment.CENTER);

  body.appendHorizontalRule();

  // 2. Alcance de las Tareas
  var sec1 = body.appendParagraph("1. ALCANCE DE LAS TAREAS");
  sec1.setAttributes(styleSectionHeader);

  var intro = body.appendParagraph("Provisión de materiales, montaje mecánico en cubierta, conexionado DC/AC, protecciones, ingeniería de detalle, ensayos y gestión completa de habilitación para un Sistema Solar Fotovoltaico On-Grid Trifásico de 10 kW (10,44 kWp en campo generador):");
  intro.setAttributes(styleBody);

  var items = [
    "• Campo Fotovoltaico (10,44 kWp): Montaje de 18 módulos monocristalinos TOPCon N-Type Amerisolar de 580 Wp (144 celdas) sobre 5 kits de estructuras de aluminio anodizado ISECOM con fijación estanca a cubierta.",
    "• Inversor y Conversión Trifásica: 1 Inversor On-Grid GoodWe GW10-SDT-30 de 10 kW con 2 MPPT, protección de arco (AFCI), envolvente IP66, antena Wi-Fi para telemetría remota y 10 años de garantía oficial.",
    "• Cuadros y Cableado DC/AC: 120 m cable solar Amphenol 4/6 mm² (PV 1.8 kV UV), conectores MC4 IP68, 2 Cajas de Combinación DC Suntree IP65 con fusibles y descargadores (SPD), y protector AC tetrapolar Suntree 385V 20-40kA.",
    "• Ingeniería, Certificación y Trámites: Planos y esquema unifilar con firma profesional, medición de puesta a tierra con protocolo oficial, tramitación de Usuario-Generador ante EPEC (Ley 27.424), medidor bidireccional y puesta en marcha."
  ];

  for (var i = 0; i < items.length; i++) {
    var pItem = body.appendParagraph(items[i]);
    pItem.setAttributes(styleBody);
    pItem.setIndentLeft(10);
  }

  // 3. Resumen Económico (Tabla con Totales en ARS y USD)
  var sec2 = body.appendParagraph("2. RESUMEN ECONÓMICO DE LA INVERSIÓN (COTIZACIÓN BNA: $ 1.535,00)");
  sec2.setAttributes(styleSectionHeader);

  var tableData = [
    ["Rubro / Concepto", "Alcance Técnico", "Total en Pesos (ARS)", "Total en Dólares (USD)"],
    [
      "Materiales",
      "18 Paneles 580Wp (10,44 kWp), Inversor GoodWe 10kW WiFi, cajas DC, cables y estructuras.",
      "$ 8.442.500,00",
      "USD 5.500,00"
    ],
    [
      "Mano de Obra, Ing. y Certificación",
      "Montaje de techo, conexionado DC/AC, protocolos PAT, planos firmados y trámite EPEC.",
      "$ 4.800.000,00",
      "USD 3.127,04"
    ],
    [
      "TOTAL GENERAL (Sin IVA)",
      "Sistema Llave en Mano On-Grid 10 kW (Bimonetario: USD 5.500 + $ 4.800.000)",
      "$ 13.242.500,00",
      "USD 8.627,04"
    ]
  ];

  var table = body.appendTable(tableData);
  table.setBorderColor('#CBD5E1');
  table.setBorderWidth(1);

  // Cabecera Tabla
  var headerRow = table.getRow(0);
  for (var c = 0; c < headerRow.getNumCells(); c++) {
    var cell = headerRow.getCell(c);
    cell.setBackgroundColor('#0F172A');
    var pCell = cell.getChild(0).asParagraph();
    pCell.setFontFamily('Calibri');
    pCell.setFontSize(8.5);
    pCell.setBold(true);
    pCell.setForegroundColor('#FFFFFF');
    if (c >= 2) pCell.setAlignment(DocumentApp.HorizontalAlignment.RIGHT);
  }

  // Filas Tabla
  for (var r = 1; r < table.getNumRows(); r++) {
    var row = table.getRow(r);
    var isTotal = (r === table.getNumRows() - 1);
    var bg = isTotal ? '#E0F2FE' : (r % 2 === 1 ? '#FFFFFF' : '#F8FAFC');
    for (var c = 0; c < row.getNumCells(); c++) {
      var cell = row.getCell(c);
      cell.setBackgroundColor(bg);
      var pCell = cell.getChild(0).asParagraph();
      pCell.setFontFamily('Calibri');
      pCell.setFontSize(8);
      var textColor = isTotal ? '#0369A1' : '#1F2937';
      pCell.setForegroundColor(textColor);
      if (isTotal || c === 0) pCell.setBold(true);
      if (c >= 2) pCell.setAlignment(DocumentApp.HorizontalAlignment.RIGHT);
    }
  }

  body.appendParagraph(""); // Espaciador

  // 4. Condiciones Comerciales
  var sec3 = body.appendParagraph("3. CONDICIONES COMERCIALES Y OBSERVACIONES");
  sec3.setAttributes(styleSectionHeader);

  var notes = [
    "1. Cotización del Dólar BNA: Conversión calculada a $ 1.535,00 (Dólar Oficial Vendedor Billete Banco Nación del día). En pagos en pesos o cheques diferidos, se tomará la cotización oficial del día hábil anterior a la efectiva acreditación, ajustando diferencias en efectivo.",
    "2. Fletes y Traslados: Los precios NO incluyen fletes, acarreos ni viáticos fuera del radio urbano de la obra (se coordinan por cuenta y orden del cliente).",
    "3. Condición Impositiva: Precios expresados SIN IVA (10,5% en paneles solares; 21% en inversor, componentes, mano de obra e ingeniería).",
    "4. Pago y Validez: Contado (o anticipo para reserva de stock y saldo contra avance). Validez de la oferta: 5 días hábiles sujeta a disponibilidad de stock.",
    "5. Requisitos del Cliente: Acometida trifásica normalizada y jabalina de puesta a tierra reglamentaria en el predio."
  ];

  for (var n = 0; n < notes.length; n++) {
    var pNote = body.appendParagraph(notes[n]);
    pNote.setAttributes(styleBody);
    pNote.setFontSize(8);
  }

  doc.saveAndClose();
  Logger.log("Presupuesto con Totales ARS/USD generado: " + doc.getUrl());
  return doc.getUrl();
}
