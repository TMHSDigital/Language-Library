import scala.collection.mutable.ListBuffer

case class Book(title: String, author: String)

class Bookstore {
  private val books = ListBuffer[Book]()

  def addBook(title: String, author: String): Unit = {
    books += Book(title, author)
  }

  def viewBooks(): Unit = {
    if (books.isEmpty) {
      println("No books available.")
    } else {
      books.zipWithIndex.foreach { case (book, index) =>
        println(s"${index + 1}. ${book.title} by ${book.author}")
      }
    }
  }

  def deleteBook(index: Int): Unit = {
    if (index >= 1 && index <= books.size) {
      books.remove(index - 1)
      println(s"Book $index deleted.")
    } else {
      println("Invalid book number.")
    }
  }
}

object BookstoreManagementSystem extends App {
  val bookstore = new Bookstore

  while (true) {
    println("\nBookstore Management System")
    println("1. Add Book")
    println("2. View Books")
    println("3. Delete Book")
    println("4. Exit")
    print("Choose an option: ")
    val choice = scala.io.StdIn.readInt()

    choice match {
      case 1 =>
        print("Enter book title: ")
        val title = scala.io.StdIn.readLine()
        print("Enter book author: ")
        val author = scala.io.StdIn.readLine()
        bookstore.addBook(title, author)
      case 2 =>
        bookstore.viewBooks()
      case 3 =>
        print("Enter book number to delete: ")
        val index = scala.io.StdIn.readInt()
        bookstore.deleteBook(index)
      case 4 =>
        println("Exiting...")
        System.exit(0)
      case _ =>
        println("Invalid option. Please try again.")
    }
  }
}
