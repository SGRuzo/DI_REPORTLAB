import sqlite3
import os
import platform
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie


def obtener_datos_completos(limite=5):
    """Obtiene Nombre, Conteo de Facturas e Importe Total de la BD"""
    db_path = 'bdTendaOrdeadoresBig.bd'
    if not os.path.exists(db_path):
        print(f"Error: No se encuentra la base de datos {db_path}")
        return []

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Consulta unificada para obtener tanto el conteo como el total
    query = """SELECT
                   c.nome,
                   COUNT(DISTINCT f.id_factura) as num_facturas,
                   SUM(lf.cantidade * lf.prezo_unitario * (1 - lf.desconto / 100) * (1 + p.iva / 100)) as facturacion_total
               FROM clientes c
               JOIN facturas f ON c.id_cliente = f.id_cliente
               JOIN linhas_factura lf ON f.id_factura = lf.id_factura
               JOIN produtos p ON lf.id_produto = p.id_produto
               GROUP BY c.id_cliente, c.nome
               ORDER BY facturacion_total DESC
               LIMIT ?"""

    cursor.execute(query, (limite,))
    resultados = cursor.fetchall()
    conn.close()
    return resultados


def generar_informe_unificado():
    # 1. Obtener los datos
    datos = obtener_datos_completos(5)
    if not datos:
        print("No hay datos disponibles para generar el informe.")
        return

    # 2. Configuración del PDF
    pdf_name = "Informe_Facturacion.pdf"
    doc = SimpleDocTemplate(pdf_name, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()

    # --- TÍTULO ---
    story.append(Paragraph("Informe Ejecutivo de Ventas", styles['Title']))
    story.append(Spacer(1, 15))
    story.append(Paragraph("Análisis de los 5 clientes con mayor volumen de facturación.", styles['Normal']))
    story.append(Spacer(1, 25))

    # --- TABLA ---
    story.append(Paragraph("Detalle de Facturación", styles['Heading2']))
    story.append(Spacer(1, 10))

    tabla_data = [['Pos.', 'Cliente', 'Nº Facturas', 'Total Facturado']]
    for i, (nombre, num_fact, total) in enumerate(datos, start=1):
        tabla_data.append([str(i), nombre, str(num_fact), f"{total:,.2f} €"])

    t = Table(tabla_data, colWidths=[40, 200, 80, 120], rowHeights=25)

    estilo_tabla = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (1, 1), (1, -1), 'LEFT'),
        ('ALIGN', (3, 1), (3, -1), 'RIGHT'),
    ])

    # Cebra para las filas
    for i in range(1, len(tabla_data)):
        if i % 2 == 0:
            estilo_tabla.add('BACKGROUND', (0, i), (-1, i), colors.lightgrey)

    t.setStyle(estilo_tabla)
    story.append(t)
    story.append(Spacer(1, 40))

    # --- GRÁFICO ---
    story.append(Paragraph("Distribución Porcentual del Ingreso", styles['Heading2']))
    story.append(Spacer(1, 10))

    # Preparar datos para el gráfico
    nombres = [d[0] for d in datos]
    totales = [float(d[2]) for d in datos]

    d = Drawing(400, 200)
    pc = Pie()
    pc.x = 125
    pc.y = 10
    pc.width = 150
    pc.height = 150
    pc.data = totales
    pc.labels = nombres
    pc.sideLabels = True
    pc.slices.strokeWidth = 0.5

    # Colores personalizados
    mis_colores = [colors.cadetblue, colors.coral, colors.seagreen, colors.indianred, colors.mediumpurple]
    for i, color in enumerate(mis_colores):
        if i < len(pc.data):
            pc.slices[i].fillColor = color

    d.add(pc)
    story.append(d)

    # 3. Construcción del PDF
    doc.build(story)
    print(f"Informe generado: {pdf_name}")

    # 4. Abrir automáticamente
    try:
        if platform.system() == "Darwin":
            os.system(f'open "{pdf_name}"')
        elif platform.system() == "Windows":
            os.startfile(pdf_name)
        else:
            os.system(f'xdg-open "{pdf_name}"')
    except Exception as e:
        print(f"No se pudo abrir el archivo automáticamente: {e}")


if __name__ == "__main__":
    generar_informe_unificado()