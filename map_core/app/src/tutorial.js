const chariot = require('@tehsurfer/chariot-tooltips/release/chariot')
require('@tehsurfer/chariot-tooltips/release/chariot.css')
require('./css/tutorial.css')


exports.tutorial = new chariot({
    mapcore_tutorial: [
        {
            selectors: 'div#MAPcore_Banner',
            tooltip : {
                position: 'bottom',
                title: 'Visualise Maps tutorial',
                text: 'This 20s tutorial will show how to navigate and view mapped data'
            }
        },

      {
        selectors: 'div.mapcore-search-field-container',
        tooltip: {
          position: 'left',
          title: 'Search Field',
          text: 'Search terms in all Blackfynn data plus some extra curated data. Try searching for "heart".'
        }
      },
      {
        selectors: 'div#mapcore_search_results_container',
        tooltip: {
          position: 'right',
          title: 'Navigate Results',
          text: "Resuslts from the the search are displayed here. Click on a card to see an \
          extended description of the data, or hover over an icon to see "
        }
      }
    ]
  });

  