function graphHourlyUsers(ele_id, d) {
  
  var hours = [];
  var users = [];
  
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Hour');
  data.addColumn('number', 'Users');
  
  for(x in d){
    data.addRow([(d[x].hour).toString(), d[x].users]);
  }
  
  new google.visualization.AreaChart(document.getElementById(ele_id)).draw(data, {legend: 'none', hAxis: {fontSize: 8}});
    
}

function graphWeekUsers(ele_id, d) {
    graphHourlyUsers(ele_id, d)
}


function graphVisitorPercentage(ele_id, d, title){
    if(!title){
      title="New vs Returning";
    }
    
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Player Type');
    data.addColumn('number', 'Players');
    
    data.addRow(['new', d[0]['new']]);
    data.addRow(['returning', d[0]['returning']]);
    
    new google.visualization.PieChart(document.getElementById(ele_id)).draw(data, {legend: 'none', colors:['#9aea5a','#333']});
}