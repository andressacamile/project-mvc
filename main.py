# Modelo (Model)
class Book:
    def __init__(self, title, author, read=False):
        self.title = title
        self.author = author
        self.read = read

# Controlador (Controller)
class BookController:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def mark_as_read(self, index):
        if 0 <= index < len(self.books):
            self.books[index].read = True

    def delete_book(self, index):
        if 0 <= index < len(self.books):
            del self.books[index]

# Visualização (View)
class BookView:
    def show_books(self, books):
        print("Lista de Livros:")
        for index, book in enumerate(books):
            status = "Lido" if book.read else "Não lido"
            print(f"{index + 1}. \"{book.title}\" por {book.author} - {status}")

# Controlador Principal (Main Controller)
class MainController:
    def __init__(self):
        self.book_controller = BookController()
        self.book_view = BookView()

    def run(self):
        while True:
            self.book_view.show_books(self.book_controller.books)
            print("\n1. Adicionar Livro")
            print("2. Marcar Livro como Lido")
            print("3. Deletar Livro")
            print("4. Sair")

            choice = input("Escolha uma opção: ")

            if choice == "1":
                title = input("Digite o título do livro: ")
                author = input("Digite o autor do livro: ")
                self.book_controller.add_book(title, author)
            elif choice == "2":
                index = int(input("Digite o número do livro que deseja marcar como lido: ")) - 1
                self.book_controller.mark_as_read(index)
            elif choice == "3":
                index = int(input("Digite o número do livro que deseja deletar: ")) - 1
                self.book_controller.delete_book(index)
            elif choice == "4":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    app = MainController()
    app.run()
