/* ==========================================================================
   Main JavaScript Logic — Energy CPY Investment Showroom 2026
   ========================================================================== */

// Official Consultant Data (Internal Emails & WhatsApp Direct)
const CONSULTANTS = {
    javier: {
        id: "javier",
        name: "Javier Ignacio Diaz",
        role_es: "Consultor Capital Introducer & Finder",
        role_en: "Capital Introducer & Finder Consultant",
        specialties_es: "Minería, Energía Renovable, Proyectos de Ingeniería y Proyectos en Inglés",
        specialties_en: "Mining, Renewable Energy, Engineering Projects & English Language Deals",
        phone: "+54 9 351 2064791",
        phoneClean: "5493512064791",
        whatsappLink: "https://wa.me/5493512064791",
        internalEmail: "areasostenible.consultorespyme@gmail.com"
    },
    daniel: {
        id: "daniel",
        name: "Daniel Gonzalez",
        role_es: "Consultor Capital Introducer & Finder",
        role_en: "Capital Introducer & Finder Consultant",
        specialties_es: "Hotelería, Pesca, Petróleo, TRUST Real Estate, REIT, Renta Corporativa y Asesoramiento Financiero",
        specialties_en: "Hospitality, Fisheries, Oil & Gas, TRUST Real Estate, REIT, Corporate Yield & Financial Advisory",
        phone: "+54 9 2974 23-3028",
        phoneClean: "5492974233028",
        whatsappLink: "https://wa.me/5492974233028",
        internalEmail: "gonzalezmarcelo2105ypf@gmail.com"
    }
};

// Authorized Consultant Emails for Admin Access
const AUTHORIZED_ADMIN_EMAILS = [
    "areasostenible.consultorespyme@gmail.com",
    "gonzalezmarcelo2105ypf@gmail.com",
    "inventario.energycpy@gmail.com"
];

// Project Master Database
const PROJECTS_DATA = {
    "solar-cuatro-vientos": {
        "id": "solar-cuatro-vientos",
        "category": "energia",
        "sector": "Energía Solar & Renovable",
        "assignedAgent": "javier",
        "amountUSD": 300.0,
        "basePrice": 300000000,
        "overpriceTarget": 15000000,
        "currency": "USD",
        "amountDisplay": "USD 300M",
        "defaultStatus": "activo",
        "modality": "Socio Inversor",
        "roi": "7 Años",
        "statusProgress": "Ingeniería avanzada y estudios de red listos para PPA MATER/CAMMESA",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 13,
        "slidePrefix": "assets/slides/Inversión_en_Plantas_Solares_en_Argentina_2026_page_",
        "es": {
            "categoryTag": "Energía Solar Fotovoltaica",
            "title": "Parque Solar Sol de los Cuatro Vientos 300 MW",
            "location": "Mendoza, Argentina",
            "statusLabel": "USD 300M — Socio Inversor",
            "description": "Desarrollo solar fotovoltaico de gran escala (300 MW) en zona de radiación solar excepcional en Mendoza. Estructuración orientada a contratos PPA a largo plazo indexados en USD bajo el marco MATER / CAMMESA.",
            "thesis": "Proyecto utility-scale con factor de planta líder en el cono sur, nodo de evacuación en alta tensión reservado y modelo de sindicación para socio inversor de primer nivel.",
            "highlights": [
                "300 MW de potencia nominal con factor de capacidad líder mundial en Cuyo.",
                "Estructuración de contratos PPA indexados en USD a 15-20 años bajo marco MATER/CAMMESA.",
                "Búsqueda de socio inversor / equity partner con entrada estratégica y gobierno compartido.",
                "Prioridad de despacho y estudios de interconexión eléctrica en etapa avanzada.",
                "Elegible para beneficios fiscales y cambiarios bajo el régimen RIGI (Ley 27.742)."
            ],
            "metrics": [
                {
                    "label": "Inversión Final",
                    "val": "USD 300M",
                    "color": "text-gold"
                },
                {
                    "label": "Potencia Nominal",
                    "val": "300 MW",
                    "color": "text-cyan"
                },
                {
                    "label": "ROI Estimado",
                    "val": "7 Años",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "Socio Inversor",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Fuerte demanda de contratos PPA entre grandes usuarios industriales (MATER) que buscan descarbonización y cobertura tarifaria ante la quita de subsidios nacionales. El nodo de Cuyo cuenta con el factor de capacidad solar líder del país.",
                "intl": "Creciente asignación de capital por fondos de inversión globales hacia activos solares utility-scale en economías emergentes con marcos de estabilidad fiscal como el RIGI."
            }
        },
        "en": {
            "categoryTag": "Solar PV Energy",
            "title": "Sol de los Cuatro Vientos 300 MW Solar Park",
            "location": "Mendoza, Argentina",
            "statusLabel": "USD 300M — Equity Partner",
            "description": "Large-scale utility solar PV development (300 MW) located in Mendoza's premier solar irradiance belt. Designed for long-term USD-indexed PPAs under the MATER / CAMMESA framework.",
            "thesis": "World-class capacity factor, high-voltage grid interconnection in advanced permitting, and strategic co-equity structure for institutional investors.",
            "highlights": [
                "300 MW nominal capacity in Cuyo's premier solar corridor.",
                "USD-denominated 15-20 year PPA structure (MATER / CAMMESA).",
                "Equity partnership model with attractive risk-adjusted IRR.",
                "Interconnection priority and advanced environmental clearance.",
                "Eligible for RIGI investment incentive regime."
            ],
            "metrics": [
                {
                    "label": "Final Ticket",
                    "val": "USD 300M",
                    "color": "text-gold"
                },
                {
                    "label": "Nominal Power",
                    "val": "300 MW",
                    "color": "text-cyan"
                },
                {
                    "label": "Estimated ROI",
                    "val": "7 Years",
                    "color": "text-green"
                },
                {
                    "label": "Deal Type",
                    "val": "Equity Partner",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "High demand for private corporate PPAs (MATER) driven by industrial decarbonization and utility tariff normalization in Argentina. Cuyo grid node offers peak solar irradiance.",
                "intl": "Expanding institutional capital allocation towards utility-scale solar assets in emerging markets under long-term USD contracts and tax stability frameworks."
            }
        },
        "dealType": "Socio Inversor",
        "tir": "18.5%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 26.5M/año (Margen 78%)",
        "capitalStructure": "Socio Inversor / Project Finance (70/30)",
        "regulatoryRegime": "Régimen RIGI (Ley 27.742) & PPA MATER (Res. 281/CAMMESA)",
        "financialNote_es": "Cálculo de TIR: Modelado DCF a 20 años con WACC 9.0% en USD y factor de planta del 31.5% en Mendoza. Supera holgadamente el TIR > 15%.",
        "financialNote_en": "IRR Methodology: 20-year DCF model with 9.0% USD WACC and 31.5% capacity factor in Mendoza. Comfortably exceeds the IRR > 15%."
    },
    "solar-vaca-muerta": {
        "id": "solar-vaca-muerta",
        "category": "energia",
        "sector": "Energía Solar & Renovable",
        "assignedAgent": "javier",
        "amountUSD": 30.0,
        "basePrice": 30000000,
        "overpriceTarget": 2000000,
        "currency": "USD",
        "amountDisplay": "USD 30M",
        "defaultStatus": "activo",
        "modality": "Socio Inversor",
        "roi": "5 Años",
        "statusProgress": "Proyecto ejecutivo orientado a offtakers industriales de hidrocarburos en Añelo",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 13,
        "slidePrefix": "assets/slides/Inversión_en_Plantas_Solares_en_Argentina_2026_page_",
        "es": {
            "categoryTag": "Energía Solar & O&G",
            "title": "Parque Solar 30 MW Vaca Muerta",
            "location": "Añelo, Neuquén, Argentina",
            "statusLabel": "USD 30M — Socio Inversor",
            "description": "Planta fotovoltaica de 30 MW emplazada en el corazón de la formación no convencional Vaca Muerta. Provisión directa de energía limpia y descarbonización para operaciones de operadoras petroleras y de servicios.",
            "thesis": "Generación distribuida de alta demanda en boca de yacimiento, reemplazando costosa generación térmica diésel con PPA industrial privado en USD y payback acelerado a 5 años.",
            "highlights": [
                "30 MW dedicados al suministro de energía renovable en Añelo / Vaca Muerta.",
                "Offtakers corporativos de primer nivel en el sector de petróleo y gas.",
                "Retorno de inversión acelerado en 5 años por alta competitividad frente al diésel.",
                "Reducción directa de emisiones de Alcance 2 para metas ESG de operadoras.",
                "Opción de ampliación modular por etapas sucesivas."
            ],
            "metrics": [
                {
                    "label": "Inversión Final",
                    "val": "USD 30M",
                    "color": "text-gold"
                },
                {
                    "label": "Potencia",
                    "val": "30 MW",
                    "color": "text-cyan"
                },
                {
                    "label": "ROI Estimado",
                    "val": "5 Años",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "Socio Inversor",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Las operadoras en Vaca Muerta precisan descarbonizar operaciones upstream y reemplazar costosa generación diésel en boca de pozo por energía solar fotovoltaica con amortización acelerada.",
                "intl": "Los compromisos internacionales Net-Zero de las petroleras globales impulsan la electrificación limpia de campos no convencionales para reducir la huella de carbono del crudo Medanito."
            }
        },
        "en": {
            "categoryTag": "Solar & O&G Decarbonization",
            "title": "30 MW Vaca Muerta Solar Park",
            "location": "Añelo, Neuquén, Argentina",
            "statusLabel": "USD 30M — Equity Partner",
            "description": "30 MW PV solar plant strategically positioned in Añelo, the core of Vaca Muerta shale play. Direct clean power supply to O&G operators replacing diesel generation.",
            "thesis": "Fast 5-year payback backed by private industrial USD offtake agreements and critical ESG impact for shale drilling clusters.",
            "highlights": [
                "30 MW dedicated to Vaca Muerta oilfield operations.",
                "Direct industrial USD PPA with tier-1 O&G operators.",
                "Accelerated 5-year payback substituting expensive diesel power.",
                "Direct Scope 2 carbon footprint abatement.",
                "Modular scalable architecture."
            ],
            "metrics": [
                {
                    "label": "Final Ticket",
                    "val": "USD 30M",
                    "color": "text-gold"
                },
                {
                    "label": "Capacity",
                    "val": "30 MW",
                    "color": "text-cyan"
                },
                {
                    "label": "Est. ROI",
                    "val": "5 Years",
                    "color": "text-green"
                },
                {
                    "label": "Deal Type",
                    "val": "Equity Partner",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Upstream operators in Vaca Muerta urgently replacing expensive diesel generation with low-cost on-site solar power to reduce lifting costs.",
                "intl": "Global oil majors prioritizing clean field electrification to meet international Scope 1 emissions targets and lower crude carbon intensity."
            }
        },
        "dealType": "Socio Inversor",
        "tir": "22.0%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 3.8M/año (Margen 74%)",
        "capitalStructure": "Socio Inversor / Equity Directo",
        "regulatoryRegime": "PPA Privado B2B con Operadoras Petroleras en Boca de Pozo",
        "financialNote_es": "Cálculo de TIR: Modelado a 15 años sustituyendo generación térmica diésel en cuenca con tarifa dolarizada. Supera ampliamente la TIR > 15%.",
        "financialNote_en": "IRR Methodology: 15-year DCF displacing diesel generation with USD dollarized off-take price. Strongly exceeds the IRR > 15%."
    },
    "solar": {
        "id": "solar",
        "category": "energia",
        "sector": "Energía Solar & Renovable",
        "assignedAgent": "javier",
        "amountUSD": 50.0,
        "basePrice": 50000000,
        "overpriceTarget": 2500000,
        "currency": "USD",
        "amountDisplay": "USD 50M (50% Pre-Financiado)",
        "defaultStatus": "activo",
        "modality": "EPC Llave en Mano",
        "roi": "6 Años",
        "statusProgress": "Ready to Build con co-financiamiento asegurado por fabricante Tier 1",
        "isPrivatePlacement": false,
        "pdfPath": "assets/docs/plantas_solares_2026.pdf",
        "totalSlides": 13,
        "slidePrefix": "assets/slides/Inversión_en_Plantas_Solares_en_Argentina_2026_page_",
        "coverImage": "assets/slides/Inversión_en_Plantas_Solares_en_Argentina_2026_page_1.png",
        "es": {
            "categoryTag": "Energía Solar Fotovoltaica",
            "title": "Plantas Solares Llave en Mano con Financiamiento Asegurado",
            "location": "Cuyo y NOA, Argentina",
            "statusLabel": "Co-Financiado 50% CAPEX",
            "description": "Desarrollo estratégico de parques fotovoltaicos llave en mano con el 50% del CAPEX pre-financiado por fabricante líder global de paneles e inversores. Contratos PPA a 15-20 años indexados al USD.",
            "thesis": "Estructura de co-inversión que minimiza el capital inicial y maximiza la TIR mediante financiamiento directo del proveedor tecnológico internacional.",
            "highlights": [
                "50% del CAPEX pre-financiado directamente por fabricante global.",
                "Contratos PPA indexados al Dólar estadounidense a 15-20 años.",
                "Recurso solar excepcional en Cuyo y NOA con factor líder.",
                "Contrato EPC llave en mano con costos y plazos cerrados y garantizados.",
                "Garantía de rendimiento y mantenimiento integral bajo contratos O&M."
            ],
            "metrics": [
                {
                    "label": "Co-Financiamiento",
                    "val": "50% CAPEX",
                    "color": "text-gold"
                },
                {
                    "label": "Plazo PPA",
                    "val": "15 - 20 Años",
                    "color": "text-cyan"
                },
                {
                    "label": "Mercado",
                    "val": "MATER / CAMMESA",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "EPC Llave en Mano",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Modelo de co-inversión EPC llave en mano con pre-financiamiento del 50% de fábrica, superando la principal barrera crediticia local y acelerando la puesta en marcha.",
                "intl": "Alianzas directas con fabricantes globales Tier-1 de módulos e inversores garantizan precios de equipamiento altamente competitivos y garantías extendidas a 25 años."
            }
        },
        "en": {
            "categoryTag": "Photovoltaic Solar Energy",
            "title": "Turnkey Solar Plants with Secured Co-Financing",
            "location": "Cuyo & NOA Regions, Argentina",
            "statusLabel": "50% Co-Financed CAPEX",
            "description": "Strategic turnkey solar park developments with 50% of CAPEX pre-financed by a world-leading PV manufacturer. Long-term PPA contracts (15 to 20 years) indexed to USD.",
            "thesis": "Co-investment architecture minimizing upfront equity and maximizing equity IRR through vendor financing.",
            "highlights": [
                "50% of CAPEX pre-financed directly by top-tier global manufacturer.",
                "USD-indexed PPA contracts with 15 to 20 years duration.",
                "Exceptional solar irradiance in Cuyo & NOA regions.",
                "Turnkey EPC agreement with guaranteed fixed cost.",
                "Guaranteed performance metrics and preventative O&M."
            ],
            "metrics": [
                {
                    "label": "Co-Financing",
                    "val": "50% CAPEX",
                    "color": "text-gold"
                },
                {
                    "label": "PPA Term",
                    "val": "15 - 20 Yrs USD",
                    "color": "text-cyan"
                },
                {
                    "label": "Target Market",
                    "val": "MATER / CAMMESA",
                    "color": "text-green"
                },
                {
                    "label": "Delivery",
                    "val": "Turnkey EPC",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Turnkey EPC co-investment model with 50% vendor pre-financing overcoming capital barriers and accelerating COD in Argentina.",
                "intl": "Direct strategic supply agreements with global Tier-1 PV manufacturers securing volume-discounted hardware and 25-year performance warranties."
            }
        },
        "dealType": "Venta / Socio Inversor",
        "tir": "24.0%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 6.2M/año (Margen 70%)",
        "capitalStructure": "50% Pre-Financiado por Fabricante Tier-1 / 50% Equity",
        "regulatoryRegime": "Contratos Llave en Mano EPC + Marco MATER/CAMMESA",
        "financialNote_es": "Cálculo de TIR: Estructura de co-inversión apalancada con crédito de proveedor que maximiza el retorno sobre capital propio. TIR > 15% holgadamente superada.",
        "financialNote_en": "IRR Methodology: Leveraged co-investment model with vendor credit maximizing equity IRR. Well above the IRR > 15%."
    },
    "hotel-casino-mendoza-3s": {
        "id": "hotel-casino-mendoza-3s",
        "category": "hoteleria",
        "sector": "Hotelería & Renta",
        "assignedAgent": "daniel",
        "amountUSD": 40.0,
        "basePrice": 40000000,
        "overpriceTarget": 2500000,
        "currency": "USD",
        "amountDisplay": "USD 40M",
        "defaultStatus": "activo",
        "modality": "Venta",
        "roi": "1 Año",
        "statusProgress": "Activo operativo en marcha con flujo consolidado y licencias de juego vigentes",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Hotelería & Casino",
            "title": "Hotel 3 Estrellas + Casino + Salón de Eventos",
            "location": "Mendoza, Argentina",
            "statusLabel": "USD 40M — Venta Directa",
            "description": "Complejo hotelero de 3 estrellas en funcionamiento pleno con sala de casino equipada y habilitación provincial. Cuenta con salón de eventos corporativos y sociales con alta demanda turística internacional.",
            "thesis": "Extraordinario cash flow operativo derivado del juego y turismo vitivinícola, generando un retorno de capital estimado en 1 año sobre el valor de venta del activo.",
            "highlights": [
                "Hotel de 3 estrellas operativo con sólida tasa de ocupación anual.",
                "Licencia y explotación activa de casino con alto flujo de caja en efectivo.",
                "Salón de eventos de gran capacidad para turismo MICE y convenciones.",
                "Retorno de inversión sin precedentes proyectado en 1 año.",
                "Venta del 100% del activo inmobiliario y paquete comercial sin pasivos."
            ],
            "metrics": [
                {
                    "label": "Inversión Final",
                    "val": "USD 40M",
                    "color": "text-gold"
                },
                {
                    "label": "Tipo Activo",
                    "val": "Hotel 3★ + Casino",
                    "color": "text-cyan"
                },
                {
                    "label": "ROI Estimado",
                    "val": "1 Año",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "Venta Directa",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Mendoza lidera la recepción de turismo enológico y corporativo. La licencia oficial de casino otorga un flujo de caja diario en efectivo, sumamente resistente a fluctuaciones macroeconómicas.",
                "intl": "Crecimiento sostenido del turismo internacional de Brasil, EE.UU. y Europa atraído por la enogastronomía andina de alta gama, con tarifas ADR dolarizadas."
            }
        },
        "en": {
            "categoryTag": "Hospitality & Casino",
            "title": "3-Star Hotel + Casino + Event Convention Center",
            "location": "Mendoza, Argentina",
            "statusLabel": "USD 40M — Asset Sale",
            "description": "Operational 3-star hotel complex featuring an active licensed casino hall and convention center. Strong year-round occupancy supported by Mendoza's wine and gaming tourism.",
            "thesis": "Exceptional cash flow from gaming operations delivering a projected 1-year payback on enterprise asset value.",
            "highlights": [
                "Fully operational 3-star hotel with solid occupancy history.",
                "Active gaming casino license with high daily cash flow.",
                "Large convention hall catering to corporate and social events.",
                "Unprecedented 1-year projected payback.",
                "Clean title and corporate structure with zero debt."
            ],
            "metrics": [
                {
                    "label": "Final Ticket",
                    "val": "USD 40M",
                    "color": "text-gold"
                },
                {
                    "label": "Asset Type",
                    "val": "Hotel 3★ + Casino",
                    "color": "text-cyan"
                },
                {
                    "label": "Est. ROI",
                    "val": "1 Year",
                    "color": "text-green"
                },
                {
                    "label": "Deal Type",
                    "val": "Direct Sale",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Mendoza heads regional wine and executive tourism. The official casino gaming license provides daily resilient, high-margin cash flow.",
                "intl": "Sustained international traveler influx from the Americas and Europe seeking premium wine experiences with dollarized room rates."
            }
        },
        "dealType": "Venta",
        "tir": "65.0%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 14.2M/año (Margen 42%)",
        "capitalStructure": "100% Venta de Activo y Licencia de Juego",
        "regulatoryRegime": "Concesión Provincial de Juego Oficial y Habilitación Turística",
        "financialNote_es": "Cálculo de TIR: Flujo de caja diario intensivo generado por slots, mesas de juego y hotelería enológica. Recupero en 1 año con TIR muy superior al TIR > 15%.",
        "financialNote_en": "IRR Methodology: Daily intensive cash generation from gaming floor and wine tourism hotel. 1-year payback exceeding the IRR > 15%."
    },
    "hotel-casino-mendoza-5s": {
        "id": "hotel-casino-mendoza-5s",
        "category": "hoteleria",
        "sector": "Hotelería & Renta",
        "assignedAgent": "daniel",
        "amountUSD": 60.0,
        "basePrice": 60000000,
        "overpriceTarget": 3500000,
        "currency": "USD",
        "amountDisplay": "USD 60M",
        "defaultStatus": "activo",
        "modality": "Venta",
        "roi": "1 Año",
        "statusProgress": "Hotel 5 estrellas de lujo en operación con sala de juego y cocheras",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Hotelería de Lujo & Casino",
            "title": "Hotel 5 Estrellas (72 Habitaciones) + Casino + Cocheras",
            "location": "Mendoza, Argentina",
            "statusLabel": "USD 60M — Venta Directa",
            "description": "Exclusivo hotel de 5 estrellas con 72 habitaciones de alta gama, casino privado en operación, restaurante gourmet, spa y estacionamiento subterráneo en la mejor ubicación de Mendoza.",
            "thesis": "Activo trophy de alta rentabilidad con tarifa promedio diaria (ADR) dolarizada, clientela internacional y un ROI extraordinario de 1 año traccionado por la sala de casino.",
            "highlights": [
                "72 habitaciones y suites de lujo totalmente equipadas con amenities de 5 estrellas.",
                "Casino de alta categoría en funcionamiento con licencias y equipamiento de última generación.",
                "Edificio icónico con cocheras subterráneas y salones ejecutivos.",
                "Retorno acelerado en 1 año respaldado por el flujo de caja del casino y hotelería.",
                "Operación llave en mano con personal calificado y marca consolidada."
            ],
            "metrics": [
                {
                    "label": "Inversión Final",
                    "val": "USD 60M",
                    "color": "text-gold"
                },
                {
                    "label": "Habitaciones",
                    "val": "72 Suites 5★",
                    "color": "text-cyan"
                },
                {
                    "label": "ROI Estimado",
                    "val": "1 Año",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "Venta Directa",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Activo trophy de 72 suites de ultra-lujo y complejo de juego con ocupación ejecutiva de alta gama en el polo vitivinícola más prestigioso de Sudamérica.",
                "intl": "Escasez absoluta de activos hoteleros 5 estrellas con licencia de casino habilitada en plazas turísticas consolidadas del Cono Sur."
            }
        },
        "en": {
            "categoryTag": "Luxury Hospitality & Casino",
            "title": "5-Star Hotel (72 Rooms) + Casino + Underground Parking",
            "location": "Mendoza, Argentina",
            "statusLabel": "USD 60M — Asset Sale",
            "description": "Premier 5-star boutique hotel featuring 72 luxury rooms, operational private casino, fine dining restaurant, luxury spa, and private parking in prime Mendoza.",
            "thesis": "Trophy asset with strong USD average daily rates and high-margin casino revenue driving a projected 1-year capital payback.",
            "highlights": [
                "72 luxury suites with complete 5-star amenities.",
                "High-end operational casino with modern gaming licenses.",
                "Prime architectural building with underground parking.",
                "Rapid 1-year payback backed by combined hotel and gaming cash flows.",
                "Turnkey management and established reputation."
            ],
            "metrics": [
                {
                    "label": "Final Ticket",
                    "val": "USD 60M",
                    "color": "text-gold"
                },
                {
                    "label": "Rooms",
                    "val": "72 Suites 5★",
                    "color": "text-cyan"
                },
                {
                    "label": "Est. ROI",
                    "val": "1 Year",
                    "color": "text-green"
                },
                {
                    "label": "Deal Type",
                    "val": "Direct Sale",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Trophy hospitality asset featuring 72 luxury suites and premium casino gaming in South America premier wine capital.",
                "intl": "Extreme scarcity of licensed 5-star hotel-casinos in top South American leisure and convention destination markets."
            }
        },
        "dealType": "Venta",
        "tir": "58.0%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 19.8M/año (Margen 45%)",
        "capitalStructure": "100% Venta Trophy Asset Inmobiliario + Licencia",
        "regulatoryRegime": "Licencia Exclusiva de Casino 5 Estrellas & Habilitación Internacional",
        "financialNote_es": "Cálculo de TIR: Tarifa ADR dolarizada con clientes corporativos e internacionales de alta gama. Retorno en 1 año superando ampliamente la TIR > 15%.",
        "financialNote_en": "IRR Methodology: Dollarized ADR room rates and high-end international gaming clientele. 1-year payback exceeding the IRR > 15%."
    },
    "hotel-lujo-bariloche": {
        "id": "hotel-lujo-bariloche",
        "category": "hoteleria",
        "sector": "Hotelería & Renta",
        "assignedAgent": "daniel",
        "amountUSD": 0.0,
        "basePrice": 0,
        "overpriceTarget": 0,
        "currency": "USD",
        "amountDisplay": "A Invitación Exclusiva",
        "defaultStatus": "activo",
        "modality": "Venta Exclusiva a Invitación",
        "roi": "Confidencial",
        "statusProgress": "Operación off-market estrictamente confidencial disponible solo bajo NDA firmado",
        "isPrivatePlacement": true,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Private Placement — Gran Lujo",
            "title": "Venta Exclusiva a Invitación — Hotel de Lujo en Bariloche",
            "location": "San Carlos de Bariloche, Patagonia, Argentina",
            "statusLabel": "🔒 Private Placement Off-Market",
            "description": "Emblemático hotel de ultra-lujo situado en un entorno natural privilegiado en Bariloche, Patagonia. Comercialización off-market reservada exclusivamente para inversores calificados bajo estricto acuerdo de confidencialidad (NDA).",
            "thesis": "Activo hotelero trofeo sin equivalentes en la Patagonia, con vistas directas al lago y clientela internacional de alto poder adquisitivo. Datos financieros y dossier disponibles únicamente a invitación.",
            "highlights": [
                "Venta off-market estrictamente confidencial (sin publicación de montos en web).",
                "Ubicación irrepetible con vistas panorámicas al lago y arquitectura patagónica.",
                "Instalaciones de máxima jerarquía hotelera internacional.",
                "Acceso al Data Room y estados contables supeditado a calificación previa y NDA.",
                "Acompañamiento personalizado directo con la dirección de Energy CPY."
            ],
            "metrics": [
                {
                    "label": "Modalidad",
                    "val": "Private Placement",
                    "color": "text-gold"
                },
                {
                    "label": "Categoría",
                    "val": "Ultra Lujo",
                    "color": "text-cyan"
                },
                {
                    "label": "Acceso",
                    "val": "Bajo NDA",
                    "color": "text-green"
                },
                {
                    "label": "Estado",
                    "val": "Venta Exclusiva",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Bariloche registra ocupación plena en las 4 temporadas del año, combinando esquí de clase mundial en invierno con ecoturismo y eventos náuticos en verano.",
                "intl": "Multiplicación de vuelos internacionales directos hacia la Patagonia y demanda global inelástica de viajeros High-Net-Worth por naturaleza virgen."
            }
        },
        "en": {
            "categoryTag": "Private Placement — Ultra Luxury",
            "title": "Exclusive Invitation Sale — Luxury Hotel in Bariloche",
            "location": "Bariloche, Patagonia, Argentina",
            "statusLabel": "🔒 Private Placement Off-Market",
            "description": "Iconic ultra-luxury hotel situated in a prime natural setting in Bariloche, Patagonia. Off-market transaction available exclusively to qualified investors under non-disclosure agreement (NDA).",
            "thesis": "Irreplaceable trophy asset with direct lakefront views and elite international patronage. Financial dossier available strictly upon invitation.",
            "highlights": [
                "Strictly confidential off-market sale (no public financial figures).",
                "Irreplaceable lakefront location with signature Andean architecture.",
                "Highest tier of international hospitality standards.",
                "Data room access granted exclusively following investor verification and signed NDA.",
                "Direct confidential advisory with Energy CPY executives."
            ],
            "metrics": [
                {
                    "label": "Deal Structure",
                    "val": "Private Placement",
                    "color": "text-gold"
                },
                {
                    "label": "Category",
                    "val": "Ultra Luxury",
                    "color": "text-cyan"
                },
                {
                    "label": "Access",
                    "val": "Under NDA",
                    "color": "text-green"
                },
                {
                    "label": "Status",
                    "val": "Exclusive Sale",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Bariloche records year-round prime occupancy, driven by winter ski seasons and luxury lake-district summer tourism.",
                "intl": "Expansion of direct international flights to Patagonia boosting ultra-high-net-worth foreign guest arrivals."
            }
        },
        "dealType": "Venta",
        "tir": "26.0%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 12.5M/año (Margen 38%)",
        "capitalStructure": "Venta Exclusiva a Invitación / Private Placement",
        "regulatoryRegime": "Dominio Privado Registrado con Habilitación Hotelera 5 Estrellas",
        "financialNote_es": "Cálculo de TIR: Ocupación en 4 estaciones en Bariloche con ADR promedio de USD 420/noche. TIR proyectada del 26.0% vs. TIR > 15%.",
        "financialNote_en": "IRR Methodology: 4-season prime occupancy with average USD 420 ADR. Projected 26.0% IRR vs. IRR > 15%."
    },
    "hotel-lujo-cordoba": {
        "id": "hotel-lujo-cordoba",
        "category": "hoteleria",
        "sector": "Hotelería & Renta",
        "assignedAgent": "daniel",
        "amountUSD": 0.0,
        "basePrice": 0,
        "overpriceTarget": 0,
        "currency": "USD",
        "amountDisplay": "A Invitación Exclusiva",
        "defaultStatus": "activo",
        "modality": "Venta Exclusiva a Invitación",
        "roi": "Confidencial",
        "statusProgress": "Operación off-market estrictamente confidencial disponible solo bajo NDA firmado",
        "isPrivatePlacement": true,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Private Placement — Gran Lujo",
            "title": "Venta Exclusiva a Invitación — Hotel de Lujo en Córdoba",
            "location": "Córdoba, Argentina",
            "statusLabel": "🔒 Private Placement Off-Market",
            "description": "Distinguido establecimiento hotelero de máxima jerarquía en la provincia de Córdoba. Operación off-market de colocación privada sin mención de estudios financieros públicos, orientada a grupos selectos.",
            "thesis": "Patrimonio arquitectónico e inmobiliario de primer orden con posicionamiento líder en turismo corporativo y eventos de alta gama en el centro del país.",
            "highlights": [
                "Venta off-market de colocación privada mediante invitación.",
                "Instalaciones de primer nivel para congresos internacionales y hotelería premium.",
                "Historial de ocupación y marca consolidada en la región central.",
                "Entrega de memorias económicas y técnicas supeditada a firma de NDA formal.",
                "Atención directa y reservada por parte del consultor a cargo."
            ],
            "metrics": [
                {
                    "label": "Modalidad",
                    "val": "Private Placement",
                    "color": "text-gold"
                },
                {
                    "label": "Categoría",
                    "val": "Gran Lujo",
                    "color": "text-cyan"
                },
                {
                    "label": "Acceso",
                    "val": "Bajo NDA",
                    "color": "text-green"
                },
                {
                    "label": "Estado",
                    "val": "Venta Exclusiva",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Epicentro nacional para turismo de convenciones corporativas, torneos de golf y relax en las Sierras de Córdoba, con acceso vial y aéreo federal privilegiado.",
                "intl": "Interés de grupos patrimoniales extranjeros por adquirir hoteles boutique con valor histórico y potencial de desarrollo fiduciario a largo plazo."
            }
        },
        "en": {
            "categoryTag": "Private Placement — Ultra Luxury",
            "title": "Exclusive Invitation Sale — Luxury Hotel in Córdoba",
            "location": "Córdoba, Argentina",
            "statusLabel": "🔒 Private Placement Off-Market",
            "description": "Distinguished premier luxury hotel in Córdoba province. Private placement off-market transaction without public financial figures, tailored for select institutional groups.",
            "thesis": "Prime architectural and real estate asset leading in executive tourism and major corporate conventions in Central Argentina.",
            "highlights": [
                "Private placement off-market transaction by direct invitation.",
                "State-of-the-art facilities for international conventions and luxury lodging.",
                "Proven historical occupancy and distinguished regional brand.",
                "Economic and operational disclosures released exclusively upon signed NDA.",
                "Confidential engagement directly with senior partners."
            ],
            "metrics": [
                {
                    "label": "Deal Structure",
                    "val": "Private Placement",
                    "color": "text-gold"
                },
                {
                    "label": "Category",
                    "val": "Grand Luxury",
                    "color": "text-cyan"
                },
                {
                    "label": "Access",
                    "val": "Under NDA",
                    "color": "text-green"
                },
                {
                    "label": "Status",
                    "val": "Exclusive Sale",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Central hub for corporate conventions, championship golf, and mountain leisure with federal highway and airport connections.",
                "intl": "Rising interest from cross-border family offices acquiring heritage boutique hospitality assets with capital appreciation potential."
            }
        },
        "dealType": "Venta",
        "tir": "25.5%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 6.8M/año (Margen 36%)",
        "capitalStructure": "Venta Exclusiva a Invitación / Private Placement",
        "regulatoryRegime": "Título Notarial Perfecto & Certificación Turística Provincial",
        "financialNote_es": "Cálculo de TIR: Centro de convenciones y golf resort con ingresos por eventos corporativos y escapadas de fin de semana. TIR del 25.5% frente al TIR > 15%.",
        "financialNote_en": "IRR Methodology: Convention center and golf resort with recurring corporate events cash flow. 25.5% IRR vs. IRR > 15%."
    },
    "estancia-17000ha-riego": {
        "id": "estancia-17000ha-riego",
        "category": "agro",
        "sector": "Agro, Campo & Industria",
        "assignedAgent": "javier",
        "amountUSD": 60.0,
        "basePrice": 60000000,
        "overpriceTarget": 3500000,
        "currency": "USD",
        "amountDisplay": "USD 60M",
        "defaultStatus": "activo",
        "modality": "Venta",
        "roi": "2 Años",
        "statusProgress": "Establecimiento productivo en marcha con pivotes de riego y títulos perfectos",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Agroindustria & Tierras",
            "title": "Estancia 17.000 Hectáreas con Riego en Zona Turística",
            "location": "Región Centro, Argentina",
            "statusLabel": "USD 60M — Venta",
            "description": "Extraordinario establecimiento agropecuario de 17.000 hectáreas con infraestructura completa de riego presurizado instalada. Emplazado en una comarca de alto valor paisajístico y turístico en la región centro del país.",
            "thesis": "Combinación inusual de alta productividad agrícola bajo riego con formidable plusvalía inmobiliaria y turística, permitiendo un recupero acelerado en 2 años.",
            "highlights": [
                "17.000 hectáreas con aptitud mixta y módulos de riego de alta tecnología.",
                "Ubicación privilegiada en zona turística de rápida valorización territorial.",
                "Rápido recupero proyectado a 2 años mediante cultivos intensivos y desarrollos asociados.",
                "Infraestructura completa: casco, galpones, corrales, caminos internos y electrificación.",
                "Títulos de propiedad consolidados y posesión inmediata sin pasivos."
            ],
            "metrics": [
                {
                    "label": "Inversión Final",
                    "val": "USD 60M",
                    "color": "text-gold"
                },
                {
                    "label": "Superficie",
                    "val": "17.000 Ha",
                    "color": "text-cyan"
                },
                {
                    "label": "ROI Estimado",
                    "val": "2 Años",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "Venta Directa",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "17.000 hectáreas con concesiones definitivas de riego tecnificado para nogales, olivos, vid y ganadería intensiva en corredor turístico estratégico.",
                "intl": "La seguridad alimentaria global y la apreciación de la tierra fértil con agua asegurada consolidan este activo como refugio patrimonial anti-inflacionario."
            }
        },
        "en": {
            "categoryTag": "Agribusiness & Prime Land",
            "title": "17,000-Hectare Irrigated Ranch in Prime Tourist Area",
            "location": "Central Region, Argentina",
            "statusLabel": "USD 60M — Asset Sale",
            "description": "Exceptional 17,000-hectare agricultural estate equipped with extensive pressurized irrigation infrastructure, located in a scenic and high-growth tourist corridor in Central Argentina.",
            "thesis": "Unique synergy of intensive irrigated crop yields and real estate capital appreciation offering a 2-year estimated capital return.",
            "highlights": [
                "17,000 hectares combining crop irrigation and pastoral land.",
                "Strategic setting in a fast-appreciating tourism and lifestyle zone.",
                "Rapid projected 2-year payback from high-yield crops and land upside.",
                "Full operational infrastructure: main house, sheds, power, and road network.",
                "Clear titles and immediate handover with zero encumbrances."
            ],
            "metrics": [
                {
                    "label": "Final Ticket",
                    "val": "USD 60M",
                    "color": "text-gold"
                },
                {
                    "label": "Total Area",
                    "val": "17,000 Ha",
                    "color": "text-cyan"
                },
                {
                    "label": "Est. ROI",
                    "val": "2 Years",
                    "color": "text-green"
                },
                {
                    "label": "Deal Type",
                    "val": "Direct Sale",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "17,000 hectares with permanent water rights and pivot irrigation systems suitable for intensive agriculture and livestock in prime valley.",
                "intl": "Global food security priorities cementing water-secured agricultural land as a premier long-term inflation hedge."
            }
        },
        "dealType": "Venta",
        "tir": "38.0%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 11.2M/año (Margen 52%)",
        "capitalStructure": "100% Venta de Dominio Inmobiliario con Agua Definitiva",
        "regulatoryRegime": "Derechos Concesionados de Riego Definitivo y Título Escritural",
        "financialNote_es": "Cálculo de TIR: Renta agrícola-ganadera de alta precisión bajo pivotes centrales y plusvalía de suelo productivo. TIR del 38.0% superando el umbral TIR > 15%.",
        "financialNote_en": "IRR Methodology: High-precision pivot irrigation agriculture, livestock and land appreciation. 38.0% IRR well above the IRR > 15%."
    },
    "mineria-diente-oro-verde": {
        "id": "mineria-diente-oro-verde",
        "category": "mineria",
        "sector": "Minería",
        "assignedAgent": "javier",
        "amountUSD": 60.0,
        "basePrice": 60000000,
        "overpriceTarget": 3500000,
        "currency": "USD",
        "amountDisplay": "USD 60M",
        "defaultStatus": "activo",
        "modality": "Venta",
        "roi": "Activo Minero",
        "statusProgress": "Yacimiento aurífero a certificar bajo estándar internacional NI 43-101",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Minería Metalífera — Oro",
            "title": "Yacimiento de Oro 'Diente Oro Verde'",
            "location": "San Luis, Argentina",
            "statusLabel": "USD 60M — Venta",
            "description": "Propiedad minera de oro a certificar bajo código internacional canadiense NI 43-101. Posee importantes estructuras de vetas hidrotermales con leyes superficiales y en profundidad de alto interés comercial.",
            "thesis": "Oportunidad de adquisición directa de un yacimiento aurífero en una provincia con tradición minera, ideal para empresas junior o intermedias con capacidad de exploración y cubicación.",
            "highlights": [
                "Yacimiento de oro con estudios previos y listo para certificación técnica NI 43-101.",
                "Estructuras mineralizadas continuas con potencial de explotación a cielo abierto y subterránea.",
                "Provincia con facilidades logísticas, red vial pavimentada y energía cercana.",
                "Venta del 100% de los derechos de explotación y mensura minera definitiva.",
                "Alto apalancamiento ante el ciclo alcista internacional del precio del oro."
            ],
            "metrics": [
                {
                    "label": "Inversión Final",
                    "val": "USD 60M",
                    "color": "text-gold"
                },
                {
                    "label": "Mineral",
                    "val": "Oro (Au)",
                    "color": "text-cyan"
                },
                {
                    "label": "Estándar",
                    "val": "A cert. NI 43-101",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "Venta Total",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Distrito minero histórico con régimen RIGI aplicable que otorga 30 años de estabilidad fiscal, exención arancelaria y libre disponibilidad de divisas.",
                "intl": "Cotización del oro en máximos históricos impulsada por compras masivas de bancos centrales soberanos y cobertura ante volatilidad geopolítica."
            }
        },
        "en": {
            "categoryTag": "Precious Metals — Gold",
            "title": "'Diente Oro Verde' Gold Deposit",
            "location": "San Luis, Argentina",
            "statusLabel": "USD 60M — Asset Sale",
            "description": "High-potential gold deposit prepared for international technical certification under NI 43-101 standard. Contains extensive hydrothermal vein structures with attractive grades.",
            "thesis": "Direct acquisition opportunity of a promising gold concession in a mining-friendly jurisdiction, perfectly positioned for junior or mid-tier exploration firms.",
            "highlights": [
                "Gold deposit ready for NI 43-101 technical report certification.",
                "Continuous mineralized structures suitable for open-pit and underground methods.",
                "Excellent regional infrastructure, paved access, and nearby grid power.",
                "100% ownership sale of granted mining concessions and survey titles.",
                "Direct exposure to the historic secular bull market in precious metals."
            ],
            "metrics": [
                {
                    "label": "Final Ticket",
                    "val": "USD 60M",
                    "color": "text-gold"
                },
                {
                    "label": "Commodity",
                    "val": "Gold (Au)",
                    "color": "text-cyan"
                },
                {
                    "label": "Standard",
                    "val": "NI 43-101 Path",
                    "color": "text-green"
                },
                {
                    "label": "Deal Type",
                    "val": "100% Asset Sale",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Historical mining district benefiting from Argentine RIGI framework offering 30-year tax stability and customs duty exemptions.",
                "intl": "Gold bullion prices hovering near historic records driven by central bank reserve accumulation and global currency hedging."
            }
        },
        "dealType": "Venta",
        "tir": "34.0%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 16.5M/año (Margen 62%)",
        "capitalStructure": "100% Venta de Concesión Minera Registrada",
        "regulatoryRegime": "Código de Minería de la Nación & Régimen RIGI (Ley 27.742)",
        "financialNote_es": "Cálculo de TIR: Costo de extracción All-In Sustaining Cost (AISC) de USD 1.050/oz frente a cotización internacional récord del oro. TIR del 34.0% vs. TIR > 15%.",
        "financialNote_en": "IRR Methodology: All-In Sustaining Cost (AISC) below USD 1,050/oz against peak gold prices. 34.0% IRR vs. IRR > 15%."
    },
    "mineria-marmol-san-luis": {
        "id": "mineria-marmol-san-luis",
        "category": "mineria",
        "sector": "Minería",
        "assignedAgent": "javier",
        "amountUSD": 50.0,
        "basePrice": 50000000,
        "overpriceTarget": 3000000,
        "currency": "USD",
        "amountDisplay": "USD 50M",
        "defaultStatus": "activo",
        "modality": "Venta",
        "roi": "Activo Minero",
        "statusProgress": "Canteras con reservas cubicadas de roca de aplicación ornamental y bloques",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Minería No Metalífera — Mármol",
            "title": "Canteras y Yacimiento de Mármol Ornamental",
            "location": "San Luis, Argentina",
            "statusLabel": "USD 50M — Venta",
            "description": "Depósitos masivos de mármoles y rocas de aplicación de altísima calidad estética para la industria de la construcción y revestimientos premium. Reservas cubicadas listas para corte y extracción en bloques.",
            "thesis": "Monopolio natural de variedades de mármol cotizadas en mercados de exportación (Europa, Medio Oriente y EE.UU.) con bajo costo de extracción y alto margen operativo.",
            "highlights": [
                "Yacimiento de mármol y travertino con frentes de cantera explorados y habilitados.",
                "Reservas masivas de bloques dimensionados para exportación y mercado interno.",
                "Bajo costo de explotación a cielo abierto con tecnología de corte con hilo diamantado.",
                "Títulos mineros consolidados sin litigios y permisos ambientales vigentes.",
                "Venta total del complejo extractivo por USD 50M."
            ],
            "metrics": [
                {
                    "label": "Inversión Final",
                    "val": "USD 50M",
                    "color": "text-gold"
                },
                {
                    "label": "Mineral",
                    "val": "Mármol & Travertino",
                    "color": "text-cyan"
                },
                {
                    "label": "Destino",
                    "val": "Exportación & Constr.",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "Venta Directa",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Canteras operativas de mármol y travertino con reservas comprobadas para abastecer proyectos de arquitectura corporativa y residencial de alta gama en Argentina.",
                "intl": "Demanda internacional sostenida de bloques y placas de piedra natural ornamental para desarrollos hoteleros y residenciales de lujo en EE.UU. y Europa."
            }
        },
        "en": {
            "categoryTag": "Industrial Minerals — Marble",
            "title": "Quarries & Ornamental Marble Deposit",
            "location": "San Luis, Argentina",
            "statusLabel": "USD 50M — Asset Sale",
            "description": "Extensive marble and dimensional stone deposits of superior aesthetic quality for luxury architecture and export markets. Large measured reserves ready for block quarrying.",
            "thesis": "Natural monopoly in prized marble varieties with competitive open-pit mining costs and high export margins to Europe and North America.",
            "highlights": [
                "Marble and travertine deposits with active and surveyed quarry faces.",
                "Massive measured reserves of dimensioned blocks for premium architecture.",
                "Cost-effective open-pit extraction using modern diamond-wire cutting.",
                "Clear mineral tenure with active environmental and provincial permits.",
                "Complete asset sale for USD 50M."
            ],
            "metrics": [
                {
                    "label": "Final Ticket",
                    "val": "USD 50M",
                    "color": "text-gold"
                },
                {
                    "label": "Commodity",
                    "val": "Marble & Stone",
                    "color": "text-cyan"
                },
                {
                    "label": "Target",
                    "val": "Export & Luxury",
                    "color": "text-green"
                },
                {
                    "label": "Deal Type",
                    "val": "Direct Sale",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Active marble and travertine quarries holding verified reserves supplying premium domestic commercial construction.",
                "intl": "Solid international export demand for dimensional natural stone across luxury architectural developments worldwide."
            }
        },
        "dealType": "Venta",
        "tir": "30.0%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 8.4M/año (Margen 48%)",
        "capitalStructure": "100% Venta de Canteras Activas con Planta",
        "regulatoryRegime": "Derechos Mineros Concedidos e Impacto Ambiental Aprobado",
        "financialNote_es": "Cálculo de TIR: Extracción a cielo abierto de mármol y travertino con demanda cautiva en construcción de lujo. TIR del 30.0% superando el umbral de >9%.",
        "financialNote_en": "IRR Methodology: Open-pit extraction with captive luxury architectural demand. 30.0% IRR exceeding the IRR > 15%."
    },
    "mineria-oro-san-juan": {
        "id": "mineria-oro-san-juan",
        "category": "mineria",
        "sector": "Minería",
        "assignedAgent": "javier",
        "amountUSD": 150.0,
        "basePrice": 150000000,
        "overpriceTarget": 8000000,
        "currency": "USD",
        "amountDisplay": "USD 100M - 200M",
        "defaultStatus": "activo",
        "modality": "Socio Inversor",
        "roi": "En Producción",
        "statusProgress": "Yacimiento en producción inicial (28 t/d) buscando capital para ampliación de planta",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Minería de Oro — Producción",
            "title": "Yacimiento de Oro en Producción Inicial (28 ton/día)",
            "location": "San Juan, Argentina",
            "statusLabel": "USD 100M-200M — Socio Inversor",
            "description": "Mina de oro en producción operativa inicial a razón de 28 toneladas diarias procesadas. Convocatoria a socio inversor estratégico para inyectar entre USD 100M y USD 200M para escalamiento de planta y lixiviación.",
            "thesis": "Des-riesgo técnico comprobado al encontrarse ya en explotación activa en San Juan, la provincia minera por excelencia de Argentina. Rápido incremento de rentabilidad al multiplicar la escala.",
            "highlights": [
                "Operación aurífera activa con planta de procesamiento en marcha (28 ton/día).",
                "San Juan: Jurisdicción líder en estabilidad legal e institucional para minería.",
                "Estructuración de capital (USD 100M a 200M) para ampliación de capacidad de beneficio.",
                "Flujo de caja positivo inmediato y reservas en expansión continua.",
                "Modelo de socio inversor con participación societaria y derechos de offtake de oro."
            ],
            "metrics": [
                {
                    "label": "Rango Inversión",
                    "val": "USD 100M - 200M",
                    "color": "text-gold"
                },
                {
                    "label": "Producción Actual",
                    "val": "28 Ton / Día",
                    "color": "text-cyan"
                },
                {
                    "label": "Provincia",
                    "val": "San Juan",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "Socio Inversor",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Yacimiento en etapa de producción inicial (28 ton/día) con permisos ambientales al día en San Juan, la provincia con mayor seguridad jurídica minera de Argentina.",
                "intl": "Márgenes operativos extraordinarios por la cotización del oro, atrayendo socios internacionales para escalar la capacidad de molienda y beneficio."
            }
        },
        "en": {
            "categoryTag": "Gold Mining — Operating",
            "title": "Gold Mine in Initial Production (28 tons/day)",
            "location": "San Juan, Argentina",
            "statusLabel": "USD 100M-200M — Equity Partner",
            "description": "Operating gold mine currently processing 28 tons/day. Seeking strategic equity partner to deploy USD 100M to 200M for plant expansion, milling, and leaching facilities.",
            "thesis": "De-risked operating asset in San Juan, Argentina's leading mining jurisdiction. Substantial economies of scale upon processing capacity expansion.",
            "highlights": [
                "Active gold mining operation with processing plant handling 28 tons/day.",
                "San Juan: Top-tier Argentine mining jurisdiction with solid legal backing.",
                "Capital call of USD 100M-200M to multiply milling and leaching throughput.",
                "Immediate positive operational cash flow with ongoing resource expansion.",
                "Equity partnership model with gold off-take and board participation."
            ],
            "metrics": [
                {
                    "label": "Investment Range",
                    "val": "USD 100M - 200M",
                    "color": "text-gold"
                },
                {
                    "label": "Current Output",
                    "val": "28 Tons / Day",
                    "color": "text-cyan"
                },
                {
                    "label": "Jurisdiction",
                    "val": "San Juan",
                    "color": "text-green"
                },
                {
                    "label": "Deal Type",
                    "val": "Equity Partner",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Operating mine processing 28 tons/day with approved environmental baseline in San Juan, Argentina top-rated mining jurisdiction.",
                "intl": "Extraordinary gold extraction margins driving institutional joint-venture interest to scale crushing and flotation capacity."
            }
        },
        "dealType": "Socio Inversor",
        "tir": "42.0%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 38.0M/año (Margen 65%)",
        "capitalStructure": "Socio Inversor / Capital de Expansión de Molienda",
        "regulatoryRegime": "Ley de Inversiones Mineras 24.196 & Estabilidad Fiscal San Juan",
        "financialNote_es": "Cálculo de TIR: Yacimiento operativo (28 ton/día) con ley media de 4.8 g/t Au, escalable a 100 ton/día. TIR proyectada del 42.0% superando la TIR > 15%.",
        "financialNote_en": "IRR Methodology: Operating mine (28 tpd) averaging 4.8 g/t Au, expandable to 100 tpd. 42.0% IRR well above the IRR > 15%."
    },
    "mineria-litio-catamarca": {
        "id": "mineria-litio-catamarca",
        "category": "mineria",
        "sector": "Minería",
        "assignedAgent": "javier",
        "amountUSD": 11.0,
        "basePrice": 11000000,
        "overpriceTarget": 1000000,
        "currency": "USD",
        "amountDisplay": "USD 11M",
        "defaultStatus": "activo",
        "modality": "Venta",
        "roi": "Exploración OK",
        "statusProgress": "Estudios de exploración geoquímica y geofísica concluidos con dictamen favorable",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Minería de Litio — Salmueras",
            "title": "Yacimiento de Litio — Estudios de Exploración OK",
            "location": "Catamarca, Argentina",
            "statusLabel": "USD 11M — Venta",
            "description": "Concesión minera de salmueras de litio en la puna de Catamarca (Triángulo del Litio). Campaña exploratoria inicial completada con éxito (geofísica y sondeos geoquímicos con excelentes relaciones Mg/Li).",
            "thesis": "Entrada estratégica de bajo ticket (USD 11M) en un salar de alta ley, con saneamiento legal total y listo para perforación de pozos y estimación de recursos NI 43-101.",
            "highlights": [
                "Ubicación en el epicentro mundial de salmueras de litio en Catamarca.",
                "Estudios de exploración geoeléctrica y muestreos hidroquímicos concluidos (OK).",
                "Baja relación magnesio/litio favoreciendo procesos de precipitación química directa.",
                "Título de propiedad minera perfecto y canon al día.",
                "Venta total por USD 11M, ideal para fondos de recursos naturales o desarrolladores de baterías."
            ],
            "metrics": [
                {
                    "label": "Inversión Final",
                    "val": "USD 11M",
                    "color": "text-gold"
                },
                {
                    "label": "Mineral",
                    "val": "Litio (Li)",
                    "color": "text-cyan"
                },
                {
                    "label": "Estado",
                    "val": "Exploración OK",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "Venta Directa",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Propiedad minera en el corazón del Triángulo del Litio catamarqueño con estudios hidrogeológicos favorables y reservas de salmuera de alta concentración.",
                "intl": "La revolución global de vehículos eléctricos y almacenamiento en baterías a escala de red requiere suministro estratégico garantizado de litio grado batería."
            }
        },
        "en": {
            "categoryTag": "Critical Minerals — Lithium",
            "title": "Lithium Brine Deposit — Exploration OK",
            "location": "Catamarca, Argentina",
            "statusLabel": "USD 11M — Asset Sale",
            "description": "Lithium brine mining concession located in the Catamarca Puna within the global Lithium Triangle. Preliminary exploration campaign successfully completed with favorable Mg/Li ratios.",
            "thesis": "Low-entry ticket (USD 11M) in a premium salar basin with clean legal status, ready for resource drilling and NI 43-101 resource estimation.",
            "highlights": [
                "Located in the world-class Catamarca lithium brine basin.",
                "Geophysical and hydrogeochemical exploratory studies confirmed (OK).",
                "Favorable magnesium-to-lithium ratio enabling low processing OPEX.",
                "Clear legal title with mining cadastre fees in full standing.",
                "100% asset sale for USD 11M, ideal for battery metal developers."
            ],
            "metrics": [
                {
                    "label": "Final Ticket",
                    "val": "USD 11M",
                    "color": "text-gold"
                },
                {
                    "label": "Commodity",
                    "val": "Lithium (Li)",
                    "color": "text-cyan"
                },
                {
                    "label": "Stage",
                    "val": "Exploration OK",
                    "color": "text-green"
                },
                {
                    "label": "Deal Type",
                    "val": "Direct Sale",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Prime acreage in the Catamarca Lithium Triangle with proven brine chemistry, low impurity ratios, and exploration permits.",
                "intl": "Global EV and grid battery expansion driving long-term strategic supply security for high-purity lithium carbonate."
            }
        },
        "dealType": "Venta",
        "tir": "29.0%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 5.2M/año (Exploración / Upside USD 120M)",
        "capitalStructure": "100% Venta de Propiedad Minera en Salar",
        "regulatoryRegime": "Código Minero & Acuerdos Comunitarios Catamarca OK",
        "financialNote_es": "Cálculo de TIR: Modelo de exploración avanzada con recursos inferidos de carbonato de litio grado batería. TIR proyectada del 29.0% vs. TIR > 15%.",
        "financialNote_en": "IRR Methodology: Advanced brine exploration model with battery-grade lithium carbonate reserves. 29.0% IRR vs. IRR > 15%."
    },
    "mineria-oro-san-antonio-san-juan": {
        "id": "mineria-oro-san-antonio-san-juan",
        "category": "mineria",
        "sector": "Minería",
        "assignedAgent": "javier",
        "amountUSD": 3500.0,
        "basePrice": 3500000000,
        "overpriceTarget": 50000000,
        "currency": "USD",
        "amountDisplay": "USD 3.500M (USD 3.5B)",
        "defaultStatus": "activo",
        "modality": "Venta / Socio Inversor",
        "roi": "Exploración Avanzada NI 43-101",
        "statusProgress": "Valuación estratégica de USD 3.500M (USD 3.5B) basada en potencial de 35,68M Oz Au in-situ (37 Mt @ 30 g/t Au). Venta total o socio inversor.",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Minería Metalífera — Oro & Plata",
            "title": "Proyecto Minero de Oro 'Mina San Antonio'",
            "location": "San Juan, Argentina",
            "statusLabel": "USD 3.500M (USD 3.5B) — Venta / Socio Inversor",
            "description": "Propiedad minera aurífera de gran escala (> 2.700 hectáreas, 150 pertenencias) emplazada en el prolífico cinturón aurífero andino de San Juan (Cordillera Frontal). Cuenta con informe técnico bajo estándar NI 43-101, leyes de hasta 65,7 g/t Au certificadas por laboratorio internacional con oro visible comprobado, amparo minero y canon al día, plan de inversiones aprobado por la autoridad e IIA vigente.",
            "thesis": "Oportunidad de adquisición total (USD 3.500M) o incorporación de socio inversor estratégico en un megayacimiento aurífero de clase mundial con potencial de 35,68 millones de Onzas Troy in-situ en el cinturón Veladero - Del Carmen. Valuación de USD 98/oz in-situ (3,8% del metal contenido a USD 2.600/oz) con estabilidad fiscal RIGI a 30 años.",
            "highlights": [
                "Concesión minera de 1ª categoría que consolida más de 2.700 ha (150 pertenencias). Titularidad 100% saneada bajo mandato exclusivo, libre de litigios y gravámenes.",
                "Ensayos certificados por laboratorio internacional independiente (ISO 17025) con leyes excepcionales de hasta 65,7 g/t Au y presencia de oro visible dendrítico.",
                "Cumplimiento legal pleno: Canon minero y amparo 100% al día, Plan de Inversiones (Art. 217 CM) ratificado por la autoridad minera e IIA aprobado y vigente.",
                "Emplazamiento estratégico en el cinturón aurífero andino de San Juan (Cordillera Frontal / Corredor El Indio - Veladero) con acceso logístico troncal y RIGI 30 años.",
                "Presupuesto técnico de exploración Fases 1 y 2 modelado en ~USD 1.240.000 (con 1.500m de perforación diamantina HQ) listo para ejecutar."
            ],
            "metrics": [
                {
                    "label": "Valuación Activo",
                    "val": "USD 3.500M (USD 3.5B)",
                    "color": "text-gold"
                },
                {
                    "label": "Ley Máxima",
                    "val": "65.7 g/t Au",
                    "color": "text-cyan"
                },
                {
                    "label": "Superficie",
                    "val": "> 2.700 Hectáreas",
                    "color": "text-green"
                },
                {
                    "label": "Jurisdicción",
                    "val": "San Juan (RIGI)",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "San Juan consolida su liderazgo nacional como la provincia con mayor seguridad jurídica e institucional para inversiones mineras bajo el régimen RIGI (Ley 27.742).",
                "intl": "Cotización internacional del oro en máximos históricos (> USD 2.600/oz) impulsando la reactivación de proyectos auríferos de alta ley en cinturones probados de clase mundial."
            }
        },
        "en": {
            "categoryTag": "Precious Metals — Gold & Silver",
            "title": "'San Antonio' Gold Mining Project",
            "location": "San Juan, Argentina",
            "statusLabel": "USD 3.5B (USD 3,500M) — Asset Sale / Equity Partner",
            "description": "Large-scale gold mining asset (> 2,700 hectares across 150 claims) located in San Juan's world-class Andean gold belt (Frontal Cordillera). Features NI 43-101 technical report, certified assays up to 65.7 g/t Au with confirmed visible gold, statutory mining fees in full standing, approved investment plan, and active environmental baseline.",
            "thesis": "100% asset sale (USD 3.5 Billion) or strategic joint-venture partnership in a Tier-1 world-class gold deposit boasting 35.68 million Troy Ounces of in-situ gold potential along the Veladero - Del Carmen metallogenic trend. Attractively valued at USD 98/oz in-situ (3.8% of gross contained gold at USD 2,600/oz) with 30-year RIGI investment protections.",
            "highlights": [
                "First-category mining concession consolidating over 2,700 ha (150 claims). 100% clean corporate ownership under exclusive mandate, free of liens and litigation.",
                "Assays certified by an independent international laboratory (ISO 17025) with bonanza grades up to 65.7 g/t Au and confirmed dendritic visible gold.",
                "Full statutory compliance: mining cadastre fees 100% up to date, formal Investment Plan (Mining Code Art. 217) approved, and active EIA in good standing.",
                "Strategic setting in San Juan's world-class Andean gold belt (Frontal Cordillera / El Indio - Veladero trend) with arterial logistics and 30-year RIGI stability.",
                "Phases 1 & 2 technical exploration budget modeled at ~USD 1.24M (including 1,500m of HQ diamond drilling) ready for immediate deployment."
            ],
            "metrics": [
                {
                    "label": "Asset Valuation",
                    "val": "USD 3.5B",
                    "color": "text-gold"
                },
                {
                    "label": "Top Grade",
                    "val": "65.7 g/t Au",
                    "color": "text-cyan"
                },
                {
                    "label": "Surface Area",
                    "val": "> 2,700 Hectares",
                    "color": "text-green"
                },
                {
                    "label": "Jurisdiction",
                    "val": "San Juan (RIGI)",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "San Juan reinforces its status as Argentina's premier mining jurisdiction backed by provincial stability and the Federal RIGI incentive framework (Law 27,742).",
                "intl": "Gold bullion trading near historic records (> USD 2,600/oz), catalyzing strong institutional M&A appetite for high-grade Andean deposits."
            }
        },
        "dealType": "Venta / Socio Inversor",
        "tir": "38.5%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 650M/año (Régimen Tier-1)",
        "capitalStructure": "100% Venta de Concesión Minera o Joint Venture (Earn-in exploratorio)",
        "regulatoryRegime": "Código de Minería de la Nación, Ley 24.196 & Régimen RIGI (Ley 27.742)",
        "financialNote_es": "Valuación de USD 3.500M sustentada en el potencial in-situ de 35,68M Oz Au estimadas por dictamen mineralógico sobre 37 Mt a 30 g/t Au promedio. Múltiplo de USD 98/oz in-situ en el corredor aurífero más rico de Latinoamérica. Modelo de mega-operación escalable a 500.000 Oz Au/año generando > USD 650M EBITDA/año.",
        "financialNote_en": "USD 3.5 Billion valuation underpinned by 35.68M Oz Au in-situ resource potential based on mineralogical assessment of 37 Mt at 30 g/t Au. Benchmark multiple of USD 98/oz in-situ along South America's premier gold belt. Scalable to a Tier-1 500k Oz Au/year operation generating > USD 650M EBITDA/year."
    },
    "refipampa-medanito": {
        "id": "refipampa-medanito",
        "category": "petroleo",
        "sector": "Petróleo, Gas & Infraestructura",
        "assignedAgent": "daniel",
        "amountUSD": 180.0,
        "basePrice": 180000000,
        "overpriceTarget": 10000000,
        "currency": "USD",
        "amountDisplay": "USD 180M",
        "defaultStatus": "activo",
        "modality": "Venta",
        "roi": "En Producción",
        "statusProgress": "Refinería activa 750 m³/d (proy. 3.000 m³/d), 500 pozos en Medanito y Data Room listo",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Petróleo & Refinación Integrada",
            "title": "Oferta de Refineria y explotacion de pozos - La Pampa Argentina",
            "location": "La Pampa / Cuenca Neuquina, Argentina",
            "statusLabel": "USD 180M — Venta Inmediata",
            "description": "Operación downstream y upstream integrada: refinería Refipampa procesando 750 m³/día con expansión proyectada a 3.000 m³/día y yacimiento Medanito con 500 pozos en producción activa. Data Room listo para auditoría inmediata.",
            "thesis": "Adquisición de un operador integrado con refinería propia, red de despacho y suministro asegurado de crudo liviano de Cuenca Neuquina por USD 180M.",
            "highlights": [
                "Refinería Refipampa operativa: 750 m³/día actual con proyecto a 3.000 m³/día.",
                "Yacimiento Medanito: 500 pozos productores con reservas y concesión vigente.",
                "Data Room completo y actualizado listo para Due Diligence de cierre rápido.",
                "Cadena de valor integrada desde boca de pozo hasta expendio de combustibles.",
                "Venta del paquete de control por USD 180M."
            ],
            "metrics": [
                {
                    "label": "Inversión Final",
                    "val": "USD 180M",
                    "color": "text-gold"
                },
                {
                    "label": "Refinería",
                    "val": "750 a 3.000 m³/d",
                    "color": "text-cyan"
                },
                {
                    "label": "Pozos",
                    "val": "500 Activos",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "Venta Total",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Refinería modular conectada a 500 pozos en producción activa en Cuenca Neuquina, con red de estaciones y distribución mayorista directa en el centro del país.",
                "intl": "La desregulación del mercado energético en Argentina permite fijar precios a paridad de importación en dólares, maximizando márgenes de refinación."
            }
        },
        "en": {
            "categoryTag": "Integrated Oil & Refining",
            "title": "Refinery & Well Exploitation Offer — La Pampa Argentina",
            "location": "La Pampa / Neuquina Basin, Argentina",
            "statusLabel": "USD 180M — Immediate Sale",
            "description": "Integrated upstream & downstream business: Refipampa refinery producing 750 m³/day with expansion plan to 3,000 m³/day, paired with Medanito field operating 500 producing wells. Complete Data Room ready for fast due diligence.",
            "thesis": "Turnkey acquisition of an integrated domestic energy player with dedicated refining capacity, logistics network, and secure crude supply.",
            "highlights": [
                "Refipampa operating refinery: 750 m³/day with expansion pipeline to 3,000 m³/day.",
                "Medanito oilfield: 500 active producing wells with established reserves.",
                "Fully populated and audited virtual Data Room ready for rapid closing.",
                "Integrated value chain from wellhead extraction to wholesale fuel delivery.",
                "100% controlling interest sale for USD 180M."
            ],
            "metrics": [
                {
                    "label": "Final Ticket",
                    "val": "USD 180M",
                    "color": "text-gold"
                },
                {
                    "label": "Refinery",
                    "val": "750-3,000 m³/d",
                    "color": "text-cyan"
                },
                {
                    "label": "Wells",
                    "val": "500 Active",
                    "color": "text-green"
                },
                {
                    "label": "Deal Type",
                    "val": "Direct Sale",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Fully operating modular refinery interconnected with 500 active producing wells in Neuquen Basin with private fuel retail network.",
                "intl": "Downstream deregulation in Argentina enabling full dollarized import-parity pricing and robust crack-spread margins."
            }
        },
        "dealType": "Venta",
        "tir": "33.0%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 42.0M/año (Margen 28%)",
        "capitalStructure": "100% Venta de Paquete Integral (Refinería + 500 Pozos)",
        "regulatoryRegime": "Mercado Desregulado de Combustibles & Concesiones Hidrocarburíferas",
        "financialNote_es": "Cálculo de TIR: Integración vertical upstream-downstream que captura el crack spread completo sin intermediarios. TIR del 33.0% vs. TIR > 15%.",
        "financialNote_en": "IRR Methodology: Fully integrated upstream-downstream capturing complete crack spread margin. 33.0% IRR vs. IRR > 15%."
    },
    "refinor-salta": {
        "id": "refinor-salta",
        "category": "petroleo",
        "sector": "Petróleo, Gas & Infraestructura",
        "assignedAgent": "daniel",
        "amountUSD": 50.0,
        "basePrice": 50000000,
        "overpriceTarget": 3000000,
        "currency": "USD",
        "amountDisplay": "USD 50M",
        "defaultStatus": "activo",
        "modality": "Venta",
        "roi": "En Producción",
        "statusProgress": "Refinería activa en Campo Durán con capacidad de 4.000 m³/día y red de ductos",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Downstream & Poliductos",
            "title": "Complejo de Refinación y Poliductos NOA - Salta Argentina",
            "location": "Campo Durán, Salta, Argentina",
            "statusLabel": "USD 50M — Venta",
            "description": "Refinería estratégica en Campo Durán, Salta, con capacidad de procesamiento de 4.000 m³ diarios de crudo y condensados. Red troncal de poliductos y estaciones de carga asociadas para abastecimiento del NOA.",
            "thesis": "Adquisición a valuación de distress industrial (USD 50M) con gigantesca infraestructura instalada de destilación, ductos y logística regional insustituible.",
            "highlights": [
                "Capacidad instalada de refinación de 4.000 m³/día en el norte argentino.",
                "Red troncal propia de poliductos para transporte de combustibles y GLP.",
                "Posicionamiento estratégico en la frontera de gas y petróleo con Bolivia y Chile.",
                "Facilidades de almacenamiento masivo y despacho multimodal.",
                "Venta por USD 50M con enorme potencial de sinergia de crudos livianos."
            ],
            "metrics": [
                {
                    "label": "Inversión Final",
                    "val": "USD 50M",
                    "color": "text-gold"
                },
                {
                    "label": "Capacidad",
                    "val": "4.000 m³/Día",
                    "color": "text-cyan"
                },
                {
                    "label": "Red",
                    "val": "Poliductos NOA",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "Venta Directa",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Complejo de refinación, poliductos y fraccionamiento de GLP con posición dominante de abastecimiento en 7 provincias del Noroeste Argentino.",
                "intl": "La reversión del Gasoducto Norte transforma a REFINOR en el nudo logístico indispensable para procesar y transportar gas y condensados hacia Brasil y Bolivia."
            }
        },
        "en": {
            "categoryTag": "Downstream & Pipelines",
            "title": "NOA Refinery & Pipeline Complex — Salta Argentina",
            "location": "Campo Durán, Salta, Argentina",
            "statusLabel": "USD 50M — Asset Sale",
            "description": "Strategic regional refinery in Campo Durán, Salta, with 4,000 m³/day processing capacity for crude and gas condensates. Features an extensive regional pipeline and fuel distribution network.",
            "thesis": "Opportunity to acquire critical energy infrastructure in Northern Argentina at an attractive valuation (USD 50M) with irreplaceable transport assets.",
            "highlights": [
                "Refining capacity of 4,000 m³/day in northern Argentina.",
                "Proprietary multi-product pipeline network for fuels and LPG.",
                "Strategic cross-border logistical hub near Bolivia and Chile.",
                "Extensive tank storage and multimodal rack distribution facilities.",
                "Attractive asset sale for USD 50M with major synergy upside."
            ],
            "metrics": [
                {
                    "label": "Final Ticket",
                    "val": "USD 50M",
                    "color": "text-gold"
                },
                {
                    "label": "Capacity",
                    "val": "4,000 m³/Day",
                    "color": "text-cyan"
                },
                {
                    "label": "Logistics",
                    "val": "NOA Pipelines",
                    "color": "text-green"
                },
                {
                    "label": "Deal Type",
                    "val": "Direct Sale",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "The sole refining, LPG fractionation, and pipeline complex in Northwest Argentina, commanding wholesale supply across 7 provinces.",
                "intl": "Northern Gas Pipeline reversal establishes REFINOR as the primary logistics bridge for hydrocarbon transit to Brazil."
            }
        },
        "dealType": "Venta",
        "tir": "36.0%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 18.5M/año (Margen 32%)",
        "capitalStructure": "100% Venta de Complejo de Refinación y Poliductos",
        "regulatoryRegime": "Posición Monopólica Regulada de Transporte en el NOA",
        "financialNote_es": "Cálculo de TIR: Beneficiado por la reversión del Gasoducto Norte para fraccionar gas licuado hacia Brasil. TIR del 36.0% superando holgadamente el TIR > 15%.",
        "financialNote_en": "IRR Methodology: Leveraged by Northern Pipeline reversal for NGL fractionation towards Brazil. 36.0% IRR vs. IRR > 15%."
    },
    "palermo-aike-chubut": {
        "id": "palermo-aike-chubut",
        "category": "petroleo",
        "sector": "Petróleo, Gas & Infraestructura",
        "assignedAgent": "daniel",
        "amountUSD": 200.0,
        "basePrice": 200000000,
        "overpriceTarget": 10000000,
        "currency": "USD",
        "amountDisplay": "A Estructurar con Socio",
        "defaultStatus": "activo",
        "modality": "Socio Inversor",
        "roi": "Plan No Convencional",
        "statusProgress": "Proyecto oficial integral presentado por Chubut para exploración no convencional",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Shale Oil & Gas — Palermo Aike",
            "title": "Desarrollo No Convencional Palermo Aike Chubut",
            "location": "Chubut / Cuenca Austral, Argentina",
            "statusLabel": "Socio Inversor — Plan Integral",
            "description": "Proyecto exploratorio y de desarrollo no convencional en la formación Palermo Aike, considerada la segunda mayor reserva de shale de Argentina después de Vaca Muerta. Presentado oficialmente por la provincia de Chubut.",
            "thesis": "Oportunidad pionera de ingresar en la frontera no convencional de la Patagonia sur con beneficios tributarios provinciales y elegibilidad para el régimen RIGI.",
            "highlights": [
                "Segunda roca generadora no convencional de mayor volumen de Argentina.",
                "Proyecto integral con respaldo institucional de la Gobernación de Chubut.",
                "Búsqueda de operadoras y consorcios inversores para pozos exploratorios horizontales.",
                "Infraestructura portuaria y de evacuación en el Atlántico Sur.",
                "Elegible para incentivos RIGI de libre disponibilidad de divisas."
            ],
            "metrics": [
                {
                    "label": "Formación",
                    "val": "Palermo Aike",
                    "color": "text-gold"
                },
                {
                    "label": "Recurso",
                    "val": "Shale Oil & Gas",
                    "color": "text-cyan"
                },
                {
                    "label": "Provincia",
                    "val": "Chubut",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "Socio Inversor",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "La formación shale más prometedora fuera de Vaca Muerta, con espesores netos y madurez térmica ideales para petróleo liviano y gas en la Cuenca Austral.",
                "intl": "Operadoras internacionales buscan posicionarse tempranamente en la próxima frontera no convencional de Sudamérica a una fracción del costo por acre de Texas."
            }
        },
        "en": {
            "categoryTag": "Shale Play — Palermo Aike",
            "title": "Palermo Aike Unconventional Play Chubut",
            "location": "Chubut / Austral Basin, Argentina",
            "statusLabel": "Equity Partner — Master Plan",
            "description": "Unconventional exploration and development play targeting the Palermo Aike shale formation, recognized as Argentina's second-largest shale deposit after Vaca Muerta. Officially sponsored by Chubut Province.",
            "thesis": "Pioneering entry into Argentina's newest shale frontier with strong provincial incentives and full RIGI federal investment eligibility.",
            "highlights": [
                "Second-largest unconventional shale resource in Argentina.",
                "Comprehensive development package sponsored by the Chubut Government.",
                "Seeking operating and financial partners for horizontal drilling campaign.",
                "Proximity to deepwater Atlantic export terminals.",
                "Eligible for RIGI FX deregulation and tax stability benefits."
            ],
            "metrics": [
                {
                    "label": "Formation",
                    "val": "Palermo Aike",
                    "color": "text-gold"
                },
                {
                    "label": "Resource",
                    "val": "Shale Oil & Gas",
                    "color": "text-cyan"
                },
                {
                    "label": "Province",
                    "val": "Chubut",
                    "color": "text-green"
                },
                {
                    "label": "Deal Type",
                    "val": "Equity Partner",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Argentina premier emerging shale play outside Neuquen, featuring excellent thermal maturity for light oil in the Austral Basin.",
                "intl": "International E&P firms targeting early-entry acreage in South America next shale frontier at attractive valuation multiples."
            }
        },
        "dealType": "Socio Inversor",
        "tir": "27.5%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 22.0M/año (Margen 55%)",
        "capitalStructure": "Socio Inversor / Farm-in UTE",
        "regulatoryRegime": "Concesión Provincial de Exploración No Convencional & RIGI",
        "financialNote_es": "Cálculo de TIR: Segunda reserva de shale de Argentina con costos de acceso por acre 80% menores a Neuquén. TIR del 27.5% vs. TIR > 15%.",
        "financialNote_en": "IRR Methodology: Argentina second-largest shale play with entry costs 80% below Vaca Muerta. 27.5% IRR vs. IRR > 15%."
    },
    "vacamuerta-3refinerias-puerto": {
        "id": "vacamuerta-3refinerias-puerto",
        "category": "petroleo",
        "sector": "Petróleo, Gas & Infraestructura",
        "assignedAgent": "daniel",
        "amountUSD": 350.0,
        "basePrice": 350000000,
        "overpriceTarget": 15000000,
        "currency": "USD",
        "amountDisplay": "USD 350M",
        "defaultStatus": "activo",
        "modality": "Venta Llave en Mano",
        "roi": "Reactivación 6 Meses",
        "statusProgress": "3 refinerías y Puerto Galván con título propio; puesta a punto a 6 meses",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Infraestructura & Refinación Vaca Muerta",
            "title": "Paquete 3 Refinerías en Vaca Muerta + Puerto de Aguas Profundas",
            "location": "Cuenca Neuquina & Puerto Galván (Bahía Blanca), Argentina",
            "statusLabel": "USD 350M — Venta Llave en Mano",
            "description": "Excepcional paquete accionario que incluye 3 unidades de negocio de refinación especializadas en Vaca Muerta y terminal marítima de aguas profundas con título de propiedad en Puerto Galván, Bahía Blanca. Reactivación llave en mano a 6 meses.",
            "thesis": "Infraestructura estratégica de downstream y biocombustibles acoplada a logística portuaria privada de aguas profundas, eliminando cuellos de botella en la exportación de crudo.",
            "highlights": [
                "Refinería 1: Tratamiento de crudos livianos (1.400 m³/día; almacenaje 22.000 m³).",
                "Refinería 2: Refinación de naftas, hidrotratamiento e isomerización (1.040 m³/día; almacenaje 8.000 m³).",
                "Refinería 3: Producción de biocombustibles (130 ton/día; almacenaje 2.000 ton).",
                "Puerto Galván: Con título de propiedad privado en Bahía Blanca con muelle de aguas profundas.",
                "Modalidad llave en mano con 6 meses para reactivación total y acompañamiento estratégico por USD 350M."
            ],
            "metrics": [
                {
                    "label": "Inversión Final",
                    "val": "USD 350M",
                    "color": "text-gold"
                },
                {
                    "label": "Refinerías",
                    "val": "3 Complejos",
                    "color": "text-cyan"
                },
                {
                    "label": "Puerto",
                    "val": "Propiedad Galván",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "Llave en Mano",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Paquete de 3 refinerías modulares y terminal portuaria de aguas profundas diseñada para evacuar crudo no convencional sin depender de oleoductos congestionados.",
                "intl": "La producción de Vaca Muerta superará 1 millón de barriles diarios en 2030, demandando infraestructura privada de despacho marítimo a mercados del Atlántico."
            }
        },
        "en": {
            "categoryTag": "Refining & Deepwater Port Hub",
            "title": "3 Vaca Muerta Refineries + Deepwater Port Complex",
            "location": "Neuquina Basin & Puerto Galván (Bahía Blanca), Argentina",
            "statusLabel": "USD 350M — Turnkey Asset Sale",
            "description": "Strategic equity package comprising 3 specialized refining business units in Vaca Muerta plus a private deepwater ocean terminal with freehold title in Puerto Galván, Bahía Blanca. Turnkey restart within 6 months.",
            "thesis": "Unmatched combination of midstream refining and private oceanfront port infrastructure debottlenecking export logistics for Vaca Muerta crude.",
            "highlights": [
                "Refinery 1: Light crude processing (1,400 m³/day; 22,000 m³ storage capacity).",
                "Refinery 2: Hydrotreating, reforming, and isomerization (1,040 m³/day; 8,000 m³ storage).",
                "Refinery 3: Biofuel manufacturing unit (130 tons/day; 2,000 tons storage).",
                "Deepwater Ocean Terminal: Freehold title in Puerto Galván, Bahía Blanca port.",
                "Turnkey delivery within 6 months with full engineering transition for USD 350M."
            ],
            "metrics": [
                {
                    "label": "Final Ticket",
                    "val": "USD 350M",
                    "color": "text-gold"
                },
                {
                    "label": "Refineries",
                    "val": "3 Units",
                    "color": "text-cyan"
                },
                {
                    "label": "Deepwater Port",
                    "val": "Freehold Title",
                    "color": "text-green"
                },
                {
                    "label": "Deal Type",
                    "val": "Turnkey Sale",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Strategic package of 3 modular refineries and deep-water terminal bypassing domestic pipeline bottlenecks for Vaca Muerta crude.",
                "intl": "Vaca Muerta surging towards 1M bpd by 2030, creating critical need for private offshore tanker loading to global export routes."
            }
        },
        "dealType": "Venta",
        "tir": "45.0%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 95.0M/año (Margen 34%)",
        "capitalStructure": "100% Venta Llave en Mano de Activos Portuarios y Refinación",
        "regulatoryRegime": "Habilitación Portuaria de Aguas Profundas & Régimen RIGI",
        "financialNote_es": "Cálculo de TIR: Tarifas de desahogo y exportación directa de crudo Medanito sin estrangulamiento de oleoductos. TIR del 45.0% frente al TIR > 15%.",
        "financialNote_en": "IRR Methodology: Direct offshore loading tariffs avoiding pipeline evacuation bottlenecks. 45.0% IRR well above the IRR > 15%."
    },
    "vacamuerta-operadora-15concesiones": {
        "id": "vacamuerta-operadora-15concesiones",
        "category": "petroleo",
        "sector": "Petróleo, Gas & Infraestructura",
        "assignedAgent": "daniel",
        "amountUSD": 340.0,
        "basePrice": 340000000,
        "overpriceTarget": 15000000,
        "currency": "USD",
        "amountDisplay": "USD 340M",
        "defaultStatus": "activo",
        "modality": "Socio Inversor",
        "roi": "En Producción",
        "statusProgress": "15 concesiones en 3.000 km², ~1.200 pozos, >500 empleados; inversión llave en mano",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Upstream Operadora — Vaca Muerta",
            "title": "Operadora de Pozos Petroleros en Vaca Muerta (15 Concesiones)",
            "location": "Cuenca Neuquina, Neuquén, Argentina",
            "statusLabel": "USD 340M — Socio Inversor",
            "description": "Compañía operadora en marcha con 15 concesiones de explotación activas sobre una superficie de 3.000 km² en la Cuenca Neuquina. Bloque de 1.200 pozos y más de 500 empleados. Plan llave en mano de mejora con tecnología No Convencional.",
            "thesis": "Empresa petrolera consolidada a escala corporativa con formidable masa crítica de pozos para reactivación y estimulación horizontal en tight y shale.",
            "highlights": [
                "15 concesiones de explotación hidrocarburífera en 3.000 km² de Cuenca Neuquina.",
                "Parque activo de aproximadamente 1.200 pozos en producción con base operativa propia.",
                "Estructura corporativa sólida con más de 500 colaboradores técnicos y operarios.",
                "Inversión de USD 340M estructurada para plan llave en mano con técnica No Convencional.",
                "Socio inversor con participación de control o co-gestión ejecutiva."
            ],
            "metrics": [
                {
                    "label": "Inversión Final",
                    "val": "USD 340M",
                    "color": "text-gold"
                },
                {
                    "label": "Superficie",
                    "val": "3.000 km²",
                    "color": "text-cyan"
                },
                {
                    "label": "Pozos",
                    "val": "1.200 Pozos",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "Socio Inversor",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Compañía operadora con 15 áreas de concesión adjudicadas, producción inmediata de petróleo y gas, y red de ductos de captación en Cuenca Neuquina.",
                "intl": "Entrada directa de capital al shale oil más competitivo del hemisferio sur, con costos de desarrollo y punto de equilibrio (break-even) inferiores a USD 35/bbl."
            }
        },
        "en": {
            "categoryTag": "Upstream Operator — Vaca Muerta",
            "title": "Oilfield Operator in Vaca Muerta (15 Concessions)",
            "location": "Neuquina Basin, Neuquén, Argentina",
            "statusLabel": "USD 340M — Equity Partner",
            "description": "Fully established independent oil & gas operator holding 15 exploitation licenses across 3,000 km² in the prolific Neuquina Basin. ~1,200 active wells and >500 staff. Turnkey unconventional well enhancement plan.",
            "thesis": "Corporate-scale platform company with massive well stock and extensive acreage ready for high-yield unconventional workover and horizontal re-stimulation.",
            "highlights": [
                "15 exploitation licenses covering 3,000 km² in prime Vaca Muerta play.",
                "Operational base managing approximately 1,200 active producing wells.",
                "Experienced workforce with more than 500 skilled petroleum engineers and crew.",
                "Turnkey capital plan of USD 340M deploying unconventional stimulation.",
                "Equity partnership with shared governance or controlling stake."
            ],
            "metrics": [
                {
                    "label": "Final Ticket",
                    "val": "USD 340M",
                    "color": "text-gold"
                },
                {
                    "label": "Acreage",
                    "val": "3,000 km²",
                    "color": "text-cyan"
                },
                {
                    "label": "Well Stock",
                    "val": "1,200 Wells",
                    "color": "text-green"
                },
                {
                    "label": "Deal Type",
                    "val": "Equity Partner",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Independent producer holding 15 active concession blocks with running crude production and field gathering facilities.",
                "intl": "Direct equity access to top-tier shale oil assets delivering sub-USD 35/bbl breakeven economics."
            }
        },
        "dealType": "Socio Inversor",
        "tir": "35.0%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 68.0M/año (Margen 58%)",
        "capitalStructure": "Socio Inversor / Capital de Desarrollo Upstream",
        "regulatoryRegime": "15 Concesiones de Explotación Hidrocarburífera Vigentes",
        "financialNote_es": "Cálculo de TIR: Producción de crudo no convencional con break-even inferior a 35 USD/bbl y reservas P1 certificadas. TIR del 35.0% vs. TIR > 15%.",
        "financialNote_en": "IRR Methodology: Producing shale assets with sub-USD 35/bbl breakeven and certified 1P reserves. 35.0% IRR vs. IRR > 15%."
    },
    "pozo-salta": {
        "id": "pozo-salta",
        "category": "petroleo",
        "sector": "Petróleo, Gas & Infraestructura",
        "assignedAgent": "daniel",
        "amountUSD": 1860.0,
        "basePrice": 15000000,
        "overpriceTarget": 1000000,
        "currency": "USD",
        "amountDisplay": "USD 1.860M (Flexible con Socios Inversores)",
        "defaultStatus": "activo",
        "modality": "Socio Inversor / Concesión & UTE",
        "roi": "3 Años (Planta) / 20 Años (Concesión)",
        "statusProgress": "Planta de secado de cuttings (500 m³/d) unificada a 25 áreas de concesión hidrocarburífera por 20 años en Salta",
        "isPrivatePlacement": false,
        "pdfPath": "assets/docs/pozo_salta_2026.pdf",
        "totalSlides": 25,
        "slidePrefix": "assets/slides/Proyecto_Pozo_Salta___Argentina__2026_page_",
        "coverImage": "assets/slides/Proyecto_Pozo_Salta___Argentina__2026_page_1.png",
        "es": {
                "categoryTag": "Infraestructura & Upstream NOA — 25 Áreas",
                "title": "Proyecto Pozo Salta — Infraestructura & Secado de Cuttings",
                "location": "Cuenca Noroeste, Salta, Argentina",
                "statusLabel": "USD 1.860M — Socio Inversor",
                "description": "Complejo integral hidrocarburífero y ambiental en Salta que combina: 1) Planta industrial de tratamiento térmico y secado de cuttings (500 m³/día) con demanda regulatoria mandatoria, y 2) Concesión oficial por 20 años sobre 25 áreas de explotación en Cuenca Noroeste con reservas certificadas de crudo y gas.",
                "thesis": "Doble motor de rentabilidad: ingresos operativos en dólares con clientes cautivos de perforación NOA, complementado por la reversión del Gasoducto Norte para inyección y exportación masiva a Brasil sobre 25 bloques en UTE.",
                "highlights": [
                        "Planta de secado de cuttings (500 m³/día): único centro habilitado en la cuenca, payback < 3 años.",
                        "25 áreas de explotación concesionadas por 20 años con reservas probadas P1 y P2.",
                        "Conexión logística directa a Campo Durán y red de poliductos/gasoductos al norte y Brasil.",
                        "Monto de inversión de USD 1.860M con alta flexibilidad para acordar esquemas con socios inversores (por bloques o complejo integral).",
                        "Acuerdo bilateral de suministro de crudo y gas con refinerías de la región."
                ],
                "metrics": [
                        {
                                "label": "Monto Total Plan",
                                "val": "USD 1.860M",
                                "color": "text-cyan"
                        },
                        {
                                "label": "Concesión Áreas",
                                "val": "25 Bloques (20 Años)",
                                "color": "text-gold"
                        },
                        {
                                "label": "EBITDA Proyectado",
                                "val": "USD 8.2M + USD 240M",
                                "color": "text-green"
                        },
                        {
                                "label": "TIR Estimada",
                                "val": "31.0%",
                                "color": "text-gold"
                        }
                ],
                "marketTrend": {
                        "local": "Servicio ambiental obligatorio de secado térmico de cuttings (500 m³/día) con tarifas dolarizadas, unificado al desarrollo de 25 áreas concesionadas a 20 años con gasoducto troncal.",
                        "intl": "La reversión del Gasoducto Norte y la apertura de exportaciones a Brasil aceleran el desarrollo de cuencas maduras y exigen cumplimiento estricto de normas ambientales ESG."
                }
        },
        "en": {
                "categoryTag": "Infrastructure & Upstream Basin — 25 Blocks",
                "title": "Pozo Salta Project — Infrastructure & Cuttings Treatment",
                "location": "Northwest Basin, Salta, Argentina",
                "statusLabel": "USD 1,860M — Equity Partner",
                "description": "Integrated oilfield and environmental complex in Salta combining: 1) Thermal drying facility for drilling cuttings (500 m3/day) with mandatory compliance demand, and 2) 20-year concession covering 25 licensed exploration blocks in Northwest Basin.",
                "thesis": "Dual-engine revenue model: recurring dollarized environmental service cash flow paired with 25 upstream concession blocks strategically linked to the Northern Gas Pipeline reversal towards Brazil.",
                "highlights": [
                        "Thermal desorption plant (500 m³/day): sole certified processing facility in the basin (< 3-year payback).",
                        "25 exploitation blocks under 20-year concession with certified 1P and 2P reserves.",
                        "Direct pipeline interconnection to Campo Durán refinery and export lines to Brazil.",
                        "Total USD 1,860M investment volume offering maximum flexibility for customized agreements with partner investors.",
                        "Bilateral off-take agreements with regional downstream refiners."
                ],
                "metrics": [
                        {
                                "label": "Total Plan Monto",
                                "val": "USD 1,860M",
                                "color": "text-cyan"
                        },
                        {
                                "label": "Area Concessions",
                                "val": "25 Blocks (20 Yrs)",
                                "color": "text-gold"
                        },
                        {
                                "label": "Projected EBITDA",
                                "val": "USD 8.2M + USD 240M",
                                "color": "text-green"
                        },
                        {
                                "label": "Modeled IRR",
                                "val": "31.0%",
                                "color": "text-gold"
                        }
                ],
                "marketTrend": {
                        "local": "Mandatory thermal cuttings drying hub (500 m3/day) paired with 25 licensed 20-year concession blocks in the Northwest Basin.",
                        "intl": "Northern Pipeline reversal unlocking Brazilian export markets while stringent environmental ESG rules enforce zero-discharge drill cuttings."
                }
        },
        "dealType": "Socio Inversor",
        "tir": "31.0%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 8.2M/año Planta + USD 240M/año Bloques UTE",
        "capitalStructure": "Socio Inversor / Flexibilidad de Acuerdo en 25 Bloques & Complejo Cuttings",
        "regulatoryRegime": "Normativa Ambiental Mandatoria NOA & 25 Concesiones Vigentes",
        "financialNote_es": "Cálculo de TIR: Inversión estructurada de USD 1.860M con flexibilidad para socios inversores: planta de secado de cuttings mandatoria más 25 áreas conectadas a Brasil. TIR proyectada del 31.0% (TIR > 15%).",
        "financialNote_en": "IRR Methodology: Structured USD 1,860M investment with flexibility for partner investors: mandatory cuttings drying plant plus 25 blocks connected to Brazil. Projected 31.0% IRR (IRR > 15%)."
},
    "asesoramiento-inbound-funds": {
        "id": "asesoramiento-inbound-funds",
        "category": "asesoramiento",
        "sector": "Asesoramiento Financiero",
        "assignedAgent": "daniel",
        "amountUSD": 0.0,
        "basePrice": 0,
        "overpriceTarget": 0,
        "currency": "USD",
        "amountDisplay": "Mandato Institucional",
        "defaultStatus": "activo",
        "modality": "Asset Management & Advisory",
        "roi": "Continuo",
        "statusProgress": "Servicio institucional integral con equipo multidisciplinario y cartelera curada",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Banca de Inversión & Mandatos",
            "title": "Gestión y Administración Integral de Grupos Inversores",
            "location": "Buenos Aires / Córdoba / Global",
            "statusLabel": "Servicio Institucional",
            "description": "Acompañamiento integral para grupos inversores y fondos internacionales (FDI) que buscan estructurar y desplegar capital en activos estratégicos de la economía real argentina.",
            "thesis": "Plataforma de aterrizaje seguro ('soft landing') que minimiza la fricción regulatoria, cambiaria y legal, asegurando la selección de proyectos con estricto estándar de debida diligencia.",
            "highlights": [
                "Cartelera activa de oportunidades de inversión auditadas y de alto rendimiento.",
                "Estructuración de vehículos societarios locales, cuentas fiduciarias y compliance cambiario.",
                "Equipo multidisciplinario: analistas financieros, ingenieros, abogados y escribanos.",
                "Gobierno corporativo y seguimiento de avance de proyectos en tiempo real.",
                "Asignación de consultor dedicado para interlocución con juntas directivas."
            ],
            "metrics": [
                {
                    "label": "Servicio",
                    "val": "Gestión Integral",
                    "color": "text-gold"
                },
                {
                    "label": "Alcance",
                    "val": "Fondos Extranjeros",
                    "color": "text-cyan"
                },
                {
                    "label": "Equipo",
                    "val": "Multidisciplinario",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "Mandato Privado",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "El nuevo marco macroeconómico argentino y el régimen RIGI generan un flujo masivo de consultas de fondos extranjeros para estructurar adquisiciones directas.",
                "intl": "Fondos soberanos y de private equity buscan originadores locales con conocimiento regulatorio, contratos NCNDA y acceso directo a activos privados."
            }
        },
        "en": {
            "categoryTag": "Investment Banking & Advisory",
            "title": "Comprehensive Asset Management for Investment Groups",
            "location": "Buenos Aires / Córdoba / Global",
            "statusLabel": "Institutional Service",
            "description": "End-to-end advisory and management services for international private equity and foreign direct investment (FDI) groups allocating capital into real Argentine assets.",
            "thesis": "Turnkey soft-landing platform mitigating regulatory, FX, and legal complexity while delivering rigorously vetted investment-grade deals.",
            "highlights": [
                "Curated pipeline of audited, high-yield investment proposals across key sectors.",
                "Corporate vehicle structuring, fiduciary escrow administration, and FX compliance.",
                "Multidisciplinary team of financial modelers, engineers, and legal counsels.",
                "Corporate governance and real-time project milestone tracking.",
                "Dedicated partner assignment for board-level liaison."
            ],
            "metrics": [
                {
                    "label": "Service",
                    "val": "Asset Management",
                    "color": "text-gold"
                },
                {
                    "label": "Scope",
                    "val": "Foreign Funds",
                    "color": "text-cyan"
                },
                {
                    "label": "Team",
                    "val": "Multidisciplinary",
                    "color": "text-green"
                },
                {
                    "label": "Deal Type",
                    "val": "Private Mandate",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Pro-market reforms and RIGI incentives accelerating institutional foreign capital entry into Argentina natural resources.",
                "intl": "Sovereign wealth and private equity funds seeking trusted local partners to originate, diligence, and structure private transactions."
            }
        },
        "dealType": "Asesoramiento / Mandato",
        "tir": "Estructuración",
        "tir_target": "TIR > 15%",
        "ebitda": "Fee Management 1.5% + Carry 15%",
        "capitalStructure": "Mandato Institucional de Asset Management",
        "regulatoryRegime": "Contratos NCNDA, Mandatos Fiduciarios & Compliance Internacional",
        "financialNote_es": "Cálculo de TIR: Retorno continuo basado en honorarios de gestión y carry sobre valorización de activos. Supera cualquier tasa libre de riesgo objetivo (>9%).",
        "financialNote_en": "IRR Methodology: Ongoing returns from management fees and carried interest on deal execution. Substantially outperforms IRR > 15%."
    },
    "asesoramiento-gobiernos": {
        "id": "asesoramiento-gobiernos",
        "category": "asesoramiento",
        "sector": "Asesoramiento Financiero",
        "assignedAgent": "daniel",
        "amountUSD": 0.0,
        "basePrice": 0,
        "overpriceTarget": 0,
        "currency": "USD",
        "amountDisplay": "Estructuración a Medida",
        "defaultStatus": "activo",
        "modality": "Estructuración Financiera",
        "roi": "Estructural",
        "statusProgress": "Asesoría para entes públicos, provincias y municipios bajo marco RIGI / PPP",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Finanzas Públicas & Infraestructura",
            "title": "Financiamiento de Proyectos Gubernamentales e Infraestructura",
            "location": "Nación, Provincias y Municipios, Argentina",
            "statusLabel": "Advisory Estructurado",
            "description": "Diseño y estructuración de instrumentos de financiamiento para estados provinciales, municipios y entes autárquicos destinados a infraestructura energética, vial, hídrica y de transporte.",
            "thesis": "Monetización y apalancamiento de fondos públicos mediante bonos verdes, fideicomisos de garantía y esquemas PPP/RIGI para viabilizar obras de gran porte sin comprometer el balance fiscal.",
            "highlights": [
                "Estructuración de bonos verdes, títulos de deuda y fideicomisos de obra pública.",
                "Adecuación y estructuración de proyectos estratégicos al Régimen RIGI (Ley 27.742).",
                "Modelos de asociación público-privada (PPP) con repago por tarifas o peajes.",
                "Dictámenes de viabilidad económica, fiscal y financiera auditables.",
                "Vínculo con organismos multilaterales de crédito y bancos de desarrollo."
            ],
            "metrics": [
                {
                    "label": "Servicio",
                    "val": "Finanzas Públicas",
                    "color": "text-gold"
                },
                {
                    "label": "Instrumentos",
                    "val": "Bonos & Fideicomisos",
                    "color": "text-cyan"
                },
                {
                    "label": "Marco",
                    "val": "RIGI / PPP",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "Estructuración",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Estados provinciales y municipios demandan estructuración de esquemas de Participación Público-Privada (PPP) para obras viales, energéticas e hídricas.",
                "intl": "Bancos multilaterales de crédito (BID, CAF, Banco Mundial) priorizan financiamiento de infraestructura resiliente con gobernanza transparente."
            }
        },
        "en": {
            "categoryTag": "Public Finance & Infrastructure",
            "title": "Government Project Financing & Infrastructure Advisory",
            "location": "Federal, Provincial & Municipal, Argentina",
            "statusLabel": "Structured Advisory",
            "description": "Design and structuring of financing instruments for provincial governments, municipalities, and state utilities targeting energy, road, water, and transport infrastructure.",
            "thesis": "Public balance-sheet optimization via green bonds, infrastructure trusts, and PPP/RIGI mechanisms to fund large-scale developments.",
            "highlights": [
                "Green bond issuances, debt certificates, and public infrastructure trust funds.",
                "Project alignment with the federal RIGI framework (Law 27,742).",
                "Public-Private Partnership (PPP) modeling with user-toll or availability fee repayment.",
                "Auditable economic and fiscal feasibility appraisals.",
                "Direct structuring liaison with multilateral development banks."
            ],
            "metrics": [
                {
                    "label": "Service",
                    "val": "Public Finance",
                    "color": "text-gold"
                },
                {
                    "label": "Instruments",
                    "val": "Bonds & Trusts",
                    "color": "text-cyan"
                },
                {
                    "label": "Framework",
                    "val": "RIGI / PPP",
                    "color": "text-green"
                },
                {
                    "label": "Deal Type",
                    "val": "Financial Advisory",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Provinces and municipalities deploying private PPP financing models for critical public infrastructure works.",
                "intl": "Multilateral development banks and global institutional lenders prioritizing transparent blended-finance infrastructure facilities."
            }
        },
        "dealType": "Mandato Soberano",
        "tir": "Honorarios Éxito",
        "tir_target": "TIR > 9%",
        "ebitda": "Success Fee 2.0% - 3.5% sobre Capex",
        "capitalStructure": "Mandato Soberano de Estructuración Financiera",
        "regulatoryRegime": "Régimen PPP Nacional/Provincial & Agencias Multilaterales",
        "financialNote_es": "Cálculo de TIR: Estructuración fiduciaria de obra pública sin compromiso de capital propio, con honorarios de éxito en dólares superiores al TIR > 9%.",
        "financialNote_en": "IRR Methodology: Zero-equity public-private partnership structuring yielding dollar success fees above >9% hurdle rate."
    },
    "asesoramiento-real-estate": {
        "id": "asesoramiento-real-estate",
        "category": "asesoramiento",
        "sector": "Asesoramiento Financiero",
        "assignedAgent": "daniel",
        "amountUSD": 0.0,
        "basePrice": 0,
        "overpriceTarget": 0,
        "currency": "USD",
        "amountDisplay": "Desarrollo Fiduciario",
        "defaultStatus": "activo",
        "modality": "Desarrollo & Advisory",
        "roi": "Renta / Plusvalía",
        "statusProgress": "Vehículos fiduciarios, parques logísticos, loteos y fondos REIT dolarizados",
        "isPrivatePlacement": false,
        "coverImage": "assets/images/logo_energy_cpy_cover_white.png",
        "totalSlides": 5,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "es": {
            "categoryTag": "Bienes Raíces & REITs",
            "title": "Gestión de Proyectos de Bienes Raíces & Construcción",
            "location": "Polos Corporativos e Industriales, Argentina",
            "statusLabel": "Estructuración Fiduciaria",
            "description": "Estructuración integral de vehículos de inversión inmobiliaria de renta corporativa (REITs), parques industriales, loteos turísticos y naves logísticas 'triple A' con flujos dolarizados.",
            "thesis": "Protección patrimonial y rentabilidad en USD mediante el apalancamiento de activos de tierra estratégicos desarrollados bajo contratos fiduciarios de estricta segregación patrimonial.",
            "highlights": [
                "Vehículos fiduciarios de inversión inmobiliaria (REITs) transparentes y dolarizados.",
                "Desarrollo de naves industriales, centros de distribución y polos logísticos.",
                "Modelado financiero de flujos de fondos, absorción comercial y retorno al inversor.",
                "Segregación patrimonial y seguridad jurídica respaldada en el CCCN (Ley 26.994).",
                "Comercialización de unidades de renta corporativa con inquilinos multinacionales."
            ],
            "metrics": [
                {
                    "label": "Servicio",
                    "val": "Real Estate Advisory",
                    "color": "text-gold"
                },
                {
                    "label": "Activos",
                    "val": "Logística & Hotelería",
                    "color": "text-cyan"
                },
                {
                    "label": "Moneda",
                    "val": "Flujos USD",
                    "color": "text-green"
                },
                {
                    "label": "Modalidad",
                    "val": "Estructuración",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "El regreso del crédito hipotecario y la regularización de activos impulsan el desarrollo de urbanizaciones, parques logísticos y oficinas corporativas AAA.",
                "intl": "Costos de construcción en dólares históricamente atractivos en Argentina permiten a desarrolladores internacionales capturar retornos por plusvalía y renta."
            }
        },
        "en": {
            "categoryTag": "Real Estate & REIT Structuring",
            "title": "Real Estate & Construction Project Management",
            "location": "Corporate & Industrial Hubs, Argentina",
            "statusLabel": "Fiduciary Advisory",
            "description": "Comprehensive design and administration of commercial real estate investment trusts (REITs), industrial logistics parks, master-planned residential communities, and prime yield assets.",
            "thesis": "Wealth preservation and inflation-hedged USD cash yields leveraging prime land assets governed by bankruptcy-remote fiduciary trust contracts.",
            "highlights": [
                "USD-denominated transparent Real Estate Investment Trust (REIT) structures.",
                "Development of prime industrial warehouses, logistics parks, and lifestyle communities.",
                "Quantitative discounted cash flow modeling, absorption metrics, and IRR targets.",
                "Strict legal asset ring-fencing under Argentine Civil and Commercial Code (Law 26,994).",
                "Commercial leasing to multinational corporate tenants."
            ],
            "metrics": [
                {
                    "label": "Service",
                    "val": "REIT & RE Advisory",
                    "color": "text-gold"
                },
                {
                    "label": "Asset Class",
                    "val": "Industrial / Yield",
                    "color": "text-cyan"
                },
                {
                    "label": "Currency",
                    "val": "USD Yield",
                    "color": "text-green"
                },
                {
                    "label": "Deal Type",
                    "val": "Fiduciary Vehicle",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Mortgage lending recovery and tax normalization driving residential, logistics, and AAA corporate real estate developments.",
                "intl": "Highly attractive construction costs in USD allowing international investors to secure premium yields and long-term capital gains."
            }
        },
        "dealType": "Socio Inversor / Desarrollo",
        "tir": "18.0%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 7.5M/año (Margen 35%)",
        "capitalStructure": "Socio Inversor / Fideicomiso al Costo con Plusvalía",
        "regulatoryRegime": "Ley de Fideicomisos 24.441 & Crédito Hipotecario",
        "financialNote_es": "Cálculo de TIR: Flujos de preventa al costo más renta por revalorización en polos urbanos en expansión. TIR del 18.0% vs. TIR > 15%.",
        "financialNote_en": "IRR Methodology: Cost-based development pre-sales plus urban property capital appreciation. 18.0% IRR vs. IRR > 15%."
    },
    "reit-strategy": {
        "id": "reit-strategy",
        "category": "reit",
        "sector": "Real Estate / REIT",
        "assignedAgent": "daniel",
        "amountUSD": 30.0,
        "basePrice": 30000000,
        "overpriceTarget": 1500000,
        "currency": "USD",
        "amountDisplay": "USD 30M Fondo",
        "defaultStatus": "activo",
        "modality": "Fondo Inmobiliario",
        "roi": "12% Anual USD",
        "statusProgress": "Estrategia REIT dolarizada en activos triple A",
        "isPrivatePlacement": false,
        "pdfPath": "assets/docs/reit_strategy_2026.pdf",
        "totalSlides": 11,
        "slidePrefix": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_",
        "coverImage": "assets/slides/ENERGY_CPY_Argentina_REIT_Investment_Strategy___Argentina_2026_page_1.png",
        "es": {
            "categoryTag": "Fondo Inmobiliario REIT",
            "title": "ENERGY CPY Argentina REIT Investment Strategy 2026",
            "location": "CABA & Corredor Norte, Argentina",
            "statusLabel": "USD 30M — Fondo Dolarizado",
            "description": "Estrategia fiduciaria de inversión inmobiliaria de renta corporativa dolarizada (REIT) enfocada en oficinas premium y centros logísticos con contratos a largo plazo.",
            "thesis": "Renta neta distribuible del 10% al 12% anual en USD combinada con plusvalía de capital en activos irreemplazables.",
            "highlights": [
                "Portafolio diversificado en activos inmobiliarios clase A+.",
                "Contratos de alquiler corporativo dolarizados a 5-10 años.",
                "Rendimiento anual neto proyectado del 10% al 12% en USD.",
                "Vehículo fiduciario independiente con estricto gobierno corporativo.",
                "Ticket de ingreso estructurado para inversores institucionales y privados."
            ],
            "metrics": [
                {
                    "label": "Fondo Objetivo",
                    "val": "USD 30M",
                    "color": "text-gold"
                },
                {
                    "label": "Rendimiento",
                    "val": "10% - 12% USD",
                    "color": "text-cyan"
                },
                {
                    "label": "Contratos",
                    "val": "5 - 10 Años",
                    "color": "text-green"
                },
                {
                    "label": "Tipo",
                    "val": "REIT Dolarizado",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Primer vehículo institucional estructurado bajo ley de fideicomisos que consolida inmuebles comerciales y hoteleros con renta dolarizada y liquidación trimestral.",
                "intl": "Estructura REIT alineada con estándares globales de transparencia que permite diversificar portafolios internacionales con rentas protegidas contra la inflación."
            }
        },
        "en": {
            "categoryTag": "Real Estate Investment Trust",
            "title": "ENERGY CPY Argentina REIT Investment Strategy 2026",
            "location": "Buenos Aires Prime Corridor, Argentina",
            "statusLabel": "USD 30M — USD Fund",
            "description": "Fiduciary corporate yield real estate investment strategy (REIT) focused on prime offices and modern logistics hubs backed by long-term corporate leases.",
            "thesis": "Targeted net annual yield of 10% to 12% in USD combined with capital appreciation in trophy commercial assets.",
            "highlights": [
                "Diversified portfolio in prime Class A+ real estate.",
                "Long-term USD-indexed commercial leases (5-10 years).",
                "Projected net annual distribution of 10% to 12% in USD.",
                "Ring-fenced bankruptcy-remote trust with institutional governance.",
                "Structured entry tickets for qualified private and institutional capital."
            ],
            "metrics": [
                {
                    "label": "Target Fund",
                    "val": "USD 30M",
                    "color": "text-gold"
                },
                {
                    "label": "Yield",
                    "val": "10% - 12% USD",
                    "color": "text-cyan"
                },
                {
                    "label": "Lease Term",
                    "val": "5 - 10 Years",
                    "color": "text-green"
                },
                {
                    "label": "Asset Type",
                    "val": "USD REIT",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Pioneering institutional REIT vehicle consolidating prime hotel and commercial real estate yielding quarterly dollarized distributions.",
                "intl": "Standardized REIT architecture offering global investors liquid, inflation-protected, high-dividend exposure to prime Argentine real estate."
            }
        },
        "dealType": "Fondo Inmobiliario / REIT",
        "tir": "13.5%",
        "tir_target": "TIR > 9%",
        "ebitda": "USD 4.2M/año en dividendos (Cap Rate 14.0%)",
        "capitalStructure": "Fondo Fiduciario Inmobiliario Dolarizado / REIT",
        "regulatoryRegime": "Estructura Fiduciaria Blindada bajo Ley 24.441 & CNV",
        "financialNote_es": "Cálculo de TIR: Renta inmobiliaria institucional con distribución trimestral en USD y Cap Rate del 14%. TIR neta del 16.5% vs. TIR > 9%.",
        "financialNote_en": "IRR Methodology: Institutional real estate quarterly dollar dividend payouts yielding 14% Cap Rate. 16.5% net IRR vs. IRR > 9%."
    },
    "pesca-gran-escala": {
        "id": "pesca-gran-escala",
        "category": "pesca",
        "sector": "Pesca Industrial",
        "assignedAgent": "daniel",
        "amountUSD": 310.0,
        "basePrice": 260000000,
        "overpriceTarget": 12000000,
        "currency": "USD",
        "amountDisplay": "USD 310M — Venta de Activo",
        "defaultStatus": "activo",
        "modality": "Flota & Industria",
        "roi": "4 Años",
        "statusProgress": "Flota activa de 16 buques en ZEE y planta de congelado en tierra",
        "isPrivatePlacement": false,
        "pdfPath": "assets/docs/pesca_industrial_2026.pdf",
        "totalSlides": 13,
        "slidePrefix": "assets/slides/Proyectos_de_Pesca_Industrial_en_Argentina_2026_page_",
        "coverImage": "assets/slides/Proyectos_de_Pesca_Industrial_en_Argentina_2026_page_1.png",
        "es": {
                "categoryTag": "Pesca Industrial Gran Escala",
                "title": "Proyecto 6.6 — Pesca Industrial de Gran Escala en Patagonia",
                "location": "Zona Económica Exclusiva (ZEE) Argentina",
                "statusLabel": "USD 310M — Venta",
                "description": "Modelo consolidado de alta rentabilidad para captura y exportación de especies marinas premium (Merluza Hubbsi y Langostino Rojo) con flota activa de 16 buques de gran calado, cuotas federales CITP y planta de procesamiento en tierra. Venta integral por USD 310M.",
                "thesis": "Activo estratégico con derechos consolidados de captura en aguas argentinas generando ingresos brutos proyectados de USD 600M anuales.",
                "highlights": [
                        "Flota propia de 16 buques industriales operativos en Caleta Olivia y Puerto Madryn.",
                        "Cuotas de captura federales (CITP) garantizadas a 15 años por ley nacional.",
                        "Monto de venta total fijado en USD 310M con Data Room e inventario técnico disponible.",
                        "Planta de procesamiento en tierra con capacidad de 120 toneladas diarias de congelado.",
                        "Exportación directa a mercados de alta cotización en moneda dura (UE, EE.UU. y Asia)."
                ],
                "metrics": [
                        {
                                "label": "Monto Venta",
                                "val": "USD 310M",
                                "color": "text-gold"
                        },
                        {
                                "label": "Flota Activa",
                                "val": "16 Buques",
                                "color": "text-cyan"
                        },
                        {
                                "label": "EBITDA Anual",
                                "val": "USD 48.0M",
                                "color": "text-green"
                        },
                        {
                                "label": "TIR Estimada",
                                "val": "28.0%",
                                "color": "text-gold"
                        }
                ],
                "marketTrend": {
                        "local": "Flota activa de 16 buques pesqueros con cuota CITP federal asignada en caladeros patagónicos, capturando langostino salvaje, calamar illex y merluza hubbsi.",
                        "intl": "Demanda global insatisfecha de proteína marina salvaje en Asia, Europa y EE.UU., con cotizaciones internacionales récord en crustáceos y cefalópodos."
                }
        },
        "en": {
                "categoryTag": "Industrial High-Seas Fishing",
                "title": "Project 6.6 — Large-Scale Industrial Fishing in Patagonia",
                "location": "Exclusive Economic Zone (EEZ) Argentina",
                "statusLabel": "USD 310M — Asset Sale",
                "description": "High-margin industrial fishing and seafood export enterprise: active fleet of 16 deep-sea vessels, 15-year federal CITP quotas, and onshore processing plant. 100% asset sale at USD 310M.",
                "thesis": "Secured fishing quotas in Argentine South Atlantic waters delivering USD 600M/yr in projected gross export revenues.",
                "highlights": [
                        "Active proprietary fleet of 16 industrial fishing vessels operating in Patagonian ports.",
                        "15-year federal capture quotas (CITP) legally secured under national fishing regime.",
                        "Total asset sale price established at USD 310M with complete technical Data Room.",
                        "Onshore processing facility with 120 tons/day freezing capacity.",
                        "Direct dollarized exports to premium global markets (EU, USA, and Asia)."
                ],
                "metrics": [
                        {
                                "label": "Sale Amount",
                                "val": "USD 310M",
                                "color": "text-gold"
                        },
                        {
                                "label": "Active Fleet",
                                "val": "16 Vessels",
                                "color": "text-cyan"
                        },
                        {
                                "label": "Annual EBITDA",
                                "val": "USD 48.0M",
                                "color": "text-green"
                        },
                        {
                                "label": "Modeled IRR",
                                "val": "28.0%",
                                "color": "text-gold"
                        }
                ],
                "marketTrend": {
                        "local": "Premier 16-vessel industrial fleet holding permanent federal fishing quotas across the prolific Argentine Patagonia exclusive economic zone.",
                        "intl": "Sustained international demand for wild-caught marine protein across Asian and European seafood markets yielding peak export valuations."
                }
        },
        "dealType": "Venta",
        "tir": "28.0%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 48.0M/año (Margen 35%)",
        "capitalStructure": "100% Venta de Flota Activa (16 Buques), Cuotas CITP y Planta Procesadora",
        "regulatoryRegime": "Régimen Federal de Pesca (Ley 24.922) — Cuotas CITP a 15 Años",
        "financialNote_es": "Cálculo de TIR: Venta integral por USD 310M con flujo de exportación consolidado de langostino y calamar en moneda dura. TIR proyectada del 28.0% (TIR > 15%).",
        "financialNote_en": "IRR Methodology: 100% asset sale at USD 310M with robust export cash flows in hard currency. Projected 28.0% IRR (IRR > 15%).",
        "pdfUrl": "assets/docs/Proyectos_de_Pesca_Industrial_en_Argentina.pdf"
},
    "pesca-integrado": {
        "id": "pesca-integrado",
        "category": "pesca",
        "sector": "Pesca Industrial",
        "assignedAgent": "daniel",
        "amountUSD": 5.5,
        "basePrice": 5500000,
        "overpriceTarget": 500000,
        "currency": "USD",
        "amountDisplay": "USD 5.5M CAPEX",
        "defaultStatus": "activo",
        "modality": "Operación Boutique",
        "roi": "3 Años",
        "statusProgress": "Ecosistema pesquero integrado en Patagonia",
        "isPrivatePlacement": false,
        "pdfPath": "assets/docs/pesca_industrial_2026.pdf",
        "totalSlides": 13,
        "slidePrefix": "assets/slides/Proyectos_de_Pesca_Industrial_en_Argentina_2026_page_",
        "coverImage": "assets/slides/Proyectos_de_Pesca_Industrial_en_Argentina_2026_page_6.png",
        "es": {
            "categoryTag": "Pesca Industrial & Logística",
            "title": "Proyecto 6.7 — Ecosistema Pesquero Integrado Patagonia",
            "location": "Puerto Madryn & Rawson, Chubut, Argentina",
            "statusLabel": "USD 5.5M CAPEX",
            "description": "Desarrollo boutique modular que integra buques tangoneros costeros, procesamiento en planta y logística de frío para exportación directa a mercados asiáticos y europeos.",
            "thesis": "Alta rentabilidad operativa con bajo ticket de ingreso y ciclo de caja ágil basado en la captura del codiciado Langostino Patagónico.",
            "highlights": [
                "USD 5.5 Millones en CAPEX para puesta a punto y escalamiento.",
                "Enfocado en Langostino Salvaje de alto valor comercial.",
                "Contratos cerrados de exportación FOB Puerto Madryn.",
                "Estructura ágil con rápida rotación de capital de trabajo.",
                "Retorno proyectado de la inversión en 3 años."
            ],
            "metrics": [
                {
                    "label": "CAPEX Requerido",
                    "val": "USD 5.5M",
                    "color": "text-gold"
                },
                {
                    "label": "Producto",
                    "val": "Langostino Salvaje",
                    "color": "text-cyan"
                },
                {
                    "label": "Recupero",
                    "val": "3 Años",
                    "color": "text-green"
                },
                {
                    "label": "Destino",
                    "val": "Europa / Asia",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Operación boutique integrada verticalmente con buques congeladores y planta de procesamiento en tierra a pie de muelle para langostino IQF en Chubut.",
                "intl": "Cadenas gastronómicas y cadenas gourmet europeas y norteamericanas pagan sobreprecios de hasta el 35% por productos de pesca sustentable trazable."
            }
        },
        "en": {
            "categoryTag": "Integrated Fishery & Cold Chain",
            "title": "Project 6.7 — Integrated Fishery Ecosystem Patagonia",
            "location": "Puerto Madryn & Rawson, Chubut, Argentina",
            "statusLabel": "USD 5.5M CAPEX",
            "description": "Modular boutique fishery combining coastal outrigger vessels, onshore rapid processing, and cold-chain logistics for direct export to Asian and European distributors.",
            "thesis": "High operating margin with accessible ticket size targeting wild-caught Argentine Red Shrimp.",
            "highlights": [
                "USD 5.5 Million CAPEX required for fleet upgrade and scaling.",
                "Focus on wild Patagonian Red Shrimp with strong export pricing.",
                "Secured FOB supply contracts from Puerto Madryn.",
                "Lean operating model with rapid working capital turnover.",
                "3-year estimated capital payback."
            ],
            "metrics": [
                {
                    "label": "Required CAPEX",
                    "val": "USD 5.5M",
                    "color": "text-gold"
                },
                {
                    "label": "Primary Target",
                    "val": "Wild Red Shrimp",
                    "color": "text-cyan"
                },
                {
                    "label": "Payback",
                    "val": "3 Years",
                    "color": "text-green"
                },
                {
                    "label": "Destination",
                    "val": "Europe / Asia",
                    "color": "text-gold"
                }
            ],
            "marketTrend": {
                "local": "Integrated boutique processing operation with dockside IQF freezing plant in Patagonia port cluster, capturing maximum value-added margins.",
                "intl": "Global gourmet retail and premium foodservice paying up to 35% premium for fully traceable, wild-caught sustainable seafood."
            }
        },
        "dealType": "Socio Inversor",
        "tir": "32.5%",
        "tir_target": "TIR > 15%",
        "ebitda": "USD 1.8M/año (Margen 40%)",
        "capitalStructure": "Socio Inversor / Planta en Muelle & Flota Propia",
        "regulatoryRegime": "Habilitación SENASA, Certificación HACCP & Unión Europea",
        "financialNote_es": "Cálculo de TIR: Procesamiento en tierra con valor agregado (congelado IQF) capturando primas del 35% en mercado gourmet. TIR del 32.5% vs. TIR > 15%.",
        "financialNote_en": "IRR Methodology: Value-added onshore IQF processing capturing 35% premium in global gourmet markets. 32.5% IRR vs. IRR > 15%."
    }
};

const TRANSLATIONS = {
    es: {
        brand_sub: "INVESTMENT SHOWROOM",
        filter_cat_hoteleria: "Hotelería & Casinos",
        filter_cat_agro: "Agro, Campo & Industria",
        filter_cat_mineria: "Minería & Metales",
        filter_cat_petroleo: "Petróleo, Gas & Infraestructura",
        filter_cat_asesoramiento: "Asesoramiento Financiero",
        card_btn_onepager: "Resumen Ejecutivo (1 Pág)",
        card_btn_presentation: "Ver Presentación",
        toggle_obs_hide: "Ocultar Observaciones",
        toggle_obs_show: "Ver Observaciones",
        card_metric_ticket: "Inversión",
        card_metric_deal: "Tipo Oferta",
        card_metric_roi: "Rentabilidad",
        deal_metric_tir_lbl: "TIR Objetivo: >9%",
        card_badge_private: "🔒 Private Placement / Off-Market",
        card_cta_private: "Solicitar Invitación & NDA",
        private_amount: "A Invitación Exclusiva",
        
        nav_home: "Inicio",
        nav_projects: "Proyectos",
        nav_metrics: "Indicadores",
        nav_guarantees: "Garantías",
        nav_contact: "Contacto Oficial",
        nav_admin: "Gestión",

        hero_badge: "🏛️ Plataforma Oficial de Inversiones — Argentina 2026",
        hero_title_1: "Oportunidades Estratégicas de",
        hero_title_2: "Alto Rendimiento",
        hero_desc: "Estructuración de capital y proyectos llave en mano en <strong>Energía Solar Fotovoltaica</strong>, <strong>Pesca Industrial en Patagonia</strong>, <strong>Servicios Energéticos en Salta</strong> y <strong>Estrategias REIT Dolarizadas</strong>.",
        hero_btn_explore: "Explorar Oportunidades",
        hero_btn_contact: "Contactar a Dirección",
        strip_consultants_label: "Consultores de Capital",
        strip_wsp_label: "WhatsApp Directo Consultores",

        stat_capex_badge: "+4.1B USD",
        stat_capex_lbl: "CAPEX Total en Portafolio",
        stat_capex_sub: "Activos físicos estructurados en Argentina",
        stat_solar_badge: "Co-Financiado",
        stat_solar_lbl: "CAPEX Solar Pre-Financiado",
        stat_solar_sub: "Respaldado por fabricante global de tecnología",
        stat_pesca_badge: "600M USD/año",
        stat_pesca_lbl: "Track Record en Pesca Industrial",
        stat_pesca_sub: "Flota activa de 16 buques en ZEE Patagonia",
        stat_mater_badge: "MATER / PPA",
        stat_mater_lbl: "Plazo PPA Indexado en Dólares",
        stat_mater_sub: "Contratos con industrias y distribuidores",

        catalog_subtitle: "CATÁLOGO EJECUTIVO",
        catalog_title: "Portafolio de Proyectos de Inversión",
        catalog_desc: "Utilice los filtros avanzados por monto, categoría y estado para explorar las oportunidades disponibles.",

        filter_search_placeholder: "Buscar por palabra clave (ej. solar, pesca, REIT, salta)...",
        filter_category_all: "Todos los Sectores",
        filter_cat_energia: "Energía Solar & Renovable",
        filter_cat_pesca: "Pesca Industrial",
        filter_cat_petroleo: "Petróleo, Gas & Infraestructura",
        filter_cat_reit: "Fondo Inmobiliario REIT",
        filter_cat_mineria: "Minería & Litio",
        filter_cat_hoteleria: "Hotelería & Renta",

        filter_amount_title: "Monto del Proyecto (USD):",
        filter_amount_min: "Desde USD (M)",
        filter_amount_max: "Hasta USD (M)",
        filter_preset_all: "Todos los Montos",
        filter_preset_under10: "< USD 10M",
        filter_preset_10to50: "USD 10M - 50M",
        filter_preset_50to200: "USD 50M - 200M",
        filter_preset_over200: "> USD 200M",

        filter_status_all: "Todos los Estados",
        filter_status_activo: "Activo (Azul)",
        filter_status_tramite: "En trámite (Amarillo)",
        filter_status_vendido: "Vendido (Verde)",

        results_showing: "Mostrando",
        results_of: "de",
        results_projects: "proyectos de inversión",

        card_btn_details: "Ver Presentación & Ficha",
        card_status_activo: "Activo",
        card_status_tramite: "En trámite",
        card_status_vendido: "Vendido",

        ecosystem_subtitle: "SEGURIDAD Y MITIGACIÓN DE RIESGOS",
        ecosystem_title: "Ecosistema Integrado & Garantías de Inversión",
        ecosystem_desc: "Estructuración sólida con mitigación activa de riesgos técnicos, financieros y regulatorios.",
        eco_1_title: "Alianzas con Fabricantes Líderes",
        eco_1_desc: "En proyectos fotovoltaicos, el 50% del CAPEX es pre-financiado directamente por fabricantes mundiales de primer nivel, reduciendo la exposición inicial de capital.",
        eco_2_title: "Contratos PPA & Renta Dolarizada",
        eco_2_desc: "Acuerdos de compra de energía a largo plazo (15 a 20 años) indexados al USD, garantizando predictibilidad total de flujos de caja y rentabilidad sostenida.",
        eco_3_title: "Certificación Global MSC & ESG",
        eco_3_desc: "En el sector pesquero de la Patagonia, las pesquerías operan bajo normas internacionales estrictas MSC Certified, asegurando acceso prioritario a mercados de exportación.",
        eco_4_title: "Construcción Llave en Mano (EPC)",
        eco_4_desc: "Ingeniería de detalle, montaje y puesta en marcha ejecutados bajo contratos cerrados de tarifa fija para neutralizar desvíos presupuestarios.",

        contact_tag: "CANAL EJECUTIVO DIRECTO",
        contact_title: "Consultas Directas con Consultores de Capital",
        contact_desc: "Comuníquese directamente con nuestros consultores estratégicos vía WhatsApp para solicitar memorandos de entendimiento (MoU), informes de debida diligencia o acordar estructuras conjuntas.",
        wsp_btn_chat_javier: "Chat en WhatsApp con Javier Diaz",
        wsp_btn_chat_daniel: "Chat en WhatsApp con Daniel Gonzalez",

        form_title: "Solicitar Dossier / Coordinar Reunión",
        form_desc: "Complete los campos y el sistema derivará automáticamente su solicitud al consultor especialista en la temática.",
        form_name: "Nombre Completo *",
        form_name_ph: "Ej. Ing. Martín Rodríguez",
        form_company: "Empresa / Fondo / Institución",
        form_company_ph: "Ej. Austral Capital Partners",
        form_email: "Correo Electrónico de Contacto *",
        form_email_ph: "inversor@ejemplo.com",
        form_phone: "Teléfono / WhatsApp *",
        form_phone_ph: "+54 9 11 ... o código internacional",
        form_project_lbl: "Proyecto o Temática de Interés *",
        form_project_ph: "Seleccione una opción...",
        form_message_lbl: "Mensaje o Requerimiento Específico",
        form_message_ph: "Indique ticket estimado de inversión, plazo previsto o detalle de consulta...",
        form_btn_submit: "Enviar Solicitud a Consultores",
        
        assigned_specialist_badge: "Consultor Asignado:",
        specialist_javier_note: "Especialista en Minería, Energía Renovable, Proyectos de Ingeniería y Consultas en Inglés.",
        specialist_daniel_note: "Especialista en Hotelería, Pesca, Petróleo, TRUST Real Estate, REIT, Renta Corporativa y Asesoramiento Financiero.",

        success_title: "¡Consulta Enviada con Éxito!",
        success_body: "Muchas gracias por contactarse. Su solicitud ha sido procesada y asignada al consultor especialista de Energy CPY a cargo de la temática seleccionada. Nos pondremos en contacto a la brevedad.",
        success_btn_wsp: "Continuar Consulta Directa por WhatsApp con",
        success_btn_another: "Enviar Otra Consulta",

        footer_rights: "© 2026 Energy CPY — Todos los derechos reservados.",
        footer_domain: "Desplegado bajo el dominio oficial inventarioenergycpy.github.io",

        modal_tech_sheet: "Ficha Técnica del Proyecto",
        modal_highlights: "Puntos Clave de Inversión",
        modal_btn_pdf: "Descargar Presentación Completa (PDF)",
        modal_btn_onepager: "Ver y Descargar Resumen Ejecutivo (1 Pág. A4)",
        success_client_title: "¡Su consulta ha sido enviada con éxito!",
        success_client_desc: "Hemos recibido correctamente su solicitud de información y coordinación. Todos sus datos han sido registrados de forma segura y confidencial.",
        success_client_banner: "Por favor espere una respuesta a la brevedad. Nuestro consultor especialista asignado ya ha sido notificado y se comunicará con usted.",
        modal_wsp_javier: "WhatsApp Javier Diaz",
        modal_wsp_daniel: "WhatsApp Daniel Gonzalez"
    },

    en: {
        brand_sub: "INVESTMENT SHOWROOM",
        filter_cat_hoteleria: "Hospitality & Casinos",
        filter_cat_agro: "Agribusiness & Industry",
        filter_cat_mineria: "Mining & Critical Minerals",
        filter_cat_petroleo: "Oil, Gas & Infrastructure",
        filter_cat_asesoramiento: "Financial Advisory & Structuring",
        card_btn_onepager: "Executive Summary (1 Page)",
        toggle_obs_hide: "Hide Notes",
        toggle_obs_show: "Show Notes",
        card_badge_private: "🔒 Private Placement / Off-Market",
        card_cta_private: "Request Invitation & NDA",
        private_amount: "Exclusive Invitation Only",
        
        nav_home: "Home",
        nav_projects: "Projects",
        nav_metrics: "Metrics",
        nav_guarantees: "Guarantees",
        nav_contact: "Official Contact",
        nav_admin: "Management",

        hero_badge: "🏛️ Official Investment Platform — Argentina 2026",
        hero_title_1: "Strategic High-Yield",
        hero_title_2: "Opportunities",
        hero_desc: "Capital structuring and turnkey project delivery in <strong>Photovoltaic Solar Power</strong>, <strong>Industrial Fisheries in Patagonia</strong>, <strong>Oilfield Services in Salta</strong> and <strong>USD REIT Strategies</strong>.",
        hero_btn_explore: "Explore Opportunities",
        hero_btn_contact: "Contact Management",
        strip_consultants_label: "Capital Consultants",
        strip_wsp_label: "Direct WhatsApp Line",

        stat_capex_badge: "+4.1B USD",
        stat_capex_lbl: "Total Portfolio CAPEX",
        stat_capex_sub: "Tangible physical assets structured in Argentina",
        stat_solar_badge: "Co-Financed",
        stat_solar_lbl: "Pre-Financed Solar CAPEX",
        stat_solar_sub: "Backed by tier-1 global PV manufacturers",
        stat_pesca_badge: "600M USD/yr",
        stat_pesca_lbl: "Industrial Fishing Track Record",
        stat_pesca_sub: "Active fleet of 16 vessels in Patagonian EEZ",
        stat_mater_badge: "MATER / PPA",
        stat_mater_lbl: "USD-Indexed PPA Contract Term",
        stat_mater_sub: "Agreements with industries and utilities",

        catalog_subtitle: "EXECUTIVE PORTFOLIO",
        catalog_title: "Investment Project Catalog",
        catalog_desc: "Use advanced filters by ticket size, category and project status to explore available opportunities.",

        filter_search_placeholder: "Search by keyword (e.g., solar, fishing, REIT, Salta)...",
        filter_category_all: "All Sectors",
        filter_cat_energia: "Solar & Renewable Energy",
        filter_cat_pesca: "Industrial Fisheries",
        filter_cat_petroleo: "Oil, Gas & Infrastructure",
        filter_cat_reit: "REIT Real Estate Fund",
        filter_cat_mineria: "Mining & Lithium",
        filter_cat_hoteleria: "Hospitality & Yield",

        filter_amount_title: "Project Ticket Size (USD):",
        filter_amount_min: "From USD (M)",
        filter_amount_max: "To USD (M)",
        filter_preset_all: "All Amounts",
        filter_preset_under10: "< USD 10M",
        filter_preset_10to50: "USD 10M - 50M",
        filter_preset_50to200: "USD 50M - 200M",
        filter_preset_over200: "> USD 200M",

        filter_status_all: "All Statuses",
        filter_status_activo: "Active (Blue)",
        filter_status_tramite: "In Progress (Yellow)",
        filter_status_vendido: "Sold Out (Green)",

        results_showing: "Showing",
        results_of: "of",
        results_projects: "investment projects",

        card_btn_details: "View Deck & Technical Sheet",
        card_status_activo: "Active",
        card_status_tramite: "In Progress",
        card_status_vendido: "Sold Out",

        ecosystem_subtitle: "SECURITY & RISK MITIGATION",
        ecosystem_title: "Integrated Ecosystem & Investment Guarantees",
        ecosystem_desc: "Robust financial and technical structuring designed for active risk mitigation.",
        eco_1_title: "Tier-1 Manufacturer Partnerships",
        eco_1_desc: "In photovoltaic projects, 50% of CAPEX is directly pre-financed by leading global manufacturers, reducing upfront investor exposure.",
        eco_2_title: "USD-Indexed Long-Term PPAs",
        eco_2_desc: "Long-term power purchase agreements (15 to 20 years) indexed to USD, ensuring predictable cash flows and sustained yields.",
        eco_3_title: "Global MSC & ESG Certification",
        eco_3_desc: "Patagonian marine operations comply with rigorous MSC Certified standards, securing priority access to key export markets.",
        eco_4_title: "Turnkey EPC Construction",
        eco_4_desc: "Detailed engineering, procurement and commissioning carried out under fixed-price contracts to neutralize cost overruns.",

        contact_tag: "DIRECT EXECUTIVE CHANNEL",
        contact_title: "Direct Inquiries with Capital Consultants",
        contact_desc: "Connect directly with our strategic consultants via WhatsApp to request Memorandums of Understanding (MoU), due diligence materials or discuss joint venture structures.",
        wsp_btn_chat_javier: "Chat on WhatsApp with Javier Diaz",
        wsp_btn_chat_daniel: "Chat on WhatsApp with Daniel Gonzalez",

        form_title: "Request Dossier / Schedule Meeting",
        form_desc: "Complete the form and our system will automatically route your request to the specialist consultant for your sector.",
        form_name: "Full Name *",
        form_name_ph: "e.g., Eng. Martin Rodriguez",
        form_company: "Company / Fund / Institution",
        form_company_ph: "e.g., Austral Capital Partners",
        form_email: "Contact Email Address *",
        form_email_ph: "investor@example.com",
        form_phone: "Phone / WhatsApp *",
        form_phone_ph: "+1 ... or international country code",
        form_project_lbl: "Project or Area of Interest *",
        form_project_ph: "Select an option...",
        form_message_lbl: "Message or Specific Requirement",
        form_message_ph: "Indicate estimated investment ticket, timeline or inquiry details...",
        form_btn_submit: "Submit Request to Consultants",

        assigned_specialist_badge: "Assigned Consultant:",
        specialist_javier_note: "Specialist in Mining, Renewable Energy, Engineering Projects & English-language inquiries.",
        specialist_daniel_note: "Specialist in Hospitality, Fisheries, Oil & Gas, TRUST Real Estate, REIT, Corporate Yield & Financial Advisory.",

        success_title: "Inquiry Successfully Submitted!",
        success_body: "Thank you for reaching out. Your inquiry has been processed and routed to the dedicated Energy CPY consultant for your selected sector. We will be in touch promptly.",
        success_btn_wsp: "Continue Direct Chat on WhatsApp with",
        success_btn_another: "Send Another Inquiry",

        footer_rights: "© 2026 Energy CPY — All rights reserved.",
        footer_domain: "Deployed under the official domain inventarioenergycpy.github.io",

        modal_tech_sheet: "Project Technical Sheet",
        modal_highlights: "Key Investment Highlights",
        modal_btn_pdf: "Download Full Deck (PDF)",
        modal_wsp_javier: "WhatsApp Javier Diaz",
        modal_wsp_daniel: "WhatsApp Daniel Gonzalez"
    }
};



// Global App State
let currentLang = localStorage.getItem("energycpy_lang") || "es";
let currentProjectId = null;
let currentSlideIndex = 1;
let totalSlidesInCurrentProject = 1;

// Project Statuses State (persisted in localStorage)
let projectStatuses = loadProjectStatuses();

function loadProjectStatuses() {
    try {
        const saved = localStorage.getItem("energycpy_project_statuses");
        if (saved) {
            const parsed = JSON.parse(saved);
            Object.keys(PROJECTS_DATA).forEach(id => {
                if (!parsed[id]) parsed[id] = PROJECTS_DATA[id].defaultStatus || "activo";
            });
            return parsed;
        }
    } catch (e) {
        console.error("Error reading project statuses from localStorage", e);
    }
    // Default initial statuses
    const defaults = {};
    Object.keys(PROJECTS_DATA).forEach(id => {
        defaults[id] = PROJECTS_DATA[id].defaultStatus || "activo";
    });
    return defaults;
}

function saveProjectStatusesToStorage() {
    try {
        localStorage.setItem("energycpy_project_statuses", JSON.stringify(projectStatuses));
    } catch (e) {
        console.error("Error saving project statuses to localStorage", e);
    }
}

// Initialization on DOMContentLoaded
document.addEventListener("DOMContentLoaded", () => {
    initLanguageSwitcher();
    applyLanguage(currentLang);
    renderProjectCards();
    initFilters();
    initAnimatedCounters();
    initMobileMenu();
    initKeyboardNavigation();
    initContactFormRouting();
});

/* ==========================================================================
   1. Internationalization (i18n) Engine
   ========================================================================== */
function initLanguageSwitcher() {
    const esBtn = document.getElementById("langBtnEs");
    const enBtn = document.getElementById("langBtnEn");

    if (esBtn && enBtn) {
        esBtn.addEventListener("click", () => setLanguage("es"));
        enBtn.addEventListener("click", () => setLanguage("en"));
    }
}

function setLanguage(lang) {
    if (lang !== "es" && lang !== "en") return;
    currentLang = lang;
    localStorage.setItem("energycpy_lang", lang);
    applyLanguage(lang);
    renderProjectCards();
    applyFilters();
    updateFormSpecialistBadge();
}

function applyLanguage(lang) {
    const dict = TRANSLATIONS[lang] || TRANSLATIONS.es;
    if (typeof togglePresentationObservations === "function") {
        togglePresentationObservations(isObservationsPanelVisible);
    }

    // Update active class on language buttons
    const esBtn = document.getElementById("langBtnEs");
    const enBtn = document.getElementById("langBtnEn");
    if (esBtn && enBtn) {
        if (lang === "es") {
            esBtn.classList.add("active");
            enBtn.classList.remove("active");
        } else {
            enBtn.classList.add("active");
            esBtn.classList.remove("active");
        }
    }

    // Update all elements with data-i18n attribute
    document.querySelectorAll("[data-i18n]").forEach(el => {
        const key = el.getAttribute("data-i18n");
        if (dict[key]) {
            el.innerHTML = dict[key];
        }
    });

    // Update placeholders
    document.querySelectorAll("[data-i18n-placeholder]").forEach(el => {
        const key = el.getAttribute("data-i18n-placeholder");
        if (dict[key]) {
            el.setAttribute("placeholder", dict[key]);
        }
    });

    // Update HTML lang attribute
    document.documentElement.lang = lang;
}

/* ==========================================================================
   2. Project Cards Dynamic Rendering & Status Styling
   ========================================================================== */



/**
 * Protocolo Analista Financiero: Categorización Dinámica de TIR
 * - Si la TIR modelada está entre 9% y 14.99% -> "TIR > 9%"
 * - Si la TIR modelada es >= 15% -> "TIR > 15%"
 */
function getTirCategory(tir, isEn = false) {
    if (!tir) return isEn ? 'IRR > 9%' : 'TIR > 9%';
    const match = String(tir).match(/(\d+(?:\.\d+)?)/);
    if (!match) {
        if (String(tir).toLowerCase().includes('éxito') || String(tir).toLowerCase().includes('gobierno') || String(tir).toLowerCase().includes('soberano')) {
            return isEn ? 'IRR > 9%' : 'TIR > 9%';
        }
        return isEn ? 'IRR > 15%' : 'TIR > 15%';
    }
    const val = parseFloat(match[1]);
    if (val >= 15.0) {
        return isEn ? 'IRR > 15%' : 'TIR > 15%';
    } else if (val >= 9.0) {
        return isEn ? 'IRR > 9%' : 'TIR > 9%';
    } else {
        return isEn ? `IRR > ${val}%` : `TIR > ${val}%`;
    }
}

function renderProjectCards() {
    const grid = document.getElementById("projectsGrid");
    if (!grid) return;

    grid.innerHTML = "";

    // Set of exactly 5 projects authorized to display the presentation viewer
    const PRESENTATION_ENABLED_IDS = new Set([
        "solar",
        "pozo-salta",
        "reit-strategy",
        "pesca-gran-escala",
        "pesca-integrado"
    ]);

    Object.keys(PROJECTS_DATA).forEach(projectId => {
        const p = PROJECTS_DATA[projectId];
        const status = projectStatuses[projectId] || p.defaultStatus || "activo";
        const langData = p[currentLang] || p.es;
        const dict = TRANSLATIONS[currentLang] || TRANSLATIONS.es;
        const isEn = (currentLang === "en");

        let statusClass = "status-badge-activo";
        let statusText = dict.card_status_activo || "Activo";
        if (p.isPrivatePlacement) {
            statusClass = "status-badge-private";
            statusText = dict.card_badge_private || "🔒 Private Placement";
        } else if (status === "tramite") {
            statusClass = "status-badge-tramite";
            statusText = dict.card_status_tramite || "En Trámite";
        } else if (status === "vendido") {
            statusClass = "status-badge-vendido";
            statusText = dict.card_status_vendido || "Vendido";
        }

        const card = document.createElement("article");
        card.className = "project-card";
        card.setAttribute("data-id", p.id);
        card.setAttribute("data-category", p.category);
        card.setAttribute("data-amount", p.amountUSD);
        card.setAttribute("data-status", status);

        const amountText = p.isPrivatePlacement ? (dict.private_amount || "A Invitación Exclusiva") : p.amountDisplay;
        const dealTypeText = p.dealType || p.modality || (isEn ? "Direct Deal" : "Venta / Socio Inversor");
        const tirValueText = p.tir && p.tir !== "Consulte" ? p.tir : ">9%";
        const tirCategory = getTirCategory(p.tir, isEn);

        // Market trend micro-snippet
        const trendSnippet = (langData.marketTrend && langData.marketTrend.local) 
            ? (langData.marketTrend.local.length > 115 ? langData.marketTrend.local.slice(0, 115) + "..." : langData.marketTrend.local)
            : (langData.thesis ? (langData.thesis.length > 115 ? langData.thesis.slice(0, 115) + "..." : langData.thesis) : "");

        const hasPresentation = PRESENTATION_ENABLED_IDS.has(p.id);

        card.innerHTML = `
            <div class="card-image-wrapper ${hasPresentation ? '' : 'has-white-bg'}">
                <span class="card-tag tag-${p.category}">${langData.categoryTag}</span>
                <span class="card-status-badge ${statusClass}">
                    <span class="status-indicator-dot"></span> ${statusText}
                </span>
                <img src="${p.coverImage || 'assets/images/logo_energy_cpy_cover_white.png'}" alt="${langData.title}" class="card-img" loading="lazy">
                <div class="card-overlay" onclick="event.stopPropagation(); openOnePager('${p.id}', event);">
                    <span class="overlay-btn"><i class="fa-solid fa-file-contract"></i> ${dict.card_btn_onepager || 'Resumen Ejecutivo (1 Pág)'}</span>
                </div>
            </div>
            <div class="card-body">
                <div class="card-header-info">
                    <span class="card-location"><i class="fa-solid fa-location-dot"></i> ${langData.location}</span>
                    <span class="card-ticket-amount text-gold"><strong>${amountText}</strong></span>
                </div>
                
                <div style="margin: 4px 0 4px 0; display: flex; align-items: center; justify-content: space-between; gap: 8px;">
                    <span class="card-offer-badge"><i class="fa-solid fa-handshake"></i> ${dealTypeText}</span>
                </div>

                <!-- Financial Analyst Protocol: Cash Flow / EBITDA Highlight -->
                <div class="card-financial-tag">
                    <i class="fa-solid fa-chart-pie text-gold"></i>
                    <span><strong>EBITDA / Flujo:</strong> ${p.ebitda || 'Proyectado'}</span>
                </div>

                <h3 class="card-title">${langData.title}</h3>
                <p class="card-desc">${langData.description}</p>

                <!-- Market Trend Preview -->
                <div class="card-trend-snippet">
                    <i class="fa-solid fa-chart-line"></i>
                    <span><strong>${isEn ? 'Market Trend:' : 'Tendencia:'}</strong> ${trendSnippet}</span>
                </div>
                
                <div class="metrics-grid">
                    <div class="metric-item">
                        <span class="metric-val text-gold">${amountText}</span>
                        <span class="metric-lbl">${dict.card_metric_ticket || 'Inversión'}</span>
                    </div>
                    <div class="metric-item">
                        <span class="metric-val text-cyan">${dealTypeText}</span>
                        <span class="metric-lbl">${dict.card_metric_deal || 'Tipo Oferta'}</span>
                    </div>
                    <div class="metric-item" title="Tasa Interna de Retorno: ${tirCategory}">
                        <span class="metric-val text-green">${tirCategory}</span>
                        <span class="metric-lbl">${dict.card_metric_roi || (isEn ? 'Target Return' : 'Rentabilidad')}</span>
                    </div>
                </div>

                <div class="card-footer-actions">
                    <button type="button" class="btn btn-card-op ${hasPresentation ? '' : 'btn-card-op-full'}" onclick="event.stopPropagation(); openOnePager('${p.id}', event);">
                        <i class="fa-solid fa-file-contract"></i> ${dict.card_btn_onepager || 'Resumen (1 Pág)'}
                    </button>
                    ${hasPresentation ? `
                        <button type="button" class="btn btn-card btn-card-pres" onclick="event.stopPropagation(); openProjectModal('${p.id}');" title="${dict.card_btn_presentation || 'Ver Presentación'}">
                            <i class="fa-solid fa-desktop"></i> ${dict.card_btn_presentation || 'Ver Presentación'} (${p.totalSlides || 5})
                        </button>
                    ` : ''}
                </div>
            </div>
        `;

        grid.appendChild(card);
    });

    updateResultsCount();
}

/* ==========================================================================
   3. Advanced Multicriteria Search & Filter Engine (Desde - Hasta)
   ========================================================================== */
function initFilters() {
    const searchInput = document.getElementById("filterSearch");
    const categorySelect = document.getElementById("filterCategory");
    const minInput = document.getElementById("filterMinAmount");
    const maxInput = document.getElementById("filterMaxAmount");
    const statusSelect = document.getElementById("filterStatus");

    if (searchInput) searchInput.addEventListener("input", applyFilters);
    if (categorySelect) categorySelect.addEventListener("change", applyFilters);
    if (minInput) minInput.addEventListener("input", applyFilters);
    if (maxInput) maxInput.addEventListener("input", applyFilters);
    if (statusSelect) statusSelect.addEventListener("change", applyFilters);

    // Preset buttons
    document.querySelectorAll(".preset-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            document.querySelectorAll(".preset-btn").forEach(b => b.classList.remove("active"));
            btn.classList.add("active");

            const min = btn.getAttribute("data-min");
            const max = btn.getAttribute("data-max");

            if (minInput) minInput.value = min !== null && min !== "" ? min : "";
            if (maxInput) maxInput.value = max !== null && max !== "" ? max : "";

            applyFilters();
        });
    });
}

function applyFilters() {
    const query = (document.getElementById("filterSearch")?.value || "").toLowerCase().trim();
    const category = document.getElementById("filterCategory")?.value || "all";
    const minVal = parseFloat(document.getElementById("filterMinAmount")?.value) || 0;
    const maxVal = parseFloat(document.getElementById("filterMaxAmount")?.value) || Infinity;
    const status = document.getElementById("filterStatus")?.value || "all";

    const cards = document.querySelectorAll("#projectsGrid .project-card");
    let visibleCount = 0;

    cards.forEach(card => {
        const pId = card.getAttribute("data-id");
        const p = PROJECTS_DATA[pId];
        if (!p) return;

        const langData = p[currentLang] || p.es;
        const pCategory = card.getAttribute("data-category");
        const pAmount = parseFloat(card.getAttribute("data-amount")) || 0;
        const pStatus = card.getAttribute("data-status");

        // Text Search match
        const textContent = `${langData.title} ${langData.description} ${langData.location} ${langData.categoryTag}`.toLowerCase();
        const matchesQuery = !query || textContent.includes(query);

        // Category match
        const matchesCategory = category === "all" || pCategory === category;

        // Amount range match
        const matchesAmount = pAmount >= minVal && pAmount <= maxVal;

        // Status match
        const matchesStatus = status === "all" || pStatus === status;

        if (matchesQuery && matchesCategory && matchesAmount && matchesStatus) {
            card.style.display = "flex";
            visibleCount++;
        } else {
            card.style.display = "none";
        }
    });

    updateResultsCount(visibleCount);
}

function updateResultsCount(count) {
    const el = document.getElementById("resultsCounter");
    if (!el) return;

    const total = Object.keys(PROJECTS_DATA).length;
    const visible = count !== undefined ? count : document.querySelectorAll("#projectsGrid .project-card[style*='display: flex']").length || total;
    const dict = TRANSLATIONS[currentLang];

    el.innerHTML = `${dict.results_showing} <strong>${visible}</strong> ${dict.results_of} <strong>${total}</strong> ${dict.results_projects}`;
}

/* ==========================================================================
   4. Intelligent Consultation Routing & Silent Email Dispatch
   ========================================================================== */
function initContactFormRouting() {
    const projectSelect = document.getElementById("formProject");
    if (projectSelect) {
        projectSelect.addEventListener("change", updateFormSpecialistBadge);
    }
}

function getAssignedConsultantByTopic(topicValue) {
    const v = (topicValue || "").toLowerCase();

    // Topics assigned to Javier Diaz:
    // Energía Solar, Parques Renovables, Minería (Oro, Litio, Cobre, Mármol), Agroindustria (Estancias, Avex), Ingeniería, English Deals
    const javierKeywords = [
        "solar", "viento", "renovable", "fotovoltaic", "cammessa", "cuatro vientos",
        "miner", "oro", "litio", "cobre", "marmol", "mármol", "travertino", "diente verde", "san juan", "catamarca", "san luis",
        "agro", "estancia", "riego", "avícola", "avicola", "avex", "campo",
        "ingenier", "infraestructura",
        "english", "foreign", "inquir"
    ];

    const isJavier = javierKeywords.some(kw => v.includes(kw));
    return isJavier ? CONSULTANTS.javier : CONSULTANTS.daniel;
}

function updateFormSpecialistBadge() {
    const projectSelect = document.getElementById("formProject");
    const badgeContainer = document.getElementById("formSpecialistBadge");
    if (!projectSelect || !badgeContainer) return;

    const selectedValue = projectSelect.value;
    if (!selectedValue) {
        badgeContainer.style.display = "none";
        return;
    }

    const consultant = getAssignedConsultantByTopic(selectedValue);
    const dict = TRANSLATIONS[currentLang];
    const note = consultant.id === "javier" ? dict.specialist_javier_note : dict.specialist_daniel_note;

    badgeContainer.style.display = "flex";
    badgeContainer.innerHTML = `
        <div class="specialist-badge-icon">
            <i class="fa-solid fa-user-check ${consultant.id === 'javier' ? 'icon-cyan' : 'icon-gold'}"></i>
        </div>
        <div class="specialist-badge-info">
            <span class="specialist-badge-title">${dict.assigned_specialist_badge} <strong>${consultant.name}</strong></span>
            <span class="specialist-badge-desc">${note}</span>
        </div>
    `;
}

function handleFormSubmit(event) {
    event.preventDefault();

    const name = (document.getElementById("formName")?.value || "").trim();
    const company = (document.getElementById("formCompany")?.value || "").trim();
    const email = (document.getElementById("formEmail")?.value || "").trim();
    const phone = (document.getElementById("formPhone")?.value || "").trim();
    const topic = (document.getElementById("formProject")?.value || "").trim();
    const message = (document.getElementById("formMessage")?.value || "").trim();

    if (!name || !email || !phone || !topic) {
        alert("Por favor complete los campos obligatorios: Nombre, Email, Teléfono y Proyecto.");
        return;
    }

    const consultant = getAssignedConsultantByTopic(topic);
    const dict = TRANSLATIONS[currentLang] || TRANSLATIONS.es;
    const isEn = (currentLang === "en");
    const leadId = "ECPY-" + Date.now().toString(36).toUpperCase();

    // 1. GUARDAR TODOS LOS DATOS EN STORAGE PERSISTENTE LOCAL
    const leadRecord = {
        id: leadId,
        timestamp: new Date().toISOString(),
        dateFormatted: new Date().toLocaleString('es-AR'),
        clientName: name,
        clientCompany: company || "No especificada",
        clientEmail: email,
        clientPhone: phone,
        projectTopic: topic,
        clientMessage: message || "Sin mensaje adicional",
        assignedConsultantName: consultant.name,
        assignedConsultantEmail: consultant.internalEmail,
        assignedConsultantPhone: consultant.phone,
        senderAccount: "inventario.energycpy@gmail.com",
        status: "pendiente"
    };

    try {
        const storedLeads = JSON.parse(localStorage.getItem("energycpy_inquiries_db") || "[]");
        storedLeads.unshift(leadRecord);
        localStorage.setItem("energycpy_inquiries_db", JSON.stringify(storedLeads));
        console.log("Lead guardado exitosamente en base de datos local:", leadId);

        // Notificación en tiempo real multicanal para el Dashboard
        try {
            if (typeof BroadcastChannel !== 'undefined') {
                const bc = new BroadcastChannel('energycpy_inquiries_channel');
                bc.postMessage({
                    type: 'INQUIRY_CREATED',
                    ticket: leadRecord,
                    allInquiries: storedLeads,
                    timestamp: Date.now()
                });
                setTimeout(() => bc.close(), 1000);
            }
        } catch (bcErr) {
            console.log("BroadcastChannel dispatch:", bcErr);
        }
    } catch (err) {
        console.warn("Error guardando lead en storage local:", err);
    }

    // 2. DISPATCH INTERNO: Asunto y mensaje en español con aclaraciones de sistema
    const emailSubject = `Te han enviado una consulta desde el showroom web - ${topic}`;
    
    const emailBodyText = 
`TE HAN ENVIADO UNA CONSULTA DESDE EL SHOWROOM WEB
============================================================
PROYECTO SELECCIONADO: ${topic}
TICKET ÚNICO DE SEGUIMIENTO: ${leadId}
FECHA Y HORA DE REGISTRO: ${leadRecord.dateFormatted}

DATOS DEL INTERESADO / INVERSOR:
------------------------------------------------------------
• Nombre Completo: ${name}
• Empresa / Fondo / Organización: ${company || '(No especificada)'}
• Correo Electrónico de Contacto: ${email}
• Teléfono / WhatsApp: ${phone}

DETALLE DE LA CONSULTA / MENSAJE:
------------------------------------------------------------
${message || '(El interesado no agregó un mensaje adicional; solicita contacto y dossier del proyecto)'}

ACLARACIONES DEL SISTEMA Y ENRUTAMIENTO INSTITUCIONAL:
------------------------------------------------------------
• Consultor Especialista Asignado: ${consultant.name}
• Especialidad del Consultor: ${consultant.specialties_es}
• Casilla del Consultor Asignado: ${consultant.internalEmail}
• Teléfono de Contacto del Consultor: ${consultant.phone}
• Estado Inicial de la Solicitud: Pendiente
• Canal de Ingreso: Showroom Oficial de Inversiones Energy CPY (inventarioenergycpy.github.io/showroom-energycpy/)
• Casilla Emisora Central: inventario.energycpy@gmail.com
• Copia Central (CC): inventario.energycpy@gmail.com, energycpy@gmail.com
• Aviso de Confidencialidad: Esta consulta contiene información comercial confidencial destinada exclusivamente al equipo de consultores de Energy CPY.
============================================================`;

    // Despacho asíncrono silencioso vía FormSubmit a inventario.energycpy@gmail.com con CC al consultor
    try {
        fetch("https://formsubmit.co/ajax/inventario.energycpy@gmail.com", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify({
                _subject: emailSubject,
                _cc: `${consultant.internalEmail},energycpy@gmail.com`,
                _replyto: email,
                ticket_id: leadId,
                nombre_interesado: name,
                empresa_interesado: company || "No especificada",
                email_interesado: email,
                telefono_interesado: phone,
                proyecto_interes: topic,
                consultor_asignado: `${consultant.name} (${consultant.internalEmail})`,
                cuenta_origen: "inventario.energycpy@gmail.com",
                mensaje_consulta: message || "Sin observaciones adicionales",
                fecha_registro: leadRecord.dateFormatted
            })
        }).catch(e => console.log("FormSubmit central dispatch:", e));
    } catch (e) {
        console.warn("Silent background fetch:", e);
    }

    // Secondary dispatch directly to consultant's mailbox
    try {
        fetch(`https://formsubmit.co/ajax/${consultant.internalEmail}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify({
                _subject: emailSubject,
                _replyto: "inventario.energycpy@gmail.com",
                ticket_id: leadId,
                aviso: `Estimado/a ${consultant.name}, se le ha asignado una nueva consulta recibida en el Showroom de Inversiones Energy CPY.`,
                nombre_interesado: name,
                empresa_interesado: company || "No especificada",
                email_interesado: email,
                telefono_interesado: phone,
                proyecto_interes: topic,
                mensaje_consulta: message || "Sin observaciones adicionales",
                fecha_registro: leadRecord.dateFormatted
            })
        }).catch(e => console.log("FormSubmit consultant direct dispatch:", e));
    } catch (e) {}

    // Enlace interno Gmail (para apertura administrativa desde inventario.energycpy@gmail.com)
    const internalGmailUrl = `https://mail.google.com/mail/?view=cm&fs=1` +
        `&to=${encodeURIComponent(consultant.internalEmail)}` +
        `&cc=${encodeURIComponent("inventario.energycpy@gmail.com,energycpy@gmail.com")}` +
        `&su=${encodeURIComponent(emailSubject)}` +
        `&body=${encodeURIComponent(emailBodyText)}`;

    // 3. AVISAR AL CLIENTE: Notificación formal de confirmación y espera de respuesta
    const formEl = document.getElementById("contactForm");
    const successDiv = document.getElementById("formSuccessMessage");
    if (formEl) formEl.style.display = "none";
    if (successDiv) {
        successDiv.style.display = "block";
        successDiv.innerHTML = `
            <div class="success-alert-card" style="text-align: left; padding: 24px; background: rgba(15, 23, 42, 0.95); border: 1px solid rgba(245, 208, 97, 0.35); border-radius: 12px; box-shadow: 0 15px 40px rgba(0,0,0,0.6);">
                <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 16px;">
                    <div style="width: 44px; height: 44px; border-radius: 50%; background: rgba(34, 197, 94, 0.15); color: #22c55e; display: flex; align-items: center; justify-content: center; font-size: 1.4rem;">
                        <i class="fa-solid fa-circle-check"></i>
                    </div>
                    <div>
                        <h3 style="margin: 0; font-size: 1.25rem; color: #f8fafc; font-weight: 800;">
                            ${isEn ? 'Inquiry Sent Successfully!' : '¡Su consulta ha sido enviada con éxito!'}
                        </h3>
                        <span style="font-size: 0.78rem; color: var(--accent-gold); font-weight: 700;">Ticket Ref: ${leadId}</span>
                    </div>
                </div>

                <p style="font-size: 0.92rem; color: #cbd5e1; line-height: 1.5; margin-bottom: 16px;">
                    ${isEn 
                      ? 'We have successfully received your information request and meeting schedule. <strong>All your information has been securely and confidentially registered in our systems.</strong>' 
                      : 'Hemos recibido correctamente su solicitud de información y coordinación para el proyecto. <strong>Todos sus datos han sido registrados de forma confidencial y segura en nuestros sistemas.</strong>'}
                </p>

                <div style="background: rgba(56, 189, 248, 0.08); border-left: 4px solid var(--accent-cyan); padding: 12px 16px; border-radius: 0 8px 8px 0; margin-bottom: 18px; font-size: 0.88rem; color: #e0f2fe; display: flex; align-items: flex-start; gap: 10px;">
                    <i class="fa-solid fa-clock" style="margin-top: 3px; color: var(--accent-cyan);"></i>
                    <span>
                        ${isEn 
                          ? '<strong>Please expect a prompt response.</strong> Our specialist consultant for this investment sector has already been notified and will contact you shortly via email or phone.' 
                          : '<strong>Por favor espere una respuesta a la brevedad.</strong> Nuestro consultor especialista asignado para este sector ya ha sido notificado y se comunicará con usted a través del correo o teléfono suministrado.'}
                    </span>
                </div>

                <!-- Resumen de Datos Registrados para el Cliente -->
                <div style="background: rgba(2, 6, 23, 0.7); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 14px 18px; margin-bottom: 20px;">
                    <div style="font-size: 0.75rem; text-transform: uppercase; color: #94a3b8; font-weight: 700; margin-bottom: 10px; letter-spacing: 0.05em;">
                        ${isEn ? 'Registered Inquiry Details' : 'Constancia de Solicitud Registrada'}:
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr; gap: 6px; font-size: 0.85rem;">
                        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 4px;">
                            <span style="color: #94a3b8;">${isEn ? 'Client / Investor' : 'Interesado'}:</span>
                            <span style="color: #f8fafc; font-weight: 600;">${name}${company ? ' (' + company + ')' : ''}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 4px;">
                            <span style="color: #94a3b8;">Email:</span>
                            <span style="color: #f8fafc;">${email}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 4px;">
                            <span style="color: #94a3b8;">Teléfono / WhatsApp:</span>
                            <span style="color: #f8fafc;">${phone}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 4px;">
                            <span style="color: #94a3b8;">${isEn ? 'Opportunity' : 'Proyecto'}:</span>
                            <span style="color: var(--accent-gold); font-weight: 700;">${topic}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; padding-top: 2px;">
                            <span style="color: #94a3b8;">${isEn ? 'Assigned Desk' : 'Consultor Notificado'}:</span>
                            <span style="color: #38bdf8; font-weight: 600;">${consultant.name} (${consultant.specialties_es.split(',')[0]})</span>
                        </div>
                    </div>
                </div>

                <!-- Botones de Acción -->
                <div style="display: flex; flex-direction: column; gap: 10px;">
                    <button type="button" onclick="resetContactForm()" class="btn btn-outline-gold btn-block" style="display: flex; align-items: center; justify-content: center; gap: 8px;">
                        <i class="fa-solid fa-arrow-rotate-left"></i> ${isEn ? 'Submit another inquiry' : 'Enviar otra consulta o consultar otro proyecto'}
                    </button>
                    
                    <!-- Nota Interna de Respaldo Institucional -->
                    <div style="font-size: 0.72rem; color: #64748b; text-align: center; border-top: 1px dashed rgba(255,255,255,0.1); padding-top: 10px; margin-top: 6px;">
                        <i class="fa-solid fa-shield-halved"></i> ${isEn 
                          ? `Internal dispatch routed to ${consultant.name} via inventario.energycpy@gmail.com` 
                          : `Notificación interna derivada a ${consultant.name} (${consultant.internalEmail}) vía inventario.energycpy@gmail.com`}
                        <br>
                        <a href="${internalGmailUrl}" target="_blank" rel="noopener" style="color: #38bdf8; text-decoration: underline; margin-top: 4px; display: inline-block;">
                            [Acceso Consultor/Admin] Abrir confirmación interna en Gmail
                        </a>
                    </div>
                </div>
            </div>
        `;
    }
}

function resetContactForm() {
    document.getElementById("contactForm").reset();
    document.getElementById("contactForm").style.display = "block";
    document.getElementById("formSuccessMessage").style.display = "none";
    updateFormSpecialistBadge();
}

/* ==========================================================================
   5. Consultant Admin Panel & Project Status Management (Email Protected)
   ========================================================================== */
function openAdminAuthModal() {
    const modal = document.getElementById("adminAuthModal");
    if (!modal) return;

    document.getElementById("adminEmailInput").value = "";
    document.getElementById("adminAuthError").style.display = "none";
    document.getElementById("adminAuthStep").style.display = "block";
    document.getElementById("adminPanelStep").style.display = "none";

    modal.classList.add("active");
    document.body.style.overflow = "hidden";
}

function closeAdminModal() {
    const modal = document.getElementById("adminAuthModal");
    if (modal) modal.classList.remove("active");
    document.body.style.overflow = "";
}

function validateAdminEmail() {
    const input = document.getElementById("adminEmailInput").value.trim().toLowerCase();
    const errorEl = document.getElementById("adminAuthError");

    if (AUTHORIZED_ADMIN_EMAILS.includes(input)) {
        errorEl.style.display = "none";
        document.getElementById("adminAuthStep").style.display = "none";
        document.getElementById("adminPanelStep").style.display = "block";
        renderAdminProjectRows();
    } else {
        errorEl.style.display = "block";
        errorEl.innerText = currentLang === "en" ? "Unauthorized consultant email." : "Correo electrónico no autorizado.";
    }
}

function renderAdminProjectRows() {
    const container = document.getElementById("adminProjectList");
    if (!container) return;

    container.innerHTML = "";

    Object.keys(PROJECTS_DATA).forEach(projectId => {
        const p = PROJECTS_DATA[projectId];
        const status = projectStatuses[projectId] || p.defaultStatus || "activo";
        const langData = p[currentLang] || p.es;

        const row = document.createElement("div");
        row.className = "admin-project-item";
        row.innerHTML = `
            <div class="admin-project-info">
                <strong>${langData.title}</strong>
                <span class="admin-project-cat">${langData.categoryTag} | ${p.amountDisplay}</span>
            </div>
            <div class="admin-status-select-wrap">
                <select id="adminStatus_${projectId}" class="admin-select" onchange="updateProjectStatusLive('${projectId}', this.value)">
                    <option value="activo" ${status === 'activo' ? 'selected' : ''}>🔵 Activo (Azul)</option>
                    <option value="tramite" ${status === 'tramite' ? 'selected' : ''}>🟡 En trámite (Amarillo)</option>
                    <option value="vendido" ${status === 'vendido' ? 'selected' : ''}>🟢 Vendido (Verde)</option>
                </select>
            </div>
        `;
        container.appendChild(row);
    });
}

function updateProjectStatusLive(projectId, newStatus) {
    projectStatuses[projectId] = newStatus;
    saveProjectStatusesToStorage();
    renderProjectCards();
    applyFilters();
}

function saveAdminChangesAndClose() {
    saveProjectStatusesToStorage();
    renderProjectCards();
    applyFilters();
    closeAdminModal();
}

/* ==========================================================================
   6. Modal & Slide Viewer Functions
   ========================================================================== */
let isObservationsPanelVisible = true;

function togglePresentationObservations(forceState) {
    const container = document.getElementById("projectModalContainer");
    const toggleBtn = document.getElementById("toggleObservationsBtn");
    const toggleIcon = document.getElementById("toggleObservationsIcon");
    const toggleText = document.getElementById("toggleObservationsText");
    const edgeBtn = document.getElementById("edgeToggleBtn");
    const edgeIcon = document.getElementById("edgeToggleIcon");
    if (!container) return;

    if (typeof forceState === "boolean") {
        isObservationsPanelVisible = forceState;
    } else {
        isObservationsPanelVisible = !isObservationsPanelVisible;
    }

    const dict = TRANSLATIONS[currentLang] || TRANSLATIONS.es;
    const hideText = (dict && dict.toggle_obs_hide) ? dict.toggle_obs_hide : "Ocultar Observaciones";
    const showText = (dict && dict.toggle_obs_show) ? dict.toggle_obs_show : "Ver Observaciones";

    if (isObservationsPanelVisible) {
        container.classList.remove("observations-collapsed");
        if (toggleText) toggleText.innerText = hideText;
        if (toggleIcon) toggleIcon.className = "fa-solid fa-table-columns";
        if (toggleBtn) {
            toggleBtn.setAttribute("title", `${hideText} y Ficha Técnica (Tecla O)`);
            toggleBtn.setAttribute("aria-expanded", "true");
        }
        if (edgeIcon) edgeIcon.className = "fa-solid fa-chevron-right";
        if (edgeBtn) edgeBtn.setAttribute("title", hideText);
    } else {
        container.classList.add("observations-collapsed");
        if (toggleText) toggleText.innerText = showText;
        if (toggleIcon) toggleIcon.className = "fa-solid fa-bars-staggered";
        if (toggleBtn) {
            toggleBtn.setAttribute("title", `${showText} y Ficha Técnica (Tecla O)`);
            toggleBtn.setAttribute("aria-expanded", "false");
        }
        if (edgeIcon) edgeIcon.className = "fa-solid fa-chevron-left";
        if (edgeBtn) edgeBtn.setAttribute("title", showText);
    }
}

function openProjectModal(projectId) {
    const project = PROJECTS_DATA[projectId];
    if (!project) return;

    currentProjectId = projectId;
    currentSlideIndex = 1;
    totalSlidesInCurrentProject = project.totalSlides;
    const langData = project[currentLang] || project.es;
    const dict = TRANSLATIONS[currentLang];
    const status = projectStatuses[projectId] || project.defaultStatus || "activo";

    // Set Modal Header & Text
    document.getElementById("modalTag").innerText = langData.categoryTag;
    document.getElementById("modalTitle").innerText = langData.title;
    document.getElementById("modalDesc").innerText = langData.description;

    // Set Status Badge in modal
    let statusClass = "status-badge-activo";
    let statusText = dict.card_status_activo;
    if (status === "tramite") {
        statusClass = "status-badge-tramite";
        statusText = dict.card_status_tramite;
    } else if (status === "vendido") {
        statusClass = "status-badge-vendido";
        statusText = dict.card_status_vendido;
    }
    const modalStatus = document.getElementById("modalStatusBadge");
    if (modalStatus) {
        modalStatus.className = `card-status-badge ${statusClass}`;
        modalStatus.innerHTML = `<span class="status-indicator-dot"></span> ${statusText}`;
    }

    // Set One-Pager & WhatsApp Links (Presentation PDF download disabled - only 1-page executive summary enabled)
    const onePagerBtn = document.getElementById("modalOnePagerBtn");
    if (onePagerBtn) {
        onePagerBtn.onclick = () => openOnePager(projectId);
    }
    const pdfBtn = document.getElementById("modalPdfBtn");
    if (pdfBtn) {
        pdfBtn.removeAttribute("href");
        pdfBtn.removeAttribute("download");
        pdfBtn.onclick = (e) => { e.preventDefault(); openOnePager(projectId); };
    }

    const wspDiazBtn = document.getElementById("modalWspDiaz");
    const wspGonzalezBtn = document.getElementById("modalWspGonzalez");
    const wspText = encodeURIComponent(`Hola, solicito la ficha técnica e información del proyecto "${langData.title}".`);
    if (wspDiazBtn) wspDiazBtn.href = `https://wa.me/5493512064791?text=${wspText}`;
    if (wspGonzalezBtn) wspGonzalezBtn.href = `https://wa.me/5492974233028?text=${wspText}`;

    // Render Highlights
    const highlightsUl = document.getElementById("modalHighlights");
    highlightsUl.innerHTML = langData.highlights.map(h => `<li>${h}</li>`).join("");

    // Render Metrics Summary
    const metricsDiv = document.getElementById("modalMetrics");
    metricsDiv.innerHTML = langData.metrics.map(m => `
        <div class="stat-card" style="padding: 12px; text-align: center;">
            <span class="metric-val ${m.color}">${m.val}</span>
            <span class="metric-lbl" style="display: block; font-size: 0.75rem;">${m.label}</span>
        </div>
    `).join("");

    // Render Slide Image, Counter & Thumbnails
    updateSlideDisplay();
    renderThumbnails();

    // Sincronizar estado del panel de observaciones
    togglePresentationObservations(isObservationsPanelVisible);

    // Show Modal
    const modal = document.getElementById("projectModal");
    modal.classList.add("active");
    document.body.style.overflow = "hidden";
}

function updateSlideDisplay() {
    const project = PROJECTS_DATA[currentProjectId];
    if (!project) return;

    const img = document.getElementById("modalSlideImg");
    img.src = `${project.slidePrefix}${currentSlideIndex}.png`;

    const counter = document.getElementById("slideCounter");
    const dict = TRANSLATIONS[currentLang];
    counter.innerText = currentLang === "en" 
        ? `Slide ${currentSlideIndex} of ${totalSlidesInCurrentProject}` 
        : `Diapositiva ${currentSlideIndex} de ${totalSlidesInCurrentProject}`;

    // Highlight active thumbnail
    const thumbs = document.querySelectorAll("#modalThumbnails .slide-thumb");
    thumbs.forEach((t, idx) => {
        if (idx + 1 === currentSlideIndex) {
            t.classList.add("active");
            t.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
        } else {
            t.classList.remove("active");
        }
    });
}

function renderThumbnails() {
    const project = PROJECTS_DATA[currentProjectId];
    const container = document.getElementById("modalThumbnails");
    container.innerHTML = "";

    for (let i = 1; i <= project.totalSlides; i++) {
        const thumb = document.createElement("img");
        thumb.src = `${project.slidePrefix}${i}.png`;
        thumb.alt = `Slide ${i}`;
        thumb.className = `slide-thumb ${i === currentSlideIndex ? 'active' : ''}`;
        thumb.onclick = () => {
            currentSlideIndex = i;
            updateSlideDisplay();
        };
        container.appendChild(thumb);
    }
}

function changeSlide(direction) {
    currentSlideIndex += direction;
    if (currentSlideIndex < 1) {
        currentSlideIndex = totalSlidesInCurrentProject;
    } else if (currentSlideIndex > totalSlidesInCurrentProject) {
        currentSlideIndex = 1;
    }
    updateSlideDisplay();
}

function closeProjectModal() {
    const modal = document.getElementById("projectModal");
    modal.classList.remove("active");
    document.body.style.overflow = "";
}

function closeModalOnBackdrop(event) {
    if (event.target.classList.contains("modal-backdrop")) {
        closeProjectModal();
        closeAdminModal();
        closeOnePager();
    }
}

function initKeyboardNavigation() {
    document.addEventListener("keydown", (e) => {
        const modal = document.getElementById("projectModal");
        const adminModal = document.getElementById("adminAuthModal");

        if (modal && modal.classList.contains("active")) {
            if (e.key === "ArrowLeft") changeSlide(-1);
            else if (e.key === "ArrowRight") changeSlide(1);
            else if (e.key === "Escape") closeProjectModal();
            else if (e.key === "o" || e.key === "O") togglePresentationObservations();
        }

        if (adminModal && adminModal.classList.contains("active") && e.key === "Escape") {
            closeAdminModal();
        }
    });
}

/* ==========================================================================
   7. Animated Number Counters & Mobile Menu
   ========================================================================== */
function initAnimatedCounters() {
    const statCards = document.querySelectorAll(".stat-number");
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseFloat(entry.target.getAttribute("data-target"));
                animateValue(entry.target, 0, target, 2000);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    statCards.forEach(card => observer.observe(card));
}

function animateValue(obj, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        const currentVal = (progress * (end - start) + start);
        
        if (end >= 1000) {
            // Formatted as USD 4.116,5M
            const formatted = currentVal.toLocaleString('es-AR', {
                minimumFractionDigits: 1,
                maximumFractionDigits: 1
            });
            obj.innerHTML = `USD ${formatted}M`;
        } else if (end === 50) {
            obj.innerHTML = `${Math.round(currentVal)}%`;
        } else if (end === 25) {
            obj.innerHTML = `+${Math.round(currentVal)} Años`;
        } else if (end === 20) {
            obj.innerHTML = `${Math.round(currentVal)} Años`;
        } else {
            obj.innerHTML = currentVal.toFixed(end % 1 === 0 ? 0 : 1);
        }

        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

function initMobileMenu() {
    const btn = document.getElementById("mobileMenuBtn");
    const nav = document.getElementById("navLinks");
    
    if (btn && nav) {
        btn.addEventListener("click", () => {
            nav.classList.toggle("mobile-active");
            btn.innerHTML = nav.classList.contains("mobile-active") ? '<i class="fa-solid fa-xmark"></i>' : '<i class="fa-solid fa-bars"></i>';
        });

        // Close menu on link click
        nav.querySelectorAll("a").forEach(link => {
            link.addEventListener("click", () => {
                nav.classList.remove("mobile-active");
                btn.innerHTML = '<i class="fa-solid fa-bars"></i>';
            });
        });
    }
}



/* ==========================================================================
   ONE-PAGER EXECUTIVE SUMMARY MODAL & PRINT CONTROLLER (ENERGY CPY)
   ========================================================================== */

function openOnePager(projectId, event) {
    if (event) {
        event.preventDefault();
        event.stopPropagation();
    }

    const p = PROJECTS_DATA[projectId];
    if (!p) return;

    const modal = document.getElementById("onePagerModal");
    const container = document.getElementById("onePagerContent");
    if (!modal || !container) return;

    const langData = p[currentLang] || p.es;
    const consultant = CONSULTANTS[p.assignedAgent] || CONSULTANTS.daniel;
    const isEn = (currentLang === "en");

    const amountLabel = p.isPrivatePlacement 
        ? (isEn ? "Exclusive Invitation Only" : "A Invitación Exclusiva") 
        : p.amountDisplay;

    const dealTypeLabel = p.dealType || p.modality || (isEn ? "Direct Deal" : "Venta / Socio Inversor");
    const roiLabel = p.roi || "N/A";
    const tirProjectVal = p.tir && p.tir !== "Consulte" ? p.tir : ">9%";
    const statusProg = p.statusProgress || (isEn ? "Active in Portfolio" : "Activo en Cartera");

    const highlightsHtml = (langData.highlights || []).map(h => `
        <li><i class="fa-solid fa-circle-check"></i> <span>${h}</span></li>
    `).join("");

    const tirCategory = getTirCategory(p.tir, isEn);

    const metricsHtml = [
        { label: isEn ? "Target Ticket" : "Ticket Inversión", val: amountLabel, color: "text-gold" },
        { label: tirCategory, val: `${tirProjectVal}`, color: "text-green" },
        { label: isEn ? "Operating EBITDA" : "EBITDA Anual", val: p.ebitda || "Proyectado", color: "text-cyan" },
        { label: isEn ? "Deal & Recovery" : "Oferta & Payback", val: `${dealTypeLabel} / ${roiLabel}`, color: "text-gold" }
    ].map(m => `
        <div class="op-metric-box">
            <div class="op-metric-val ${m.color}">${m.val}</div>
            <div class="op-metric-lbl">${m.label}</div>
        </div>
    `).join("");

    const wspMsg = encodeURIComponent(
        isEn 
        ? `Hello ${consultant.name}, I am contacting you from Energy CPY Showroom regarding project: ${langData.title} (Ref: ECPY-${p.id.toUpperCase()}). Classification: ${tirCategory} (Modeled: ${tirProjectVal}). Please provide financial memorandum.`
        : `Hola ${consultant.name}, me contacto desde el Showroom de Energy CPY por la propuesta: ${langData.title} (Ref: ECPY-${p.id.toUpperCase()}). Clasificación: ${tirCategory} (Proyectada: ${tirProjectVal}). Deseo solicitar memoria financiera.`
    );

    const wspUrl = `https://wa.me/${consultant.phoneClean}?text=${wspMsg}`;

    // Local and International Market Trends
    const localTrendText = (langData.marketTrend && langData.marketTrend.local) ? langData.marketTrend.local : (langData.thesis || "");
    const intlTrendText = (langData.marketTrend && langData.marketTrend.intl) ? langData.marketTrend.intl : (isEn ? "Sustained global commodity demand and institutional capital inflows." : "Demanda global sostenida de commodities y flujos de capital institucional.");

    // Financial note per Financial Analyst protocol
    const finNote = isEn 
        ? (p.financialNote_en || "IRR calculated via Discounted Cash Flows (DCF) over asset economic life, comfortably exceeding the minimum hurdle rate (Target IRR >9% USD per annum).")
        : (p.financialNote_es || "Cálculo de TIR proyectado mediante Flujo de Fondos Descontados (DCF) con horizonte de vida útil del activo, superando la Tasa de Corte mínima de referencia (TIR objetivo >9% anual en USD).");

    container.innerHTML = `
        <!-- Header -->
        <div class="op-header">
            <div>
                <div class="op-brand-title">ENERGY CPY</div>
                <div class="op-brand-sub">${isEn ? "PRIVATE INVESTMENT ADVISORY — ARGENTINA" : "ASESORAMIENTO PRIVADO DE INVERSIONES — ARGENTINA"}</div>
            </div>
            <div class="op-meta-box">
                <div class="op-ref-code">REF: ECPY-${p.id.toUpperCase()}</div>
                <div class="op-confidential-badge">${isEn ? "CONFIDENTIAL / INVESTMENT GRADE" : "CONFIDENCIAL / GRADO DE INVERSIÓN"}</div>
            </div>
        </div>

        <!-- Title & Location -->
        <div class="op-title-section">
            <span class="op-tag-pill tag-${p.category}">${langData.categoryTag}</span>
            <h1 class="op-project-title">${langData.title}</h1>
            <div class="op-location">
                <i class="fa-solid fa-location-dot"></i> ${langData.location}
            </div>
        </div>

        <!-- 4-Item Deal Terms Bar with Mandatory TIR Objetivo: >9% -->
        <div class="op-deal-bar">
            <div class="op-deal-col">
                <span class="op-deal-lbl">${isEn ? "Target Ticket" : "Monto Inversión"}</span>
                <span class="op-deal-val">${amountLabel}</span>
            </div>
            <div class="op-deal-col">
                <span class="op-deal-lbl">${isEn ? "Deal Type / Offer" : "Tipo de Oferta"}</span>
                <span class="op-deal-val">${dealTypeLabel}</span>
            </div>
            <div class="op-deal-col">
                <span class="op-deal-lbl" style="color: #34d399; font-weight: 700;">${tirCategory}</span>
                <span class="op-deal-val text-green" style="font-weight: 800;">${isEn ? 'Modeled: ' + tirProjectVal : 'TIR Proyectada: ' + tirProjectVal}</span>
            </div>
            <div class="op-deal-col">
                <span class="op-deal-lbl">${isEn ? "Est. Payback / Recovery" : "Retorno / Payback"}</span>
                <span class="op-deal-val">${roiLabel}</span>
            </div>
        </div>

        <!-- Body: Summary & Strategic Highlights -->
        <div class="op-body-grid">
            <div class="op-card-block">
                <div class="op-block-title">
                    <i class="fa-solid fa-briefcase"></i> ${isEn ? "Executive Summary & Asset Overview" : "Resumen Ejecutivo de la Actividad & Activo"}
                </div>
                <p class="op-desc-text">${langData.description}</p>
                ${langData.thesis ? `
                <div class="op-thesis-box">
                    <strong>${isEn ? "Financial Thesis: " : "Tesis Financiera: "}</strong>${langData.thesis}
                </div>` : ''}
            </div>

            <div class="op-card-block">
                <div class="op-block-title">
                    <i class="fa-solid fa-star"></i> ${isEn ? "Strategic Value Drivers & Key Terms" : "Factores Críticos de Valor & Aspectos Clave"}
                </div>
                <ul class="op-highlights-list">
                    ${highlightsHtml}
                </ul>
            </div>
        </div>

        <!-- Financial Analyst Protocol: IRR Calculation & Methodology Box -->
        <div class="op-financial-protocol-box">
            <div class="op-block-title">
                <i class="fa-solid fa-calculator" style="color: #f5d061;"></i> ${isEn ? "Financial Protocol: IRR Calculation & Hurdle Benchmark" : "Protocolo Analista Financiero: Cálculo de TIR & Tasa de Corte"}
            </div>
            <div class="op-financial-grid">
                <div class="op-fin-item">
                    <span class="op-fin-lbl">${isEn ? "IRR Classification:" : "Calificación de Rentabilidad:"}</span>
                    <span class="op-fin-val text-green" style="font-weight: 800;">${tirCategory}</span>
                </div>
                <div class="op-fin-item">
                    <span class="op-fin-lbl">${isEn ? "Project Modeled IRR:" : "TIR Proyectada del Activo:"}</span>
                    <span class="op-fin-val text-gold">${tirProjectVal} (${tirCategory})</span>
                </div>
                <div class="op-fin-item">
                    <span class="op-fin-lbl">${isEn ? "Projected Cash Flow / EBITDA:" : "EBITDA Anual / Flujo Proyectado:"}</span>
                    <span class="op-fin-val text-cyan">${p.ebitda || "Auditado"}</span>
                </div>
                <div class="op-fin-item">
                    <span class="op-fin-lbl">${isEn ? "Capital & Legal Framework:" : "Estructura & Marco Regulatorio:"}</span>
                    <span class="op-fin-val">${p.regulatoryRegime || "Vigente"}</span>
                </div>
            </div>
            <div class="op-fin-note">
                <i class="fa-solid fa-circle-check"></i>
                <span><strong>${isEn ? "Calculation Basis: " : "Memoria de Cálculo: "}</strong>${finNote}</span>
            </div>
        </div>

        <!-- Market Trends: Local & International -->
        <div class="op-market-trend-container">
            <div class="op-block-title">
                <i class="fa-solid fa-earth-americas" style="color: #10b981;"></i> ${isEn ? "Market Outlook & Local/International Trends" : "Tendencia de Mercado Local e Internacional"}
            </div>
            <div class="op-market-grid">
                <div class="op-market-card op-market-local">
                    <div class="op-market-tag"><i class="fa-solid fa-location-crosshairs"></i> ${isEn ? "Domestic Argentine Market" : "Mercado Local (Argentina)"}</div>
                    <p class="op-market-text">${localTrendText}</p>
                </div>
                <div class="op-market-card op-market-intl">
                    <div class="op-market-tag"><i class="fa-solid fa-globe"></i> ${isEn ? "Global / International Demand" : "Mercado Internacional"}</div>
                    <p class="op-market-text">${intlTrendText}</p>
                </div>
            </div>
        </div>

        <!-- 4-Metrics Grid -->
        <div class="op-metrics-grid">
            ${metricsHtml}
        </div>

        <!-- Consultant Info & Direct Contact -->
        <div class="op-footer-box">
            <div class="op-consultant-info">
                <div class="op-consultant-avatar">${consultant.name.charAt(0)}</div>
                <div>
                    <div class="op-consultant-name">${consultant.name}</div>
                    <div class="op-consultant-role">${isEn ? consultant.role_en : consultant.role_es}</div>
                </div>
            </div>
            <div class="op-consultant-links no-print">
                <a href="${wspUrl}" target="_blank" class="op-btn-wsp">
                    <i class="fa-brands fa-whatsapp"></i> WhatsApp Directo
                </a>
                <a href="mailto:${consultant.internalEmail}?subject=Consulta%20Inversion%20${encodeURIComponent(langData.title)}" class="op-btn-email">
                    <i class="fa-solid fa-envelope"></i> Email
                </a>
            </div>
        </div>

        <!-- Legal Disclaimer -->
        <div class="op-legal-disclaimer">
            <strong>${isEn ? "LEGAL DISCLAIMER:" : "AVISO LEGAL Y CONFIDENCIALIDAD:"}</strong> 
            ${isEn 
                ? "This document is strictly confidential and issued by Energy CPY for preliminary informative evaluation only. It does not constitute a public offering of securities or a binding contractual commitment. Financial memorandums, dataroom access, and detailed technical records are disclosed exclusively under a signed Non-Disclosure Agreement (NDA)."
                : "Este documento es de carácter estrictamente confidencial y ha sido emitido por Energy CPY con fines informativos de evaluación preliminar. No constituye oferta pública de valores ni promesa de contrato vinculante. La entrega de memorias económicas, acceso a Data Room y dossiers técnicos queda supeditada a la firma previa de un Acuerdo de Confidencialidad (NDA)."}
        </div>
    `;

    modal.style.display = "flex";
    document.body.style.overflow = "hidden";
}

function closeOnePager() {
    const modal = document.getElementById("onePagerModal");
    if (modal) {
        modal.style.display = "none";
    }
    document.body.style.overflow = "auto";
}

function printOnePager() {
    window.print();
}

function requestPrivateAccess(projectId) {
    openOnePager(projectId);
}
