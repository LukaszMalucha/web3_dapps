
function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("searchTable");
  switching = true;
  dir = "down";
  while (switching) {
    switching = false;
    rows = table.rows;
    for (i = 1; i < (rows.length - 1); i++) {
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      if (dir == "down") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          shouldSwitch = true;

          break;
        }
      } else if (dir == "up") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          shouldSwitch = true;

          break;
        }
      }
    }
    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      switchcount ++;

    } else {
      if (switchcount == 0 && dir == "down") {
        dir = "up";
        switching = true;
      }
    }
  }
}
function sortTableInt(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("searchTable");
  switching = true;
  dir = "asc";
  while (switching) {
    switching = false;
    rows = table.rows;
    for (i = 1; i < (rows.length - 1); i++) {
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      var x_int = (x.innerHTML).replaceAll(',','')
      var y_int = (y.innerHTML).replaceAll(',','')
      if (dir == "asc") {
        if (parseInt(x_int) > parseInt(y_int))  {
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (parseInt(x_int) < parseInt(y_int))  {
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      switchcount ++;
    } else {
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}

function sortTableFloat(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("searchTable");
  switching = true;
  dir = "down";
  while (switching) {
    switching = false;
    rows = table.rows;
    for (i = 1; i < (rows.length - 1); i++) {
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      var x_int = (x.innerHTML).replaceAll(',','')
      var y_int = (y.innerHTML).replaceAll(',','')
      if (dir == "down") {
        if (parseFloat(x_int) > parseFloat(y_int))  {
          shouldSwitch = true;
          break;
        }
      } else if (dir == "up") {
        if (parseFloat(x_int) < parseFloat(y_int))  {
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      switchcount ++;
    } else {
      if (switchcount == 0 && dir == "down") {
        dir = "up";
        switching = true;
      }
    }
  }
}

export { sortTable, sortTableInt, sortTableFloat };
