/**
 * Script de Automatización de Google Apps Script para Google Docs
 * Generador Automático del Acuerdo de Corretaje BESANA - ERV (2026) Corregido
 * 
 * INSTRUCCIONES DE USO EN GOOGLE DRIVE (inventario.energycpy@gmail.com):
 * 
 * OPCIÓN 1 (Carga Directa .docx - RECOMENDADA Y MÁS RÁPIDA):
 * 1. Abrir Google Drive (https://drive.google.com) con la cuenta inventario.energycpy@gmail.com.
 * 2. Hacer clic en "+ Nuevo" > "Subir archivo".
 * 3. Seleccionar el archivo "BESANA - ERV - Broker de Fondos de inversion - Acuerdo de Corretaje - Brokerage Agreement - ENERGY CPY - 2026 (ACTUALIZADO).docx" generado en la carpeta Descargas.
 * 4. Hacer doble clic sobre el archivo subido: Google Drive lo abrirá de forma nativa como un Google Doc 100% editable con formato preservado.
 * 
 * OPCIÓN 2 (Generador por Código mediante Google Apps Script):
 * 1. Crear un documento en blanco en Google Docs.
 * 2. Ir al menú superior "Extensiones" > "Apps Script".
 * 3. Borrar el código por defecto, pegar todo el contenido de este archivo y presionar el icono "Guardar".
 * 4. Hacer clic en "Ejecutar" (botón de Play) y conceder los permisos solicitados.
 * 5. Se creará automáticamente un nuevo documento denominado "BESANA - ERV - Broker de Fondos de inversion - Acuerdo de Corretaje - Brokerage Agreement - ENERGY CPY - 2026 (ACTUALIZADO)" en la raíz de su Google Drive.
 */

function crearDocumentoGoogleDocsBesana() {
  var docName = "BESANA - ERV - Broker de Fondos de inversion - Acuerdo de Corretaje - Brokerage Agreement - ENERGY CPY - 2026 (ACTUALIZADO)";
  var doc = DocumentApp.create(docName);
  var body = doc.getBody();
  body.clear();

  // Estilos de texto
  var styleHeader = {};
  styleHeader[DocumentApp.Attribute.FONT_FAMILY] = 'Calibri';
  styleHeader[DocumentApp.Attribute.FONT_SIZE] = 16;
  styleHeader[DocumentApp.Attribute.BOLD] = true;
  styleHeader[DocumentApp.Attribute.FOREGROUND_COLOR] = '#0F172A';

  var styleSubHeader = {};
  styleSubHeader[DocumentApp.Attribute.FONT_FAMILY] = 'Calibri';
  styleSubHeader[DocumentApp.Attribute.FONT_SIZE] = 12;
  styleSubHeader[DocumentApp.Attribute.BOLD] = true;
  styleSubHeader[DocumentApp.Attribute.FOREGROUND_COLOR] = '#334155';

  var styleSection = {};
  styleSection[DocumentApp.Attribute.FONT_FAMILY] = 'Calibri';
  styleSection[DocumentApp.Attribute.FONT_SIZE] = 12;
  styleSection[DocumentApp.Attribute.BOLD] = true;
  styleSection[DocumentApp.Attribute.FOREGROUND_COLOR] = '#1E3A8A';

  var styleBody = {};
  styleBody[DocumentApp.Attribute.FONT_FAMILY] = 'Calibri';
  styleBody[DocumentApp.Attribute.FONT_SIZE] = 11;
  styleBody[DocumentApp.Attribute.FOREGROUND_COLOR] = '#1F2937';

  // Título Principal
  var p1 = body.appendParagraph("ACUERDO DE CONFIDENCIALIDAD Y COLABORACIÓN ENTRE INTERMEDIARIOS");
  p1.setAttributes(styleHeader);
  p1.setAlignment(DocumentApp.HorizontalAlignment.CENTER);

  var p2 = body.appendParagraph("NON-DISCLOSURE AND INTERMEDIARY COLLABORATION AGREEMENT\n");
  p2.setAttributes(styleSubHeader);
  p2.setAlignment(DocumentApp.HorizontalAlignment.CENTER);

  // Sección I
  var sec1 = body.appendParagraph("I. PRESENTACIÓN / PREAMBLE");
  sec1.setAttributes(styleSection);

  body.appendParagraph("ESPAÑOL").setBold(true);
  body.appendParagraph("El presente Acuerdo de Confidencialidad y Colaboración entre Intermediarios (en adelante, el “Acuerdo”) se celebra con el objeto de establecer los términos y condiciones bajo los cuales las Partes colaborarán en la identificación, estructuración, presentación y cierre de oportunidades de inversión, incluyendo la intermediación entre proyectos y fondos de inversión, resguardando la confidencialidad de la información compartida y definiendo los derechos económicos derivados de dicha colaboración.\nLas Partes reconocen que actuarán de manera conjunta en el desarrollo de oportunidades aportando cada una su red de contactos, capacidades técnicas y comerciales.").setAttributes(styleBody);

  body.appendParagraph("ENGLISH").setBold(true);
  body.appendParagraph("This Non-Disclosure and Intermediary Collaboration Agreement (hereinafter, the “Agreement”) is entered into for the purpose of establishing the terms and conditions under which the Parties shall collaborate in the identification, structuring, presentation, and closing of investment opportunities, including intermediation between projects and investment funds, while safeguarding the confidentiality of shared information and defining the economic rights arising from such collaboration.\nThe Parties acknowledge that they will jointly participate in the development of opportunities, each contributing its network, technical expertise, and commercial capabilities.\n").setAttributes(styleBody);

  // Cláusula 1 - Partes
  var c1 = body.appendParagraph("CLÁUSULA 1 – PARTES / CLAUSE 1 – PARTIES");
  c1.setAttributes(styleSection);

  body.appendParagraph("ESPAÑOL").setBold(true);
  body.appendParagraph("El presente Acuerdo se celebra entre las siguientes partes:").setAttributes(styleBody);
  body.appendParagraph("1.1. CONSULTOR ARGENTINO: Representado de manera exclusiva por:\nDIAZ JAVIER IGNACIO, pasaporte N° AAM207115, con domicilio en Rodriguez Peña 442, ciudad de Córdoba, Provincia de Córdoba, República Argentina, dirección de correo electrónico: areasostenible.consultorespyme@gmail.com; denominándose en adelante como el “Consultor Argentino”; y").setAttributes(styleBody);

  body.appendParagraph("1.2. BROKER: Conformado conjuntamente por dos equipos de trabajo:").setAttributes(styleBody);
  body.appendParagraph("• Primer equipo consultor, liderado por:\n  A) Hugo Fabian Besana, DNI N° 21.732.221, domicilio en Velzquez 10 - Urbanizacion El Vicario - CP 29610, ciudad de Malaga, Provincia de Andalucía del País de España, correo: hugo.besana70@gmail.com;").setAttributes(styleBody);
  body.appendParagraph("• Segundo equipo consultor, liderado por ADRIAN ALEJANDRO MARTINEZ y compuesto por:\n  B.1) ADRIAN ALEJANDRO MARTINEZ, DNI/CUIL N.º 20-25069766-0, domicilio BELGRANO 1822 BLOK B DPT 6, SALTA, Argentina, correo: alemati11@hotmail.com;\n  B.2) MARIANO GABRIEL CEBALLO, DNI/CUIL N.º 20-25406261-9, domicilio ONAS 1617, RADA TILLY, Argentina, correo: mariano.17.ceballo@gmail.com;\n  B.3) CARLOS HECTOR FOLLONI, DNI/CUIL N.º 20-28259750-1, domicilio RUTA NAC. 51km S/N, SALTA, Argentina, correo: cfolloni@gmail.com; y\n  B.4) ROQUE DANUEL PEDROZA, DNI/CUIL N.º 20-25885480-3, domicilio EL PRADO- LOTE 227, SALTA, Argentina, correo: roquedpf16@gmail.com;\ndenominándose todos ellos en conjunto e indistintamente en adelante como el “Broker”.\n").setAttributes(styleBody);

  body.appendParagraph("ENGLISH").setBold(true);
  body.appendParagraph("This Agreement is entered into by and between the following parties:").setAttributes(styleBody);
  body.appendParagraph("1.1. ARGENTINE CONSULTANT: Represented exclusively by:\nDIAZ JAVIER IGNACIO, passport No. AAM207115, domiciled at Rodriguez Peña 442, city of Córdoba, Province of Córdoba, Argentine Republic, email address: areasostenible.consultorespyme@gmail.com; hereinafter referred to as the “Argentine Consultant”; and").setAttributes(styleBody);
  body.appendParagraph("1.2. BROKER: Jointly comprised of two work teams:").setAttributes(styleBody);
  body.appendParagraph("• First consulting team, led by:\n  A) Hugo Fabian Besana, DNI No. 21.732.221, domiciled at Velzquez 10 - Urbanizacion El Vicario - CP 29610, city of Malaga, Province of Andalusia, Spain, email: hugo.besana70@gmail.com;").setAttributes(styleBody);
  body.appendParagraph("• Second consulting team, led by ADRIAN ALEJANDRO MARTINEZ and composed of:\n  B.1) ADRIAN ALEJANDRO MARTINEZ, DNI/CUIL No. 20-25069766-0, BELGRANO 1822 BLOK B DPT 6, SALTA, Argentina, email: alemati11@hotmail.com;\n  B.2) MARIANO GABRIEL CEBALLO, DNI/CUIL No. 20-25406261-9, ONAS 1617, RADA TILLY, Argentina, email: mariano.17.ceballo@gmail.com;\n  B.3) CARLOS HECTOR FOLLONI, DNI/CUIL No. 20-28259750-1, RUTA NAC. 51km S/N, SALTA, Argentina, email: cfolloni@gmail.com; and\n  B.4) ROQUE DANUEL PEDROZA, DNI/CUIL No. 20-25885480-3, EL PRADO- LOTE 227, SALTA, Argentina, email: roquedpf16@gmail.com;\nall of them collectively and indistinctly referred to hereinafter as the “Broker”.\n").setAttributes(styleBody);

  // Cláusula 4 - Honorarios y Comisiones
  var c4 = body.appendParagraph("CLÁUSULA 4 – HONORARIOS Y COMISIONES / CLAUSE 4 – FEES AND COMMISSIONS");
  c4.setAttributes(styleSection);

  body.appendParagraph("ESPAÑOL").setBold(true);
  body.appendParagraph("De manera general, para todos los demás casos, en caso de concretarse una operación de inversión derivada de la colaboración establecida en el presente Acuerdo, se aplicará la siguiente estructura de honorarios:").setAttributes(styleBody);
  body.appendParagraph("1. Se establecerá una comisión total del cinco por ciento (5%) sobre el monto total efectivamente invertido en cada operación (la “Comisión Total”).\n2. Dicha Comisión Total corresponderá al conjunto del equipo de intermediación involucrado.\n3. La Comisión Total se dividirá en dos partes iguales (cincuenta por ciento o 50% para cada parte) entre las siguientes dos partes:\n   i. Un cincuenta por ciento (50%) para el Consultor Argentino, representado de manera exclusiva por DIAZ JAVIER IGNACIO; y\n   ii. Un cincuenta por ciento (50%) para la parte denominada el “Broker”, conformada conjuntamente por el Primer equipo consultor (Hugo Fabian Besana) y el Segundo equipo consultor (liderado por ADRIAN ALEJANDRO MARTINEZ e integrado por MARIANO GABRIEL CEBALLO, CARLOS HECTOR FOLLONI y ROQUE DANUEL PEDROZA).\n4. El pago de las comisiones estará sujeto a la efectiva recepción de los fondos y trazabilidad.\n5. Las Partes podrán suscribir acuerdos complementarios (deal-by-deal).\n").setAttributes(styleBody);

  body.appendParagraph("ENGLISH").setBold(true);
  body.appendParagraph("Generally, for all other cases, should an investment transaction be concluded as a result of the collaboration established in this Agreement, the following fee structure shall apply:").setAttributes(styleBody);
  body.appendParagraph("1. A total commission of five percent (5%) shall be applied to the total amount effectively invested in each transaction (the “Total Commission”).\n2. The Total Commission shall correspond to the entire intermediation team involved.\n3. The Total Commission shall be divided in two equal parts (fifty percent or 50% for each party) between the following two parties:\n   i. Fifty percent (50%) for the Argentine Consultant, represented exclusively by DIAZ JAVIER IGNACIO; and\n   ii. Fifty percent (50%) for the party designated as the “Broker”, jointly comprised of the First consulting team (Hugo Fabian Besana) and the Second consulting team (led by ADRIAN ALEJANDRO MARTINEZ and composed of MARIANO GABRIEL CEBALLO, CARLOS HECTOR FOLLONI, and ROQUE DANUEL PEDROZA).\n4. Payment of commissions shall be subject to effective receipt of funds and traceability.\n5. The Parties may sign supplementary agreements (deal-by-deal).\n").setAttributes(styleBody);

  // Cláusula 10 - Canales Oficiales
  var c10 = body.appendParagraph("CLÁUSULA 10 – COMUNICACIONES Y CANALES OFICIALES / CLAUSE 10 – OFFICIAL CHANNELS");
  c10.setAttributes(styleSection);
  body.appendParagraph("• Consultor Argentino (Diaz Javier Ignacio): areasostenible.consultorespyme@gmail.com\n• Broker (Besana & Martinez Team): hugo.besana70@gmail.com, alemati11@hotmail.com, mariano.17.ceballo@gmail.com, cfolloni@gmail.com, roquedpf16@gmail.com\n").setAttributes(styleBody);

  // Cláusula 12 - Firmas
  var c12 = body.appendParagraph("CLÁUSULA 12 – FIRMAS / CLAUSE 12 – SIGNATURES");
  c12.setAttributes(styleSection);
  body.appendParagraph("EN PRUEBA DE CONFORMIDAD, las Partes firman el presente Acuerdo / IN WITNESS WHEREOF, the Parties have executed this Agreement:\n").setAttributes(styleBody);

  body.appendParagraph("CONSULTOR ARGENTINO / ARGENTINE CONSULTANT").setBold(true);
  body.appendParagraph("DIAZ JAVIER IGNACIO (Pasaporte N°: AAM207115)\nFirma: _________________________\nFecha: _________________________\n").setAttributes(styleBody);

  body.appendParagraph("BROKER").setBold(true);
  body.appendParagraph("PRIMER EQUIPO CONSULTOR:\nHugo Fabian Besana (DNI N°: 21.732.221)\nFirma: _________________________\n\nSEGUNDO EQUIPO CONSULTOR:\n• ADRIAN ALEJANDRO MARTINEZ (DNI/CUIL: 20-25069766-0)\n• MARIANO GABRIEL CEBALLO (DNI/CUIL: 20-25406261-9)\n• CARLOS HECTOR FOLLONI (DNI/CUIL: 20-28259750-1)\n• ROQUE DANUEL PEDROZA (DNI/CUIL: 20-25885480-3)").setAttributes(styleBody);

  Logger.log("Documento Google Docs creado exitosamente: " + doc.getUrl());
}
