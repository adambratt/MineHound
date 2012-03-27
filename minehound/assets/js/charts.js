function graphHourlyUsers(ele_id, d) {
  var hours = [];
  var users = [];
  
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Hour');
  data.addColumn('number', 'Users');
  
  for(x in d){
    data.addRow((d[x].hour).toString(), d[x].users);
  }
  
  new google.visualization.ImageAreaChart(document.getElementById(ele_id)).draw(data, null);
    
}