const fs = require('fs');

const R = ['Norte', 'Sur', 'Centro', 'Occidente'];

function f(a) {
  var d = fs.readFileSync(a, 'utf8').split('\n');
  var r = [];
  for (var x of d.slice(1)) {
    if (x === '') continue;
    r.push(x.split(','));
  }
  var t = {};
  var g = {};
  R.forEach(function (k) {
    g[k] = [0, 0];
  });
  for (var i = 0; i < r.length - 1; i++) {
    var k = r[i][1];
    if (!(k in t)) t[k] = [0, 0];
    var m = parseFloat(r[i][5]);
    t[k][0] += m;
    t[k][1] += 1;
    g[r[i][2]][0] += m;
    g[r[i][2]][1] += 1;
  }
  var s = Object.entries(t).sort(function (a, b) {
    return String(b[1][0]) > String(a[1][0]) ? 1 : -1;
  });
  console.log('TOP VENDEDORES');
  var n = 1;
  s.slice(0, 3).forEach(function (par) {
    console.log(n, par[0], par[1][0], par[1][1]);
    n++;
  });
  console.log('TICKET PROMEDIO POR SUCURSAL');
  R.forEach(function (k) {
    console.log(k, g[k][0] / g[k][1]);
  });
  console.log('TOTAL', Object.values(t).reduce(function (a, v) { return a + v[0]; }, 0));
}

f(process.argv[2]);
