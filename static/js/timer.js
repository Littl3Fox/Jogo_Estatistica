console.log("timer.js carregado!");

let tempo = parseInt(document.getElementById("tempo").dataset.value);

let contador = document.getElementById("contador");
let form = document.getElementById("form");
let penalidade = document.getElementById("penalidade");

let intervalo = setInterval(() => {
    tempo--;
    contador.innerText = tempo;

    if (tempo <= 0) {
        clearInterval(intervalo);
        penalidade.submit();  // envia penalidade automaticamente
    }
}, 1000);
