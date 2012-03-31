function graphHourlyUsers(ele_id, d, title) {
  
  if(!title){
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


function graphVisitorPercentage(ele_id, d, title){
    if(!title){
      title="New vs Returning";
    }
    
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Player Type');
    data.addColumn('number', 'Players');
    
    for(x in d){
      data.addRow([x, d[x]]);
    }
    
    new google.visualization.PieChart(document.getElementById(ele_id)).draw(data, {legend: 'none', title: title});
}