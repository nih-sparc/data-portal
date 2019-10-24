const chariot = require('@tehsurfer/chariot-tooltips/release/chariot')
require('@tehsurfer/chariot-tooltips/release/chariot.css')
require('./css/tutorial.css')


exports.tutorial = new chariot({
    mapcore_tutorial: [
        {
            selectors: 'div#MAPcore_Banner',
            tooltip : {
                position: 'bottom',
                arrowLength: 0,
                title: 'Visualise Mapped Data tutorial',
                text: 'This 20s tutorial will show you how to navigate and view mapped data from the SPARC project'
            }
        },

      {
        selectors: 'div.mapcore-search-field-container',
        tooltip: {
          position: 'left',
          title: 'Search Field',
          text: 'Search here across all Blackfynn data plus some extra curated data. Try searching for "heart".'
        }
      },
      {
        selectors: 'div#mapcore_search_results_container',
        tooltip: {
          position: 'right',
          title: 'Navigate Results',
          text: "Resuslts from the search are displayed here. Click on a card to see an \
          extended description of the data, or hover over an icon to see how you can visualise the data"
        }
      }
    ]
  });

  