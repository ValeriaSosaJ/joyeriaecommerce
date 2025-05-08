# Aura Joyería - Ecommerce con Django
Este es un sistema web de ecommerce para una joyería, desarrollado con Django.
Incluye gestión de productos, categorías, pedidos y usuarios.

## Requisitos
- Python 3.10 
- Django 3.1.3
- Bootstrap 5

## Requerimientos Funcionales y no Funcionales 
- El sistema permitirá al administrador crear, actualizar, eliminar y leer productos.
- Los productos deberán contener campos representativos como: nombre, precio, imagen y categoría.
- Los formularios de producto deben validar que el nombre y precio sean campos obligatorios.
- El sistema permitirá al administrador crear, actualizar, eliminar y leer categorías.
- El sistema tendrá un apartado “Categoría” en el cual se mostrará todas las categorías de productos que hay en existencia para el usuario con los datos respectivos de cada categoría: código y nombre de categoría.
- El nombre de cada categoría será único y tendrá un máximo de 50 caracteres.
- El sistema solicitará a los usuarios registrarse en caso de que no tengan una cuenta previamente. El apartado de registro solicitará los siguientes campos: nombre de usuario,nombre completo, correo electrónico, número de teléfono, y contraseña.
- El correo utilizado deberá ser un correo válido y único por cuenta, de lo contrario el sistema no permitirá que se registre.
- El sistema almacenará las contraseñas de manera encriptada utilizando el sistema de autenticación por defecto de Django.
Los formularios de producto permitirán que el nombre, correo, contraseña, nombre de usuario y teléfono sean campos obligatorios.
- El sistema contará con una base de datos la cual llevará el registro de todos los clientes que han iniciado sesión en la que existirá la información que ingresó el usuario al registrarse y un número identificador de cliente con el que se identificará cada uno.
- El sistema restringirá el acceso a ciertas vistas mostrando un mensaje diciendo que solo los clientes registrados podrán realizar compras . Solo los usuarios registrados podrán realizar compras.
- El administrador deberá poder ver una lista de pedidos realizados con detalles como estado del pedido y nombre del cliente.
- El sistema permitirá cambiar el estado de los pedidos a: pendiente, procesado, enviado o entregado.
- El sistema mostrará un desglose del subtotal de pago del carrito de compra, mostrando cada producto y el precio respectivo. El sistema realizará una suma de todos los costos y mostrará la cantidad tentativa a pagar. Al final del total se mostrará el botón de “pagar”, que mostrará un mensaje si el pago se realizó exitosamente.
- Las actualizaciones y modificaciones de productos deben reflejarse en tiempo real en todas las partes del sistema.
- El sistema almacenará las contraseñas de manera encriptada utilizando el sistema de autenticación por defecto de Django.
- El diseño del sistema será responsive, adaptándose automáticamente a distintos tamaños de pantallas.
- Los productos eliminados desde el administrador ya no serán visibles para los usuarios en el apartado de categorías.
- El acceso al panel de administración de Django estará restringido exclusivamente a usuarios con privilegios de superusuario, gestionados mediante el sistema de autenticación y permisos integrado en Django. Los usuarios no autorizados no podrán acceder a esta sección del sistema.


## 🖥️ Secciones del sitio
- 🏠🗂️ Página de inicio con categorias (Anillos, Aretes, Collares, Pulseras)
![inicio](Gestion/static/img/README/inicio1.png)

![categorias](Gestion/static/img/README/cateogorias.png)

- 🛍️ Carrito de compras
![carrito](Gestion/static/img/README/carrito.png)

- 👤 Registro e inicio de sesión de clientes
![iniciar](Gestion/static/img/README/iniciarsesion.png)

![registro](Gestion/static/img/README/registro.png)
![registro](Gestion/static/img/README/registroo.png)

- 🛠️ Administración (Django Admin)
![admin](Gestion/static/img/README/admin.png)

## Diagrama Caso de Uso 
![diagrama](Gestion/static/img/README/diagrama.png)