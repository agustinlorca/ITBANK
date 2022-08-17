fetch("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
  .then((res) => res.json())
  .then((data) => {
    console.log(data);
    miObj(data);
  });

function miObj(data) {
  /* Dolar Liqui */

  let venta3 = document.getElementById("venta3");
  venta3.innerHTML = `$${data[3].casa.venta}`;

  let variacion3 = document.getElementById("variacion3");
  let flecha3 = data[3].casa.variacion;
  if (flecha3.includes("-")) {
    variacion3.innerHTML = `<i class="fa-solid fa-caret-down"></i> Variacion: ${data[3].casa.variacion}%`;
  } else {
    variacion3.innerHTML = `<i class="fa-solid fa-caret-up"></i> Variacion: ${data[3].casa.variacion}%`;
  }

  /* Dolar Turista */

  let venta6 = document.getElementById("venta6");
  venta6.innerHTML = `$${data[6].casa.venta}`;

  let variacion6 = document.getElementById("variacion6");
  let flecha6 = data[6].casa.variacion;
  if (flecha6.includes("-")) {
    variacion6.innerHTML = `<i class="fa-solid fa-caret-down"></i> Variacion: ${data[6].casa.variacion}%`;
  } else {
    variacion6.innerHTML = `<i class="fa-solid fa-caret-up"></i> Variacion: ${data[6].casa.variacion}%`;
  }

  /* Dolar Blue */

  let compra = document.getElementById("compra");
  compra.innerHTML = `$${data[1].casa.compra}`;

  let venta = document.getElementById("venta");
  venta.innerHTML = `$${data[1].casa.venta}`;

  let variacion = document.getElementById("variacion");
  let flecha = data[1].casa.variacion;
  if (flecha.includes("-")) {
    variacion.innerHTML = `<i class="fa-solid fa-caret-down"></i> Variacion: ${data[1].casa.variacion}%`;
  } else {
    variacion.innerHTML = `<i class="fa-solid fa-caret-up"></i> Variacion: ${data[1].casa.variacion}%`;
  }

  /* Dolar Bolsa */

  let venta5 = document.getElementById("venta5");
  venta5.innerHTML = `$${data[4].casa.venta}`;

  let variacion5 = document.getElementById("variacion5");
  let flecha5 = data[4].casa.variacion;
  if (flecha5.includes("-")) {
    variacion5.innerHTML = `<i class="fa-solid fa-caret-down"></i> Variacion: ${data[4].casa.variacion}%`;
  } else {
    variacion5.innerHTML = `<i class="fa-solid fa-caret-up"></i> Variacion: ${data[4].casa.variacion}%`;
  }

  /* Dolar Promedio */

  let venta7 = document.getElementById("venta7");
  venta7.innerHTML = `$${data[7].casa.venta}`;

  let compra7 = document.getElementById("compra7");
  compra7.innerHTML = `$${data[7].casa.compra}`;

  let variacion7 = document.getElementById("variacion7");
  let flecha7 = data[6].casa.variacion;
  if (flecha7.includes("-")) {
    variacion7.innerHTML = `<i class="fa-solid fa-caret-down"></i> Variacion: ${data[6].casa.variacion}%`;
  } else {
    variacion7.innerHTML = `<i class="fa-solid fa-caret-up"></i> Variacion: ${data[6].casa.variacion}%`;
  }

  /* Dolar Oficial */

  let venta1 = document.getElementById("venta1");
  venta1.innerHTML = `$${data[0].casa.venta}`;

  let compra1 = document.getElementById("compra1");
  compra1.innerHTML = `$${data[0].casa.compra}`;

  let variacion1 = document.getElementById("variacion1");
  let flecha1 = data[0].casa.variacion;
  if (flecha1.includes("-")) {
    variacion1.innerHTML = `<i class="fa-solid fa-caret-down"></i> Variacion: ${data[0].casa.variacion}%`;
  } else {
    variacion1.innerHTML = `<i class="fa-solid fa-caret-up"></i> Variacion: ${data[0].casa.variacion}%`;
  }
}
