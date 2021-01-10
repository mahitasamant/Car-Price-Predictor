function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");

    var wheelbase = document.getElementById("wheelbasemetre");
    var CarName = document.getElementById("uiCarName");
    var carlength = document.getElementById("carlengthmetre");
    var carwidth = document.getElementById("carwidthmetre"); 
    var carheight = document.getElementById("carheight");  
    var  curbweight = document.getElementById("weightkilo");  
    var  cylindernumber = document.getElementById("cylindernumber"); 
    var  enginesize = document.getElementById("enginesizecc");   
    var  horsepower = document.getElementById("horsepoweruni");   
    var   peakrpm= document.getElementById("peakrpmunit");   
    var  citympg = document.getElementById("citympgunit"); 
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/estimate_price"; 
    
  
    $.post(url, {
        wheelbase: parseFloat(wheelbase.value),
        carlength: parseFloat(carlength.value),
        carheight: parseFloat(carheight.value),
        carwidth: parseFloat(carwidth.value),
        curbweight: parseFloat(curbweight.value),
        cylindernumber: parseFloat(cylindernumber.value),
        enginesize: parseFloat(enginesize.value),
        horsepower: parseFloat(horsepower.value),
        peakrpm: parseFloat(peakrpm.value),
        citympg: parseFloat(citympg.value),
        
        CarName: CarName.value
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString()/10 + " dollars</h2>";
        console.log(status);
    });
  }
function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_brand_names"; 
    $.get(url,function(data, status) {
        console.log("got response for get_brand_names request");
        if(data) {
            var CarName = data.CarName;
            var uiCarName = document.getElementById("uiCarName");
            $('#uiCarName').empty();
            for(var i in CarName) {
                var opt = new Option(CarName[i]);
                $('#uiCarName').append(opt);
            }
        }
    });
  }
  
  window.onload = onPageLoad;