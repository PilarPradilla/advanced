function hello_ud(){
    // Actualiza el contenido del elemento con id 'result' con el mensaje de bienvenida
    document.getElementById('result').innerHTML = "Welcome to UD!";
}

async function callMessage() {
    try {
        // Realiza una solicitud al endpoint '/hello_ud'
        const response = await fetch('http://127.0.0.1:8000/hello_ud');
        // Lee la respuesta como texto
        const data = await response.text();
        // Muestra el mensaje obtenido en el elemento con id 'result'
        document.getElementById('result').innerHTML = data;
    } catch (error) {
        // Muestra cualquier error en la consola y en el elemento 'result'
        console.error('Error:', error);
        document.getElementById('result').innerHTML = 'Error';
    }
}

async function callTable() {
    try {
        // Realiza una solicitud al endpoint '/products'
        const response = await fetch('http://localhost:8000/products');
        // Verifica si la solicitud fue exitosa
        if (!response.ok) {
            throw new Error(`Error ${response.status}: ${response.statusText}`);
        }
        // Lee la respuesta como JSON
        const data = await response.json();
        // Construye una tabla HTML con los datos de los productos
        let table = '<table>';
        table += '<tr><th>ID</th><th>Name</th><th>Description</th></tr>';
        data.forEach(item => {
            table += `<tr><td>${item.id}</td><td>${item.name}</td><td>${item.description}</td></tr>`;
        });
        table += '</table>';
        // Muestra la tabla en el elemento con id 'result'
        document.getElementById('result').innerHTML = table;
    } catch (error) {
        // Muestra cualquier error en la consola y en el elemento 'result'
        console.error('Error:', error);
        document.getElementById('result').innerHTML = 'Error';
    }
}
