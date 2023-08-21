// Define an array of book objects
const allBooks = [
    {
        title: "Harry Potter",
        author: "JK Rowling",
        image: "https://example.com/harry_potter.jpg",
        alreadyRead: true
    },
    {
        title: "The Great Gatsby",
        author: "F. Scott Fitzgerald",
        image: "https://example.com/great_gatsby.jpg",
        alreadyRead: false
    }
];

// Function to render each book
function renderBooks() {
    const listBooksSection = document.querySelector('.listBooks');

    allBooks.forEach(book => {
        const bookDiv = document.createElement('div');
        const bookTitle = document.createElement('p');
        const bookAuthor = document.createElement('p');
        const bookImage = document.createElement('img');

        bookTitle.textContent = `${book.title} written by ${book.author}`;
        bookAuthor.textContent = book.alreadyRead ? 'Already read' : 'Not read yet';
        bookImage.src = book.image;
        bookImage.style.width = '100px';

        if (book.alreadyRead) {
            bookTitle.style.color = 'red';
            bookAuthor.style.color = 'red';
        }

        bookDiv.appendChild(bookTitle);
        bookDiv.appendChild(bookAuthor);
        bookDiv.appendChild(bookImage);

        listBooksSection.appendChild(bookDiv);
    });
}

// Call the renderBooks function to display books
renderBooks();
