d3.json('./data').then(function(response){
 	x=response.map(row=>row[2]);
 	y=response.map(row=>row[10]);
 	trace={
 		'type': 'bar',  
 		'x': x, 
 		'y': y
 	}
	layout = {
		        title: 'California Unemployment Rate Over Years',
		        xaxis: {
		                    title: 'Year',
							tickmode:[2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024], 
                            tickvals: x,        
                            tickangle: -45  
		                },
		        yaxis: {
		                    title: 'Unemployment Rate'
		                }
		    };
 	Plotly.newPlot('plot', [trace],layout)
 });

 
