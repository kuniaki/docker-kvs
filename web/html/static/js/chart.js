google.charts.load('current', {'packages':['corechart']});

$('#btn-getinfo').click(function(){
    var code = $('#code').val()
    var dates = $('#start').val()
    var datee = $('#end').val()
    var countryc =  $('#country').val()
    var ds = dates.split('-'); 
    var de = datee.split('-'); 
    dates  = ds[2] + '/' +  ds[1] + '/' +  ds[0]
    datee  = de[2] + '/' +  de[1] + '/' +  de[0]
    getInfo(code,dates,datee,countryc,mainChart);
})

function getInfo(code,dates,datee,countryc,callback){
    $.ajax({
        url : '//stock.ngrok.io/api/v1/stock?code=' + code + '&country='+ countryc  + '&from_date=' + dates + '&to_date=' + datee,
        type : 'GET',       
        async : true,        
        cashe : false,     
        dataType : 'json',  
        contentType : 'application/json' 
    }).done(function(result){
        callback(result);
    }).fail(function(result){
        alert('Failed to load the information');
        console.log(result)
    });  
}

function mainChart(result){
    //チャートに描画するための最終的なデータを入れる
    var chartData = new google.visualization.DataTable();
        //日付ようにString型のカラムを一つ、チャート描画用に数値型のカラムを７つ作成
        chartData.addColumn('string');
        for(var x = 0;x < 7; x++){
            chartData.addColumn('number');
        }
        //いちいち書くのが面倒なので、取得した情報の長さを配列に入れる
        date_d = result["date"]
        var length = date_d.length;
        open_d = result["open"]
        close_d = result["close"]
        high_d = result["high"]
        low_d = result["low"]
        volume_d = result["volume"]
        //描画用のデータを一時的に入れる
        var insertingData = new Array(length);
        //平均を出すための割り算の分母
        var divide = 0;
        //二次元配列aveに、平均線の日数と平均値を入れる
        var ave = new Array();
        //５日平均線用
        ave[0] = new Array();
        //25日平均線用
        ave[1] = new Array();
        //50日平均線用
        ave[2] = new Array();
        //平均線の計算に用いる
        var temp = 0;
        //５日移動平均線の算出
        //基準日より５日前までのデータを足し合わせ、平均値を出す
        for(var m = 0; m < length - 4; m++){
            for(var n = 0; n < 5; n++){
                if(close_d[m+n] != ''){
                    temp = temp + parseFloat(close_d[m+n]);
                    divide++;
                }
            }
            ave[0][m] = temp / divide;
            temp = 0;
            divide = 0;
        }
        //2５日移動平均線の算出
        //上と同様の処理
        for(var m = 0; m < length - 24; m++){
            for(var n = 0; n < 25; n++){
                if(close_d[m+n] != ''){
                    temp = temp + parseFloat(close_d[m+n]);
                    divide++
                }
            }
            ave[1][m] = temp / divide;
            temp = 0;
            divide = 0;
        }
        //５0日移動平均線の算出
        //上と同様の処理
        for(var m = 0; m < length - 49; m++){
            for(var n = 0; n < 49; n++){
                if(close_d[m+n] != ''){
                    temp = temp + parseFloat(close_d[m+n]);
                    divide++
                }
            }
            ave[2][m] = temp / divide;
            temp = 0;
            divide = 0;
        }
        //for文をまとめるため、出来高棒グラフの処理もここで行う
        //出来高を保持する配列
        var volume = new Array();
        //チャートの日付を保持する配列
        var dates = new Array();
        for(var s = 0; s < length; s++){
            if(volume_d[s] != ''){
                volume[s] = volume_d[s];
                dates[s] = String(date_d[s]);
            }
        }
        //配列insertingDataの中に、[安値、始値、高値、終値、５日移動平均線、２５日移動平均線、５０日移動平均線]の形で値を入れ込む
        for(var a = 0; a < length; a++){
            insertingData[a] = [dates[a],parseFloat(low_d[a]),parseFloat(open_d[a]),parseFloat(close_d[a]),parseFloat(high_d[a]),ave[0][a],ave[1][a],ave[2][a]]
        }
        //チャート描画用の配列の中に、insertingDataの値を入れ込む
        //最古の50日分のデータまでは移動平均線のデータが揃っていないので、取り除く
        for (var i = insertingData.length - 50; i > 0; i--){
            chartData.addRow(insertingData[i]);
        }
        //チャートの見た目に関する記述、詳細は公式ドキュメントをご覧になってください
        var options = {
            chartArea:{left:80,top:10,right:80,bottom:10},
            colors: ['#003A76'],
            legend: {
                position: 'none',
            },
            vAxis:{
                viewWindowMode:'maximized'
            },
            hAxis: {
                format: 'yy/MM/dd',
                direction: -1,
            },
            bar: { 
                groupWidth: '100%' 
            },
            width: 1200,
            height: 400,
            lineWidth: 2,
            curveType: 'function',
            //チャートのタイプとして、ローソク足を指定
            seriesType: "candlesticks",  
            //ローソク足だでなく、線グラフも三種類表示することを記述
            series: {
                1:{
                    type: "line",
                    color: 'green',
                },
                2:{
                    type: "line",
                    color: 'red',                
                },
                3:{
                    type: "line",
                    color: 'orange',                
                },
            } 
        };
        //描画の処理
        var chart = new google.visualization.ComboChart(document.getElementById('appendMain'));
        chart.draw(chartData, options);
        //出来高棒グラフを作成する関数を呼び出し
        volumeChart(volume, dates, length);
}

function volumeChart(volume, dates, length){
    var chartData = new google.visualization.DataTable();
    //出来高の値と日付のためのカラムを作成
    chartData.addColumn('string');
    chartData.addColumn('number');
    var insertingData = new Array();
    //配列insertingDataの中に、[日付、出来高]の形式でデータを入れ込む
    for(var a = 0; a < length; a++){
        insertingData[a] = [dates[a],parseInt(volume[a])]
    }
    //insertingDataの値をチャート描画用の変数に入れ込む
    for (var i = insertingData.length - 50; i > 0; i--){
        chartData.addRow(insertingData[i]);
    }
    //ローソク足の時と同じように、見た目の設定をする
    var options = {
        chartArea:{left:80,top:10,right:80,bottom:80},
        colors: ['#003A76'],
        legend: {
            position: 'none',
        },
        bar: { 
            groupWidth: '100%' 
        },
        hAxis: {direction: -1},
        width: 1200,
        vAxis:{
            viewWindowMode:'maximized'
        },
    }
    var chart = new google.visualization.ColumnChart(document.getElementById('appendVolume'));
    chart.draw(chartData, options);
}
