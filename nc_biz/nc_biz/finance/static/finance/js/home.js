// var map;
//
// $( document ).ready(function() {
//     // initMap();
//     init();
//   })



// Global container for our winner data
window.Company = {
    params: {}
};

// fetchData
function fetchData() {
    $.get("/api/")
        .done(function(config) {
            // $('#bar-chart').text(JSON.stringify(config, null, '  '));
            // Add data to global container
            window.Company.data = config;
            // Re-render the bar chart
            window.Company.bar.render();
        })
        .fail(function(){
            console.log("Could not load data");
            // alert("Could not load data");
        });
}

function init(){
  var tickSel = $('#sel-tick');
  var yrEstSel = $('#sel-yrEst');


    function updateSelections() {
        var params = window.Company.params || {};
        params.tick = tickSel.val();
        params.yrEst = yrEstSel.val();
        fetchData();
    }

    // Initialize bar chart
    initBar(window.Company);

    tickSel.on('change', updateSelections);
    yrEstSel.on('change', updateSelections);
    updateSelections();

}



$(init);

// function loadData(){
//   $.ajax({
//           type:"GET",
//           url:"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=35.8941264,-78.9133741&radius=500&type=restaurant&key=AIzaSyBdg1bcYkhdNsId5_5IoBoNX-vkZHs41KM",
//           dataType:"json",
//           success: parseData
//         });
// }
//
// function showData() {
//   $.getJSON("/static/finance/data/all_companies.json", function(json) {
//       console.log(json); // this will show the info it in firebug console
//   });
// }

  // $.getJSON("/static/finance/data/all_companies.json", function(json) {
  //     console.log(json); // this will show the info it in firebug console
  // });


// function initMap() {
//   var triangle = {lat: 35.913620, lng: -78.937204};
//   var triangleMobile = {lat: 35.932342, lng: -78.881729};
//   const mq = window.matchMedia( "(max-width: 768px)" );
//   if (mq.matches) {
//     map = new google.maps.Map(document.getElementById('map'), {
//       zoom: 10,
//       center: triangleMobile,
//       disableDefaultUI: true,
//       styles: [
//         {elementType: 'geometry', stylers: [{color: '#f5f5f5'}]},
//         {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
//         {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
//         {
//           featureType: 'administrative.locality',
//           elementType: 'labels.text.fill',
//           stylers: [{color: '#746855'}]
//         },
//         {
//           featureType: 'poi',
//           elementType: 'labels.text.fill',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'poi.park',
//           elementType: 'geometry',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'poi.park',
//           elementType: 'labels.text.fill',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'road',
//           elementType: 'geometry',
//           stylers: [{color: '#38414e'}]
//         },
//         {
//           featureType: 'road',
//           elementType: 'geometry.stroke',
//           stylers: [{color: '#212a37'}]
//         },
//         {
//           featureType: 'road',
//           elementType: 'labels.text.fill',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'road',
//           elementType: 'labels.icon',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'road.highway',
//           elementType: 'geometry',
//           stylers: [{color: '#dadada'}]
//         },
//         {
//           featureType: 'road.highway',
//           elementType: 'geometry.stroke',
//           stylers: [{color: '#1f2835'}]
//         },
//         {
//           featureType: 'road.highway',
//           elementType: 'labels.text.fill',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'road.highway',
//           elementType: 'labels.icon',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'transit',
//           elementType: 'geometry',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'transit.station',
//           elementType: 'labels.text.fill',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'water',
//           elementType: 'geometry',
//           stylers: [{color: '#c9c9c9'}]
//         },
//         {
//           featureType: 'water',
//           elementType: 'labels.text.fill',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'water',
//           elementType: 'labels.text.stroke',
//           stylers: [{color: '#9e9e9e'}]
//         }
//       ]
//     });
//   } else {
//     map = new google.maps.Map(document.getElementById('map'), {
//       zoom: 11,
//       center: triangle,
//       mapTypeControl: false,
//       styles: [
//         {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
//         {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
//         {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
//         {
//           featureType: 'administrative.locality',
//           elementType: 'labels.text.fill',
//           stylers: [{color: '#746855'}]
//         },
//         {
//           featureType: 'poi',
//           elementType: 'labels.text.fill',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'poi.park',
//           elementType: 'geometry',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'poi.park',
//           elementType: 'labels.text.fill',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'road',
//           elementType: 'geometry',
//           stylers: [{color: '#38414e'}]
//         },
//         {
//           featureType: 'road',
//           elementType: 'geometry.stroke',
//           stylers: [{color: '#212a37'}]
//         },
//         {
//           featureType: 'road',
//           elementType: 'labels.text.fill',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'road',
//           elementType: 'labels.icon',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'road.highway',
//           elementType: 'geometry',
//           stylers: [{color: '#746855'}]
//         },
//         {
//           featureType: 'road.highway',
//           elementType: 'geometry.stroke',
//           stylers: [{color: '#1f2835'}]
//         },
//         {
//           featureType: 'road.highway',
//           elementType: 'labels.text.fill',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'road.highway',
//           elementType: 'labels.icon',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'transit',
//           elementType: 'geometry',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'transit.station',
//           elementType: 'labels.text.fill',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'water',
//           elementType: 'geometry',
//           stylers: [{color: '#17263c'}]
//         },
//         {
//           featureType: 'water',
//           elementType: 'labels.text.fill',
//           stylers: [{ "visibility": "off" }]
//         },
//         {
//           featureType: 'water',
//           elementType: 'labels.text.stroke',
//           stylers: [{color: '#17263c'}]
//         }
//       ]
//     });
//
//       }
//
//     }

    // function createMarker(){
    //   var data =
    // }
