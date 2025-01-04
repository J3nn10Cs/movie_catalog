from domain.movie import Movie
from services.movie_catalog import MovieCatalog as mc

print('Bienvenido al catalago de peliculas'.center(50,'-'))

close = False

while close == False:
  try:
    print('Menu \n 1.Agregar pelicula \n 2. Listar peliculas \n 3. Eliminar archivo de peliculas \n 4. Salir')

    option = int(input('Ingrese una opción : '))
    
    match(option):
      case 1:
        #le pedimos una pelicula al usuario
        name_movie = input('Ingrese el nombre de una pelicula : ')
        #creamos el objeto de tipo pelicula
        movie = Movie(name_movie)
        #agregamos al archivo
        mc.add_movie(movie)
      case 2:
        #listamos -> mostramos la pelicula por consola
        mc.list_movie()
      
      case 3:
        #eliminamos el archivo
        mc.delete_movie()
      
      case 4:
        print('Gracias por su visita')
        close = True
  except Exception as e:
    print(f'Ocurrió un error : {e}')
    close = False