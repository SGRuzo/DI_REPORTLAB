# Importar las librerías necesarias de ReportLab para crear documentos PDF
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.pagesizes import A4  # Importar tamaño de página A4
from reportlab.lib import colors  # Importar módulo de colores
from reportlab.lib.styles import getSampleStyleSheet  # Importar estilos predefinidos
from reportlab.lib.styles import ParagraphStyle


def generar_formulario_simple():
    # Crear un documento PDF con tamaño A4 y guardarlo como "Formulario_Simple_ReportLab.pdf"
    doc = SimpleDocTemplate("Formulario_Simple_ReportLab.pdf", pagesize=A4)

    # Lista que contendrá todos los elementos del PDF (tablas, espaciadores, etc.)
    story = []

    # Obtener los estilos predefinidos de ReportLab (ej: Normal, Heading1, etc.)
    styles = getSampleStyleSheet()

    # Colores personalizados en formato RGB (valores 0-1)
    # Verde claro para el fondo de celdas normales
    lightverde = colors.Color(216 / 255, 235 / 255, 213 / 255)
    # Verde oscuro para encabezados y totales
    darkverde = colors.Color(35 / 255, 78 / 255, 25 / 255)

    # Crear estilo personalizado para H1 (Heading1 con color darkverde)
    style_h1 = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading1'],
        textColor=darkverde
    )

    # Crear estilo personalizado para H2 (Heading3 sin cursiva con color darkverde)
    style_h2 = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading3'],
        textColor=darkverde,
        fontName='Helvetica-Bold'  # Sin cursiva, solo bold
    )

    # Cargar imagen con tamaño de 100x100 píxeles
    I = Image('Gatogato.jpg', width=35, height=35)

    # Crear párrafo con estilo personalizado para el nombre de la empresa (color darkverde)
    H1 = Paragraph('''Nombre de tu Empresa''', style_h1)

    # Crear párrafo con estilo personalizado para el título "FACTURA SIMPLIFICADA" (Heading3, sin cursiva, color darkverde)
    # Matriz de datos que representa cada fila y columna de la tabla
    data = [
        # Fila 0: Título principal "FACTURA SIMPLIFICADA" (abarca varias columnas)
        ['', '', '', '','FACTURA SIMPLIFICADA' , ''],
        # Fila 1: Nombre de la empresa (será expandido con SPAN)
        [H1, '', '', '', '', I],
        # Fila 2: Dirección
        ['Dirección', '', '', '', '', ''],
        # Fila 3: Ciudad y País
        ['Ciudad y País', '', '', '', '', ''],
        # Fila 4: CIF/NIF a la izquierda, Fecha Emisión a la derecha
        ['CIF/NIF', '', '', '', 'Fecha Emisión', 'DD/MM/AAAA'],
        # Fila 5: Teléfono a la izquierda, Número de Factura a la derecha
        ['Teléfono', '', '', '', 'Número de Factura', 'A0001'],
        # Fila 6: Mail
        ['Mail', '', '', '', '', ''],
        # Fila 7: Fila vacía (espaciador visual)
        ['', '', '', '', '', ''],
        # Fila 8: Encabezados de la tabla de productos (Descripción, Importe, Cantidad, Total)
        ['Descripción', '', '', 'Importe', 'Cantidad', 'Total'],
        # Fila 9: Producto 1
        ['Producto 1', '', '', '3,2', '5', '16,00'],
        # Fila 10: Producto 2
        ['Producto 2', '', '', '2,1', '3', '6,30'],
        # Fila 11: Producto 3
        ['Producto 3', '', '', '2,9', '76', '220,40'],
        # Fila 12: Producto 4
        ['Producto 4', '', '', '5', '23', '115,00'],
        # Fila 13: Producto 5
        ['Producto 5', '', '', '4,95', '3', '14,85'],
        # Fila 14: Producto 6
        ['Producto 6', '', '', '6', '2', '12,00'],
        # Fila 15: Fila vacía pequeña (espaciador visual entre productos y total)
        ['', '', '', '', '', ''],
        # Fila 16: Fila de TOTAL con fondo verde oscuro
        ['', '', '', '', 'TOTAL', '385€'],
        # Fila 17: Fila vacía (espaciador antes del mensaje final)
        ['', '', '', '', '', ''],
        # Fila 18: Mensaje de agradecimiento (abarcará todas las columnas con SPAN)
        ['GRACIAS POR SU CONFIANZA', '', '', '', '', ''],
    ]

    # Crear una lista con las alturas de cada fila (por defecto 17 píxeles)
    row_heights = [17] * len(data)
    row_heights[0] = 30
    row_heights[1] = 40
    # Fila 16 (TOTAL): altura de 30 píxeles para que sea más visible
    row_heights[16] = 30
    # Fila 15 (espaciador): altura de 7 píxeles (muy pequeña)
    row_heights[15] = 7
    # Fila 17 (espaciador antes del mensaje): altura de 35 píxeles
    row_heights[17] = 35
    # Fila 18 (mensaje final): altura de 30 píxeles
    row_heights[18] = 30

    # Crear la tabla con los datos, ancho de columna de 80 y alturas de fila definidas arriba
    t1 = Table(data, colWidths=80, rowHeights=row_heights)

    # Aplicar estilos a la tabla usando TableStyle
    t1.setStyle(TableStyle([
        # Color de texto: negro en todas las celdas (por defecto)
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        # Color de texto: verde oscuro para las filas de encabezado (0-8)
        ('TEXTCOLOR', (0, 0), (-1, 8), darkverde),
        # Color de texto: blanco para el encabezado de productos (fila 8)
        ('TEXTCOLOR', (0, 8), (-1, 8), colors.white),
        # Color de texto: blanco para la fila de TOTAL (fila 16)
        ('TEXTCOLOR', (0, 16), (-1, 16), colors.white),

        # Fuente: Helvetica Bold, tamaño 9, para la zona de datos de empresa (filas 0-7)
        ('FONT', (0, 0), (4, 7), 'Helvetica-Bold', 9),
        # Fuente: Helvetica Bold, tamaño 15, para el título principal (fila 1)
        ('FONT', (0, 0), (-1, 1), 'Helvetica-Bold', 15),
        # Fuente: Helvetica Bold + Cursiva, para las etiquetas de datos (filas 2-7, columna 0)
        ('FONT', (0, 2), (1, 7), 'Helvetica-BoldOblique'),
        # Fuente: Helvetica Bold, tamaño 10, para la fila de TOTAL
        ('FONT', (0, 16), (-1, 16), 'Helvetica-Bold', 10),
        # Fuente: Helvetica Bold, tamaño 9, para el encabezado de productos (fila 8)
        ('FONT', (0, 8), (-1, 8), 'Helvetica-Bold', 9),

        # Fondo: verde claro para las filas de productos (filas 9-15)
        ('BACKGROUND', (0, 16), (-1, 8), lightverde),
        # Fondo: verde oscuro para el encabezado de productos (fila 8)
        ('BACKGROUND', (0, 8), (-1, 8), darkverde),
        # Fondo: blanco para la fila separadora (fila 15)
        ('BACKGROUND', (0, 15), (-1, 15), colors.white),
        # Fondo: verde oscuro para el TOTAL (columnas 4-5, fila 16)
        ('BACKGROUND', (4, 16), (-1, 16), darkverde),

        # SPAN (fusionar celdas): Título principal "FACTURA SIMPLIFICADA" (fila 1, columnas 0-2)
        ('SPAN', (0, 1), (2, 1)),
        # SPAN: "FACTURA SIMPLIFICADA" (fila 0, columnas 4-5)
        ('SPAN', (4, 0), (5, 0)),
        # SPAN: "Descripción" en fila 8 (columnas 0-2) - ocupa 3 columnas
        ('SPAN', (0, 8), (2, 8)),
        # SPAN: Nombre de Producto en filas 9-14 (columnas 0-2)
        ('SPAN', (0, 9), (2, 9)),
        ('SPAN', (0, 10), (2, 10)),
        ('SPAN', (0, 11), (2, 11)),
        ('SPAN', (0, 12), (2, 12)),
        ('SPAN', (0, 13), (2, 13)), # desde la columna 0 fila 13 hasta columna 2 fila 13
        ('SPAN', (0, 14), (2, 14)),
        # SPAN: Mensaje final "GRACIAS POR SU CONFIANZA" (fila 18, todas las columnas)
        ('SPAN', (0, 17), (5, 17)),
        ('SPAN', (0, 18), (5, 18)),

        # Alineación horizontal: DERECHA para el título "FACTURA SIMPLIFICADA"
        ('ALIGN', (4, 0), (5, 0), 'RIGHT'),
        # Alineación horizontal: DERECHA para Fecha Emisión y Número de Factura
        ('ALIGN', (4, 4), (4, 5), 'RIGHT'),
        ('ALIGN', (5, 4), (5, 5), 'CENTER'),
        # Alineación horizontal: CENTRO para todo el área de productos y TOTAL
        ('ALIGN', (0, 8), (5, 16), 'CENTER'),
        # Alineación horizontal: CENTRO para el mensaje final
        ('ALIGN', (0, 18), (6, 18), 'CENTER'),
        # Alineación horizontal: DERECHA para la columna de precios totales
        ('ALIGN', (5, 9), (5, 14), 'RIGHT'),
        # Alineación vertical: MIDDLE (centrado) para la fila de TOTAL
        ('VALIGN', (4, 16), (5, 16), 'MIDDLE'),
        # Línea superior gruesa (3 píxeles) en negro para el mensaje final
        ('LINEABOVE', (0, 18), (-1, 18), 3, colors.black),
        # Rejilla (grid): bordes de 1 píxel en blanco para todas las celdas
        ('GRID', (0, 0), (-1, -1), 1, colors.white)
    ]))

    # Añadir la tabla al documento
    story.append(t1)
    # Añadir un espaciador de 15 píxeles después de la tabla
    story.append(Spacer(1, 15))

    # Construir el PDF con todos los elementos de la lista story
    doc.build(story)


# Llamar a la función para generar el PDF
generar_formulario_simple()