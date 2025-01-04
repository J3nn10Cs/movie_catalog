class Movie:
  count_movie = 0
  def __init__(self,name_movie):
    Movie.count_movie += 1
    self.id =Movie.count_movie
    self._name_movie = name_movie
  
  #metodo get
  @property
  def name_movie(self):
    return self._name_movie

  #set
  @name_movie.setter
  def name_movie(self,name_movie):
    self._name_movie = name_movie

  def __str__(self):
    return f'''{self.name_movie}'''