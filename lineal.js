fetch("navbar.html")
  .then((response) => response.text())
  .then((data) => {
    document.getElementById("navbar").innerHTML = data;
  });

function gcd(a, b) {
  while (b !== 0) {
    let t = b;
    b = a % b;
    a = t;
  }
  return a;
}

function generar() {
  const x0 = parseInt(document.getElementById("x0").value);
  const k = parseInt(document.getElementById("k").value);
  const c = parseInt(document.getElementById("c").value);
  const p = parseInt(document.getElementById("p").value);
  const d = parseInt(document.getElementById("d").value);

  const a = 1 + 4 * k;
  const g = Math.ceil(Math.log2(p));
  const m = Math.pow(2, g);

  if (gcd(c, m) !== 1) {
    alert(`⚠️ El valor de c = ${c} no es relativamente primo con m = ${m}. 
Por favor elige otro valor.`);
    return;
  }

  const n = p;
  document.getElementById("params").innerText = 
    `a: ${a} ; c: ${c} ; g: ${g} ; m: ${m} ; Generados: ${n}`;

  let xi = x0;
  let tbody = document.querySelector("#tabla tbody");
  tbody.innerHTML = "";

  let primerValor = null;
  let repetido = false;

  for (let i = 1; i <= n + 1; i++) {
    let xNext = (a * xi + c) % m;
    let ri = (xNext / (m - 1)).toFixed(d);
    if (i === 1) primerValor = xNext;
    if (i === n + 1 && xNext === primerValor) {
      repetido = true;
    }

    let row = `
      <tr ${i === n + 1 && repetido ? "style='background:#ffe6e6; font-weight:bold;'" : ""}>
        <td>${i}</td>
        <td>${xi}</td>
        <td>(${a} * ${xi} + ${c}) mod ${m}</td>
        <td>${xNext}</td>
        <td>${ri}</td>
      </tr>
    `;
    tbody.innerHTML += row;

    xi = xNext;
  }
}

function limpiar() {
  document.querySelector("#tabla tbody").innerHTML = "";
  document.getElementById("params").innerText = "";
}
