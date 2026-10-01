function f1(l) {
  var r = {};
  for (var i = 0; i < l.length; i++) {
    var k = l[i].categoria;
    r[k] = (r[k] || 0) + l[i].precio * l[i].stock;
  }
  return r;
}

function f2(s) {
  s = s.trim().toLowerCase();
  s = s.replace(/[^a-z0-9\s-]/g, '');
  return s.replace(/\s+/g, '-');
}

function f3(l, n) {
  // promedio móvil de ventana n
  var out = [];
  for (var i = 0; i < l.length; i++) {
    var v = l.slice(i, i + n);
    out.push(v.reduce((a, b) => a + b, 0) / n);
  }
  return out;
}

function f4(precio, pct) {
  return precio - (precio * pct) / 100;
}

module.exports = { f1, f2, f3, f4 };
