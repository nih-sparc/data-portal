let FlatmapsDialog = require('mapcoreintegratedwebapp').FlatmapsDialog;
let FlatmapsModule = require('mapcoreintegratedwebapp').FlatmapsModule;
let BFCSVExporterDialog = require('mapcoreintegratedwebapp').BFCSVExporterDialog;
let BFCSVExporterModule = require('mapcoreintegratedwebapp').BFCSVExporterModule;
let SimulationDialog = require('mapcoreintegratedwebapp').SimulationDialog;
let SimulationModule = require('mapcoreintegratedwebapp').SimulationModule;
let fdi_kb_query_module = require('fdikbquery').FDI_KB_Query_Module;
let physiomeportal = require('mapcoreintegratedwebapp').physiomeportal;
require('./css/mapcore.css');

main = function () {
  let tabManager = undefined;
  let moduleManager = undefined;
  let parent = document.getElementById("MAPcorePortalArea");
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

  let createOrganViewer = function (species, organ, annotation, url) {
    if (tabManager) {
      let data = tabManager.createDialog("Organ Viewer");
      data.module.loadOrgansFromURL(url, species, organ, annotation);
      let title = annotation + "(Scaffold)";
      if (organ)
        title = organ + " " + title;
      data.module.setName(title);
      tabManager.setTitle(data, title);

      return data;
    }
    return undefined;
  };

  let createDataViewer = function (organ, annotation, url, channelNames) {
    if (tabManager) {
      let data = tabManager.createDialog("Data Viewer");
      let title = annotation + "(Data)";
      if (organ)
        title = organ + " " + title;
      data.module.setName(title);
      tabManager.setTitle(data, title);
      data.module.plotManager.openCSV(url).then(function () {
        if (channelNames) {
          for (let i = 0; i < channelNames.length; i++) {
            data.module.plotManager.plotByName(channelNames[i]);
          }
        }
      });
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
  let resizeMAPDrawingArea = function () {
    let contentHeight = window.innerHeight - document.getElementById("maptab_contents").offsetTop;
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
          window.open(message.resource, '_blank');
        }
        break;
      case "simulation-show":
        if (message.resource) {
          console.log(message.resource);
          console.log(message.data);
          createSimulationViewer(message.data['simulation_name'], message.resource)
        }
        break;
      default:
        break;
    }

  };

  /**
   * Initialise all the panels required for PJP to function correctly.
   * Modules used include - {@link PJP.ModelsLoader}, {@link PJP.BodyViewer},
   * {@link PJP.OrgansViewer}, {@link PJP.TissueViewer}, {@link PJP.CellPanel}
   * and {@link PJP.ModelPanel}.
   */
  let initialiseMain = function () {
    if (moduleManager) {
      let channel = new (require('broadcast-channel')).default(channelName);
      channel.onmessage = processMessage;
      resizeMAPDrawingArea();
      moduleManager.addConstructor("Flatmap", FlatmapsModule, FlatmapsDialog);
      moduleManager.addConstructor("Data Viewer", BFCSVExporterModule, BFCSVExporterDialog);
      moduleManager.addConstructor("Simulation Interface", SimulationModule, SimulationDialog);
      let tabContainment = document.getElementById("maptab_container");
      tabManager = new (require('./tabmanager').TabManager)(tabContainment, moduleManager);
      if (window.location.hash !== "") {
        tabManager.processHash(window.location.hash);
      } else {
        createFlatmap("Human", "NCBITaxon:9606");
      }
    }
  };

  //initialise all required elements/objects
  let initialise = function () {
    moduleManager = new physiomeportal.ModuleManager();
    moduleManager.serialiseDiv = false;
    moduleManager.allowStateChange = true;
    fdikbquery = new fdi_kb_query_module(parent);
    initialiseMain()
  };

  initialise();

  //Resize when window size has changed
  window.onresize = function (event) {
    resizeMAPDrawingArea();
  }
};

window.document.addEventListener('DOMContentLoaded', main);
