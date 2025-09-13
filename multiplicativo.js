fetch("navbar.html")
  .then((res) => res.text())
  .then((data) => (document.getElementById("navbar").innerHTML = data));

function generar() {
  let x0 = parseInt(document.getElementById("x0").value);
  let k = parseInt(document.getElementById("k").value);
  let aTipo = parseInt(document.getElementById("aTipo").value); 
  let p = parseInt(document.getElementById("p").value);
  let d = parseInt(document.getElementById("d").value);

  let g = Math.ceil(Math.log2(p));
  let m = Math.pow(2, g);

  let a = aTipo + 8 * k;

  if (x0 % 2 === 0) {
    alert(`⚠️ El valor de X₀ = ${x0} no es válido. Debe ser impar.`);
    return;
  }

  document.getElementById("params").innerHTML =
    `X₀ = ${x0}; k = ${k}; a = ${a}; m = ${m}; g = ${g}; generados = ${p}`;

  let tbody = document.querySelector("#tabla tbody");
  tbody.innerHTML = "";

  let xi = x0;
  let primerValor = null;
  let repetido = false;

  for (let i = 1; i <= p + 1; i++) {
    let xiPrev = xi;
    let operacion = `(${a} * ${xiPrev}) mod ${m}`;
    xi = (a * xiPrev) % m;
    let ri = (xi / (m - 1)).toFixed(d);

    if (i === 1) primerValor = xi;
    if (i === p + 1 && xi === primerValor) {
      repetido = true;
    }

    let row = `
      <tr ${i === p + 1 && repetido ? "style='background:#ffe6e6; font-weight:bold;'" : ""}>
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
