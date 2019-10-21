const mapapp = undefined;
require('./css/mapcore.css');

let main = function () {
  let tabManager = undefined;
  let moduleManager = undefined;
  let parent = document.getElementById("MAPcorePortalArea");
	let fullscreenButton = document.getElementById("fullscreen-button");
  let mapContent = document.querySelector(".maptab-contents");
  let fdikbquery = undefined;
  let channelName = "sparc-mapcore-channel";

  let findItemWithTypeNameInManager = function (manager, typeName) {
    let items = moduleManager.getAllManagerItems();
    for (let i = 0; i < items.length; i++) {
      let module = items[i].getModule();
      if (module !== undefined && (module.typeName === typeName)) {
        return items[i];
      }
    }
    return undefined;
  };

  let findModulesWithTypeNameInManager = function (manager, typeName) {
    let items = moduleManager.getAllManagerItems();
    for (let i = 0; i < items.length; i++) {
      let module = items[i].getModule();
      if (module !== undefined && (module.typeName === typeName)) {
        return module;
      }
    }
    return undefined;
  };

	let upperCaseFirstLetter = function(source) {
		let firstLetter = source.charAt(0).toUpperCase();
		return firstLetter + source.slice(1);
	};

	let createOrganViewer = function (species, organ, annotation, url) {
    if (tabManager) {
      let data = tabManager.createDialog("Organ Viewer");
      data.module.loadOrgansFromURL(url, species, organ, annotation);
      let title = annotation + "(Scaffold)";
      if (organ)
        title = organ + " " + title;
			title = upperCaseFirstLetter(title);
      data.module.setName(title);
      tabManager.setTitle(data, title);

      return data;
    }
    return undefined;
  };

  let createDataViewer = function (organ, annotation, url, channelNames) {
    if (tabManager) {
      let options = {"url":url};
      let data = tabManager.createDialog("Data Viewer", options);
      let title = annotation + "(Data)";
      if (organ)
        title = organ + " " + title;
			title = upperCaseFirstLetter(title);
			data.module.setName(title);
			tabManager.setTitle(data, title);
      return data;
    }
  };

  let createSimulationViewer = function (simulation_name, options) {
    if (tabManager) {
      let data = tabManager.createDialog("Simulation Interface", options);
      let title = simulation_name + "(Simulation)";
      tabManager.setTitle(data, title);
      return data;
    }
  };

  let createBiolucidaViewer = function (tab_name, options) {
    if (tabManager) {
      let data = tabManager.createDialog("Biolucida Interface", options);
      let truncated_tab_name = (tab_name.length > 21) ? tab_name.substr(0, 17) + '&hellip;': tab_name;
      let title = truncated_tab_name + "(Image)";
      tabManager.setTitle(data, title);
      return data;
    }
  };

  let createFlatmap = function (species, entry) {
    if (tabManager) {
      let data = tabManager.createDialog("Flatmap", {flatmapEntry: entry});
      let title = entry + "(Flatmap)";
      if (species)
        title = species + " " + title;
      data.module.setName(title);
      tabManager.setTitle(data, title);
    }
  };

  //Resize the required drawing area
	let resizeMAPDrawingArea = function() {
		let height = Math.ceil(window.innerHeight * 0.9);
		let searchContainer = document.querySelector("#mapcore_search_results_container");
		let searchContainerOptimalHeight = 860;
		let searchHeight = searchContainerOptimalHeight + (searchContainer.offsetTop - parent.offsetTop);
		if (searchHeight > height)
			height = searchHeight;
		parent.style.height = height + "px";
		height = parent.clientHeight;
		let top = mapContent.offsetTop - parent.offsetTop;
		let contentHeight = height - top;
		mapContent.style.height = contentHeight + "px";
	};

	//Messages come in from letious module, this method determine what to do with them
  let processMessage = function (message) {
    switch (message.action) {
      case "query-data":
        break;
      case "flatmap-show":
        if (message.resource) {
          let species = message.data ? message.data.species : undefined;
          let index = message.resource.indexOf('NCBITaxon');
          if (index > -1)
            createFlatmap(species, message.resource.slice(index));
        }
        break;
      case "scaffold-show":
        if (message.resource) {
          let annotation = message.data ? message.data.annotation : undefined;
          let species = message.data ? message.data.species : undefined;
          let organ = message.data ? message.data.organ : undefined;
          createOrganViewer(species, organ, annotation, message.resource);
        }
        break;
      case "data-viewer-show":
        if (message.resource) {
          let organ = message.data ? message.data.organ : undefined;
          let annotation = message.data ? message.data.annotation : undefined;
          createDataViewer(organ, annotation, message.resource);
        }
        break;
      case "image-show":
        if (message.resource) {
          createBiolucidaViewer(message.data['Title'], message.resource)
          // window.open(message.resource, '_blank');
        }
        break;
      case "simulation-show":
        if (message.resource) {
          createSimulationViewer(message.data['simulation_name'], message.resource)
        }
        break;
      default:
        break;
    }

  };

	let fullscreenToggle = function() {
		if (document.fullscreenElement || document.webkitFullscreenElement ||
			document.mozFullScreenElement || document.msFullscreenElement ) {
			if (document.exitFullscreen) {
				document.exitFullscreen();
			} else if (document.mozCancelFullScreen) { /* Firefox */
				document.mozCancelFullScreen();
			} else if (document.webkitExitFullscreen) { /* Chrome, Safari and Opera */
				document.webkitExitFullscreen();
			} else if (document.msExitFullscreen) { /* IE/Edge */
				document.msExitFullscreen();
			}
			fullscreenButton.innerHTML = "Fullscreen";
		} else {
			if (parent.requestFullscreen) {
				parent.requestFullscreen();
			} else if (parent.mozRequestFullScreen) { /* Firefox */
				parent.mozRequestFullScreen();
			} else if (parent.webkitRequestFullscreen) { /* Chrome, Safari and Opera */
				parent.webkitRequestFullscreen();
			} else if (parent.msRequestFullscreen) { /* IE/Edge */
				parent.msRequestFullscreen();
			}
			fullscreenButton.innerHTML = "Exit Fullscreen";
		}
	};

	const reopenDefaultDialog = function() {
		createFlatmap("Human", "NCBITaxon:9606");
  };
  
  const switchBackgroundContent = function() {
    let target = document.querySelector(".overlay-page");
    target.style.display = "none";
    target = document.querySelector("#background-message");
    target.style.display = "block";
  }

	/**
   * Initialise all the panels required for PJP to function correctly.
   * Modules used include - {@link PJP.ModelsLoader}, {@link PJP.BodyViewer},
   * {@link PJP.OrgansViewer}, {@link PJP.TissueViewer}, {@link PJP.CellPanel}
   * and {@link PJP.ModelPanel}.
   */
  let initialiseMain = function (maplibIn) {
    maplib = maplibIn;
    moduleManager = new maplib.physiomeportal.ModuleManager();
    moduleManager.serialiseDiv = false;
    moduleManager.allowStateChange = true;
    if (moduleManager) {
      let channel = new (require('broadcast-channel')).default(channelName);
      channel.onmessage = processMessage;
      resizeMAPDrawingArea();
      moduleManager.addConstructor("Flatmap", maplib.FlatmapsModule, maplib.FlatmapsDialog);
      moduleManager.addConstructor("Data Viewer", maplib.PlotsvyModule, maplib.PlotsvyDialog);
      moduleManager.addConstructor("Simulation Interface", maplib.SimulationModule, maplib.SimulationDialog);
      moduleManager.addConstructor("Biolucida Interface", maplib.BiolucidaModule, maplib.BiolucidaDialog);
      let tabContainment = document.getElementById("maptab_container");
      tabManager = new (require('./tabmanager').TabManager)(tabContainment, moduleManager);
      switchBackgroundContent();
      if (window.location.hash !== "") {
        tabManager.processHash(window.location.hash);
      } else {
        reopenDefaultDialog();
      }
    }
  };

  let preloadQuery = function() {
    return import(/* webpackPreload: true */
      /* webpackChunkName: "fdikbquery" */
      'fdikbquery').then(({ default: fdi_kb_query_module }) => {
      fdikbquery = new fdi_kb_query_module.FDI_KB_Query_Module(parent);
      return;
    });
  }

  let preloadMAP = function() {
    return import(/* webpackPreload: true */
      /* webpackChunkName: "map" */
      'mapcoreintegratedwebapp').then(({ default: maplib }) => {
      return maplib;
    });
  }

	var hasVisted = function () {
		return localStorage.getItem('hasVisitedMaps');
	}

  // startTutorial imports tutorial.js then runs the chariot.js tutorial
	var startTutorial = function () {
    import(/* webpackPreload: true */
      /* webpackChunkName: "tutorial" */
      './tutorial').then(({ default: tut }) => {
        tut.tutorial.startTutorial('mapcore_tutorial');
        localStorage.setItem('hasVisitedMaps', true);
      })
	}

  //initialise all required elements/objects
  let initialise = function () {
    preloadQuery().then(() => {
      let target = document.querySelector("#loading-message");
      target.innerHTML = "Search engine loaded successfully...";
      preloadMAP().then(maplibIn => {
        initialiseMain(maplibIn);
        document.getElementById("fullscreen-button").onclick = fullscreenToggle;
        document.getElementById("reopen").onclick = reopenDefaultDialog;
        resizeMAPDrawingArea();
      });
    });
    if (hasVisted() === null || hasVisted() === false){
      startTutorial()
    }
	};

  initialise();

  //Resize when window size has changed
  window.onresize = function (event) {
    resizeMAPDrawingArea();
  }
};

window.document.addEventListener('DOMContentLoaded', main);
