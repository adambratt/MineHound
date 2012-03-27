function graphHourlyUsers(ele_id, data) {
  var hours = [];
  var users = [];
  
  for(x in data) {
    hours = data[x].hour
    users = data[x].users
  }
    
  var wrapper = new google.visualization.ChartWrapper({
    chartType: 'ColumnChart',
    dataTable: [hours, users],
    options: {'title': 'Hourly Users'},
    containerId: ele_id
  });
  wrapper.draw();
}