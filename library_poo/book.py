class Book:

    def __init__(self, title='<unknown>', author='unknown', genre='indefined', number_pages=0, status=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.number_pages = number_pages
        self.status = status
    
    def to_dict(self):
      #Return the book formatted for dictionary
      return {
          'title': self.title,
          'author': self.author,
          'genre': self.genre,
          'number_pages': self.number_pages,
          'status': self.status,

      }