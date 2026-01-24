# -*- coding:utf-8 -*-
# IMPORTACIONES Y CONFIGURACIÓN INICIAL
# ======================================

import os  # Para abrir archivos del sistema operativo

# IMPORTACIONES DE PLATYPUS (Estructura y formato del PDF)
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, PageBreak
# - Paragraph: Crea párrafos de texto formateado
# - SimpleDocTemplate: Crea el documento PDF base
# - Spacer: Añade espacios en blanco entre elementos
# - PageBreak: Crea un salto de página

from reportlab.lib.styles import getSampleStyleSheet  # Estilos predefinidos (títulos, párrafos, etc.)
from reportlab.lib.pagesizes import A4  # Tamaño de página A4 (210x297 mm)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY  # Alineaciones de texto
from reportlab.lib import colors  # Colores predefinidos (red, blue, yellow, etc.)
from reportlab.lib.units import inch  # Para medir en pulgadas (1 inch = 2.54 cm)

# IMPORTACIONES DE GRAPHICS (Para dibujar formas)
from reportlab.graphics.shapes import Drawing, Rect, String, Group, Line
# - Drawing: Lienzo donde se dibujan las formas
# - Rect: Rectángulos
# - String: Texto dentro de gráficos
# - Group: Agrupa múltiples objetos en uno solo
# - Line: Líneas

from reportlab.graphics.widgets.markers import makeMarker  # Crea símbolos (círculos, cuadrados, etc.)

# CONFIGURACIÓN DEL DOCUMENTO
# ============================
doc = SimpleDocTemplate('test.pdf', pagesize=A4)  # Crea PDF llamado 'test.pdf' en tamaño A4
story = []  # Lista vacía que contendrá TODO lo que aparecerá en el PDF (en orden)
estilo = getSampleStyleSheet()  # Obtiene estilos predefinidos para textos

# EJEMPLO 01: FORMAS Y TEXTO BÁSICO
# ==================================
# UBICACIÓN EN PDF: Página 1, parte superior
# QUÉ HACE: Crea un rectángulo amarillo con borde rojo y dos textos

d = Drawing(400, 200)  # Crea un "lienzo" de 400 puntos de ancho × 200 de alto

# Crea un rectángulo en posición (50,50), ancho 300, alto 100, relleno amarillo
r = (Rect(50, 50, 300, 100, fillColor=colors.yellow))
r.strokeColor = colors.red  # Cambia el borde del rectángulo a rojo
r.strokeWidth = 3  # Grosor del borde: 3 puntos
d.add(r)  # Añade el rectángulo al lienzo

# Añade texto "Hola mundo" en posición (150, 100), tamaño 18, color rojo
d.add(String(150, 100, 'Hola mundo', fontSize=18, fillColor=colors.red))

# Añade caracteres especiales (©, ®, ¥, α, β) en posición (180, 86), color rojo
d.add(String(180, 86, 'Caracteres especiales: \
             \xc2\xa2\xc2\xa9\xc2\xae\xc2\xa3\xce\xb1\xce\xb2',
             fillColor=colors.red))

story.append(d)  # Añade el lienzo completo a la lista 'story' → aparecerá en el PDF
# Formas disponibles: Rect, Circle, Ellipse, Wedge, Polygon, Line, PolyLine, String, Group


# EJEMPLO 02: INSPECCIONAR PROPIEDADES DE OBJETOS
# ================================================
# UBICACIÓN EN PDF: No aparece en el PDF (solo imprime en la terminal)
# QUÉ HACE: Muestra todas las propiedades que se pueden modificar de un objeto

import pprint  # Librería para imprimir datos de forma legible en consola

r = Rect(0, 0, 200, 100)  # Crea un rectángulo de prueba
pprint.pprint(r.getProperties())  # Muestra en terminal TODAS las propiedades disponibles
# PARA QUÉ: Útil para aprender qué atributos se pueden personalizar de cada objeto

# EJEMPLO 03: LABEL (ETIQUETA DE TEXTO AVANZADA)
# ===============================================
# UBICACIÓN EN PDF: Página 2, parte superior
# QUÉ HACE: Crea una etiqueta girada con borde verde

from reportlab.graphics.charts.textlabels import Label  # Importa el componente Label

d = Drawing(200, 100)  # Nuevo lienzo de 200×100 puntos
lab = Label()  # Crea una etiqueta vacía
lab.setOrigin(100, 90)  # Posiciona el origen en (100, 90)
lab.angle = 45  # Gira la etiqueta 45 grados
lab.dx = 0  # Desplazamiento horizontal: 0 (sin movimiento)
lab.dy = -20  # Desplazamiento vertical: -20 puntos (hacia abajo)
lab.boxStrokeColor = colors.green  # Borde verde alrededor de la etiqueta
lab.setText('Un \nLabel \nMulti-Linea')  # Texto con 3 líneas (el \n es salto de línea)
d.add(lab)  # Añade la etiqueta al lienzo
pprint.pprint(lab.getProperties())  # Muestra propiedades disponibles en terminal
# NOTA: Label tiene más opciones que String (rotación, desplazamiento, borde, etc.)
story.append(d)  # Añade el lienzo a la historia del PDF

# EJEMPLO 04: EJES DE COORDENADAS (SIN DATOS AÚN)
# ================================================
# UBICACIÓN EN PDF: Página 2, abajo / Página 3, arriba
# QUÉ HACE: Crea ejes X (horizontal) e Y (vertical) con etiquetas personalizadas

from reportlab.graphics.charts.axes import XCategoryAxis, YValueAxis  # Importa tipos de ejes

d = Drawing(400, 200)  # Nuevo lienzo de 400×200 puntos
data = [(10, 20, 30, 40), (15, 22, 37, 42)]  # Datos de ejemplo (no se mostrarán aún)

# CREAR EJE X (CATEGORÍAS)
xAxis = XCategoryAxis()  # Crea eje X para categorías (no números)
xAxis.setPosition(75, 75, 300)  # Posición: x=75, y=75, ancho=300 puntos
xAxis.configure(data)  # Configura el eje basándose en los datos
xAxis.categoryNames = ['Oso', 'Tigre', 'León', 'Camaleón']  # Nombres que aparecen en eje X
# Personaliza solo la TERCERA etiqueta (índice 2):
xAxis.labels[2].dy = -15  # Desplaza 15 puntos hacia abajo
xAxis.labels[2].angle = 30  # Gira 30 grados (para no solapar con otras)
xAxis.labels[2].fontName = 'Times-Bold'  # Cambia fuente a Times Bold

# CREAR EJE Y (VALORES NUMÉRICOS)
yAxis = YValueAxis()  # Crea eje Y para valores numéricos
yAxis.setPosition(50, 80, 125)  # Posición: x=50, y=80, alto=125 puntos
yAxis.configure(data)  # Configura el eje basándose en los datos

# AÑADIR LOS EJES AL LIENZO
d.add(xAxis)  # Añade eje X
d.add(yAxis)  # Añade eje Y

story.append(d)  # Añade el lienzo a la historia
story.append(PageBreak())  # CREA UN SALTO DE PÁGINA → siguiente página en blanco

# EJEMPLO 05: GRÁFICO DE BARRAS VERTICALES
# ==========================================
# UBICACIÓN EN PDF: Página 3, zona principal
# QUÉ HACE: Muestra 2 series de datos en forma de barras verticales agrupadas

from reportlab.graphics.charts.barcharts import VerticalBarChart  # Importa gráfico de barras

d = Drawing(400, 200)  # Nuevo lienzo de 400×200 puntos
# DATOS: 2 series (filas) con 8 valores cada una (meses)
data = [
    (13, 5, 20, 22, 37, 45, 19, 4),  # Serie 1
    (14, 6, 21, 23, 38, 46, 20, 5)   # Serie 2
]

bc = VerticalBarChart()  # Crea gráfico de barras verticales
bc.x = 50  # Posición X del gráfico: 50 puntos desde la izquierda
bc.y = 50  # Posición Y del gráfico: 50 puntos desde abajo
bc.height = 125  # Alto del área del gráfico
bc.width = 300  # Ancho del área del gráfico
bc.data = data  # Asigna los datos al gráfico
bc.strokeColor = colors.black  # Color del borde: negro
# CONFIGURAR EJE Y (VERTICAL - VALORES)
bc.valueAxis.valueMin = 0  # Valor mínimo en eje Y
bc.valueAxis.valueMax = 50  # Valor máximo en eje Y
bc.valueAxis.valueStep = 10  # Distancia entre líneas horizontales (0, 10, 20, 30...)
# CONFIGURAR EJE X (HORIZONTAL - CATEGORÍAS/MESES)
bc.categoryAxis.labels.boxAnchor = 'ne'  # Ancla labels en esquina nordeste
bc.categoryAxis.labels.dx = 8  # Desplazamiento horizontal de etiquetas
bc.categoryAxis.labels.dy = -2  # Desplazamiento vertical de etiquetas (hacia abajo)
bc.categoryAxis.labels.angle = 30  # Gira etiquetas 30 grados para legibilidad
# NOMBRES DE LOS MESES (8 categorías para 8 valores en cada serie)
bc.categoryAxis.categoryNames = ['Ene-14', 'Feb-14', 'Mar-14',
                                 'Abr-14', 'May-14', 'Jun-14', 'Jul-14', 'Ago-14']
bc.groupSpacing = 10  # Espaciado entre GRUPOS de barras (entre meses)
bc.barSpacing = 2  # Espaciado entre BARRAS DENTRO de un grupo (entre series)
# bc.categoryAxis.style = 'stacked'  # Si descomenta: muestra barras apiladas en vez de agrupadas
d.add(bc)  # Añade gráfico al lienzo
pprint.pprint(bc.getProperties())  # Muestra propiedades disponibles en terminal
story.append(d)  # Añade el lienzo a la historia del PDF

# EJEMPLO 06: GRÁFICO DE LÍNEAS HORIZONTAL
# ==========================================
# UBICACIÓN EN PDF: Página 4, con título arriba
# QUÉ HACE: Muestra calificaciones como línea horizontal con símbolos en los puntos

from reportlab.graphics.charts.linecharts import HorizontalLineChart  # Importa gráfico lineal

# Añade un TÍTULO al documento (usando Platypus, no Graphics)
titulo = Paragraph("Calificaciones Informática", estilo['title'])  # Crea párrafo con estilo título
story.append(titulo)  # Añade título a la historia del PDF
story.append(Spacer(0, inch * .1))  # Añade espacio en blanco (0.1 pulgadas)

d = Drawing(400, 200)  # Nuevo lienzo de 400×200 puntos
lc = HorizontalLineChart()  # Crea gráfico de líneas horizontal
lc.x = 30  # Posición X del gráfico
lc.y = 50  # Posición Y del gráfico
lc.height = 125  # Alto del área del gráfico
lc.width = 350  # Ancho del área del gráfico
lc.data = [[8, 10, 5, 2]]  # 1 serie con 4 valores (para 4 categorías)
# CONFIGURAR CATEGORÍAS (EJE VERTICAL en gráfico horizontal)
lc.categoryAxis.categoryNames = ['Suspenso', 'Aprobado', 'Notable', 'Sobresaliente']
lc.categoryAxis.labels.boxAnchor = 'n'  # Ancla labels en la parte norte (arriba)
# CONFIGURAR EJE HORIZONTAL (VALORES NUMÉRICOS)
lc.valueAxis.valueMin = 0  # Valor mínimo
lc.valueAxis.valueMax = 12  # Valor máximo
lc.valueAxis.valueStep = 2  # Pasos entre valores (0, 2, 4, 6, 8, 10, 12)
# TAMBIÉN PUEDE SER: lc.valueAxis.valueStep = [10, 15, 30, 35, 40]  (valores específicos)
lc.lines[0].strokeWidth = 2  # Grosor de la línea
lc.lines[0].symbol = makeMarker('FilledCircle')  # Pone círculos rellenos en cada punto
lc.lines[1].strokeWidth = 1.5  # (Si hubiera una segunda línea, tendría este grosor)
d.add(lc)  # Añade gráfico al lienzo
story.append(d)  # Añade el lienzo a la historia del PDF

# EJEMPLO 07: GRÁFICO DE DISPERSIÓN CON LÍNEAS (XY - SCATTER PLOT)
# =================================================================
# UBICACIÓN EN PDF: Página 5
# QUÉ HACE: Muestra puntos X,Y conectados con líneas, con leyenda explicativa

from reportlab.graphics.charts.lineplots import LinePlot  # Importa gráfico XY

d = Drawing(400, 200)  # Nuevo lienzo de 400×200 puntos
# DATOS: 2 series de pares (x, y)
data = [
    ((1, 1), (2, 2), (2.5, 1), (3, 3), (4, 6)),  # Serie 1: 5 pares de coordenadas
    ((1, 2), (2, 3), (2.5, 2), (3.5, 5), (4, 3))  # Serie 2: 5 pares de coordenadas
]

lp = LinePlot()  # Crea gráfico de dispersión con líneas
lp.x = 50  # Posición X del gráfico
lp.y = 50  # Posición Y del gráfico
lp.height = 125  # Alto del área del gráfico
lp.width = 300  # Ancho del área del gráfico
lp.data = data  # Asigna los datos (pares x,y)
lp.joinedLines = 1  # 1 = conecta los puntos con líneas, 0 = solo puntos
lp.fillColor = colors.yellow  # Color de fondo del área bajo la línea
# CONFIGURAR SÍMBOLOS DE LAS LÍNEAS
lp.lines[0].symbol = makeMarker('FilledCircle')  # Serie 1: círculos rellenos
lp.lines[1].symbol = makeMarker('Circle')  # Serie 2: círculos vacíos
lp.lineLabelFormat = '%2.0f'  # Formato de etiquetas en los puntos (2 dígitos, sin decimales)
lp.strokeColor = colors.black  # Color del borde del gráfico
# CONFIGURAR EJE X (VALORES NUMÉRICOS)
lp.xValueAxis.valueMin = 0  # Valor mínimo en eje X
lp.xValueAxis.valueMax = 5  # Valor máximo en eje X
lp.xValueAxis.valueSteps = [1, 2, 2.5, 3, 4, 5]  # Valores específicos a mostrar en eje X
lp.xValueAxis.labelTextFormat = '%2.1f'  # Formato de etiquetas X (2 dígitos, 1 decimal)
# CONFIGURAR EJE Y (VALORES NUMÉRICOS)
lp.yValueAxis.valueMin = 0  # Valor mínimo en eje Y
lp.yValueAxis.valueMax = 7  # Valor máximo en eje Y
lp.yValueAxis.valueSteps = [1, 2, 3, 5, 6]  # Valores específicos a mostrar en eje Y

# CREAR Y CONFIGURAR LA LEYENDA
# ==============================
# LineLegend: Leyenda que muestra las opciones/series con sus colores
from reportlab.graphics.charts.legends import LineLegend

legend = LineLegend()  # Crea leyenda
legend.fontSize = 8  # Tamaño de fuente en la leyenda
legend.alignment = 'right'  # Alineación a la derecha
legend.x = 0  # Posición X de la leyenda
legend.y = 0  # Posición Y de la leyenda
legend.columnMaximum = 2  # Máximo de 2 columnas en la leyenda
legend.fontName = 'Helvetica'  # Fuente de la leyenda

# Definir etiquetas personalizadas y asociarlas con los colores del gráfico
etiquetas = ['Opcion 01', 'Opcion 02']  # 2 nombres para las 2 series
legend.colorNamePairs = [(lp.lines[i].strokeColor, etiquetas[i])
                         for i in range(len(lp.data))]  # Asocia color con nombre

d.add(lp)  # Añade gráfico al lienzo
d.add(legend)  # Añade leyenda al lienzo
story.append(d)  # Añade el lienzo a la historia del PDF

# EJEMPLO 08: GRÁFICO CIRCULAR (PIE CHART)
# ==========================================
# UBICACIÓN EN PDF: Página 6
# QUÉ HACE: Muestra un gráfico de pastel con 5 sectores y leyenda personalizada

from reportlab.graphics.charts.piecharts import Pie  # Importa gráfico circular

d = Drawing(300, 200)  # Nuevo lienzo de 300×200 puntos
pc = Pie()  # Crea gráfico de pastel
pc.x = 65  # Posición X del gráfico desde la izquierda
pc.y = 15  # Posición Y del gráfico desde abajo
pc.width = 170  # Ancho del círculo (diámetro)
pc.height = 170  # Alto del círculo (diámetro)
pc.data = [10, 20, 30, 40, 50]  # 5 valores = 5 sectores (proporcional al tamaño)
pc.labels = ['IE', 'Kopete', 'Chrome', 'Firefox', 'Opera']  # Nombres de cada sector

# PROPIEDADES GENERALES DE LOS SECTORES
pc.slices.strokeWidth = 0.5  # Ancho del borde de todos los sectores

# PERSONALIZAR SOLO UN SECTOR (Índice 3 = Firefox, el 4º sector)
pc.slices[3].popout = 10  # Separa el sector Firefox 10 puntos del centro
pc.slices[3].strokeWidth = 2  # Borde más grueso para Firefox
pc.slices[3].strokeDashArray = [2, 2]  # Línea punteada en Firefox (2 puntos, 2 espacios)
pc.slices[3].labelRadius = 1.75  # Distancia de la etiqueta al sector
pc.slices[3].fontColor = colors.red  # Etiqueta de Firefox en rojo
pc.sideLabels = 1  # 1 = muestra etiquetas con líneas hacia los sectores, 0 = no muestra
# ~ pc.slices.labelRadius = 0.65  # Para mostrar el texto DENTRO de los sectores (comentado)

# CREAR Y CONFIGURAR LA LEYENDA
# ==============================
from reportlab.graphics.charts.legends import Legend  # Importa leyenda normal (no LineLegend)

legend = Legend()  # Crea leyenda
legend.x = 370  # Posición X de la leyenda (a la derecha)
legend.y = 0  # Posición Y de la leyenda
legend.dx = 8  # Espaciado horizontal entre elementos
legend.dy = 8  # Espaciado vertical entre elementos
legend.fontName = 'Helvetica'  # Fuente de la leyenda
legend.fontSize = 7  # Tamaño de fuente (pequeño)
legend.boxAnchor = 'n'  # Ancla la leyenda en el norte (arriba)
legend.columnMaximum = 10  # Máximo de 10 columnas (para mostrar todo en una línea si cabe)
legend.strokeWidth = 1  # Ancho del borde de la leyenda
legend.strokeColor = colors.black  # Color del borde de la leyenda
legend.deltax = 75  # Espaciado horizontal adicional
legend.deltay = 10  # Espaciado vertical adicional
legend.autoXPadding = 5  # Relleno automático en X
legend.yGap = 0  # Espaciado vertical entre items
legend.dxTextSpace = 5  # Espaciado entre símbolo y texto
legend.alignment = 'right'  # Alineación a la derecha
legend.dividerLines = 1 | 2 | 4  # Líneas divisoras (1=izquierda, 2=derecha, 4=arriba|abajo)
legend.dividerOffsY = 4.5  # Offset vertical de las líneas divisoras
legend.subCols.rpad = 30  # Relleno derecho de las subcolunas

# ASIGNAR COLORES PERSONALIZADOS A LOS SECTORES
# ================================================
colores = [colors.blue, colors.red, colors.green, colors.yellow, colors.pink]  # 5 colores
for i, color in enumerate(colores):  # Para cada sector
    pc.slices[i].fillColor = color  # Asigna un color diferente

# CREAR LAS PAREJAS COLOR-ETIQUETA PARA LA LEYENDA
# ==================================================
legend.colorNamePairs = [(
    pc.slices[i].fillColor,  # Color del sector
    (pc.labels[i][0:20], '%0.2f' % pc.data[i])  # Nombre (máximo 20 caracteres) + valor
) for i in range(len(pc.data))]  # Para cada sector

d.add(pc)  # Añade gráfico circular al lienzo
d.add(legend)  # Añade leyenda al lienzo
story.append(d)  # Añade el lienzo a la historia del PDF

# EJEMPLO 09: GRUPO (GROUP) CON TRANSFORMACIONES
# ================================================
# UBICACIÓN EN PDF: Página 7
# QUÉ HACE: Crea un grupo de ejes (líneas y marcas) y lo replica 3 veces con transformaciones

d = Drawing(400, 200)  # Nuevo lienzo de 400×200 puntos

# CREAR UN GRUPO LLAMADO "Ejes" (contiene múltiples elementos)
Ejes = Group(
    # EJE X (línea horizontal)
    Line(0, 0, 100, 0),  # Línea desde (0,0) hasta (100,0) - línea horizontal de 100 puntos
    # EJE Y (línea vertical)
    Line(0, 0, 0, 50),  # Línea desde (0,0) hasta (0,50) - línea vertical de 50 puntos

    # MARCAS EN EL EJE Y (pequeñas líneas transversales)
    Line(0, 10, 10, 10),  # Marca en y=10
    Line(0, 20, 10, 20),  # Marca en y=20
    Line(0, 30, 10, 30),  # Marca en y=30
    Line(0, 40, 10, 40),  # Marca en y=40

    # MARCAS EN EL EJE X (pequeñas líneas verticales)
    Line(10, 0, 10, 10),  # Marca en x=10
    Line(20, 0, 20, 10),  # Marca en x=20
    Line(30, 0, 30, 10),  # Marca en x=30
    Line(40, 0, 40, 10),  # Marca en x=40
    Line(50, 0, 50, 10),  # Marca en x=50
    Line(60, 0, 60, 10),  # Marca en x=60
    Line(70, 0, 70, 10),  # Marca en x=70
    Line(80, 0, 80, 10),  # Marca en x=80
    Line(90, 0, 90, 10),  # Marca en x=90

    # ETIQUETA EN EL EJE
    String(20, 35, 'Ejes', fill=colors.black)  # Texto "Ejes" en posición (20, 35)
)

# PRIMER GRUPO DE EJES (sin transformación)
# ============================================
PrimerGrupoEjes = Group(Ejes)  # Crea una copia del grupo
PrimerGrupoEjes.translate(10, 10)  # Traslada 10 puntos a la derecha y 10 hacia arriba
d.add(PrimerGrupoEjes)  # Añade al lienzo

# SEGUNDO GRUPO DE EJES (trasladado y rotado 15°)
# ================================================
SegundoGrupoEjes = Group(Ejes)  # Crea una segunda copia del grupo
SegundoGrupoEjes.translate(150, 10)  # Traslada 150 puntos a la derecha y 10 hacia arriba
SegundoGrupoEjes.rotate(15)  # Rota 15 grados alrededor de su origen
d.add(SegundoGrupoEjes)  # Añade al lienzo

# TERCER GRUPO DE EJES (trasladado y rotado 30°)
# ===============================================
TercerGrupoEjes = Group(Ejes)  # Crea una tercera copia del grupo
TercerGrupoEjes.translate(300, 10)  # Traslada 300 puntos a la derecha y 10 hacia arriba
TercerGrupoEjes.rotate(30)  # Rota 30 grados alrededor de su origen
d.add(TercerGrupoEjes)  # Añade al lienzo

# VENTAJA DE USAR GRUPOS:
# - Reutilizar el mismo grupo múltiples veces sin redefinir todos los elementos
# - Aplicar transformaciones (trasladar, rotar) a todo el grupo de una vez
# - Código más limpio y mantenible

story.append(d)  # Añade el lienzo a la historia del PDF


# FINALIZACIÓN Y GENERACIÓN DEL PDF
# ==================================
doc.build(story)  # Construye el PDF con todos los elementos almacenados en la lista 'story'
# RESULTADO: Se crea el archivo 'test.pdf' en la carpeta actual con todas las páginas

os.system('test.pdf')  # Abre automáticamente el PDF generado con el lector predeterminado del sistema
# RESULTADO: Se abre el archivo PDF con el programa asociado (Adobe Reader, navegador, etc.)
