function graphHourlyUsers(ele_id, d, title) {
  
  if(!title.length){
    title = "Hourly Users";
  }
  
  var hours = [];
  var users = [];
  
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Hour');
  data.addColumn('number', 'Users');
  
  for(x in d){
    data.addRow([(d[x].hour).toString(), d[x].users]);
  }
  
  new google.visualization.AreaChart(document.getElementById(ele_id)).draw(data, {legend: 'none', title: title, hAxis: {fontSize: 8}});
    
}

function graphWeekUsers(ele_id, d) {
    graphHourlyUsers(ele_id, d, "Weekly Users")
}