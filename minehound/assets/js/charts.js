function graphHourlyUsers(ele_id, d) {
  var hours = [];
  var users = [];
  
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Hour');
  data.addColumn('number', 'Users');
  data.addRows(d.length);
  
  for(x in d){
    data.setCell(x, 0, (d[x].hour).toString());
    data.setCell(x, 1, d[x].users);
  }
  
  new google.visualization.ImageAreaChart(document.getElementById(ele_id)).draw(data, null);
    
}