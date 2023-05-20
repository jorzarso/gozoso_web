# Antes de empezar, ya que estamos trabajando con XAMPP, recordar que ahora hay que meter la carpeta del proyecto, en este caso tendeta_web en C:/xampp/htdocs

prompt_1 = f"""
Tu rol va a ser el de un asistente para el diseño de una página web
Tu tarea es completar las siguientes acciones : 
1 - Evaluar el código que te voy a pasar y decirme si es correcto
2 - Evaluar una vez hecho eso si los errores que me da se pueden solucionar en el propio código o debo añadir algo en otra parte de mi proyecto.
3 - Reescribir el código con las soluciones aportadas.
4 - Añade cualquier detalle adicional que creas que es necesario.



"""
response = get_completion(prompt_1)
print("\nCompletion for prompt 1:")
print(response)

# Debemos abrir xampp para visulizar el código

prompt_2 = f"""quiero el comando para darle el formato adecuado con separaciones y tabulaciones adecuadas
"""
response = get_completion(prompt_2)
print("\nCompletion for prompt 2:")
print(response)

prompt_3 = f"""
Estas son las siguientes tareas que voy a necesitar:
1 - Evaluar el código que te voy a pasar y decirme si es correcto
2 - Transformarlo para el caso de una carniceria, quiero que por ejemplo tenga una sección de productos
3 - Reescribir el código con las soluciones aportadas.
4 - Añade cualquier detalle adicional que creas que es necesario.

<!DOCTYPE html>
<html lang="es">
<head>
	<meta charset="UTF-8">
	<title>Mi sitio web</title>
    <link rel="stylesheet" type="text/css" href="main.css">
</head>
<body>
	<header>
		<h1>Bienvenidos a mi sitio web</h1>
		<nav>
			<ul>
				<li><a href="http://localhost/gozoso_web/main.html">Inicio</a></li>
				<li><a href="http://localhost/gozoso_web/acercade.html">Acerca de</a></li>
				<li><a href="http://localhost/gozoso_web/servicios.html">Servicios</a></li>
				<li><a href="http://localhost/gozoso_web/contacto.html">Contacto</a></li>
			</ul>
		</nav>
	</header>
	<main>
		<section>
			<h2>Acerca de nosotros</h2>
			<p>Somos una empresa dedicada a ofrecer soluciones digitales para empresas y particulares.</p>
		</section>
		<section>
			<h2>Nuestros servicios</h2>
			<ul>
				<li>Diseño web</li>
				<li>Desarrollo de aplicaciones móviles</li>
				<li>Marketing digital</li>
			</ul>
		</section>
	</main>
	<footer>
		<p>Derechos reservados © 2023</p>
	</footer>
</body>
</html>

"""
response = get_completion(prompt_3)
print("\nCompletion for prompt 3:")
print(response)

prompt_4 = f"""
El código lo prefiero así, con las modificaciones que me has pasado anteriormente y mi personalización:

<!DOCTYPE html>
<html lang="es">
<head>
	<meta charset="UTF-8">
	<title>Tendeta web</title>
    <link rel="stylesheet" type="text/css" href="main.css">
</head>
<body>
	<header>
		<h1>Bienvenidos a mi sitio web</h1>
		<nav>
			<ul>
				<li><a href="http://localhost/tendeta_web/main.html">Inicio</a></li>
				<li><a href="http://localhost/tendeta_web/acercade.html">Acerca de</a></li>
				<li><a href="http://localhost/tendeta_web/productos.html">Productos</a></li>
				<li><a href="http://localhost/tendeta_web/contacto.html">Contacto</a></li>
			</ul>
		</nav>
	</header>
	<main>
		<section>
			<h2>Acerca de nosotros</h2>
			<p>Somos una carnicería especializada en ofrecer productos frescos y de alta calidad a nuestros clientes.</p>
		</section>
		<section>
			<h2>Nuestros productos</h2>
			<ul>
				<li>Cortes de carne de res</li>
				<li>Pollo y productos avícolas</li>
				<li>Embutidos y productos procesados</li>
			</ul>
		</section>
	</main>
	<footer>
		<p>Derechos reservados © 2023</p>
	</footer>
</body>
</html>
"""
response = get_completion(prompt_4)
print("\nCompletion for prompt 4:")
print(response)

prompt_ = f"""
Ahora ya tenemos el inicio del html, lo siguiente es dar un formato css adecuado. Para ello quiero que:
1 - Evaluar el código que te voy a pasar y decirme si es correcto
2 - Transformarlo para el caso de una carniceria, con  colores más adecuados
3 - Reescribir el código con las soluciones aportadas.
4 - Añade cualquier detalle adicional que creas que es necesario.

/* Estilo para el cuerpo de la página */
body {
    font-family: Arial, sans-serif;
    margin: 0;
}

/* Estilo para el encabezado */
header {
    background-color: #333;
    color: #fff;
    padding: 10px;
}

header h1 {
    margin: 0;
}

header nav ul {
    margin: 0;
    padding: 0;
    list-style: none;
}

header nav li {
    display: inline-block;
    margin-right: 20px;
}

header nav li a {
    color: #fff;
    text-decoration: none;
}

/* Estilo para el contenido principal */
main {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

section {
    margin-bottom: 40px;
}

section h2 {
    font-size: 28px;
}

section ul {
    margin: 0;
    padding: 0;
    list-style: none;
}

section li {
    margin-bottom: 10px;
}

/* Estilo para el pie de página */
footer {
    background-color: #333;
    color: #fff;
    padding: 10px;
}

footer p {
    margin: 0;
}


"""
response = get_completion(prompt_5)
print("\nCompletion for prompt 5:")
print(response)

# Siguientes pasos:
# 2. Subirlo a github.
# 3. Continuar