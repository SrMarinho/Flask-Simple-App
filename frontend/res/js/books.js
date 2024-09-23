var API_URL = 'http://localhost:5000/api/books'

async function* getBooks() {
    const response = await fetch(API_URL);
    const reader = response.body.getReader();
    const decoder = new TextDecoder('utf-8');

    while (true) {
        const { done, value } = await reader.read();

        if (done) {
            break;
        }

        const chunk = decoder.decode(value, { stream: true });
        yield JSON.parse(chunk);
    }
}

function addBookInTable(book) {
    const table = document.getElementById("booksTable")
    const body = table.getElementsByTagName("tbody")[0]


    const novaLinha = document.createElement('tr');


    const id_cell = document.createElement('td');
    id_cell.innerHTML = book.id
    const title_cell = document.createElement('td');
    title_cell.innerHTML = book.title
    const author_cell = document.createElement('td');
    author_cell.innerHTML = book.author
    const rented_cell = document.createElement('td');
    rented_cell.innerHTML = book.rented

    novaLinha.appendChild(id_cell);
    novaLinha.appendChild(title_cell);
    novaLinha.appendChild(author_cell);
    novaLinha.appendChild(rented_cell);

    body.appendChild(novaLinha);

    novaLinha.classList.add('rowIn');
    
    // novaLinha.scrollIntoView({behavior: 'instant'})

    setTimeout(() => {
        novaLinha.classList.remove('rowIn');
    }, 500);

}

window.addEventListener("load", async () => {
    for await (const book of getBooks()) {
        addBookInTable(book)
    }
});
