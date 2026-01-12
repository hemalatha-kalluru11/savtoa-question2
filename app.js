const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

function drawOwnShip() {
  ctx.fillStyle = "blue";
  ctx.beginPath();
  ctx.arc(250, 250, 8, 0, Math.PI * 2);
  ctx.fill();
}

function drawTargets(data) {
  data.forEach(t => {
    if (t.risk === "Danger") ctx.fillStyle = "red";
    else if (t.risk === "Warning") ctx.fillStyle = "orange";
    else ctx.fillStyle = "green";

    let x = 250 + t.x;
    let y = 250 + t.y;

    ctx.beginPath();
    ctx.arc(x, y, 6, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = "black";
    ctx.fillText(t.risk, x + 8, y);
  });
}

function updateAlerts(data) {
  let html = "";
  data.forEach(t => {
    html += `<div class="${t.risk}">Target ${t.id} : ${t.risk} | CPA ${t.cpa}</div>`;
  });
  document.getElementById("alerts").innerHTML = html;
}

function update() {
  ctx.clearRect(0, 0, 500, 500);
  drawOwnShip();

  fetch("data.json")
    .then(r => r.json())
    .then(data => {
      drawTargets(data);
      updateAlerts(data);
    });
}

setInterval(update, 1000);
