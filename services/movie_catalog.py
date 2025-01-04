import os

class MovieCatalog:
  
  #variable de clase
  file_path = 'Catalago_peliculas/movie.txt'

  #metodo estatico - accede directamente al atributo de clase
  @classmethod
  def add_movie(cls,movie):
    #especificamos la ruta del archivo y accedemos a ella
    with open(cls.file_path,'a', encoding='utf8') as archive:#anexamos informacion
      #escribimos en el archivo
      archive.write(f'{movie}\n')
  
  @classmethod
  def list_movie(cls):
    #solo vamos a leer
    with open(cls.file_path,'r') as archive:
      print('-'.center(50))
      print(f'Catalago de Peliculas'.center(50,'-'))
      print(archive.read())
  
  @classmethod
  def delete_movie(cls):
    #eliminamos el archivo
    os.remove(cls.file_path)
    print(f'Archio eliminado {cls.file_path}')