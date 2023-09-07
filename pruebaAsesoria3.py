import PySimpleGUI as sg
import webbrowser
import csv

sg.theme("DarkGrey2")

# Función para crear la ventana de ingreso de datos de usuario
def crearVentanaDatosUsuario():
    
    layout = [
        [sg.Text("Datos de Usuario", font=("Helvetica", 16))], #Titulo de la ventana
        [sg.Text("Nombre:"), sg.InputText(key="nombre")], #Input de nombre
        [sg.Text("Edad:"), sg.InputText(key="edad")], #Input de edad
        [sg.Text("Correo:"), sg.InputText(key="correo")], #Input de correo
        [sg.Text("Motivo de consulta:"), sg.Radio("Informativo Personal", "motivo", key="personal"), sg.Radio("Informativo Ejecutivo", "motivo", key="ejecutivo")],#Boton de radio de la etiqueda motivo con valores de personal o ejecutivo 
        [sg.Text("Sexo:"), sg.Radio("Masculino", "sexo", key="masculino"), sg.Radio("Femenino", "sexo", key="femenino")], #Boton de radio de la etiqueta de sexo con valores de masculino y femenino
        [sg.Button("Guardar"), sg.Button("Cerrar")] #Eventos de los botones Guardar y cerrar
    ]
    ventana = sg.Window("Datos de Usuario", layout) #Se asigna el layout a la variable ventana
    return ventana #Regresa la ventana

# Función para ejecutar la ventana de ingreso de datos de usuario
def ejecutarVentanaDatosUsuario(ventana): #Parametro que corresponde a la ventana de datos de usuario
    while True: #Ciclo que se acaba cuando se cierra la ventana o se da click en cerrar
        evento, valores = ventana.read() #Lee los valores del parametro

        if evento == sg.WIN_CLOSED or evento == "Cerrar": #Si la condicion se cumple se sale del ciclo
            break

        if evento == "Guardar": #Si la condicion se cumple se guardan los valores del usuario en variables
            nombre = valores['nombre']
            edad = valores['edad']
            correo = valores['correo']
            motivo = "Informativo Personal" if valores['personal'] else "Informativo Ejecutivo" #Se asigna en la variable motivo, informacion personal si la etiqueta de la ventana tiene la clave de personal, cualquier otra cosa se asigna informativo ejecutivo
            sexo = "Masculino" if valores['masculino'] else "Femenino" #Se asigna en la variable sexo, el valor de masculino si la etiqueta de sexo en la ventana tiene la clave de masculino, cualquiero otra cosa asigna el valor de femenino
            
            datos = [nombre, edad, correo, motivo, sexo] #Se insertan los datos previamente guardados en una lista
            guardarCsv(datos) #Se llama a la funcion que guarda en excel los datos
            sg.popup("Datos guardados exitosamente.") #Alerta de exito

    ventana.close()

# Función para guardar datos en un archivo CSV
def guardarCsv(datos):
    with open('usuarios.csv', mode='a', newline='') as archivoCsv: #Se abre o crea el archivo csv "usuarios" para ingresar los datos
        escritor = csv.writer(archivoCsv)  #Se declara que se va a escribir en el archivo
        escritor.writerow(datos) #Se escribe un registro en el archivo

# Función para crear la ventana principal
def crearVentanaPrincipal():
    layout = [
        [sg.Button("Locación")], #Boton de locacion
        [sg.Button("Tipo de Servicio")], #Boton de servicio
        [sg.Button("Contenido Multimedia")], #Boton de  Multimedia
        [sg.Button("Salir")] #Boton para salir
    ]
    ventana = sg.Window("Interfaz Principal", layout, finalize=True) #Se asigna el layout a la variable ventana
    return ventana #regresa la ventana

# Función para ejecutar la ventana principal
def ejecutarVentanaPrincipal(ventana):
    while True: #Ciclo que acaba cuando se cierra la ventana o se da click en salir
        evento, _ = ventana.read()

        if evento == sg.WIN_CLOSED or evento == "Salir":
            break

        if evento == "Locación": #Aqui te manda al mapa
            webbrowser.open("https://www.google.com/maps/d/u/0/edit?mid=1QX9SOXj7I3IMNc7JVKpkBiM7jhgEofA&ll=22.015771344003028%2C-102.29320524999999&z=10")
        elif evento == "Tipo de Servicio": #Aqui te manda a una base de datos de excel
            webbrowser.open("https://docs.google.com/spreadsheets/d/1Y5YkTOIySihunjce5uqGuu9buEbTHkusGit3ItCaTXQ/edit#gid=0")
        elif evento == "Contenido Multimedia": #Pagina con informacion y video
            webbrowser.open("https://www.bancomundial.org/es/topic/education/overview")

    ventana.close()

# Función para crear la ventana de inicio de sesión
def crearVentanaInicioSesion():
    layout = [
        [sg.Text("Iniciar sesión", font=("Helvetica", 16))], #Titulo de la ventana
        [sg.Text("Usuario:"), sg.InputText(key="usuario")], #Usuario para loggin
        [sg.Text("Contraseña:"), sg.InputText(key="contrasena", password_char="*")], #Contraseña  para loggin
        [sg.Button("Iniciar sesión")] #Boton del evento Iniciar Sesion
    ]
    ventana = sg.Window("Iniciar sesión", layout) #Se asiga el layour en la ventana
    return ventana #Regresa la ventana

if __name__ == "__main__":
    
    ventanaInicioSesion = crearVentanaInicioSesion()#Llama a la funcion que cre la ventana de login

    while True: #Itera hastsa que se cierre la ventana
        evento, valores = ventanaInicioSesion.read() #Se asignan variables correspondientes a los eventos y valores de la ventana inicio de sesion

        if evento == sg.WIN_CLOSED: 
            break

        if evento == "Iniciar sesión": #Una vez que inicia sesion se corre este codigo
            usuario = valores["usuario"] #Se asigna a la variable usuario el valor de la etiqueta usuario de la ventana de loggin
            contraseña = valores["contrasena"]#Se asigna a la variable contraseña el valor de la etiqueta contraseña de la ventana de loggin
            if usuario == "tec2023" and contraseña == "tec2023": #Valida que el usuario y la contraseña sean "tec2023" 
                ventanaInicioSesion.close() #Se cierra la ventana de inicio de sesion

                ventanaDatosUsuario = crearVentanaDatosUsuario() #Se asignan variables correspondientes a los eventos y valores de la ventana de datos del usuario
                ejecutarVentanaDatosUsuario(ventanaDatosUsuario) #Se llama a la funcion que guarda los valores del registro de usuario y posteriormente lo guarda en excel

                ventanaPrincipal = crearVentanaPrincipal() #Se asignan variables correspondientes a los eventos y valores de la ventana de los sitios web
                ejecutarVentanaPrincipal(ventanaPrincipal) #Se llama a la funcion que redirije a los sitios web segun el boton 

                break
            else:
                sg.popup_error("Credenciales incorrectas. Inténtalo de nuevo.") #Alerta en caso de ingresar datos incorrectos
                break
