if (typeof String.prototype.startsWith != 'function') {
  String.prototype.startsWith = function (str){
    return this.indexOf(str) == 0;
  };
}

function plot_charts() {
    var company;
    for (company in flot_data) {
        if(flot_data.hasOwnProperty(company)) {
            var plotdiv = $('#' + company + '_flot');
            var mul_series = flot_data[company];
            var data = [], series;
            for (series in mul_series) {
                if (series === "Closing Price") {
                    data.push({label: series, data: mul_series[series], points: {show: false}});
                } else {
                    data.push({label: series, data: mul_series[series], points: {show: true}});
                }
            }
            $.plot(plotdiv,data,{
                    series: {
                        lines: { show: true }
//                        points: { show: false }
                    },
                    xaxis: {
                        tickDecimals: 0,
//                        ticks: [0, [Math.PI/2, "\u03c0/2"], [Math.PI, "\u03c0"], [Math.PI * 3/2, "3\u03c0/2"], [Math.PI * 2, "2\u03c0"]]
                        mode: "time",
                        timeformat: "%y",
                        tickSize: [1, "year"]
                    },
                    yaxis: {
                        ticks: 10,
                        min: 0
//                        max: 2
                    },
                    grid: {
                        backgroundColor: { colors: ["#fff", "#eee"] }
                    }
            });
        }
    }
}

var niceRed = '#DD514C';
var flot_data = {};
var addFlotDataPoint = function (x, y, series, company) {
//    x = parseInt(x);
    y = parseFloat(y);

//    if ((typeof x !== 'number' || isNaN(x)) || (typeof y !== 'number' || isNaN(y))) {
//        return;
//    }
    if (!flot_data[company]) {
        flot_data[company] = {};
    }

    if (!flot_data[company][series]) {
        flot_data[company][series] = [];
    }
    var dPoint = [x,y];
    flot_data[company][series].push(dPoint);
};

var underValuedCompanies = [];
var showUnderValuedCompaniesOnly = function() {
    $('.stock_info').each(function (e) {
        var module = $(this);
        var module_id = module.attr('id');

        if (underValuedCompanies.indexOf(module_id) === -1) {
            module.hide();
        }
    });
};

$(document).ready(function () {

    var shareValIndex, avgPriceIndex, headerRow, headers;
    function getNumberFromRand(rval) {
        return parseFloat(rval.replace('R','').replace(/,/g,''));
    }

    function colorNegativeBlocksRed () {
        var tds = $('td');
        tds.each(function (el) {
            var val = $(this).text();
            if (val.startsWith('R-')) {
                $(this).css('background-color', niceRed);
            }
        })

    }

    function markUnderValuedCompanies () {
        var rows;
        rows = $('tbody tr');
        rows.each(function (idx,e) {
            var avgPriceEl, shareValEl, avgPrice,shareVal;
            var row = $(this).children();

            avgPriceEl = $(row[avgPriceIndex]);
            shareValEl = $(row[shareValIndex]);
            avgPrice = getNumberFromRand(avgPriceEl.text());
            shareVal = getNumberFromRand(shareValEl.text());

            //Color in cells that are undervalued
            if (avgPrice < shareVal) {
                underValuedCompanies.push(shareValEl.parent().parent().parent().attr('id').replace('_valuation',''));
                shareValEl.css('background-color','green').
                    css('color','white');
            } else if (avgPrice > (shareVal*3)) {
                shareValEl.css('background-color', niceRed);
            }

        })
    }
	
    function populateShowReportButtons() {
	var toolsdivs = $('.company_tools');
        var boilderplate = '<button id="">Show Financial Report</button>'
	var reportdivs = $('.report_div');
	reportdivs.each(function (el) {
		var div = $(this);
		div.css('width','940px');
	});

	toolsdivs.each(function (el) {
		var tdiv = $(this);
		var but = $('<button></button>');
		but.attr('id',tdiv.attr('id') + '_report_but');
		but.text('Show Financial Report');
		but.click(function () {
			console.log('here"s a thing',$(this));
			var self = $(this);
			var ID = $(this).attr('id').replace('_tools_report_but','');
			var report_div = $('#' + ID + '_report_div');
			if (report_div.children().length > 0) {
				report_div.empty();
				report_div.hide();
				console.log('Hiding',report_div);
				$(this).text('Show Financial Report');
				return;
			}
			$.get('/report/?symbol=' + ID, function (d) {
				report_div.append(d);
				var useful_table = $(report_div.find('table')[2]);
				console.log('Table that"s getting fancy', useful_table);
				useful_table.addClass('table').addClass('table-bordered').addClass('table-striped')
				console.log('Showing',report_div);
				report_div.show();
				self.text('Hide Financial Report');
			});
		});
		tdiv.append(but);

	});
    }

    headers = $($('.valuation_table>thead')[0]).find('td');

    headers.each(function (i,e) {
                if($(e).text() === 'Share Value') {
                    shareValIndex = i;
                } else if ($(e).text() === 'Average Price') {
                    avgPriceIndex = i;
                }
            });



    colorNegativeBlocksRed();
    markUnderValuedCompanies();
    populateShowReportButtons();


    var uvButton = $('#under_valued_only');
    uvButton.button().
        click(function () {
            showUnderValuedCompaniesOnly();
        });



});
