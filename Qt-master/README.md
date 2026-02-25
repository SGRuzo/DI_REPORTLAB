# Guía de PyQt6 - Creación de Interfaces Gráficas

## 1. Creación de una Ventana Básica

### Código Base
```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget

class VentanaVacia(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100, 100, 250, 250)  # posición x,y y tamaño ancho,alto
        self.setWindowTitle("Mi primera ventana vacía")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaVacia()
    sys.exit(app.exec())
```

![img.png](img.png)

### Explicación del Código

#### Importaciones Necesarias
```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget
```
- **sys**: Módulo estándar para interactuar con el sistema
- **QApplication**: Maneja el bucle principal de la aplicación
- **QWidget**: Clase base para todos los elementos de interfaz

#### Clase Principal
```python
class VentanaVacia(QWidget):
```
Crea una clase que hereda de QWidget, permitiendo crear ventanas personalizadas.

#### Método Constructor
```python
def __init__(self):
    super().__init__()
    self.inicializarUI()
```
- `super().__init__()`: Llama al constructor de la clase padre (QWidget)
- `self.inicializarUI()`: Llama al método que configura la interfaz

#### Configuración de la Interfaz
```python
def inicializarUI(self):
    self.setGeometry(100, 100, 250, 250)
    self.setWindowTitle("Mi primera ventana vacía")
    self.show()
```

**Métodos clave:**
- `setGeometry(x, y, ancho, alto)`: Posición y tamaño de la ventana
- `setWindowTitle("texto")`: Título de la ventana
- `show()`: Hace visible la ventana

#### Bloque Principal
```python
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaVacia()
    sys.exit(app.exec())
```

**Flujo de ejecución:**
1. `QApplication(sys.argv)`: Crea la aplicación
2. `VentanaVacia()`: Instancia la ventana
3. `app.exec()`: Inicia el bucle de eventos
4. `sys.exit()`: Garantiza una salida limpia



# Guía de PyQt6 - Formulario de Login

## 2. Creación de un Formulario de Login

### Código del Formulario
```python
import sys
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit, QPushButton, QMessageBox, QCheckBox)

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("Mi login")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_logged = False

        # Etiqueta y campo de usuario
        user_label = QLabel(self)
        user_label.setText("Usuario:")
        user_label.setFont(QFont('Arial', 10))
        user_label.move(20, 54)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 24)
        self.user_input.move(90, 50)

        # Etiqueta y campo de contraseña
        password_label = QLabel(self)
        password_label.setText("Password:")
        password_label.setFont(QFont('Arial', 10))
        password_label.move(20, 86)

        self.password_input = QLineEdit(self)
        self.password_input.resize(250, 34)
        self.password_input.move(90, 82)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Botones
        login_button = QPushButton("Login", self)
        login_button.resize(320, 24)
        login_button.move(20, 140)
        login_button.clicked.connect(self.iniciar_mainview)

        register_button = QPushButton("Register", self)
        register_button.resize(320, 34)
        register_button.move(20, 180)
        register_button.clicked.connect(self.iniciar_register)

        # Checkbox para mostrar contraseña
        self.check_view_password = QCheckBox("Mostrar password", self)
        self.check_view_password.move(90, 112)
        self.check_view_password.clicked.connect(self.mostar_comtrasena)

    def mostar_comtrasena(self):
        pass

    def iniciar_mainview(self):
        pass

    def iniciar_register(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())
```

![img_1.png](img_1.png)

## 3. Elementos de Formulario Explicados

### QLabel - Etiquetas de Texto
```python
user_label = QLabel(self)
user_label.setText("Usuario:")
user_label.setFont(QFont('Arial', 10))
user_label.move(20, 54)
```
- **QLabel**: Muestra texto estático
- **setText()**: Define el texto a mostrar
- **setFont()**: Configura la fuente y tamaño
- **move()**: Posiciona el elemento (x, y)

### QLineEdit - Campos de Entrada
```python
self.user_input = QLineEdit(self)
self.user_input.resize(250, 24)
self.user_input.move(90, 50)
```

#### Campo de Contraseña
```python
self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
```
**Modos disponibles:**
- `Normal`: Muestra el texto normalmente
- `Password`: Muestra puntos en lugar del texto
- `NoEcho`: No muestra nada
- `PasswordEchoOnEdit`: Muestra texto mientras se escribe, luego puntos

### QPushButton - Botones
```python
login_button = QPushButton("Login", self)
login_button.resize(320, 24)
login_button.move(20, 140)
login_button.clicked.connect(self.iniciar_mainview)
```
- **clicked.connect()**: Conecta el evento click a una función

### QCheckBox - Casillas de Verificación
```python
self.check_view_password = QCheckBox("Mostrar password", self)
self.check_view_password.move(90, 112)
self.check_view_password.clicked.connect(self.mostar_comtrasena)
```

## 4. Implementando las Funciones

### Función para Mostrar/Ocultar Contraseña
```python
def mostar_comtrasena(self):
    if self.check_view_password.isChecked():
        self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
    else:
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
```

### Función de Login Básica
```python
def iniciar_mainview(self):
    usuario = self.user_input.text()
    password = self.password_input.text()
    
    # Validación básica
    if usuario == "admin" and password == "1234":
        QMessageBox.information(self, "Login", "¡Login exitoso!")
        self.is_logged = True
        # Aquí iría la lógica para abrir la ventana principal
    else:
        QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")
```

### Función de Registro
```python
def iniciar_register(self):
    QMessageBox.information(self, "Registro", "Aquí iría el formulario de registro")
```

## 5. Diseño y Posicionamiento

### Métodos de Posicionamiento
- **move(x, y)**: Posiciona el widget en coordenadas absolutas
- **resize(ancho, alto)**: Define el tamaño del widget
- **setGeometry(x, y, ancho, alto)**: Combina posición y tamaño

### Ejemplo de Layout Organizado
```python
# Posiciones calculadas para mejor organización
x_label = 20
x_input = 90
y_start = 50
y_increment = 36

user_label.move(x_label, y_start)
self.user_input.move(x_input, y_start)

password_label.move(x_label, y_start + y_increment)
self.password_input.move(x_input, y_start + y_increment)
```
# Guía de PyQt6 - Nuevas Características y Cambios

## 6. Nuevas Implementaciones y Cambios

### Cambio en la Señal del Checkbox
```python
# ANTES:
self.check_view_password.clicked.connect(self.mostar_comtrasena)

# AHORA:
self.check_view_password.toggled.connect(self.mostar_comtrasena)
```
**Explicación del cambio:**
- `toggled` envía el estado actual (True/False) como parámetro
- `clicked` solo indica que fue clickeado, sin el estado

### Implementación Completa de mostrar_contrasena
```python
def mostar_comtrasena(self, clicked):
    if clicked:
        self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
    else:
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
```
**Mejora:** Recibe el parámetro `clicked` que indica el estado del checkbox

## 7. Nueva Clase: RegistrarUsuarioView (QDialog)

### Características Principales de QDialog
```python
class RegistrarUsuarioView(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)  # ¡NUEVO!
        self.generar_formulario()
```

**setModal(True):**
- Bloquea la ventana principal hasta que se cierre el diálogo
- El usuario debe interactuar con el diálogo primero

### Formulario de Registro Mejorado
```python
# Campos de verificación de contraseña
password_1_label = QLabel(self)
password_1_label.setText("Password: ")
# ...
password_2_label = QLabel(self)
password_2_label.setText("Password: ")
```

**Validación de contraseñas:** Se pide la contraseña dos veces para verificar

### Botones de Acción Específicos
```python
create_button = QPushButton(self)
create_button.setText("Crear")
create_button.clicked.connect(self.crear_usuario)

cancel_button = QPushButton(self)
cancel_button.setText("Cancelar")
cancel_button.clicked.connect(self.cancelar_creacion)
```

## 8. Persistencia de Datos con Archivos

### Manejo de Archivos para Usuarios
```python
def crear_usuario(self):
    user_path = "usuarios.txt"
    # ...
    try:
        with open(user_path, "a+") as f:
            f.write(f"{usuario},{password_1}\n")
```

**Modo "a+":**
- **a**: Append (agregar al final)
- **+**: Crear el archivo si no existe

### Validaciones Mejoradas
```python
if password_1 == "" or password_2 == "" or usuario == "":
    QMessageBox.warning(
        self,
        "Error",
        "Ningun campo puede estar vacio",
        QMessageBox.StandardButton.Close,  # ¡NUEVO!
        QMessageBox.StandardButton.Close
    )
```

**QMessageBox.StandardButton:** Especifica botones estándar para el diálogo

### Manejo de Errores con FileNotFoundError
```python
except FileNotFoundError as e:
    QMessageBox.critical(
        self,
        "Error",
        f"La base de datos de usuarios no se ha encontrado.{e}",
        QMessageBox.StandardButton.Close,
        QMessageBox.StandardButton.Close
    )
```

## 9. Integración entre Ventanas

### Llamada desde Login a RegistrarUsuarioView
```python
def iniciar_register(self):
    self.new_user_form = RegistrarUsuarioView()
    self.new_user_form.show()
```

**Flujo de la aplicación:**
1. Ventana Login principal
2. Al hacer click en "Register" se abre RegistrarUsuarioView (modal)
3. El usuario interactúa con el diálogo de registro
4. Al cerrarse, vuelve al Login

## 10. Mejoras en los Mensajes al Usuario

### Tipos de QMessageBox
```python
# Para advertencias
QMessageBox.warning()

# Para información positiva  
QMessageBox.information()

# Para errores críticos
QMessageBox.critical()
```

### Estructura de Parámetros
```python
QMessageBox.tipo(
    parent,           # Ventana padre
    "Título",         # Título del diálogo
    "Mensaje",        # Contenido del mensaje
    botón_por_defecto,
    botones_aceptados
)
```

## 11. Próximos Pasos Sugeridos

### Para Completar la Aplicación
1. **Implementar `iniciar_mainview`** con verificación de credenciales
2. **Leer el archivo usuarios.txt** para validar login
3. **Crear ventana principal** después del login exitoso
4. **Manejar encriptación** de contraseñas (no almacenar en texto plano)



# Guía de PyQt6 - Implementación Completa del Sistema

## 12. Cambios y Nuevas Funcionalidades Implementadas

### Cambio en el Método de Login
```python
# ANTES:
login_button.clicked.connect(self.iniciar_mainview)

# AHORA:
login_button.clicked.connect(self.login)  # Método renombrado y completamente implementado
```

### Implementación Completa del Sistema de Login
```python
def login(self):
    users = []
    user_path = "usuarios.txt"

    try:
        with open(user_path, "r") as f:
            for line in f:
                users.append(line.strip("\n"))
            
            # FORMATO CORREGIDO: "usuario,contraseña"
            login_information = f"{self.user_input.text()},{self.password_input.text()}"

            if login_information in users:
                QMessageBox.information(self, "Inicio de sesión", 
                                      "Inicio de sesión exitoso", 
                                      QMessageBox.StandardButton.Ok, 
                                      QMessageBox.StandardButton.Ok)
                self.is_logged = True
                self.close()
                self.open_main_window()  # ¡NUEVO!
            else:
                QMessageBox.warning(self, "Error Message", 
                                  "Usuario o contraseña incorrectos", 
                                  QMessageBox.StandardButton.Close, 
                                  QMessageBox.StandardButton.Close)
```

**Mejoras en la validación:**
- Lee el archivo `usuarios.txt` línea por línea
- Compara el formato `usuario,contraseña` exacto
- Maneja múltiples excepciones de forma específica

### Nueva Clase: MainWindow - Ventana Principal

```python
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUi()

    def inicializarUi(self):
        self.setGeometry(100, 100, 500, 500)  # Ventana más grande
        self.setWindowTitle("Ventana Principal")
        self.generar_contenido()
        self.show()
```

## 13. Manejo de Imágenes con QPixmap

### Carga y Visualización de Imágenes
```python
def generar_contenido(self):
    image_path = "galiciaFondo.jpg"
    try:
        with open(image_path):
            image_label = QLabel(self)
            image_label.setPixmap(QPixmap(image_path))
```

**Nuevos elementos utilizados:**
- **QPixmap**: Clase para manejar imágenes
- **setPixmap()**: Método para asignar imagen a QLabel
- **Manejo de errores específico** para archivos de imagen

### Manejo de Errores Mejorado
```python
except FileNotFoundError as e:
    QMessageBox.warning(
        self,
        "Error",
        f"No se pudo cargar la imagen: {e}",
        QMessageBox.StandardButton.Close,
        QMessageBox.StandardButton.Close
    )
except Exception as e:
    QMessageBox.warning(
        self,
        "Error", 
        f"Ocurrió un error inesperado: {e}",
        QMessageBox.StandardButton.Close,
        QMessageBox.StandardButton.Close
    )
```

## 14. Flujo Completo de la Aplicación

### Secuencia de Ventanas
1. **Login** → **MainWindow** (al login exitoso)
2. **Login** → **RegistrarUsuarioView** (al hacer click en Register)

### Cierre y Apertura de Ventanas
```python
self.close()           # Cierra la ventana actual (Login)
self.open_main_window() # Abre la nueva ventana (MainWindow)
```

## 15. Estructura de Archivos del Proyecto

### Módulos Importados
```python
from registro import RegistrarUsuarioView
from main import MainWindow
```

**Estructura sugerida:**
```
proyecto/
├── main.py           # Clase MainWindow
├── registro.py       # Clase RegistrarUsuarioView  
├── login.py          # Clase Login (archivo actual)
├── usuarios.txt      # Base de datos de usuarios
└── galiciaFondo.jpg  # Imagen de fondo
```

## 16. Mejoras de Robustez en el Código

### Manejo de Excepciones Específico
```python
except FileNotFoundError as e:
    # Error específico: archivo no encontrado
    QMessageBox.warning(self, "Error Message", 
                       f"No se ha encontrado el archivo de usuarios {e}")

except Exception as e:
    # Error genérico como fallback
    QMessageBox.warning(self, "Error Message", 
                       f"Ha ocurrido un error inesperado {e}")
```

### Validación de Formato de Datos
El código ahora espera el formato exacto en el archivo:
```
usuario1,contraseña1
usuario2,contraseña2
```

## 17. Próximas Mejoras Sugeridas

### Para la Imagen en MainWindow
```python
# Podrías añadir para que la imagen se ajuste al tamaño de la ventana
image_label.setScaledContents(True)
image_label.resize(self.width(), self.height())
```

### Para el Sistema de Login
- **Encriptación** de contraseñas en el archivo
- **Sesiones** con tiempo de expiración
- **Recuperación** de contraseñas

### Para la Interfaz
- **Layouts** para mejor posicionamiento automático
- **Estilos CSS** para personalizar apariencia
- **Iconos** en los botones


## 18. Introducción a QHBoxLayout

### Código de Layout Horizontal
```python
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setMinimumWidth(600)
        self.setFixedHeight(80)
        self.setWindowTitle('Layout Horizontal')
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        correo_label = QLabel("Correo electrónico: ")
        correo_input = QLineEdit()
        enviar_button = QPushButton("Enviar")

        layout = QHBoxLayout()
        layout.addWidget(correo_label)
        layout.addWidget(correo_input)
        layout.addWidget(enviar_button)

        self.setLayout(layout) # Definimos nuestro layout como el layout principal de la ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())
```

![img_2.png](img_2.png)


### Explicación del Código

#### Importación de QHBoxLayout
```python
from PyQt6.QtWidgets import QHBoxLayout
```
- **QHBoxLayout**: Layout que organiza widgets en una fila horizontal

#### Creación del Layout
```python
layout = QHBoxLayout()
```
Crea un nuevo layout horizontal vacío.

#### Agregar Widgets al Layout
```python
layout.addWidget(correo_label)
layout.addWidget(correo_input)
layout.addWidget(enviar_button)
```
- **addWidget()**: Añade un widget al layout en orden secuencial

#### Establecer el Layout Principal
```python
self.setLayout(layout)
```
- **setLayout()**: Define este layout como el principal de la ventana

### Métodos Útiles de QHBoxLayout

#### Espaciado entre Widgets
```python
layout.setSpacing(10)  # 10 píxeles entre cada widget
```

#### Configurar Márgenes
```python
layout.setContentsMargins(20, 10, 20, 10)  # izquierda, arriba, derecha, abajo
```

#### Agregar Espacio Elástico
```python
layout.addStretch()  # Espacio que se expande para empujar widgets
```

### Ejemplo Mejorado con Funcionalidad
```python
def generar_formulario(self):
    correo_label = QLabel("Correo electrónico: ")
    self.correo_input = QLineEdit()  # Guardar referencia
    self.correo_input.setPlaceholderText("ejemplo@correo.com")
    
    enviar_button = QPushButton("Enviar")
    enviar_button.clicked.connect(self.enviar_correo)  # Conectar señal

    layout = QHBoxLayout()
    layout.setSpacing(15)  # Espacio entre widgets
    layout.setContentsMargins(20, 20, 20, 20)  # Márgenes
    
    layout.addWidget(correo_label)
    layout.addWidget(self.correo_input)
    layout.addWidget(enviar_button)
    
    self.setLayout(layout)

def enviar_correo(self):
    correo = self.correo_input.text()
    if correo:
        QMessageBox.information(self, "Éxito", f"Correo enviado a: {correo}")
    else:
        QMessageBox.warning(self, "Error", "Por favor ingrese un correo electrónico")
```

### Ventajas de Usar Layouts vs Posicionamiento Absoluto

#### Con Layouts (Recomendado)
```python
layout = QHBoxLayout()
layout.addWidget(QLabel("Texto"))
layout.addWidget(QLineEdit())
self.setLayout(layout)
```

#### Con Posicionamiento Absoluto (Menos Flexible)
```python
label = QLabel("Texto", self)
label.move(10, 10)
input = QLineEdit(self)
input.move(60, 10)
input.resize(200, 25)
```

**Beneficios de los layouts:**
- Se adaptan automáticamente al redimensionar la ventana
- Mantienen las proporciones entre widgets
- Más fácil de mantener y modificar
- Mejor organización del código

### Nota sobre la Importación Duplicada
En tu código hay:
```python
from PyQt6.QtWidgets import (..., QHBoxLayout, QHBoxLayout)
```
Puedes eliminar la duplicidad:
```python
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout)
```


## 19. QVBoxLayout y Manejo de Señales

### Código de Layout Vertical
```python
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setMinimumHeight(200)
        self.setFixedWidth(200)
        self.setWindowTitle('Layout Vertical')
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        boton1 = QPushButton("Botón #1")
        boton2 = QPushButton("Botón #2")
        boton3 = QPushButton("Botón #3")
        boton4 = QPushButton("Botón #4")

        boton1.clicked.connect(self.imprimir_nombre_boton)
        boton2.clicked.connect(self.imprimir_nombre_boton)
        boton3.clicked.connect(self.imprimir_nombre_boton)
        boton4.clicked.connect(self.imprimir_nombre_boton)

        layout = QVBoxLayout()
        layout.addWidget(boton1)
        layout.addWidget(boton2)
        layout.addWidget(boton3)
        layout.addWidget(boton4)

        self.setLayout(layout)  # Definimos nuestro layout como el layout principal de la ventana

    def imprimir_nombre_boton(self):
        boton = self.sender() # Obtiene el botón que envió la señal
        QMessageBox.information(self,"Boton press",f"Has presionado el {boton.text()}", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())
```

![img_3.png](img_3.png)

### Explicación del Código

#### Importación de QVBoxLayout
```python
from PyQt6.QtWidgets import QVBoxLayout
```
- **QVBoxLayout**: Layout que organiza widgets en una columna vertical

#### Configuración de la Ventana
```python
self.setMinimumHeight(200)
self.setFixedWidth(200)
```
- **setMinimumHeight()**: Establece la altura mínima de la ventana
- **setFixedWidth()**: Fija el ancho de la ventana (no redimensionable)

#### Creación de Botones
```python
boton1 = QPushButton("Botón #1")
boton2 = QPushButton("Botón #2")
# ...
```

#### Conexión Múltiple a la Misma Función
```python
boton1.clicked.connect(self.imprimir_nombre_boton)
boton2.clicked.connect(self.imprimir_nombre_boton)
# ...
```
Los 4 botones están conectados a la misma función `imprimir_nombre_boton`

#### Creación del Layout Vertical
```python
layout = QVBoxLayout()
layout.addWidget(boton1)
layout.addWidget(boton2)
layout.addWidget(boton3)
layout.addWidget(boton4)
self.setLayout(layout)
```

### La Función sender() - Concepto Importante

```python
def imprimir_nombre_boton(self):
    boton = self.sender() # Obtiene el botón que envió la señal
    QMessageBox.information(self,"Boton press",f"Has presionado el {boton.text()}", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
```

#### ¿Qué hace sender()?
- **sender()**: Retorna el objeto que emitió la señal
- Permite identificar qué widget específico activó la función
- Útil cuando múltiples widgets están conectados a la misma función

### Métodos Útiles de QVBoxLayout

#### Espaciado entre Widgets
```python
layout.setSpacing(10)  # 10 píxeles entre cada widget
```

#### Configurar Márgenes
```python
layout.setContentsMargins(20, 20, 20, 20)  # izquierda, arriba, derecha, abajo
```

#### Agregar Espacio Elástico
```python
layout.addStretch()  # Espacio que se expande para empujar widgets
```

### Ejemplo Mejorado con Más Configuraciones
```python
def generar_formulario(self):
    boton1 = QPushButton("Botón #1")
    boton2 = QPushButton("Botón #2")
    boton3 = QPushButton("Botón #3")
    boton4 = QPushButton("Botón #4")
    
    # Configurar tamaño de botones
    for boton in [boton1, boton2, boton3, boton4]:
        boton.setFixedHeight(40)
        boton.clicked.connect(self.imprimir_nombre_boton)

    layout = QVBoxLayout()
    layout.setSpacing(10)  # Espacio entre botones
    layout.setContentsMargins(20, 20, 20, 20)  # Márgenes
    
    layout.addWidget(boton1)
    layout.addWidget(boton2)
    layout.addStretch()  # Espacio elástico entre botón 2 y 3
    layout.addWidget(boton3)
    layout.addWidget(boton4)
    
    self.setLayout(layout)
```

### Comparación: QHBoxLayout vs QVBoxLayout

#### QHBoxLayout (Anterior)
```python
layout = QHBoxLayout()
layout.addWidget(widget1)  # ← Widget1 | Widget2 | Widget3 →
layout.addWidget(widget2)
layout.addWidget(widget3)
```

#### QVBoxLayout (Actual)
```python
layout = QVBoxLayout()
layout.addWidget(widget1)  # ↑ Widget1
layout.addWidget(widget2)  #   Widget2
layout.addWidget(widget3)  #   Widget3 ↓
```

### Ventajas de QVBoxLayout

1. **Organización vertical**: Ideal para formularios, listas de opciones
2. **Escalabilidad**: Fácil agregar más elementos sin recalcular posiciones
3. **Responsive**: Se adapta automáticamente al contenido

### Casos de Uso Comunes para QVBoxLayout

- Formularios de registro/login
- Listas de opciones/configuración
- Paneles de control verticales
- Menús de navegación


## 20. Layouts Anidados

### Código de Layouts Anidados
```python
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QLabel, QLineEdit)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100,100,400,150)
        self.setWindowTitle('Layouts Anidados')
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        mensaje_principal = QLabel("Por favor ingrasa sus datos: ")

        nombre_label = QLabel("Nombre: ")
        self.nombres_input = QLineEdit()
        apellido_label = QLabel("Apellido: ")
        self.apellidos_input = QLineEdit()
        edad_label = QLabel("Edad: ")
        self.edad_input = QLineEdit()
        correo_label = QLabel("Correo: ")
        self.correo_input = QLineEdit()
        direccion_label = QLabel("Dirección: ")
        self.direccion_input = QLineEdit()
        telefono_label = QLabel("Teléfono: ")
        self.telefono_input = QLineEdit()
        
        
        # Ajustamos el ancho de las etiquetas para que queden alineadas
        nombre_label.setFixedWidth(90)
        apellido_label.setFixedWidth(90)
        edad_label.setFixedWidth(90)
        correo_label.setFixedWidth(90)
        direccion_label.setFixedWidth(90)
        telefono_label.setFixedWidth(90)

        enviar_boton = QPushButton("Enviar")

        # creamos el layout vertical principal
        vertical_layout_main = QVBoxLayout()

        # creamos los layouts horizontales
        h_layout_1 = QHBoxLayout()
        h_layout_2 = QHBoxLayout()
        h_layout_3 = QHBoxLayout()

        # agregamos los widgets a los layouts horizontales
        h_layout_1.addWidget(nombre_label)
        h_layout_1.addWidget(self.nombres_input)
        h_layout_1.addWidget(correo_label)
        h_layout_1.addWidget(self.correo_input)

        h_layout_2.addWidget(apellido_label)
        h_layout_2.addWidget(self.apellidos_input)
        h_layout_2.addWidget(direccion_label)
        h_layout_2.addWidget(self.direccion_input)

        h_layout_3.addWidget(edad_label)
        h_layout_3.addWidget(self.edad_input)
        h_layout_3.addWidget(telefono_label)
        h_layout_3.addWidget(self.telefono_input)

        # agregamos los layouts horizontales al layout vertical principal
        vertical_layout_main.addWidget(mensaje_principal)
        vertical_layout_main.addLayout(h_layout_1)
        vertical_layout_main.addLayout(h_layout_2)
        vertical_layout_main.addLayout(h_layout_3)
        vertical_layout_main.addWidget(enviar_boton)

        self.setLayout(vertical_layout_main)  # Definimos nuestro layout como el layout principal de la ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())
```

![img_4.png](img_4.png)

### Explicación del Código

#### Concepto de Layouts Anidados
Los layouts anidados consisten en combinar diferentes tipos de layouts (verticales y horizontales) para crear interfaces más complejas y organizadas.

#### Estructura de Layouts en Este Ejemplo
```
QVBoxLayout (principal)
├── QLabel (mensaje_principal)
├── QHBoxLayout (h_layout_1)
│   ├── QLabel (nombre)
│   ├── QLineEdit (nombres)
│   ├── QLabel (correo)
│   └── QLineEdit (correo)
├── QHBoxLayout (h_layout_2)
│   ├── QLabel (apellido)
│   ├── QLineEdit (apellidos)
│   ├── QLabel (dirección)
│   └── QLineEdit (dirección)
├── QHBoxLayout (h_layout_3)
│   ├── QLabel (edad)
│   ├── QLineEdit (edad)
│   ├── QLabel (teléfono)
│   └── QLineEdit (teléfono)
└── QPushButton (enviar_boton)
```

#### Configuración de Ancho Fijo para Etiquetas
```python
nombre_label.setFixedWidth(90)
apellido_label.setFixedWidth(90)
# ...
```
- **setFixedWidth()**: Establece un ancho fijo para el widget
- **Propósito**: Alinear verticalmente todos los labels para una apariencia más ordenada

#### Creación de Layouts Anidados
```python
# Layout vertical principal
vertical_layout_main = QVBoxLayout()

# Layouts horizontales anidados
h_layout_1 = QHBoxLayout()
h_layout_2 = QHBoxLayout()
h_layout_3 = QHBoxLayout()
```

#### Agregar Layouts Dentro de Otros Layouts
```python
vertical_layout_main.addLayout(h_layout_1)
vertical_layout_main.addLayout(h_layout_2)
vertical_layout_main.addLayout(h_layout_3)
```
- **addLayout()**: Agrega un layout dentro de otro layout

### Ventajas de los Layouts Anidados

1. **Organización compleja**: Permiten crear interfaces con estructuras más elaboradas
2. **Mantenimiento fácil**: Cada sección puede modificarse independientemente
3. **Responsive**: Se adaptan mejor al redimensionamiento
4. **Código más limpio**: Mejor organización y legibilidad

### Métodos Útiles para Mejorar los Layouts Anidados

#### Configurar Espaciado Consistente
```python
# Configurar espaciado para todos los layouts
vertical_layout_main.setSpacing(10)
h_layout_1.setSpacing(15)
h_layout_2.setSpacing(15)
h_layout_3.setSpacing(15)
```

#### Establecer Márgenes
```python
vertical_layout_main.setContentsMargins(20, 20, 20, 20)
```

#### Agregar Stretch para Controlar Espacios
```python
# Para que los campos de entrada ocupen más espacio
h_layout_1.addWidget(nombre_label)
h_layout_1.addWidget(self.nombres_input, 1)  # Proporción 1
h_layout_1.addWidget(correo_label)
h_layout_1.addWidget(self.correo_input, 2)   # Proporción 2 (más espacio)
```

### Ejemplo Mejorado con Validación
```python
def generar_formulario(self):
    # ... (código anterior de creación de widgets)
    
    enviar_boton.clicked.connect(self.validar_formulario)
    
    # ... (código anterior de layouts)

def validar_formulario(self):
    # Validar que todos los campos estén completos
    campos = [
        ("Nombre", self.nombres_input.text()),
        ("Apellido", self.apellidos_input.text()),
        ("Edad", self.edad_input.text()),
        ("Correo", self.correo_input.text()),
        ("Dirección", self.direccion_input.text()),
        ("Teléfono", self.telefono_input.text())
    ]
    
    campos_vacios = [nombre for nombre, valor in campos if not valor.strip()]
    
    if campos_vacios:
        QMessageBox.warning(self, "Campos vacíos", 
                           f"Los siguientes campos están vacíos: {', '.join(campos_vacios)}")
    else:
        QMessageBox.information(self, "Éxito", "Formulario enviado correctamente")
```

### Consejos para Diseñar con Layouts Anidados

1. **Planificar la estructura**: Dibujar la interfaz en papel antes de codificar
2. **Usar nombres descriptivos**: Para los layouts y variables
3. **Mantener la consistencia**: Mismos márgenes y espaciado en todos los layouts
4. **Probar el redimensionamiento**: Verificar que la interfaz se vea bien en diferentes tamaños

### Casos de Uso Comunes para Layouts Anidados

- Formularios complejos con múltiples secciones
- Paneles de control con agrupaciones lógicas
- Interfaces de aplicaciones con barras de herramientas y áreas de contenido
- Cuadros de diálogo con múltiples opciones organizadas


## 21. QGridLayout - Diseño en Cuadrícula

### Código de Calculadora con QGridLayout
```python
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QTextEdit, QPushButton, QGridLayout, QMessageBox)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100,100,600, 400)
        self.setWindowTitle("Calculadora Simple")
        self.generar_interfaz()
        self.show()

    def generar_interfaz(self):
        self.pantalla = QTextEdit(self)
        self.pantalla.setDisabled(True)
        boton_1 = QPushButton("1")
        boton_2 = QPushButton("2")
        boton_3 = QPushButton("3")
        boton_4 = QPushButton("4")
        boton_5 = QPushButton("5")
        boton_6 = QPushButton("6")
        boton_7 = QPushButton("7")
        boton_8 = QPushButton("8")
        boton_9 = QPushButton("9")
        boton_0 = QPushButton("0")
        boton_00 = QPushButton("00")
        boton_punto = QPushButton(".")
        boton_suma = QPushButton("+")
        boton_resta = QPushButton("-")
        boton_multiplicacion = QPushButton("*")
        boton_division = QPushButton("/")
        boton_igual = QPushButton("=")
        boton_clear = QPushButton("CE")
        boton_borrar = QPushButton("<-")

        self.main_grid = QGridLayout()
        self.main_grid.addWidget(self.pantalla,0,0,2,4) # 0 fila, 0 columna, ocupa 2 filas y 4 columnas
        self.main_grid.addWidget(boton_clear, 2,0, 1,2) # 2 fila, 0 columna, ocupa 1 fila y 2 columnas
        self.main_grid.addWidget(boton_borrar,2,2) # 2 fila, 2 columna(ocupa 1 fila y 1 columna por defecto)
        self.main_grid.addWidget(boton_suma,2,3) # 2 fila, 3 columna
        self.main_grid.addWidget(boton_7,3,0) # 3 fila 0 columna
        self.main_grid.addWidget(boton_8,3,1) # 3 fila 1 columna
        self.main_grid.addWidget(boton_9,3,2) # 3 fila 2 columna
        self.main_grid.addWidget(boton_division,3, 3) # 3 fila 3 columna
        self.main_grid.addWidget(boton_4,4,0) # 4 fila 0 columna
        self.main_grid.addWidget(boton_5,4,1) # 4 fila
        self.main_grid.addWidget(boton_6,4,2) # 4 fila 2 columna
        self.main_grid.addWidget(boton_multiplicacion,4,3) # 4 fila 3 columna
        self.main_grid.addWidget(boton_1,5,0) # 5 fila 0 columna
        self.main_grid.addWidget(boton_2,5,1) # 5 fila 1 columna
        self.main_grid.addWidget(boton_3,5,2) # 5 fila 2 columna
        self.main_grid.addWidget(boton_resta,5,3) # 5 fila 3 columna
        self.main_grid.addWidget(boton_0,6,0) # 6 fila 0 columna
        self.main_grid.addWidget(boton_00,6,1) # 6 fila 1 columna
        self.main_grid.addWidget(boton_punto,6,2) # 6 fila 2 columna
        self.main_grid.addWidget(boton_igual,6,3) # 6 fila 3 columna

        self.setLayout(self.main_grid)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())
```
![img_5.png](img_5.png)
### Explicación del Código

#### QGridLayout - Layout de Cuadrícula
```python
self.main_grid = QGridLayout()
```
- **QGridLayout**: Organiza widgets en una cuadrícula de filas y columnas
- Ideal para interfaces que necesitan disposición tabular como calculadoras, teclados, etc.

#### Sintaxis de addWidget en QGridLayout
```python
self.main_grid.addWidget(widget, fila, columna, rowSpan, colSpan)
```

**Parámetros:**
- **widget**: El widget a agregar
- **fila**: Número de fila (empieza en 0)
- **columna**: Número de columna (empieza en 0)
- **rowSpan**: Cuántas filas ocupa (opcional, default: 1)
- **colSpan**: Cuántas columnas ocupa (opcional, default: 1)

#### Ejemplos del Código

**Pantalla que ocupa 2 filas y 4 columnas:**
```python
self.main_grid.addWidget(self.pantalla, 0, 0, 2, 4)
```
- Fila: 0
- Columna: 0
- Ocupa 2 filas
- Ocupa 4 columnas

**Botón CE que ocupa 1 fila y 2 columnas:**
```python
self.main_grid.addWidget(boton_clear, 2, 0, 1, 2)
```

**Botón normal (ocupa 1x1):**
```python
self.main_grid.addWidget(boton_7, 3, 0)
```

### Estructura de la Cuadrícula de la Calculadora

```
Fila 0-1: [          Pantalla (4 columnas)          ]
Fila 2:   [ CE (2 cols) ] [ <- ] [ + ]
Fila 3:   [ 7 ] [ 8 ] [ 9 ] [ / ]
Fila 4:   [ 4 ] [ 5 ] [ 6 ] [ * ]
Fila 5:   [ 1 ] [ 2 ] [ 3 ] [ - ]
Fila 6:   [ 0 ] [ 00 ] [ . ] [ = ]
```

### QTextEdit como Pantalla
```python
self.pantalla = QTextEdit(self)
self.pantalla.setDisabled(True)
```
- **QTextEdit**: Widget de texto multilínea
- **setDisabled(True)**: Hace que la pantalla sea de solo lectura
- Alternativa: `QLineEdit` para una sola línea o `QLabel`

### Métodos Útiles de QGridLayout

#### Configurar Espaciado
```python
self.main_grid.setSpacing(5)  # Espacio entre celdas
```

#### Configurar Márgenes
```python
self.main_grid.setContentsMargins(10, 10, 10, 10)
```

#### Obtener Información de la Cuadrícula
```python
row_count = self.main_grid.rowCount()
column_count = self.main_grid.columnCount()
```

### Ejemplo Mejorado con Configuraciones Adicionales
```python
def generar_interfaz(self):
    # Configurar pantalla
    self.pantalla = QTextEdit(self)
    self.pantalla.setDisabled(True)
    self.pantalla.setMaximumHeight(80)  # Limitar altura
    
    # Crear botones (código existente)
    # ...
    
    self.main_grid = QGridLayout()
    self.main_grid.setSpacing(5)  # Espacio entre botones
    self.main_grid.setContentsMargins(15, 15, 15, 15)  # Márgenes
    
    # Agregar widgets (código existente)
    # ...
    
    # Configurar tamaño de botones
    botones = [boton_0, boton_1, boton_2, boton_3, boton_4, 
               boton_5, boton_6, boton_7, boton_8, boton_9,
               boton_00, boton_punto, boton_suma, boton_resta,
               boton_multiplicacion, boton_division, boton_igual,
               boton_clear, boton_borrar]
    
    for boton in botones:
        boton.setFixedSize(60, 50)  # Tamaño uniforme para todos los botones
    
    self.setLayout(self.main_grid)
```

### Ventajas de QGridLayout

1. **Precisión**: Control exacto de la posición de cada widget
2. **Flexibilidad**: Widgets pueden ocupar múltiples celdas
3. **Organización**: Ideal para interfaces con estructura de tabla
4. **Escalabilidad**: Fácil agregar más filas/columnas

### Casos de Uso Comunes para QGridLayout

- Calculadoras
- Teclados numéricos
- Interfaces de tablero de instrumentos
- Formularios complejos con etiquetas y campos alineados
- Juegos de tablero

### Comparación con Otros Layouts

| Layout | Uso Ideal | Ventajas |
|--------|-----------|----------|
| **QGridLayout** | Interfaces tabulares | Máximo control de posición |
| **QHBoxLayout** | Filas horizontales | Simple, orden lineal |
| **QVBoxLayout** | Columnas verticales | Simple, orden vertical |
| **Anidados** | Interfaces complejas | Combinación de estructuras |


## 22. Calculadora Funcional - Lógica Completa

### Código Completo de la Calculadora Funcional

```python
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QTextEdit, QPushButton, QGridLayout, QMessageBox)
import operator

# Diccionario para mapear los operadores a las funciones correspondientes
# Esto trabaja con strings para facilitar la selección del operador
operation = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.primerValor = ""
        self.segundoValor = ""
        self.operacion = ""
        self.pointer_flag = "1"
        self.after_equal = False
        self.after_operator = False

    def inicializarUI(self):
        self.setGeometry(100,100,600, 400)
        self.setWindowTitle("Calculadora Simple")
        self.generar_interfaz()
        self.show()

    def generar_interfaz(self):
        self.pantalla = QTextEdit(self)
        self.pantalla.setDisabled(True)
        boton_1 = QPushButton("1")
        boton_2 = QPushButton("2")
        boton_3 = QPushButton("3")
        boton_4 = QPushButton("4")
        boton_5 = QPushButton("5")
        boton_6 = QPushButton("6")
        boton_7 = QPushButton("7")
        boton_8 = QPushButton("8")
        boton_9 = QPushButton("9")
        boton_0 = QPushButton("0")
        boton_00 = QPushButton("00")
        boton_punto = QPushButton(".")

        # Conectamos los botones numéricos a la función ingresar_datos
        boton_1.clicked.connect(self.ingresar_datos)
        boton_2.clicked.connect(self.ingresar_datos)
        boton_3.clicked.connect(self.ingresar_datos)
        boton_4.clicked.connect(self.ingresar_datos)
        boton_5.clicked.connect(self.ingresar_datos)
        boton_6.clicked.connect(self.ingresar_datos)
        boton_7.clicked.connect(self.ingresar_datos)
        boton_8.clicked.connect(self.ingresar_datos)
        boton_9.clicked.connect(self.ingresar_datos)
        boton_0.clicked.connect(self.ingresar_datos)
        boton_00.clicked.connect(self.ingresar_datos)
        boton_punto.clicked.connect(self.ingresar_datos)

        boton_suma = QPushButton("+")
        boton_resta = QPushButton("-")
        boton_multiplicacion = QPushButton("*")
        boton_division = QPushButton("/")
        boton_igual = QPushButton("=")
        boton_clear = QPushButton("CE")
        boton_borrar = QPushButton("<-")

        boton_suma.clicked.connect(self.ingresar_operador)
        boton_resta.clicked.connect(self.ingresar_operador)
        boton_multiplicacion.clicked.connect(self.ingresar_operador)
        boton_division.clicked.connect(self.ingresar_operador)

        boton_clear.clicked.connect(self.borrar_todo)
        boton_borrar.clicked.connect(self.borrar_parcial)
        boton_igual.clicked.connect(self.calcular_resultado)

        self.main_grid = QGridLayout()
        self.main_grid.addWidget(self.pantalla,0,0,2,4) # 0 fila, 0 columna, ocupa 2 filas y 4 columnas
        self.main_grid.addWidget(boton_clear, 2,0, 1,2) # 2 fila, 0 columna, ocupa 1 fila y 2 columnas
        self.main_grid.addWidget(boton_borrar,2,2) # 2 fila, 2 columna(ocupa 1 fila y 1 columna por defecto)
        self.main_grid.addWidget(boton_suma,2,3) # 2 fila, 3 columna
        self.main_grid.addWidget(boton_7,3,0) # 3 fila 0 columna
        self.main_grid.addWidget(boton_8,3,1) # 3 fila 1 columna
        self.main_grid.addWidget(boton_9,3,2) # 3 fila 2 columna
        self.main_grid.addWidget(boton_division,3, 3) # 3 fila 3 columna
        self.main_grid.addWidget(boton_4,4,0) # 4 fila 0 columna
        self.main_grid.addWidget(boton_5,4,1) # 4 fila
        self.main_grid.addWidget(boton_6,4,2) # 4 fila 2 columna
        self.main_grid.addWidget(boton_multiplicacion,4,3) # 4 fila 3 columna
        self.main_grid.addWidget(boton_1,5,0) # 5 fila 0 columna
        self.main_grid.addWidget(boton_2,5,1) # 5 fila 1 columna
        self.main_grid.addWidget(boton_3,5,2) # 5 fila 2 columna
        self.main_grid.addWidget(boton_resta,5,3) # 5 fila 3 columna
        self.main_grid.addWidget(boton_0,6,0) # 6 fila 0 columna
        self.main_grid.addWidget(boton_00,6,1) # 6 fila 1 columna
        self.main_grid.addWidget(boton_punto,6,2) # 6 fila 2 columna
        self.main_grid.addWidget(boton_igual,6,3) # 6 fila 3 columna

        self.setLayout(self.main_grid)

    def ingresar_datos(self):
        boton_text = self.sender().text()
        if self.after_equal:
            self.primerValor = ""
            self.pantalla.setText(self.primerValor)
            self.after_equal = False
            self.pointer_flag = "1"
        if self.pointer_flag == "1":
            self.primerValor += boton_text
            self.pantalla.setText(self.primerValor)
        else:
            self.segundoValor += boton_text
            self.pantalla.setText(self.pantalla.toPlainText()+boton_text)

    def ingresar_operador(self):
        boton_text = self.sender().text()
        self.operacion = boton_text
        self.pointer_flag = "2"

        if self.after_operator == True and self.segundoValor != "":
            self.calcular_resultado()
            self.pantalla.setText(self.primerValor + " "+self.sender().text()+"" + self.operacion + " ")
        else:
            self.pantalla.setText(self.pantalla.toPlainText() + " " + self.operacion + " ")

        self.after_operator = True
        self.after_equal = False

    def borrar_todo(self):
        self.primerValor = ""
        self.segundoValor = ""
        self.operacion = ""
        self.pointer_flag = "1"
        self.after_equal = False
        self.after_operator = False
        self.pantalla.setText("")

    def borrar_parcial(self):
        if self.after_equal:
            self.borrar_todo()
        if self.pointer_flag == "1":
            self.primerValor = self.primerValor[:-1]
            self.pantalla.setText(self.primerValor)
        else:
            self.segundoValor = self.segundoValor[:-1]
            self.pantalla.setText(self.segundoValor)

    def calcular_resultado(self):
        resultado = str(operation[self.operacion](float(self.primerValor), float(self.segundoValor)))
        self.pantalla.setText(resultado)
        self.primerValor = resultado
        self.segundoValor = ""
        self.operacion = ""
        self.after_equal = True
        self.after_operator = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())
```

### Explicación de la Lógica de la Calculadora

#### Variables de Estado
```python
self.primerValor = ""        # Primer número de la operación
self.segundoValor = ""       # Segundo número de la operación  
self.operacion = ""          # Operador actual (+, -, *, /)
self.pointer_flag = "1"      # Indica si estamos en el primer o segundo valor
self.after_equal = False     # Indica si acabamos de presionar "="
self.after_operator = False  # Indica si acabamos de presionar un operador
```

#### Uso del Módulo Operator
```python
import operator

operation = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
```
- **operator**: Módulo de Python que proporciona funciones para operadores aritméticos
- **operation**: Diccionario que mapea símbolos de operadores a funciones

#### Función `ingresar_datos`
```python
def ingresar_datos(self):
    boton_text = self.sender().text()
    if self.after_equal:
        self.primerValor = ""
        self.pantalla.setText(self.primerValor)
        self.after_equal = False
        self.pointer_flag = "1"
    if self.pointer_flag == "1":
        self.primerValor += boton_text
        self.pantalla.setText(self.primerValor)
    else:
        self.segundoValor += boton_text
        self.pantalla.setText(self.pantalla.toPlainText()+boton_text)
```

**Flujo:**
1. Obtiene el texto del botón presionado con `self.sender().text()`
2. Si se acaba de presionar "=", reinicia el estado
3. Dependiendo de `pointer_flag`, concatena al primer o segundo valor
4. Actualiza la pantalla

#### Función `ingresar_operador`
```python
def ingresar_operador(self):
    boton_text = self.sender().text()
    self.operacion = boton_text
    self.pointer_flag = "2"

    if self.after_operator == True and self.segundoValor != "":
        self.calcular_resultado()
        self.pantalla.setText(self.primerValor + " "+self.sender().text()+"" + self.operacion + " ")
    else:
        self.pantalla.setText(self.pantalla.toPlainText() + " " + self.operacion + " ")

    self.after_operator = True
    self.after_equal = False
```

**Funcionamiento:**
- Cambia `pointer_flag` a "2" para comenzar a recibir el segundo valor
- Si ya hay una operación en curso, calcula el resultado primero
- Actualiza la pantalla con el operador

#### Función `borrar_todo` (CE)
```python
def borrar_todo(self):
    self.primerValor = ""
    self.segundoValor = ""
    self.operacion = ""
    self.pointer_flag = "1"
    self.after_equal = False
    self.after_operator = False
    self.pantalla.setText("")
```
Reinicia completamente el estado de la calculadora.

#### Función `borrar_parcial` (<-)
```python
def borrar_parcial(self):
    if self.after_equal:
        self.borrar_todo()
    if self.pointer_flag == "1":
        self.primerValor = self.primerValor[:-1]
        self.pantalla.setText(self.primerValor)
    else:
        self.segundoValor = self.segundoValor[:-1]
        self.pantalla.setText(self.segundoValor)
```
Elimina el último carácter del valor actual.

#### Función `calcular_resultado` (=)
```python
def calcular_resultado(self):
    resultado = str(operation[self.operacion](float(self.primerValor), float(self.segundoValor)))
    self.pantalla.setText(resultado)
    self.primerValor = resultado
    self.segundoValor = ""
    self.operacion = ""
    self.after_equal = True
    self.after_operator = False
```

**Proceso:**
1. Usa el diccionario `operation` para obtener la función del operador
2. Convierte los valores a float y realiza la operación
3. Muestra el resultado
4. Guarda el resultado en `primerValor` para operaciones consecutivas
5. Actualiza las banderas de estado

### Conexión de Señales

#### Botones Numéricos
```python
boton_1.clicked.connect(self.ingresar_datos)
boton_2.clicked.connect(self.ingresar_datos)
# ... todos los botones numéricos
```

#### Botones de Operación
```python
boton_suma.clicked.connect(self.ingresar_operador)
boton_resta.clicked.connect(self.ingresar_operador)
# ... todos los operadores
```

#### Botones de Control
```python
boton_clear.clicked.connect(self.borrar_todo)
boton_borrar.clicked.connect(self.borrar_parcial)
boton_igual.clicked.connect(self.calcular_resultado)
```

### Flujo de una Operación Completa

**Ejemplo: 5 + 3 =**

1. **Presionar "5"**: `primerValor = "5"`, pantalla muestra "5"
2. **Presionar "+"**: `operacion = "+"`, `pointer_flag = "2"`, pantalla muestra "5 +"
3. **Presionar "3"**: `segundoValor = "3"`, pantalla muestra "5 + 3"
4. **Presionar "="**: Calcula 5+3=8, pantalla muestra "8", `primerValor = "8"`

### Mejoras Potenciales

1. **Manejo de errores**: División por cero, números muy grandes
2. **Validación de entrada**: Evitar múltiples puntos decimales
3. **Operaciones con decimales**: Mejor manejo de números flotantes
4. **Historial**: Mostrar la operación completa
5. **Teclado**: Soporte para entrada por teclado

## 23. QFormLayout - Diseño Especializado para Formularios

### Código del Formulario con QFormLayout
```python
import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QFormLayout, QHBoxLayout, QDateEdit, QComboBox)

from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100,100,200,600)
        self.setWindowTitle("FormLayout")
        self.crearFormulario()
        self.show()

    def crearFormulario(self):
        titulo = QLabel("Solicitud de ingreso")
        titulo.setFont(QFont('Arial',18))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.nombreEdit = QLineEdit()
        self.nombreEdit.setPlaceholderText("Nombre")

        self.apellidoEdit = QLineEdit()
        self.apellidoEdit.setPlaceholderText("Apellido")

        self.genero_selection = QComboBox()
        self.genero_selection.addItems(["Masculino", "Femenino", "Otro"])

        self.fechaNacimiento = QDateEdit()
        self.fechaNacimiento.setDisplayFormat("yyyy-MM-dd")
        self.fechaNacimiento.setMaximumDate(QDate.currentDate())
        self.fechaNacimiento.setCalendarPopup(True)
        self.fechaNacimiento.setDate(QDate.currentDate())

        self.telefono = QLineEdit()
        self.telefono.setPlaceholderText("000-000-000")

        submit_button = QPushButton("Enviar")
        submit_button.clicked.connect(self.mostrar_info)


        primer_h_box = QHBoxLayout()
        primer_h_box.addWidget(self.nombreEdit)
        primer_h_box.addWidget(self.apellidoEdit)

        main_form = QFormLayout()
        main_form.addRow(titulo)
        main_form.addRow("Nombre y Apellido: ", primer_h_box)
        main_form.addRow("Género: ", self.genero_selection)
        main_form.addRow("Fecha de Nacimiento: ", self.fechaNacimiento)
        main_form.addRow("Teléfono: ", self.telefono)
        main_form.addRow(submit_button)

        self.setLayout(main_form)


    def mostrar_info(self):
        QMessageBox.information(self,
                                "Información",
                                f"Nombre: {self.nombreEdit.text()}\n"
                                f"Apellido: {self.apellidoEdit.text()}\n"
                                f"Género: {self.genero_selection.currentText()}\n"
                                f"Fecha de Nacimiento: {self.fechaNacimiento.date().toString()}\n",
                                QMessageBox.StandardButton.Ok,
                                QMessageBox.StandardButton.Ok
                             )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())
```

![img_6.png](img_6.png)

### Explicación del Código

#### QFormLayout - Layout Especializado para Formularios
```python
main_form = QFormLayout()
```
- **QFormLayout**: Diseñado específicamente para formularios con etiquetas y campos
- Organiza automáticamente las etiquetas y los campos de entrada
- Ideal para formularios de registro, configuración, etc.

#### Estructura del QFormLayout
```
[Etiqueta] [Campo/Widget]
[Etiqueta] [Campo/Widget]
...
```

#### Agregar Filas al FormLayout
```python
main_form.addRow(titulo)  # Fila con un solo widget
main_form.addRow("Nombre y Apellido: ", primer_h_box)  # Fila con etiqueta y layout
main_form.addRow("Género: ", self.genero_selection)  # Fila con etiqueta y widget
```

### Nuevos Widgets Introducidos

#### QComboBox - Lista Desplegable
```python
self.genero_selection = QComboBox()
self.genero_selection.addItems(["Masculino", "Femenino", "Otro"])
```
- **QComboBox**: Widget de selección desplegable
- **addItems()**: Añade múltiples opciones a la lista

#### QDateEdit - Selector de Fecha
```python
self.fechaNacimiento = QDateEdit()
self.fechaNacimiento.setDisplayFormat("yyyy-MM-dd")
self.fechaNacimiento.setMaximumDate(QDate.currentDate())
self.fechaNacimiento.setCalendarPopup(True)
self.fechaNacimiento.setDate(QDate.currentDate())
```

**Configuraciones:**
- **setDisplayFormat()**: Formato de visualización de la fecha
- **setMaximumDate()**: Fecha máxima permitida
- **setCalendarPopup(True)**: Muestra un calendario desplegable
- **setDate()**: Fecha inicial

#### Placeholder Text
```python
self.nombreEdit.setPlaceholderText("Nombre")
```
- **setPlaceholderText()**: Texto de ejemplo que desaparece al escribir

### Configuraciones de Texto y Fuente

#### QFont - Configuración de Fuente
```python
titulo.setFont(QFont('Arial',18))
```
- **QFont**: Clase para configurar fuentes tipográficas
- Parámetros: familia de fuente y tamaño

#### Alineación de Texto
```python
titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
```
- **AlignmentFlag.AlignCenter**: Centra el texto horizontalmente

### Combinación de Layouts

#### QHBoxLayout dentro de QFormLayout
```python
primer_h_box = QHBoxLayout()
primer_h_box.addWidget(self.nombreEdit)
primer_h_box.addWidget(self.apellidoEdit)

main_form.addRow("Nombre y Apellido: ", primer_h_box)
```
- Se puede incluir cualquier layout dentro de una fila de QFormLayout
- Útil para agrupar múltiples widgets en una misma fila

### Métodos Útiles de QFormLayout

#### Agregar Diferentes Tipos de Filas
```python
# Fila con etiqueta de texto y widget
main_form.addRow("Etiqueta:", widget)

# Fila con QLabel y widget
main_form.addRow(QLabel("Etiqueta"), widget)

# Fila con solo un widget (ocupa ambas columnas)
main_form.addRow(widget)

# Fila con layout
main_form.addRow("Etiqueta:", layout)
```

#### Configurar Espaciado y Márgenes
```python
main_form.setSpacing(10)  # Espacio entre filas
main_form.setContentsMargins(20, 20, 20, 20)  # Márgenes
```

#### Configurar Alineación de Etiquetas
```python
main_form.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
```

### Función de Mostrar Información
```python
def mostrar_info(self):
    QMessageBox.information(self,
                            "Información",
                            f"Nombre: {self.nombreEdit.text()}\n"
                            f"Apellido: {self.apellidoEdit.text()}\n"
                            f"Género: {self.genero_selection.currentText()}\n"
                            f"Fecha de Nacimiento: {self.fechaNacimiento.date().toString()}\n",
                            QMessageBox.StandardButton.Ok,
                            QMessageBox.StandardButton.Ok
                         )
```

**Métodos utilizados:**
- **text()**: Obtiene el texto de QLineEdit
- **currentText()**: Obtiene el texto seleccionado en QComboBox
- **date().toString()**: Convierte QDate a string

### Ventajas de QFormLayout

1. **Organización automática**: Alinea perfectamente etiquetas y campos
2. **Código más limpio**: Menos código para lograr el mismo resultado
3. **Consistencia visual**: Todas las etiquetas tienen el mismo ancho y alineación
4. **Adaptabilidad**: Se ajusta automáticamente al contenido

### Ejemplo Mejorado con Validación
```python
def crearFormulario(self):
    # ... (código anterior)
    
    submit_button.clicked.connect(self.validar_y_mostrar)
    # ...

def validar_y_mostrar(self):
    # Validar campos obligatorios
    if not self.nombreEdit.text().strip() or not self.apellidoEdit.text().strip():
        QMessageBox.warning(self, "Error", "Nombre y Apellido son obligatorios")
        return
    
    # Validar teléfono (solo números)
    if not self.telefono.text().replace("-", "").isdigit():
        QMessageBox.warning(self, "Error", "El teléfono debe contener solo números")
        return
    
    self.mostrar_info()
```

### Casos de Uso Ideales para QFormLayout

- Formularios de registro de usuarios
- Configuraciones de aplicación
- Paneles de administración
- Diálogos de preferencias
- Formularios de contacto

### Comparación con Otros Layouts para Formularios

| Layout | Ventajas para Formularios |
|--------|---------------------------|
| **QFormLayout** | Automático, etiquetas alineadas, menos código |
| **QGridLayout** | Control total, posiciones exactas |
| **QVBoxLayout** | Simple pero requiere más configuración manual |

# Guía de PyQt6 - Continuación

## 24. QGroupBox y Botones con Estado (Toggle Buttons)

### Código de Ejemplo con QGroupBox y Toggle Buttons
```python
import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QGroupBox

class ventanaBotones(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()

    def inicializarUI(self):
        # Botones normales (Push Buttons)
        self.bMortadelo = QPushButton("Mortadelo")
        self.bFilemon = QPushButton("Filemon")
        self.bCarpanta = QPushButton("Carpanta")
        self.bRompetechos = QPushButton("Rompetechos")
        self.bPepeGotera = QPushButton("Pepe Gotera")
        self.bOtilio = QPushButton("Otilio")

        self.cajaHorizontal1 = QHBoxLayout()
        self.cajaHorizontal1.addWidget(self.bMortadelo)
        self.cajaHorizontal1.addWidget(self.bFilemon)
        self.cajaHorizontal1.addWidget(self.bCarpanta)
        self.cajaHorizontal1.addWidget(self.bRompetechos)
        self.cajaHorizontal1.addWidget(self.bPepeGotera)
        self.cajaHorizontal1.addWidget(self.bOtilio)

        self.group = QGroupBox("Push Buttons")
        self.group.setLayout(self.cajaHorizontal1)

        # Botones con estado (Toggle Buttons)
        self.tMortadelo = QPushButton("Mortadelo")
        self.tFilemon = QPushButton("Filemon")
        self.tCarpanta = QPushButton("Carpanta")
        self.tRompetechos = QPushButton("Rompetechos")
        self.tPepeGotera = QPushButton("Pepe Gotera")
        self.tOtilio = QPushButton("Otilio")

        # Configurar botones como "checkeables" (toggle)
        self.tMortadelo.setCheckable(True)
        self.tMortadelo.setChecked(False)
        self.tFilemon.setCheckable(True)
        self.tFilemon.setChecked(False)
        self.tCarpanta.setCheckable(True)
        self.tCarpanta.setChecked(False)
        self.tRompetechos.setCheckable(True)
        self.tRompetechos.setChecked(False)
        self.tPepeGotera.setCheckable(True)
        self.tPepeGotera.setChecked(False)
        self.tOtilio.setCheckable(True)
        self.tOtilio.setChecked(False)

        self.cajaHorizontal2 = QHBoxLayout()
        self.cajaHorizontal2.addWidget(self.tMortadelo)
        self.cajaHorizontal2.addWidget(self.tFilemon)
        self.cajaHorizontal2.addWidget(self.tCarpanta)
        self.cajaHorizontal2.addWidget(self.tRompetechos)
        self.cajaHorizontal2.addWidget(self.tPepeGotera)
        self.cajaHorizontal2.addWidget(self.tOtilio)

        self.group2 = QGroupBox("Toggle Buttons")
        self.group2.setLayout(self.cajaHorizontal2)

        self.cajaVertical = QVBoxLayout()
        self.cajaVertical.addWidget(self.group)
        self.cajaVertical.addWidget(self.group2)

        self.setLayout(self.cajaVertical)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ventanaBotones()
    sys.exit(app.exec())
```

![img_7.png](img_7.png)


### Explicación del Código

#### QGroupBox - Agrupación de Widgets
```python
self.group = QGroupBox("Push Buttons")
self.group.setLayout(self.cajaHorizontal1)
```
- **QGroupBox**: Widget que agrupa otros widgets con un título y un marco
- **Propósito**: Organizar visualmente elementos relacionados
- **setLayout()**: Asigna un layout al grupo

#### Botones Normales vs Toggle Buttons

**Botones Normales (Push Buttons):**
```python
self.bMortadelo = QPushButton("Mortadelo")
```
- Comportamiento normal: se presionan y sueltan
- No mantienen estado

**Toggle Buttons (Botones con Estado):**
```python
self.tMortadelo = QPushButton("Mortadelo")
self.tMortadelo.setCheckable(True)
self.tMortadelo.setChecked(False)
```

### Configuración de Toggle Buttons

#### setCheckable(True)
```python
self.tMortadelo.setCheckable(True)
```
- **setCheckable(True)**: Hace que el botón pueda mantener un estado (marcado/no marcado)
- El botón se comporta como un interruptor
- Cambia de apariencia visual cuando está marcado

#### setChecked(False/True)
```python
self.tMortadelo.setChecked(False)  # Estado inicial: no marcado
```
- **setChecked()**: Establece el estado inicial del botón
- `True`: Botón marcado/presionado
- `False`: Botón no marcado/normal

### Comportamiento de los Toggle Buttons

#### Estados del Botón:
- **No marcado**: Apariencia normal
- **Marcado**: Apariencia presionada (como si estuviera hundido)

#### Interacción:
- **Clic**: Cambia entre marcado y no marcado
- **Mantiene el estado** hasta que se vuelve a hacer clic

### Métodos Útiles para Toggle Buttons

#### Verificar Estado Actual
```python
if self.tMortadelo.isChecked():
    print("Mortadelo está marcado")
else:
    print("Mortadelo no está marcado")
```

#### Cambiar Estado Programáticamente
```python
self.tMortadelo.setChecked(True)   # Marcar
self.tMortadelo.setChecked(False)  # Desmarcar
```

#### Alternar Estado
```python
self.tMortadelo.toggle()  # Cambia al estado opuesto
```

### Conexión de Señales para Toggle Buttons

#### Señal clicked vs toggled
```python
# Se ejecuta cada vez que se hace clic (sin importar el estado)
self.tMortadelo.clicked.connect(self.boton_clicado)

# Se ejecuta cuando cambia el estado, recibe el nuevo estado como parámetro
self.tMortadelo.toggled.connect(self.boton_alternado)
```

#### Ejemplo de Funciones de Conexión
```python
def inicializarUI(self):
    # ... código anterior ...
    
    # Conectar señales de los toggle buttons
    self.tMortadelo.toggled.connect(self.actualizar_estado_mortadelo)
    self.tFilemon.toggled.connect(self.actualizar_estado_filemon)
    # ... conectar los demás botones

def actualizar_estado_mortadelo(self, estado):
    if estado:
        print("Mortadelo ACTIVADO")
    else:
        print("Mortadelo DESACTIVADO")

def actualizar_estado_filemon(self, estado):
    if estado:
        print("Filemon ACTIVADO")
    else:
        print("Filemon DESACTIVADO")
```

### Ejemplo Mejorado con Funcionalidad Completa

```python
import sys
from PyQt6.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, 
                             QApplication, QGroupBox, QLabel)

class ventanaBotones(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()

    def inicializarUI(self):
        # Configurar ventana
        self.setWindowTitle("Ejemplo de Botones")
        self.setGeometry(100, 100, 600, 200)
        
        # Botones normales
        self.crear_botones_normales()
        
        # Botones toggle
        self.crear_botones_toggle()
        
        # Etiqueta para mostrar estado
        self.etiqueta_estado = QLabel("Estado: Ningún botón toggle seleccionado")
        
        # Layout principal
        caja_vertical = QVBoxLayout()
        caja_vertical.addWidget(self.group)
        caja_vertical.addWidget(self.group2)
        caja_vertical.addWidget(self.etiqueta_estado)
        
        self.setLayout(caja_vertical)

    def crear_botones_normales(self):
        # Crear botones normales
        botones_normales = ["Mortadelo", "Filemon", "Carpanta", 
                           "Rompetechos", "Pepe Gotera", "Otilio"]
        
        self.botones_normales = {}
        caja_horizontal = QHBoxLayout()
        
        for nombre in botones_normales:
            boton = QPushButton(nombre)
            boton.clicked.connect(lambda checked, nom=nombre: self.boton_normal_pulsado(nom))
            self.botones_normales[nombre] = boton
            caja_horizontal.addWidget(boton)
        
        self.group = QGroupBox("Push Buttons (Normales)")
        self.group.setLayout(caja_horizontal)

    def crear_botones_toggle(self):
        # Crear botones toggle
        botones_toggle = ["Mortadelo", "Filemon", "Carpanta", 
                         "Rompetechos", "Pepe Gotera", "Otilio"]
        
        self.botones_toggle = {}
        caja_horizontal = QHBoxLayout()
        
        for nombre in botones_toggle:
            boton = QPushButton(nombre)
            boton.setCheckable(True)
            boton.setChecked(False)
            boton.toggled.connect(lambda estado, nom=nombre: self.boton_toggle_cambiado(nom, estado))
            self.botones_toggle[nombre] = boton
            caja_horizontal.addWidget(boton)
        
        self.group2 = QGroupBox("Toggle Buttons (Con Estado)")
        self.group2.setLayout(caja_horizontal)

    def boton_normal_pulsado(self, nombre):
        print(f"Botón normal pulsado: {nombre}")

    def boton_toggle_cambiado(self, nombre, estado):
        if estado:
            print(f"Toggle ACTIVADO: {nombre}")
        else:
            print(f"Toggle DESACTIVADO: {nombre}")
        
        # Actualizar etiqueta con los botones activos
        botones_activos = [nom for nom, btn in self.botones_toggle.items() if btn.isChecked()]
        if botones_activos:
            self.etiqueta_estado.setText(f"Estado: {', '.join(botones_activos)}")
        else:
            self.etiqueta_estado.setText("Estado: Ningún botón toggle seleccionado")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ventanaBotones()
    sys.exit(app.exec())
```

### Diferencias Visuales y de Comportamiento

| Característica | Push Button Normal | Toggle Button |
|----------------|-------------------|---------------|
| **Apariencia** | Siempre igual | Cambia cuando está marcado |
| **Estado** | No mantiene estado | Mantiene estado (on/off) |
| **Uso típico** | Acciones inmediatas | Opciones/configuraciones |
| **Señal útil** | `clicked` | `toggled` |

### Casos de Uso para Toggle Buttons

1. **Opciones de configuración**: Activar/desactivar funciones
2. **Modos de aplicación**: Modo edición vs modo visualización
3. **Selección múltiple**: Cuando se pueden elegir varias opciones
4. **Interruptores virtuales**: Encendido/apagado de características

### Ventajas de QGroupBox

1. **Organización visual**: Agrupa elementos relacionados
2. **Mejor usabilidad**: Los usuarios entienden la relación entre los widgets
3. **Ahorro de espacio**: Permite organizar más elementos de forma clara
4. **Título descriptivo**: Explica el propósito del grupo

# Guía de PyQt6 - Señales y RadioButtons

## 25. RadioButtons y Manejo de Señales

### Código de Ejemplo con RadioButtons
```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QTextEdit

class VentanaConRadioButton(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()

    def inicializarUI(self):
        self.setWindowTitle("Radio Buttons")
        self.cajaHorizontal = QHBoxLayout()

        self.boton1 = QRadioButton("Mostrar Nombre")
        self.boton2 = QRadioButton("Mostrar edad")
        self.boton3 = QRadioButton("Pasar texto a label")
        self.boton4 = QRadioButton("Pasar texto a mayusculas")

        self.cajaHorizontal.addWidget(self.boton1)
        self.cajaHorizontal.addWidget(self.boton2)
        self.cajaHorizontal.addWidget(self.boton3)
        self.cajaHorizontal.addWidget(self.boton4)

        self.panelParaEscribir = QTextEdit()
        self.panelParaMostrar = QTextEdit()
        self.panelParaMostrar.setDisabled(True)

        self.cajaVertical = QVBoxLayout()

        self.cajaVertical.addLayout(self.cajaHorizontal)
        self.cajaVertical.addWidget(self.panelParaEscribir)
        self.cajaVertical.addWidget(self.panelParaMostrar)

        self.boton1.clicked.connect(self.mostrarNombre)
        self.boton2.clicked.connect(self.mostrarEdad)
        self.boton3.clicked.connect(self.pasarTextoALabel)
        self.boton4.clicked.connect(self.pasarTextoAMayusculas)

        self.setLayout(self.cajaVertical)

    def mostrarNombre(self):
        self.panelParaMostrar.setPlainText("Daniel")
    def mostrarEdad(self):
        self.panelParaMostrar.setPlainText("22")

    def pasarTextoALabel(self):
        texto = self.panelParaEscribir.toPlainText()
        self.panelParaMostrar.setPlainText(texto)

    def pasarTextoAMayusculas(self):
        texto = self.panelParaMostrar.toPlainText()
        self.panelParaMostrar.setPlainText(texto.upper())
```

![img_8.png](img_8.png)


## Explicación Detallada

### QRadioButton - Botones de Opción Única

#### Características Principales
```python
self.boton1 = QRadioButton("Mostrar Nombre")
```
- **Selección exclusiva**: Solo un RadioButton puede estar seleccionado a la vez dentro del mismo grupo
- **Comportamiento de grupo**: Automáticamente se deseleccionan mutuamente
- **Estado visual**: Muestra un punto cuando está seleccionado

### Señales en PyQt6 - Conceptos Fundamentales

#### ¿Qué son las Señales?
- **Señales**: Eventos que emiten los widgets cuando ocurre algo (click, cambio de texto, etc.)
- **Slots**: Funciones que se ejecutan cuando se recibe una señal
- **Conexión**: Enlace entre una señal y un slot

#### Tipos de Conexiones en el Código

**Conexión Directa:**
```python
self.boton1.clicked.connect(self.mostrarNombre)
```

**Flujo:**
1. Usuario hace clic en `boton1`
2. Se emite la señal `clicked`
3. Se ejecuta la función `mostrarNombre`

### Análisis de las Señales Usadas

#### Señal `clicked` para RadioButtons
```python
self.boton1.clicked.connect(self.mostrarNombre)
```
- **Ventaja**: Simple y directa
- **Desventaja**: Se ejecuta incluso si el RadioButton ya estaba seleccionado

#### Alternativa: Señal `toggled`
```python
# Versión mejorada con toggled
self.boton1.toggled.connect(self.mostrarNombre)
```

**Diferencia:**
- `clicked`: Solo cuando se hace clic físicamente
- `toggled`: Cuando cambia el estado (recibe parámetro True/False)

### Ejemplo Mejorado con Manejo de Estados

```python
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QRadioButton, 
                             QVBoxLayout, QHBoxLayout, QTextEdit, QLabel,
                             QButtonGroup)

class VentanaConRadioButton(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()

    def inicializarUI(self):
        self.setWindowTitle("Radio Buttons - Señales Avanzadas")
        self.setGeometry(100, 100, 500, 400)
        
        # Crear RadioButtons
        self.boton1 = QRadioButton("Mostrar Nombre")
        self.boton2 = QRadioButton("Mostrar Edad")
        self.boton3 = QRadioButton("Copiar Texto")
        self.boton4 = QRadioButton("Convertir a Mayúsculas")
        
        # Crear grupo de botones para gestión automática
        self.grupo_botones = QButtonGroup()
        self.grupo_botones.addButton(self.boton1, 1)
        self.grupo_botones.addButton(self.boton2, 2)
        self.grupo_botones.addButton(self.boton3, 3)
        self.grupo_botones.addButton(self.boton4, 4)
        
        # Áreas de texto
        self.panelParaEscribir = QTextEdit()
        self.panelParaEscribir.setPlaceholderText("Escribe algo aquí...")
        
        self.panelParaMostrar = QTextEdit()
        self.panelParaMostrar.setDisabled(True)
        self.panelParaMostrar.setPlaceholderText("Aquí se mostrará el resultado")
        
        # Etiqueta para mostrar el estado
        self.etiqueta_estado = QLabel("Estado: Ninguna opción seleccionada")
        
        # Layouts
        caja_botones = QHBoxLayout()
        caja_botones.addWidget(self.boton1)
        caja_botones.addWidget(self.boton2)
        caja_botones.addWidget(self.boton3)
        caja_botones.addWidget(self.boton4)
        
        caja_vertical = QVBoxLayout()
        caja_vertical.addLayout(caja_botones)
        caja_vertical.addWidget(QLabel("Área de entrada:"))
        caja_vertical.addWidget(self.panelParaEscribir)
        caja_vertical.addWidget(QLabel("Área de salida:"))
        caja_vertical.addWidget(self.panelParaMostrar)
        caja_vertical.addWidget(self.etiqueta_estado)
        
        self.setLayout(caja_vertical)
        
        # CONEXIONES DE SEÑALES MEJORADAS
        self.conectar_señales()

    def conectar_señales(self):
        # Usar toggled en lugar de clicked para mejor control
        self.boton1.toggled.connect(self.manejar_boton1)
        self.boton2.toggled.connect(self.manejar_boton2)
        self.boton3.toggled.connect(self.manejar_boton3)
        self.boton4.toggled.connect(self.manejar_boton4)
        
        # Señal cuando cambia el texto de entrada
        self.panelParaEscribir.textChanged.connect(self.actualizar_salida)

    def manejar_boton1(self, activado):
        if activado:
            self.panelParaMostrar.setPlainText("Daniel")
            self.etiqueta_estado.setText("Estado: Mostrando nombre")

    def manejar_boton2(self, activado):
        if activado:
            self.panelParaMostrar.setPlainText("22")
            self.etiqueta_estado.setText("Estado: Mostrando edad")

    def manejar_boton3(self, activado):
        if activado:
            self.actualizar_salida()
            self.etiqueta_estado.setText("Estado: Modo copia")

    def manejar_boton4(self, activado):
        if activado:
            texto_actual = self.panelParaMostrar.toPlainText()
            self.panelParaMostrar.setPlainText(texto_actual.upper())
            self.etiqueta_estado.setText("Estado: Modo mayúsculas")

    def actualizar_salida(self):
        # Actualizar solo si el botón de copia está activado
        if self.boton3.isChecked():
            texto = self.panelParaEscribir.toPlainText()
            self.panelParaMostrar.setPlainText(texto)
        
        # Si el botón de mayúsculas está activado, aplicar transformación
        if self.boton4.isChecked():
            texto = self.panelParaMostrar.toPlainText()
            self.panelParaMostrar.setPlainText(texto.upper())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaConRadioButton()
    sys.exit(app.exec())
```
![img_10.png](img_10.png)
## Tipos de Señales Comunes en PyQt6

### Señales de Botones
```python
# QPushButton / QRadioButton
.clicked.connect(funcion)      # Al hacer clic
.toggled.connect(funcion)      # Al cambiar estado (con parámetro)
.pressed.connect(funcion)      # Al presionar (sin soltar)
.released.connect(funcion)     # Al soltar
```

### Señales de Campos de Texto
```python
# QLineEdit / QTextEdit
.textChanged.connect(funcion)           # Cuando cambia el texto
.textEdited.connect(funcion)            # Cuando el usuario edita
.returnPressed.connect(funcion)         # Al presionar Enter
.selectionChanged.connect(funcion)      # Al cambiar selección
```

### Señales de Selectores
```python
# QComboBox
.currentIndexChanged.connect(funcion)    # Al cambiar índice
.currentTextChanged.connect(funcion)     # Al cambiar texto
.activated.connect(funcion)              # Al activar un item
```

## Mejores Prácticas con Señales

### 1. Usar `toggled` en lugar de `clicked` para RadioButtons
```python
# ❌ Menos óptimo
self.radio.toggled.connect(self.funcion)

# ✅ Mejor - recibe el estado como parámetro
self.radio.toggled.connect(self.funcion)

def funcion(self, activado):
    if activado:
        # Solo ejecutar cuando se activa
        print("Radio activado")
```

### 2. Verificar Estado con `isChecked()`
```python
def alguna_funcion(self):
    if self.boton1.isChecked():
        # Hacer algo solo si está seleccionado
        self.ejecutar_accion()
```

### 3. Agrupar RadioButtons Lógicamente
```python
from PyQt6.QtWidgets import QButtonGroup

# Crear grupo para gestión automática
self.grupo = QButtonGroup()
self.grupo.addButton(self.radio1)
self.grupo.addButton(self.radio2)
self.grupo.addButton(self.radio3)

# Conectar señal del grupo
self.grupo.buttonToggled.connect(self.radio_cambiado)
```

### 4. Manejar Múltiples Señales con Lambda
```python
# Para diferenciar qué botón emitió la señal
self.boton1.toggled.connect(lambda estado, btn=1: self.manejar_radio(btn, estado))
self.boton2.toggled.connect(lambda estado, btn=2: self.manejar_radio(btn, estado))

def manejar_radio(self, numero_boton, activado):
    if activado:
        print(f"Botón {numero_boton} activado")
```

## Ejemplo Avanzado: Sistema de Filtros con RadioButtons

```python
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QRadioButton, 
                             QVBoxLayout, QHBoxLayout, QTextEdit, QLabel,
                             QButtonGroup)

class FiltroTexto(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()

    def inicializarUI(self):
        self.setWindowTitle("Sistema de Filtros con RadioButtons")
        self.setGeometry(100, 100, 600, 500)
        
        # RadioButtons para diferentes filtros
        self.radio_sin_filtro = QRadioButton("Sin filtro")
        self.radio_mayusculas = QRadioButton("Mayúsculas")
        self.radio_minusculas = QRadioButton("Minúsculas")
        self.radio_invertir = QRadioButton("Invertir texto")
        self.radio_contar = QRadioButton("Contar palabras")
        
        # Grupo de botones
        self.grupo_filtros = QButtonGroup()
        self.grupo_filtros.addButton(self.radio_sin_filtro)
        self.grupo_filtros.addButton(self.radio_mayusculas)
        self.grupo_filtros.addButton(self.radio_minusculas)
        self.grupo_filtros.addButton(self.radio_invertir)
        self.grupo_filtros.addButton(self.radio_contar)
        
        # Seleccionar uno por defecto
        self.radio_sin_filtro.setChecked(True)
        
        # Áreas de texto
        self.entrada = QTextEdit()
        self.entrada.setPlaceholderText("Escribe el texto a filtrar...")
        self.salida = QTextEdit()
        self.salida.setReadOnly(True)
        
        # Etiqueta de información
        self.info = QLabel("Texto procesado: 0 caracteres")
        
        # Layout
        layout_botones = QHBoxLayout()
        layout_botones.addWidget(self.radio_sin_filtro)
        layout_botones.addWidget(self.radio_mayusculas)
        layout_botones.addWidget(self.radio_minusculas)
        layout_botones.addWidget(self.radio_invertir)
        layout_botones.addWidget(self.radio_contar)
        
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(QLabel("Selecciona un filtro:"))
        layout_principal.addLayout(layout_botones)
        layout_principal.addWidget(QLabel("Entrada:"))
        layout_principal.addWidget(self.entrada)
        layout_principal.addWidget(QLabel("Salida:"))
        layout_principal.addWidget(self.salida)
        layout_principal.addWidget(self.info)
        
        self.setLayout(layout_principal)
        
        # Conectar señales
        self.conectar_señales()

    def conectar_señales(self):
        # Conectar cambio de texto
        self.entrada.textChanged.connect(self.aplicar_filtro)
        
        # Conectar cambio de radio buttons
        self.radio_sin_filtro.toggled.connect(self.aplicar_filtro)
        self.radio_mayusculas.toggled.connect(self.aplicar_filtro)
        self.radio_minusculas.toggled.connect(self.aplicar_filtro)
        self.radio_invertir.toggled.connect(self.aplicar_filtro)
        self.radio_contar.toggled.connect(self.aplicar_filtro)

    def aplicar_filtro(self):
        texto = self.entrada.toPlainText()
        
        if self.radio_mayusculas.isChecked():
            resultado = texto.upper()
        elif self.radio_minusculas.isChecked():
            resultado = texto.lower()
        elif self.radio_invertir.isChecked():
            resultado = texto[::-1]  # Invertir texto
        elif self.radio_contar.isChecked():
            palabras = len(texto.split())
            resultado = f"Palabras: {palabras}, Caracteres: {len(texto)}"
        else:  # Sin filtro
            resultado = texto
        
        self.salida.setPlainText(resultado)
        self.info.setText(f"Texto procesado: {len(resultado)} caracteres")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = FiltroTexto()
    sys.exit(app.exec())
```
![img_12.png](img_12.png)
## Resumen de Conceptos Clave

1. **RadioButtons**: Para selección única entre opciones mutuamente excluyentes
2. **Señales**: Mecanismo de comunicación entre widgets y funciones
3. **clicked vs toggled**: Usar `toggled` cuando necesitas saber el estado
4. **Grupos de botones**: Para gestionar RadioButtons relacionados
5. **Múltiples señales**: Pueden conectarse a una misma función

# Guía de PyQt6 - Trabajando con QButtonGroup

## 26. Grupos de Botones - QButtonGroup

### Código Base - Grupos de Botones
```python
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QRadioButton,
                             QVBoxLayout, QHBoxLayout, QTextEdit, QLabel,
                             QButtonGroup)

class trabajandoConGrupos(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()

    def inicializarUI(self):
        self.boton1 = QRadioButton("Libre")
        self.boton2 = QRadioButton("Agrupado1")
        self.boton3 = QRadioButton("Agrupado2")
        self.boton4 = QRadioButton("Agrupado3")

        # QButtonGroup es solo un contenedor lógico (no es un QLayout).
        # Se usa para gestionar exclusividad/señales, no para añadir al layout.
        self.grupo = QButtonGroup()
        self.grupo.addButton(self.boton2)
        self.grupo.addButton(self.boton3)
        self.grupo.addButton(self.boton4)

        self.cajaHorizontal = QHBoxLayout()

        # Crear un QLayout real para los botones del grupo y añadir los widgets.
        self.grupoLayout = QVBoxLayout()  # layout físico para los radio buttons agrupados
        self.grupoLayout.addWidget(self.boton2)
        self.grupoLayout.addWidget(self.boton3)
        self.grupoLayout.addWidget(self.boton4)

        # Añadir el layout del grupo al layout horizontal
        self.cajaHorizontal.addLayout(self.grupoLayout)

        # Añadir el botón independiente como widget
        self.cajaHorizontal.addWidget(self.boton1)

        self.setLayout(self.cajaHorizontal)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = trabajandoConGrupos()
    sys.exit(app.exec())
```

## Explicación Detallada de QButtonGroup

### ¿Qué es QButtonGroup?

**QButtonGroup** es un contenedor lógico (no visual) que agrupa botones para:
- Gestionar la exclusividad mutua automáticamente
- Manejar señales de forma colectiva
- Identificar botones con IDs únicos

### Diferencias Clave

| Característica | Layout Visual | QButtonGroup |
|----------------|---------------|--------------|
| **Propósito** | Organizar widgets visualmente | Gestionar lógica de botones |
| **Se ve en pantalla** | Sí | No |
| **Exclusividad** | No la proporciona | Sí, automáticamente |
| **Señales** | No emite señales | Señales grupales |

### Creación y Configuración de Grupos

#### Crear el Grupo
```python
self.grupo = QButtonGroup()
```

#### Agregar Botones al Grupo
```python
self.grupo.addButton(self.boton2)
self.grupo.addButton(self.boton3)
self.grupo.addButton(self.boton4)
```

#### Agregar con IDs Personalizados
```python
self.grupo.addButton(self.boton2, 1)  # ID = 1
self.grupo.addButton(self.boton3, 2)  # ID = 2  
self.grupo.addButton(self.boton4, 3)  # ID = 3
```

### Ejemplo Completo con Funcionalidad

```python
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QRadioButton,
                             QVBoxLayout, QHBoxLayout, QTextEdit, QLabel,
                             QButtonGroup, QGroupBox)

class trabajandoConGrupos(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()

    def inicializarUI(self):
        self.setWindowTitle("QButtonGroup - Grupos de Botones")
        self.setGeometry(100, 100, 500, 300)
        
        # Crear botones
        self.boton_libre = QRadioButton("Botón Libre (fuera de grupo)")
        self.boton_grupo1 = QRadioButton("Agrupado - Opción 1")
        self.boton_grupo2 = QRadioButton("Agrupado - Opción 2") 
        self.boton_grupo3 = QRadioButton("Agrupado - Opción 3")
        
        # CREAR GRUPO LÓGICO
        self.grupo_principal = QButtonGroup()
        
        # Agregar botones al grupo con IDs
        self.grupo_principal.addButton(self.boton_grupo1, 1)
        self.grupo_principal.addButton(self.boton_grupo2, 2)
        self.grupo_principal.addButton(self.boton_grupo3, 3)
        
        # ORGANIZACIÓN VISUAL
        # Grupo para botones agrupados (visual)
        grupo_visual = QGroupBox("Botones Agrupados (QButtonGroup)")
        layout_grupo = QVBoxLayout()
        layout_grupo.addWidget(self.boton_grupo1)
        layout_grupo.addWidget(self.boton_grupo2)
        layout_grupo.addWidget(self.boton_grupo3)
        grupo_visual.setLayout(layout_grupo)
        
        # Grupo para botón libre (visual)
        grupo_libre = QGroupBox("Botón Libre")
        layout_libre = QVBoxLayout()
        layout_libre.addWidget(self.boton_libre)
        grupo_libre.setLayout(layout_libre)
        
        # Área de información
        self.etiqueta_info = QLabel("Selecciona diferentes botones para ver el comportamiento")
        self.etiqueta_info.setStyleSheet("background-color: #f0f0f0; padding: 10px;")
        
        # Layout principal
        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(grupo_visual)
        layout_horizontal.addWidget(grupo_libre)
        
        layout_principal = QVBoxLayout()
        layout_principal.addLayout(layout_horizontal)
        layout_principal.addWidget(self.etiqueta_info)
        
        self.setLayout(layout_principal)
        
        # CONECTAR SEÑALES
        self.conectar_señales()

    def conectar_señales(self):
        # Señales de botones individuales
        self.boton_libre.toggled.connect(self.boton_libre_cambiado)
        
        # Señales del grupo
        self.grupo_principal.buttonToggled.connect(self.grupo_cambiado)
        self.grupo_principal.idClicked.connect(self.grupo_clicado)

    def boton_libre_cambiado(self, estado):
        if estado:
            self.etiqueta_info.setText("✅ Botón LIBRE seleccionado - No afecta a los agrupados")
        else:
            self.etiqueta_info.setText("🔘 Botón LIBRE deseleccionado")

    def grupo_cambiado(self, boton, estado):
        if estado:
            id_boton = self.grupo_principal.id(boton)
            texto_boton = boton.text()
            self.etiqueta_info.setText(f"✅ Grupo: Botón {id_boton} ({texto_boton}) seleccionado")

    def grupo_clicado(self, id_boton):
        self.etiqueta_info.setText(f"🖱️ Grupo: Clic en botón con ID {id_boton}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = trabajandoConGrupos()
    sys.exit(app.exec())
```

## Métodos y Señales de QButtonGroup

### Métodos Principales

#### Agregar y Remover Botones
```python
# Agregar botón
grupo.addButton(boton)
grupo.addButton(boton, id)  # Con ID específico

# Remover botón
grupo.removeButton(boton)

# Obtener botón por ID
boton = grupo.button(id)

# Obtener ID de un botón
id = grupo.id(boton)
```

#### Gestión de Exclusividad
```python
# Verificar exclusividad
es_exclusivo = grupo.exclusive()

# Cambiar exclusividad
grupo.setExclusive(True)  # Solo uno seleccionado a la vez
grupo.setExclusive(False) # Múltiples selecciones permitidas
```

#### Obtener Botones
```python
# Todos los botones del grupo
botones = grupo.buttons()

# Botón seleccionado
boton_seleccionado = grupo.checkedButton()

# ID del botón seleccionado
id_seleccionado = grupo.checkedId()
```

### Señales de QButtonGroup

#### buttonClicked
```python
# Se emite cuando se hace clic en cualquier botón del grupo
grupo.buttonClicked.connect(self.funcion)

# Con parámetro del botón
def funcion(self, boton):
    print(f"Botón clicado: {boton.text()}")
```

#### buttonClicked con ID
```python
# Se emite con el ID del botón
grupo.idClicked.connect(self.funcion_con_id)

def funcion_con_id(self, id_boton):
    print(f"Botón con ID {id_boton} fue clicado")
```

#### buttonToggled
```python
# Se emite cuando cambia el estado de cualquier botón
grupo.buttonToggled.connect(self.funcion_toggle)

def funcion_toggle(self, boton, estado):
    if estado:
        print(f"Botón {boton.text()} ACTIVADO")
    else:
        print(f"Botón {boton.text()} DESACTIVADO")
```

#### idToggled
```python
# Se emite con ID cuando cambia el estado
grupo.idToggled.connect(self.funcion_id_toggle)

def funcion_id_toggle(self, id_boton, estado):
    if estado:
        print(f"Botón ID {id_boton} ACTIVADO")
```

## Ejemplos Avanzados con Múltiples Grupos

### Ejemplo: Sistema de Configuración con Múltiples Grupos

```python
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QRadioButton,
                             QVBoxLayout, QHBoxLayout, QLabel,
                             QButtonGroup, QGroupBox, QPushButton)

class SistemaConfiguracion(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()

    def inicializarUI(self):
        self.setWindowTitle("Sistema de Configuración - Múltiples Grupos")
        self.setGeometry(100, 100, 600, 400)
        
        # CREAR MÚLTIPLES GRUPOS
        self.crear_grupo_tema()
        self.crear_grupo_idioma()
        self.crear_grupo_privacidad()
        
        # Botón de aplicación
        self.boton_aplicar = QPushButton("Aplicar Configuración")
        self.boton_aplicar.clicked.connect(self.aplicar_configuracion)
        
        # Área de resultados
        self.etiqueta_resultado = QLabel("Configuración actual: Sin cambios")
        self.etiqueta_resultado.setStyleSheet("background-color: #e8f4f8; padding: 15px; border: 1px solid #bee5eb;")
        
        # Layout principal
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.grupo_tema)
        layout_principal.addWidget(self.grupo_idioma)
        layout_principal.addWidget(self.grupo_privacidad)
        layout_principal.addWidget(self.boton_aplicar)
        layout_principal.addWidget(self.etiqueta_resultado)
        
        self.setLayout(layout_principal)

    def crear_grupo_tema(self):
        # Grupo para selección de tema
        self.tema_claro = QRadioButton("Tema Claro")
        self.tema_oscuro = QRadioButton("Tema Oscuro")
        self.tema_auto = QRadioButton("Tema Automático")
        
        self.grupo_tema_logico = QButtonGroup()
        self.grupo_tema_logico.addButton(self.tema_claro, 1)
        self.grupo_tema_logico.addButton(self.tema_oscuro, 2)
        self.grupo_tema_logico.addButton(self.tema_auto, 3)
        
        # Seleccionar por defecto
        self.tema_claro.setChecked(True)
        
        # Grupo visual
        self.grupo_tema = QGroupBox("Selección de Tema")
        layout_tema = QVBoxLayout()
        layout_tema.addWidget(self.tema_claro)
        layout_tema.addWidget(self.tema_oscuro)
        layout_tema.addWidget(self.tema_auto)
        self.grupo_tema.setLayout(layout_tema)
        
        # Conectar señales
        self.grupo_tema_logico.buttonToggled.connect(self.tema_cambiado)

    def crear_grupo_idioma(self):
        # Grupo para selección de idioma
        self.idioma_es = QRadioButton("Español")
        self.idioma_en = QRadioButton("English")
        self.idioma_fr = QRadioButton("Français")
        
        self.grupo_idioma_logico = QButtonGroup()
        self.grupo_idioma_logico.addButton(self.idioma_es, 1)
        self.grupo_idioma_logico.addButton(self.idioma_en, 2)
        self.grupo_idioma_logico.addButton(self.idioma_fr, 3)
        
        # Seleccionar por defecto
        self.idioma_es.setChecked(True)
        
        # Grupo visual
        self.grupo_idioma = QGroupBox("Selección de Idioma")
        layout_idioma = QVBoxLayout()
        layout_idioma.addWidget(self.idioma_es)
        layout_idioma.addWidget(self.idioma_en)
        layout_idioma.addWidget(self.idioma_fr)
        self.grupo_idioma.setLayout(layout_idioma)

    def crear_grupo_privacidad(self):
        # Grupo para configuración de privacidad
        self.privacidad_alta = QRadioButton("Privacidad Alta")
        self.privacidad_media = QRadioButton("Privacidad Media")
        self.privacidad_baja = QRadioButton("Privacidad Baja")
        
        self.grupo_privacidad_logico = QButtonGroup()
        self.grupo_privacidad_logico.addButton(self.privacidad_alta, 1)
        self.grupo_privacidad_logico.addButton(self.privacidad_media, 2)
        self.grupo_privacidad_logico.addButton(self.privacidad_baja, 3)
        
        # Seleccionar por defecto
        self.privacidad_media.setChecked(True)
        
        # Grupo visual
        self.grupo_privacidad = QGroupBox("Configuración de Privacidad")
        layout_privacidad = QVBoxLayout()
        layout_privacidad.addWidget(self.privacidad_alta)
        layout_privacidad.addWidget(self.privacidad_media)
        layout_privacidad.addWidget(self.privacidad_baja)
        self.grupo_privacidad.setLayout(layout_privacidad)

    def tema_cambiado(self, boton, estado):
        if estado:
            self.etiqueta_resultado.setText(f"Tema cambiado a: {boton.text()}")

    def aplicar_configuracion(self):
        # Obtener configuración actual
        tema = self.grupo_tema_logico.checkedButton().text()
        idioma = self.grupo_idioma_logico.checkedButton().text()
        privacidad = self.grupo_privacidad_logico.checkedButton().text()
        
        mensaje = f"""
        ✅ Configuración aplicada:
        • Tema: {tema}
        • Idioma: {idioma}
        • Privacidad: {privacidad}
        """
        
        self.etiqueta_resultado.setText(mensaje)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = SistemaConfiguracion()
    sys.exit(app.exec())
```
![img_13.png](img_13.png)
## Ventajas de Usar QButtonGroup

### 1. **Gestión Automática de Exclusividad**
```python
# Sin QButtonGroup - gestión manual
def boton1_pulsado(self):
    self.boton2.setChecked(False)
    self.boton3.setChecked(False)

# Con QButtonGroup - automático
grupo = QButtonGroup()
grupo.addButton(boton1)
grupo.addButton(boton2)
grupo.addButton(boton3)
```

### 2. **Identificación Fácil de Botones**
```python
# Con IDs
id_seleccionado = grupo.checkedId()
boton_seleccionado = grupo.button(id_seleccionado)
```

### 3. **Señales Colectivas**
```python
# Una señal para todos los botones del grupo
grupo.buttonToggled.connect(self.cualquier_boton_cambiado)
```

### 4. **Código Más Limpio y Mantenible**
```python
# En lugar de conectar cada botón individualmente
self.boton1.toggled.connect(...)
self.boton2.toggled.connect(...)
self.boton3.toggled.connect(...)

# Una sola conexión para el grupo
grupo.buttonToggled.connect(...)
```

## Casos de Uso Típicos para QButtonGroup

1. **Sistemas de configuración**: Tema, idioma, preferencias
2. **Formularios de opciones**: Selección única entre alternativas
3. **Sistemas de filtros**: Filtrado por categorías
4. **Interfaces de modo**: Modo edición, visualización, administración
5. **Selección de categorías**: Categorías mutuamente excluyentes

# Guía de PyQt6 - Model-View y Listas

## 27. QListView y QStandardItemModel

### Código Base - Listas con Model-View
```python
import sys
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import (QApplication, QWidget, QRadioButton,
                             QVBoxLayout, QHBoxLayout, QTextEdit, QLabel,
                             QButtonGroup, QPushButton, QListView)

class VentanaConListas(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()

    def inicializarUI(self):
        self.labelParaAñadirALista()
        self.lista()

        self.cajaVertical = QVBoxLayout()
        self.cajaVertical.addLayout(self.cajaHorizontal)
        self.cajaVertical.addWidget(self.lista1)

        self.setLayout(self.cajaVertical)

    def lista(self):
        self.model = QStandardItemModel()
        self.lista1 = QListView()

    def anadirElemento(self):
        text = self.label.toPlainText().strip()
        if not text:
            return
        self.itemPrueba = QStandardItem(text)
        self.model.appendRow(self.itemPrueba)
        self.lista1.setModel(self.model)

    def borrarUltimoElemento(self):
        if not hasattr(self, "model") or self.model is None:
            return
        count = self.model.rowCount()
        if count > 0:
            self.model.removeRow(count - 1)

    def labelParaAñadirALista(self):
        self.label = QTextEdit()
        self.botonAñadir = QPushButton("añadir")
        self.botonBorrar = QPushButton("borrar")
        self.cajaHorizontal = QHBoxLayout()
        self.cajaHorizontal.addWidget(self.label)
        self.cajaHorizontal.addWidget(self.botonAñadir)
        self.cajaHorizontal.addWidget(self.botonBorrar)

        self.botonBorrar.clicked.connect(self.borrarUltimoElemento)
        self.botonAñadir.clicked.connect(self.anadirElemento)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaConListas()
    sys.exit(app.exec())
```

## Explicación Detallada del Patrón Model-View

### ¿Qué es el Patrón Model-View?

**Model-View** es un patrón de diseño que separa:
- **Modelo (Model)**: Los datos y la lógica de negocio
- **Vista (View)**: La presentación visual de los datos
- **Controlador (Controller)**: Maneja la interacción del usuario

En PyQt6, el delegado actúa como controlador.

### Componentes en el Código

#### QStandardItemModel - El Modelo
```python
self.model = QStandardItemModel()
```
- **Función**: Almacena y gestiona los datos
- **Características**:
  - Puede contener texto, iconos, checkboxes
  - Maneja datos jerárquicos (listas, árboles)
  - Notifica a la vista cuando los datos cambian

#### QListView - La Vista
```python
self.lista1 = QListView()
```
- **Función**: Muestra los datos del modelo
- **Características**:
  - Presenta los datos en forma de lista
  - Permite selección, edición, etc.
  - Se actualiza automáticamente cuando el modelo cambia

#### Conexión Modelo-Vista
```python
self.lista1.setModel(self.model)
```
- **Propósito**: Conecta la vista con el modelo
- **Comportamiento**: La vista se actualiza automáticamente cuando el modelo cambia

### QStandardItem - Elementos del Modelo

#### Crear un Item
```python
self.itemPrueba = QStandardItem(text)
```
- **QStandardItem**: Representa un elemento en el modelo
- **Puede contener**: Texto, icono, tooltip, estado de checkbox, etc.

#### Propiedades de QStandardItem
```python
item = QStandardItem("Texto del elemento")

# Configurar propiedades
item.setToolTip("Tooltip del elemento")
item.setCheckable(True)  # Hacer que tenga checkbox
item.setEditable(False)  # No permitir edición
```

## Código Mejorado y Comentado

```python
import sys
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QHBoxLayout, QTextEdit, QPushButton, 
                             QListView, QLabel, QGroupBox)

class VentanaConListas(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()

    def inicializarUI(self):
        self.setWindowTitle("Lista con Model-View")
        self.setGeometry(100, 100, 500, 400)
        
        # Inicializar componentes
        self.crear_area_entrada()
        self.crear_lista()
        self.crear_controles_avanzados()
        
        # Layout principal
        layout_principal = QVBoxLayout()
        
        # Grupo para área de entrada
        grupo_entrada = QGroupBox("Añadir Elementos a la Lista")
        grupo_entrada.setLayout(self.cajaHorizontal)
        layout_principal.addWidget(grupo_entrada)
        
        # Grupo para lista
        grupo_lista = QGroupBox("Lista de Elementos")
        layout_lista = QVBoxLayout()
        layout_lista.addWidget(self.lista1)
        grupo_lista.setLayout(layout_lista)
        layout_principal.addWidget(grupo_lista)
        
        # Controles avanzados
        layout_principal.addWidget(self.grupo_controles)
        
        self.setLayout(layout_principal)

    def crear_area_entrada(self):
        """Crea el área para añadir nuevos elementos"""
        self.label = QTextEdit()
        self.label.setMaximumHeight(60)  # Limitar altura
        self.label.setPlaceholderText("Escribe el texto del nuevo elemento...")
        
        self.botonAñadir = QPushButton("Añadir")
        self.botonBorrar = QPushButton("Borrar Último")
        self.botonLimpiar = QPushButton("Limpiar Todo")
        
        self.cajaHorizontal = QHBoxLayout()
        self.cajaHorizontal.addWidget(self.label)
        self.cajaHorizontal.addWidget(self.botonAñadir)
        self.cajaHorizontal.addWidget(self.botonBorrar)
        self.cajaHorizontal.addWidget(self.botonLimpiar)
        
        # Conectar señales
        self.botonAñadir.clicked.connect(self.anadirElemento)
        self.botonBorrar.clicked.connect(self.borrarUltimoElemento)
        self.botonLimpiar.clicked.connect(self.limpiarLista)

    def crear_lista(self):
        """Inicializa el modelo y la vista de lista"""
        # Crear el modelo
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Elementos de la Lista"])  # Encabezado
        
        # Crear la vista
        self.lista1 = QListView()
        self.lista1.setModel(self.model)  # Conectar modelo con vista
        
        # Añadir algunos elementos de ejemplo
        elementos_ejemplo = ["Elemento de ejemplo 1", "Elemento de ejemplo 2"]
        for elemento in elementos_ejemplo:
            item = QStandardItem(elemento)
            self.model.appendRow(item)

    def crear_controles_avanzados(self):
        """Crea controles adicionales para gestionar la lista"""
        self.grupo_controles = QGroupBox("Controles de la Lista")
        layout_controles = QHBoxLayout()
        
        # Botones adicionales
        self.botonBorrarSeleccionado = QPushButton("Borrar Seleccionado")
        self.botonEditar = QPushButton("Editar Seleccionado")
        self.botonContar = QPushButton("Contar Elementos")
        
        # Etiqueta para información
        self.etiqueta_info = QLabel("Elementos: 2")
        
        layout_controles.addWidget(self.botonBorrarSeleccionado)
        layout_controles.addWidget(self.botonEditar)
        layout_controles.addWidget(self.botonContar)
        layout_controles.addWidget(self.etiqueta_info)
        
        self.grupo_controles.setLayout(layout_controles)
        
        # Conectar señales
        self.botonBorrarSeleccionado.clicked.connect(self.borrarSeleccionado)
        self.botonEditar.clicked.connect(self.editarSeleccionado)
        self.botonContar.clicked.connect(self.actualizarContador)
        
        # Conectar señal de selección cambiada
        self.lista1.selectionModel().selectionChanged.connect(self.seleccionCambiada)

    def anadirElemento(self):
        """Añade un nuevo elemento a la lista"""
        text = self.label.toPlainText().strip()
        if not text:
            return
        
        # Crear y configurar el item
        item = QStandardItem(text)
        item.setToolTip(f"Elemento añadido: {text}")
        
        # Añadir al modelo
        self.model.appendRow(item)
        
        # Limpiar el área de texto
        self.label.clear()
        
        # Actualizar contador
        self.actualizarContador()
        
        # Seleccionar el nuevo elemento
        index = self.model.index(self.model.rowCount() - 1, 0)
        self.lista1.setCurrentIndex(index)

    def borrarUltimoElemento(self):
        """Elimina el último elemento de la lista"""
        if self.model.rowCount() > 0:
            self.model.removeRow(self.model.rowCount() - 1)
            self.actualizarContador()

    def borrarSeleccionado(self):
        """Elimina el elemento seleccionado"""
        index = self.lista1.currentIndex()
        if index.isValid():
            self.model.removeRow(index.row())
            self.actualizarContador()

    def editarSeleccionado(self):
        """Permite editar el elemento seleccionado"""
        index = self.lista1.currentIndex()
        if index.isValid():
            # Activar edición en la vista
            self.lista1.edit(index)

    def limpiarLista(self):
        """Elimina todos los elementos de la lista"""
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["Elementos de la Lista"])
        self.actualizarContador()

    def seleccionCambiada(self):
        """Maneja el cambio de selección en la lista"""
        index = self.lista1.currentIndex()
        if index.isValid():
            elemento = self.model.itemFromIndex(index).text()
            self.etiqueta_info.setText(f"Seleccionado: {elemento}")

    def actualizarContador(self):
        """Actualiza el contador de elementos"""
        count = self.model.rowCount()
        self.etiqueta_info.setText(f"Elementos: {count}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaConListas()
    sys.exit(app.exec())
```

## Métodos y Propiedades del Modelo

### Métodos de QStandardItemModel

#### Gestión de Datos
```python
# Añadir elementos
model.appendRow(item)              # Añadir un item
model.appendRow([item1, item2])    # Añadir múltiples items en una fila

# Insertar elementos
model.insertRow(posicion, item)

# Eliminar elementos
model.removeRow(fila)              # Eliminar por fila
model.removeRows(fila, cantidad)   # Eliminar múltiples filas
model.clear()                      # Eliminar todo

# Obtener elementos
item = model.item(fila, columna)   # Obtener item específico
texto = model.data(index)          # Obtener datos de un índice
```

#### Información del Modelo
```python
# Información básica
filas = model.rowCount()           # Número de filas
columnas = model.columnCount()     # Número de columnas

# Búsqueda
indices = model.match(...)         # Buscar elementos

# Encabezados
model.setHorizontalHeaderLabels(["Col1", "Col2"])  # Encabezados horizontales
```

### Métodos de QListView

#### Selección
```python
# Obtener selección
index = lista.currentIndex()               # Índice actual
indices = lista.selectedIndexes()          # Todos los índices seleccionados

# Configurar selección
lista.setCurrentIndex(index)               # Seleccionar específico
lista.clearSelection()                     # Limpiar selección

# Modos de selección
lista.setSelectionMode(QListView.SingleSelection)     # Selección simple
lista.setSelectionMode(QListView.MultiSelection)      # Selección múltiple
```

#### Visualización
```python
# Modos de vista
lista.setViewMode(QListView.ListMode)      # Vista de lista
lista.setViewMode(QListView.IconMode)      # Vista de iconos

# Edición
lista.setEditTriggers(QListView.DoubleClicked)    # Editar al hacer doble clic
lista.setEditTriggers(QListView.NoEditTriggers)   # No permitir edición
```
