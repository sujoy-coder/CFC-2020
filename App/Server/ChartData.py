# This Function formating the data to plot in Line Chart ...
def get_LineChartData(date_time,actualPower):
    lineChartData = []

    for i,j in zip(date_time,actualPower):
        lineChartData.append(list((i,j)))

    return lineChartData



# This Function formating the data to plot in Bar Chart ...
def get_BarChartData(date_time,wind_speed,wind_deg,humidity):
    barChartData = [['Date-Time ', 'Wind Speed (m/s)', 'Wind Direction (°)', 'Humidity (%)']]

    for a,b,c,d in zip(date_time,wind_speed,wind_deg,humidity):
        barChartData.append(list((a,b,c,d)))

    return barChartData



def get_TableData(date_time,actualPower,wind_speed):
    tableData = []

    for p,q,r in zip(date_time,actualPower,wind_speed):
        tableData.append(list((p,q,r)))

    return tableData