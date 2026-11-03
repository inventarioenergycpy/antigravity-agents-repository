---
title: "Sincronización de Cartera de Inversiones Energy CPY: Dashboard de Gestión y Showroom Web"
tags:
  - #inversiones
  - #showroom
  - #dashboard
  - #onepager
  - #financial-advisory
  - #energycpy
created: 2026-10-21
updated: 2026-10-21
---

# 📊 Sincronización Integral de la Cartera de Inversiones Energy CPY

Integración arquitectónica y financiera entre el **Dashboard de Gestión de Intermediación** ([dashboard-gestion-intermediacion](https://github.com/inventarioenergycpy/dashboard-gestion-intermediacion)) y el **Showroom Web de Inversiones** ([showroom-energycpy](https://github.com/inventarioenergycpy/showroom-energycpy)).

---

## 🏛️ 1. Arquitectura de Datos y Sincronización
- **Archivo Maestro Compartido**: `data/projects-master.json` como *Single Source of Truth* (SSOT) para 27 proyectos y verticales en 6 sectores estratégicos.
- **Ramas de Desarrollo Activas**: `feat/cartera-inversiones-sincronizada` en ambos repositorios locales.
- **Mapeo de Estados**: Control de avance en Dashboard (`activo`, `suspendido`, `bloqueado_por_gestion`, `vendido`) reflejado dinámicamente en el catálogo del Showroom.

---

## 💼 2. Resumen de Sectores y Proyectos Sincronizados

### A. Energía Solar & Renovable (3 Proyectos)
1. **Parque Solar Sol de los Cuatro Vientos 300 MW** (Mendoza): USD 300M — Socio Inversor (ROI 7 Años).
2. **Parque Solar 30 MW Vaca Muerta** (Añelo, Neuquén): USD 30M — Socio Inversor (ROI 5 Años).
3. **Plantas Solares Llave en Mano** (Cuyo/NOA): USD 50M (50% Pre-Financiado por fabricante Tier 1).

### B. Hospitality / Hotelería & Casinos (4 Proyectos)
4. **Hotel 3★ + Casino + Salón de Eventos** (Mendoza): USD 40M — Venta Directa (ROI 1 Año).
5. **Hotel 5★ (72 Hab.) + Casino + Cocheras** (Mendoza): USD 60M — Venta Directa (ROI 1 Año).
6. **Hotel de Lujo en Bariloche**: Venta Exclusiva por Invitación (Private Placement Off-Market / Acceso bajo NDA).
7. **Hotel de Lujo en Córdoba**: Venta Exclusiva por Invitación (Private Placement Off-Market / Acceso bajo NDA).

### C. Agro, Campo & Industria (2 Proyectos)
8. **Estancia 17.000 Hectáreas con Riego** (Región Centro): USD 60M — Venta Directa (ROI 2 Años).
9. **Planta Avícola + Red Distribución (Avex)** (Río Cuarto, Cba.): USD 5M — Socio Inversor (ROI 7 Años).

### D. Minería & Minerales Críticos (5 Proyectos)
10. **Yacimiento de Oro 'Diente Oro Verde'** (San Luis): USD 60M — Venta (A certificar NI 43-101).
11. **Canteras y Yacimiento de Mármol** (San Luis): USD 50M — Venta Directa.
12. **Yacimiento de Oro en Producción 28 t/d** (San Juan): USD 100M - 200M — Socio Inversor para ampliación.
13. **Yacimiento de Litio** (Catamarca): USD 11M — Venta (Exploración OK / Salmueras).
14. **Proyecto Minero de Oro 'Mina San Antonio'** (Iglesia, San Juan): USD 25M - 50M — Venta / Socio Inversor (Concesión 2.708 ha, NI 43-101, leyes hasta 65,7 g/t Au, Oro Visible, Canon 2025 al día, Plan Art. 217 aprobado e IIA integrado).

### E. Petróleo, Gas & Infraestructura Downstream/Upstream (7 Proyectos)
15. **Refipampa + Yacimiento Medanito (500 Pozos)** (La Pampa): USD 180M — Venta Integral (Dataroom Listo).
16. **REFINOR — Complejo de Refinación y Poliductos** (Campo Durán, Salta): USD 50M — Venta Directa (4.000 m³/d).
17. **Proyecto Salta - GARRIDO (25 Áreas)**: USD 1.870M — Socio Inversor / UTE (Concesión 20 Años crudo y gas).
18. **Palermo Aike Chubut**: Socio Inversor — Plan No Convencional presentado por Chubut.
19. **3 Refinerías en Vaca Muerta + Puerto de Aguas Profundas** (Bahía Blanca): USD 350M — Venta Llave en Mano 6 meses.
20. **Operadora 15 Concesiones Vaca Muerta** (Cuenca Neuquina): USD 340M — Socio Inversor (1.200 pozos en 3.000 km²).
21. **Proyecto Pozo Salta**: USD 15M CAPEX — Tratamiento y secado de cuttings (Recupero 3 Años).

### F. Asesoramiento Financiero & Fiduciario (4 Servicios)
22. **Gestión y Administración Integral de Grupos Inversores**: Mandato Privado FDI / Cartelera curada.
23. **Financiamiento de Proyectos Gubernamentales**: Bonos verdes, fideicomisos y marco RIGI / PPP.
24. **Gestión de Proyectos de Bienes Raíces & Construcción**: Parques industriales y fideicomisos al costo.
25. **ENERGY CPY Argentina REIT Investment Strategy 2026**: USD 30M Fondo Inmobiliario Dolarizado (10-12% anual).

### G. Pesca Industrial Gran Escala (2 Proyectos)
26. **Proyecto 6.6 — Pesca Industrial Gran Escala**: USD 260M CAPEX (Flota 16 buques / USD 600M/año ingresos).
27. **Proyecto 6.7 — Ecosistema Pesquero Integrado**: USD 5.5M CAPEX (Langostino salvaje Patagonia).

---

## 📑 3. Visor One-Pager (1 Página A4 con Marca de Agua)
- **Marca de Agua Oficial**: `ENERGY CPY — PRIVATE INVESTMENT ADVISORY` en diagonal semitransparente.
- **Formato A4 Estricto**: Dimensionado y estilizado con `@media print` para generar un PDF de 1 página exacta sin saltos no deseados.
- **Asignación Personalizada de Consultores**:
  - **Javier Ignacio Díaz**: Minería, Energía Renovable, Proyectos de Ingeniería y Proyectos en Inglés.
  - **Daniel González**: Hotelería, Petróleo & Gas, Pesca, Bienes Raíces y Asesoramiento Financiero.
