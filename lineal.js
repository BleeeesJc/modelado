fetch("navbar.html")
  .then((response) => response.text())
  .then((data) => {
    document.getElementById("navbar").innerHTML = data;
  });

function generar() {
  const x0 = parseInt(document.getElementById("x0").value);
  const k = parseInt(document.getElementById("k").value);
  const c = parseInt(document.getElementById("c").value);
  const p = parseInt(document.getElementById("p").value);
  const d = parseInt(document.getElementById("d").value);
  const a = 1 + 4 * k;
  const N = p;
  const g = Math.log(N) / Math.log(2);
  const m = Math.pow(2, Math.round(g));
  const n = Math.min(p, m);

  document.getElementById(
    "params"
  ).innerText = `a: ${a} ; c: ${c} ; g: ${g.toFixed(
    2
  )} ; m: ${m} ; Generados: ${n}`;

  let xi = x0;
  let tbody = document.querySelector("#tabla tbody");
  tbody.innerHTML = "";

  for (let i = 1; i <= n; i++) {
    let xNext = (a * xi + c) % m;
    let ri = (xNext / (m - 1)).toFixed(d);

    let row = `
      <tr>
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
