from django.test import TestCase
from  . models import Book, Author

class BookTestCase(TestCase):

    #creo parámetros de inicio de la prueba 
    def setUp(self):
        a1=Author.objects.create(first_name="Ernesto")
        Book.objects.create(title="El Tunel", author=a1, summary="Algo")
        
    
    def test_libros_author(self):
        book1 = Book.objects.get(titulo="El Tunel")
        self.assertEqual(book1.author.first_name, "Ernesto") 
        