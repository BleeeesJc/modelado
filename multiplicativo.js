fetch("navbar.html")
        .then((res) => res.text())
        .then((data) => (document.getElementById("navbar").innerHTML = data));
function generar() {
  let x0 = parseInt(document.getElementById("x0").value);
  let k = parseInt(document.getElementById("k").value);
  let aTipo = parseInt(document.getElementById("aTipo").value);
  let p = parseInt(document.getElementById("p").value); 

  let g = 4;
  let m = Math.pow(2, g);
  let a = aTipo + 8 * k;
  document.getElementById("params").innerHTML =
    `X₀ = ${x0}, k = ${k}, a = ${a}, m = ${m}, generados = ${p}`;

  let tbody = document.querySelector("#tabla tbody");
  tbody.innerHTML = "";

  let xi = x0;
  for (let i = 1; i <= p; i++) {
    let xiPrev = xi;
    let operacion = `(${a} * ${xiPrev}) mod ${m}`;
    xi = (a * xiPrev) % m;
    let ri = (xi / (m - 1)).toFixed(d);

    let row = `
      <tr>
        <td>${i}</td>
        <td>${xiPrev}</td>
        <td>${operacion}</td>
        <td>${xi}</td>
        <td>${ri}</td>
      </tr>
    `;
    tbody.innerHTML += row;
  }
}

function limpiar() {
  document.querySelector("#tabla tbody").innerHTML = "";
  document.getElementById("params").innerHTML = "";
}
