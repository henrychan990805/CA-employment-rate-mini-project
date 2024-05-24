d3.json('./data').then(function(response){
    // Extract x and y values from response
    var x = response.map(row => row[2]);
    var y = response.map(row => row[10]);

    // Group y values by x values and calculate the average
    var groupedData = {};
    x.forEach((value, index) => {
        if (!groupedData[value]) {
            groupedData[value] = [];
        }
        groupedData[value].push(y[index]);
    });

    var groupedX = Object.keys(groupedData);
    var groupedY = groupedX.map(key => groupedData[key].reduce((a, b) => a + b, 0) / groupedData[key].length);

    // Create trace object
    var trace1 = {
        type: 'line',
        x: groupedX,
        y: groupedY
    };

    // Create layout
    var layout1 = {
        title: 'California Unemployment Rate Over Years (Grouped by Year)',
        xaxis: {
            title: 'Year',
            tickmode: 'array',
            tickvals: groupedX,
            tickangle: -45
        },
        yaxis: {
            title: 'Average Unemployment Rate'
        }
    };

    // Create plot
    Plotly.newPlot('bar', [trace1], layout1);

    // Step 1: Group the data by industry and year
    var ind = response.map(row => row[5]);
    var years = response.map(row => row[2]);
    var emp = response.map(row => row[6]);

    var dataByIndustryAndYear = {};
    for (var i = 0; i < ind.length; i++) {
        var industry = ind[i];
        var year = years[i];
        var employment = emp[i];

        if (!dataByIndustryAndYear[industry]) {
            dataByIndustryAndYear[industry] = {};
        }

        if (!dataByIndustryAndYear[industry][year]) {
            dataByIndustryAndYear[industry][year] = 0;
        }

        dataByIndustryAndYear[industry][year] += employment;
    }

    // Calculate the employment growth rate for each industry
    var employmentGrowthRates = {};
    for (var industry in dataByIndustryAndYear) {
        employmentGrowthRates[industry] = {};

        var years = Object.keys(dataByIndustryAndYear[industry]).sort();
        for (var i = 1; i < years.length; i++) {
            var currentYear = years[i];
            var previousYear = years[i - 1];

            var currentEmployment = dataByIndustryAndYear[industry][currentYear];
            var previousEmployment = dataByIndustryAndYear[industry][previousYear];

            var growthRate = ((currentEmployment - previousEmployment) / previousEmployment) * 100;
            employmentGrowthRates[industry][currentYear] = growthRate;
        }
    }

// Define a custom color scale for distinct colors
    var colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'];

    // Plot the employment growth rate over time for each industry
    var traces = [];
    var colorIndex = 0;
    for (var industry in employmentGrowthRates) {
        var years = Object.keys(employmentGrowthRates[industry]);
        var growthRates = Object.values(employmentGrowthRates[industry]);

        var trace = {
            x: years,
            y: growthRates,
            mode: 'lines+markers',
            name: industry,
            line: {
                color: colors[colorIndex % colors.length] // Use colors from the custom color scale
            }
        };
        traces.push(trace);
        colorIndex++;
    }

    var layout = {
        title: "California Employment Growth Rate by Industry Over Time",
        xaxis: { title: "Year" },
        yaxis: { title: "Employment Growth Rate (%)" }
    };

    // Create an interactive plot using Plotly
    Plotly.newPlot("bubble", traces, layout, { responsive: true });




});

// d3.json('./job').then(function(response){
//     // Extract x and y values from response
//     var year = response.map(row => row[2]);
//     var emp = response.map(row => row[8]);
//     var unemp = response.map(row => row[9]);

//     // Create trace objects for employment and unemployment
//     var trace1 = {
//         type: 'scatter',
//         mode: 'markers',
//         name: 'Employment', // Name of the trace for legend
//         x: year,
//         y: emp
//     };

//     var trace2 = {
//         type: 'scatter',
//         mode: 'markers',
//         name: 'Unemployment', // Name of the trace for legend
//         x: year,
//         y: unemp
//     };

//     // Create layout
//     var layout = {
//         title: 'Employment vs. Unemployment Over Years',
//         xaxis: {
//             title: 'Year',
//             tickangle: -45
//         },
//         yaxis: {
//             title: 'Count'
//         },
//         legend: {
//             x: 0,
//             y: 1
//         }
//     };

//     // Create plot
//     Plotly.newPlot('bubble', [trace1, trace2], layout);
// });




 