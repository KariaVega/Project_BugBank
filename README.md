# Proyecto_Bug_Bank :bug:
![image](https://github.com/user-attachments/assets/f0e56aaa-b0a1-43fc-a418-c07ac9c461a1)

### :page_facing_up: *Documentación utilizada:* 
- Dirección del servidor: [Link de aplicacion](https://bugbank.netlify.app/)
- Requisitos: [Link de requerimientos](https://bugbank.netlify.app/requirements)
  
### 🛠️ *Lenguajes y herramientas utilizadas:*
<div id="header" align="left">
    
- DOM: Jerarquía de los elementos
- DevTools: Generar buscadores.
- Python: Codigo para las pruebas.
- Pycharm: Ejecución de las pruebas.
- GitBash: Clonación del repositorio.
- GitHub: Respaldo del codigo.
- Selenium: Webdriver controlador del navegador
- Pytest
- Pip

<img decoding="async" src="https://img.shields.io/badge/DOM-purple?style=for-the-badge&logo=Drawio&logoColor=white" alt="Drawio"/>
<img decoding="async" src="https://img.shields.io/badge/DevTools-D80B01?style=for-the-badge&logo=Drawio&logoColor=white" alt="Drawio"/>
<img decoding="async" src="https://img.shields.io/badge/Python-0052CC?style=for-the-badge&logo=python&logoColor=white" alt="python"/>
<img decoding="async" src="https://img.shields.io/badge/PyCharm-808000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white" alt="PyCharm"/>
<img decoding="async" src="https://img.shields.io/badge/Git_Bash-D89B01?&style=for-the-badge&logo=GitBash&logoColor=white" alt="GitBash"/>
<img decoding="async" src="https://img.shields.io/badge/GitHub-000000.svg?&style=for-the-badge&logo=GitHub&logoColor=white" alt="GitHub"/>
<img decoding="async" src="https://img.shields.io/badge/Selenium-008000?style=for-the-badge&logo=Selenium&logoColor=white" alt="Selenium"/>
<img decoding="async" src="https://img.shields.io/badge/Pytest-0052CC?style=for-the-badge&logo=pytest&logoColor=white" alt="pytest"/>
<img decoding="async" src="https://img.shields.io/badge/Pip-D80B01?style=for-the-badge&logo=Pip&logoColor=white" alt="Pip"/>


### :fireworks: *Descripción del Aplicativo BugBank*
- Bug Banks es una aplicación de banca financiera que permite realizar transferencias, retiros, pagos y beneficios, estos dos últimos en desarrollo. La interfaz es bastante sencilla, contiene dos pantallas principales, la de inicio y el del formulario de registro. El formulario de acceso consta de 2 campos obligatorios que permite el acceso a los usuarios y registros válidos, no se autoriza el acceso a usuarios no válidos o no registrados. Para el formulario de registro, se permiten aquellos registros validos dentro de los parametros y rangos establecidos y al registrarse una cuenta exitosamente debe mostrarse creada número de cuenta y son dirigidos a la página de inicio. La pantalla de servicios disponibles cuenta con las opciones de: trnasferis, pagos, extrato y beneficio, como se menciono anteriormente, boton de salir, información de la cuenta y saldo.
- Se realizará la automatización de las pruebas del llenado del formulario de registro y de acceso para el servicion de banca.

### :page_facing_up: *Lista de Comprobación de Pruebas:*  

1. Selección de boton de Registrar.
2. Rellenar campo email del formulario de registro.
3. Rellenar campo name del formulario de registro.
4. Rellenar campo password del formulario de registro.
5. Rellenar campo de confirmación de password del formulario de registro.
6. Selección de botonde Cadastar del formulario de registro.
7. Ventana emergente de confirmación, aceptar.
8. Ingresar email en pagina de inicio.
9. Ingresar password en página de inicio.
10. Hacer clic en botón accesar.

### :file_folder: *Archivos:* 
1. Data.py (Datos)
2. Main.py (métodos de la clase)
3. Test_cases_BugBank (funciones de casos de prueba)
4. README (Descripcion del contenido)

### :paw_prints: *Pasos a seguir para la ejecución de las pruebas con metodología POM:* 
- Conexión al servidor medienta la URL.
- Se crean los localizadores de cada uno de los elementos que se utilizarán en las pruebas con DOM y Devtools.
- Se crea __init__ qué es el constructor de la clase BugBankPage, para crear nuevas instancias de la clase y las funciones para sus atributos.
- Se agrega WebDriverWait que permite establecer tiempos de espera para la carga y verificación de datos en la secuencia de las pruebas automatizadas.

  - Prueba 1. 
Se crean lo métodos para los campos de entrada e ingresar las direcciones utilizando;
.send_keys() y .get_propierty() respectivamente para obtener el valor de entrada de los campos de direcciones,
y realizar las comprobaciones.
  - Prueba 2. 
Se crean los métodos para la selección de la tarifa  comfort, verificando la opción flash con 
el método .is_enable() para "Pedir un taxi" con .click() y finalmente .text para la verificación de la 
selección de la tarifa Comfort.
  - Prueba 3. 
Se crean los métodos para ingresar el número de teléfono con .click(), send_keys() y .text respectivamente 
para ingresar, introducir y verificar el número de teléfono, se ingresa codigo de confirmación con la funcion:
retrieve_phone_code que devuelve el codigo de confirmación.
  - Prueba 4. 
Se crean los métodos para los campos de entrada e ingresar número y código de la tarjeta con .click(), 
.send_keys(). Posteriormente se verifica la seleccion de la tarjeta ingresada con .is_enabled() y .text para realizar
la verificación de los datos y la seleción del método de pago.





### :page_facing_up: *Resumen del informe:* 
 - Informe del producto:

Se realizaron las pruebas del producto Bug Bank, algunas de las fallas se encuentran en el formulario de registro son: (            ), los datos de entrada no cumplen con los requisitos y sus parámetros. Otras funciones importantes que fallan son:(        ), una de las funciones principales que afectan de manera directa el funcionamiento de la app. 

Finalmente los cálculos de los costos del servicio de entrega, no corresponden a los establecidos en los requisitos, algunos de los parámetros y sus restricciones, no concuerdan con los costos y el horario disponible en relación al número de productos y su peso. Por lo que se notifica un estado no aprobado y de corrección. 


   
<div id="header" align="center"> 

![image](https://github.com/user-attachments/assets/a2c62116-9d5f-406a-a3ef-37dbc45e89c0)


