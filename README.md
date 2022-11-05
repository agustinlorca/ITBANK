# ITBANK

Proyecto de Homebanking elaborado en Django.

Instalaciones antes de ejecutar el proyecto:
- pip install djangorestframework
- pip install django-widget-tweaks
- pip install django-filters

Para entrar al administrador:
- Usuario: admin
- Contraseña: itbank12345

Usuarios:

- totoa (pass: totoa) Cliente Classic
- aguslorca (pass: itbank12345) Cliente Gold
- florencia (pass: itbank12345) Cliente Black
- juansito (pass: itbank12345)
- mariamarta (pass: itbank12345)


Cada usuario tiene tipos de cuentas diferentes. Algunos tienen tarjetas y prestamos asociados a sus cuentas y otros no. Entrando en el administrador se pueden rellenar los campos como se deseen.
Al crear una cuenta nueva, unicamente va a estar el usuario creado, no va a tener ninguna cuenta, cliente, tarjetas y saldo asociado. Para ello hay que asignarlo a través del panel de admin de Django para luego verse reflejado.

Para evitar ejecutar el proyecto y los pasos que conlleva, se puede visualizar el mismo en pythonanywhere.
Link: http://aguslorca.pythonanywhere.com/

Nota: todo funciona bien pero no se visualiza correctamente el panel de Django y de Django Rest Framework. 
