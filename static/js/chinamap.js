
// Reference: http://code.highcharts.com/mapdata/countries/cn/cn-all.js
//http://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/highcharts/members/series-setdata/
//http://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/highcharts/demo/dynamic-update/

var lines = [];
var lines2 = [];
var lines3 = [];
var lines4 = [];
var lines5 = [];
var lines6 = [];

Highcharts.setOptions({
    global: {
      useUTC: false
    }
  });
  
  
  $(document).ready(function(){
    $.ajax({
          type: "GET",
          url: "./static/appliances_ownership.csv",
          dataType: "text",
          success: function(data) {processData(data);}
       });
  });

function processData(allText) {
    // var utcDate = Date.UTC(2005, 1, 1, 0, 0, 0);
    // console.log(utcDate);
     var allTextLines = allText.split(/\r\n|\n/);
     var headers = allTextLines[0].split(',');
     
     for (var i=0; i<allTextLines.length; i++) {
         var data = allTextLines[i].split(',');
         //console.log(data);
         if (data.length == headers.length) {
             var tarr = [];
             var tarr2 = [];
             var tarr3 = [];
             var tarr4 = [];
             var tarr5 = [];
             var tarr6 = [];
             for (var j=0; j<headers.length; j++) {
                    if (j==0){
                     tarr.push(data[j]);
                     tarr2.push(data[j]);
                     tarr3.push(data[j]);
                     tarr4.push(data[j]);
                     tarr5.push(data[j]);
                     tarr6.push(data[j]);
                    }
                    else if (j==1){
                     tarr.push(parseFloat(data[j]));
                    }
                    else if (j==2){
                        tarr2.push(parseFloat(data[j]));
                    }
                    else if (j==3){
                        tarr3.push(parseFloat(data[j]));
                    }
                    else if (j==4){
                        tarr4.push(parseFloat(data[j]));
                    }
                    else if (j==5){
                        tarr5.push(parseFloat(data[j]));
                    }
                    else if (j==6){
                        tarr6.push(parseFloat(data[j]));
                    }
             }
             lines.push(tarr);
             lines2.push(tarr2);
             lines3.push(tarr3);
             lines4.push(tarr4);
             lines5.push(tarr5);
             lines6.push(tarr6);
         }
     }
     console.log(lines);
     console.log(lines2);
     populatemap(lines);
}
var mymap;

function populatemap (lines){
mymap = Highcharts.mapChart('container', {
    chart: {
        map: 'countries/cn/cn-all',
        events: {
            load: function () {
                        // set up the updating of the chart each second
                        var series = this.series[0];
                        setInterval(function () {
                            //var x = (new Date()).getTime(), // current time
                            //var y = Math.random();
                            //series.addPoint([x, y], true, true);
                           //series.data[1].value = 1 +100*Math.random();

                            //lines[1].value = 1 +100*Math.random();

                            //series.setData(lines, true, true, true)
                            //console.log(series.data[1].value);
                            //console.log(lines[1].value);
                        }, 2000);
                    }
                }
    },

    title: {
        text: 'Appliance Ownswership in 2050 (million of units)'
    },

    subtitle: {
        text: 'Source map: <a href="http://www.stats.gov.cn/english/Statisticaldata/CensusData/rkpc2010/indexch.htms">2010 Population Census of the People`s Republic of China </a>'
    },


    mapNavigation: {
        enabled: true,
        buttonOptions: {
            verticalAlign: 'bottom'
        }
    },

    colorAxis: {
        min: 0
    },
    series: [{
        data: (function (){
            data= lines;
            console.log(data);
            return data;
        }()),

        name: 'Appliance ownership (million of units)',
        allowPointSelect: true,
        cursor: 'pointer',
        states: {
            hover: {
                color: '#BADA55'
            }
        },
        dataLabels: {
            enabled: true,
            format: '{point.name}'
        }
    }]
});

}

$('input[name=appliance]').click(function() {
   value_sel=$('input[name=appliance]:checked').val();
   console.log(value_sel)
   switch(value_sel) {
    case '1':
        populatemap (lines);
        break;
    case '2':
        populatemap (lines2);
        break;
    case '3':
        populatemap (lines3);
        break;
    case '4':
        populatemap (lines4);
        break;
    case '5':
        populatemap (lines5);
        break;
    case '6':
        populatemap (lines6);
        break;
    default:
        populatemap (lines);
    }
});