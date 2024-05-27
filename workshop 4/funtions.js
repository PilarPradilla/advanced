function hello_ud(){
    alert("hello")
}

async function callMessage() {
    try {
        const response = await fetch('http://localhost:5500/hello_ud');
        const data = await response.text();
        document.getElementById('result').textContent = product;
    } catch (error) {
        console.error('Error:', error);
    }
}

async function callTable() {
    try {
        const response = await fetch('http://localhost:5500/products');
        const product = await response.json();
        
        let table = '<table>';
        table += '<tr><th>ID</th><th>Name</th><th>Description</th></tr>';
        
        product.forEach(item => {
            table += `<tr><td>${item.id}</td><td>${item.name}</td><td>${item.description}</td></tr>`;
        });
        
        table += '</table>';
        
        document.getElementById('result').innerHTML = table;
    } catch (error) {
        console.error('Error:', error);
    }
}
