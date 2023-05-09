
async function lol(){

const response = await fetch("http://127.0.0.1:8000/book/");
const data = await response.json();

console.log(data)
}

lol()