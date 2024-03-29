function graphHourlyUsers(ele_id, d) {
  
  var hours = [];
  var users = [];
  
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Hour');
  data.addColumn('number', 'Users');
  
  for(x in d){
    data.addRow([(d[x].hour).toString(), d[x].users]);
  }
  
  new google.visualization.AreaChart(document.getElementById(ele_id)).draw(data, {legend: 'none', pointSize: 5, hAxis: {fontSize: 8, maxAlternation: 1, slantedText: false}, colors:['#9aea5a','#333'], areaOpacity: 0.6});
    
}

function graphWeekUsers(ele_id, d) {
    graphHourlyUsers(ele_id, d)
}


function graphPie(ele_id, d){
    
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Title');
    data.addColumn('number', 'Value');
    
    for(x in d){
      data.addRow([x, d[x]]);
    }
    
    new google.visualization.PieChart(document.getElementById(ele_id)).draw(data, {legend: 'none', chartArea: {left: 20, top: 20, width: "90%", height: "80%"}, colors:['#9aea5a','#333']});
}