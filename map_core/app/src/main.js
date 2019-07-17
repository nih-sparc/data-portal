var FlatmapsDialog = require('mapcoreintegratedwebapp').FlatmapsDialog;
var FlatmapsModule = require('mapcoreintegratedwebapp').FlatmapsModule;
var BFCSVExporterDialog = require('mapcoreintegratedwebapp').BFCSVExporterDialog;
var BFCSVExporterModule = require('mapcoreintegratedwebapp').BFCSVExporterModule;
var fdi_kb_query_module = require('fdikbquery').FDI_KB_Query_Module;
var physiomeportal = require('mapcoreintegratedwebapp').physiomeportal;
require('./css/mapcore.css');

main = function()  {
	var tabManager = undefined;
	var moduleManager = undefined;
	var UIIsReady = true;
	var nav_bar = document.querySelector(".nav");
	var parent = document.getElementById("MAPcorePortalArea");
	var mapContent = document.querySelector(".maptab-contents");
	var fdikbquery = undefined;
	var flatmapsDialog = undefined;
	var channel = undefined;
	var channelName = "sparc-mapcore-channel";
	var _this = this;
	
	var findItemWithTypeNameInManager = function(manager, typeName) {
		var items = moduleManager.getAllManagerItems();
		for (var i = 0; i < items.length; i++) {
			var module = items[i].getModule();
			if (module !== undefined && (module.typeName === typeName)) {
				return items[i];
			} 
		}
		return undefined;
	}
	
	var findModulesWithTypeNameInManager = function(manager, typeName) {
		var items = moduleManager.getAllManagerItems();
		for (var i = 0; i < items.length; i++) {
			var module = items[i].getModule();
			if (module !== undefined && (module.typeName === typeName)) {
				return module;
			} 
		}
		return undefined;
	}
	
	var createOrganViewer = function(species, organ, annotation, url) {
		if (tabManager) {
			var data = tabManager.createDialog("Organ Viewer");
			data.module.loadOrgansFromURL(url, species, organ, annotation);
			var title = annotation + "(Scaffold)";
			tabManager.setTitle(data, title);
			return data;
		}
		return undefined;
	}
	
	var createDataViewer = function(annotation, url, channelNames) {
		if (tabManager) {
			var data = tabManager.createDialog("Data Viewer");
			data.module.plotManager.openCSV(url).then(function() {
				if (channelNames) {
					for (var i = 0; i < channelNames.length; i++) {
						data.module.plotManager.plotByName(channelNames[i]);
					}
				} else {
					data.module.plotManager.plotAll();
				}
				var title = annotation + "(Data)";
				tabManager.setTitle(data, title);
			});
		}
	}
	
	var createFlatmap = function(entry) {
		if (tabManager) {
			var data = tabManager.createDialog("Flatmap", {flatmapEntry: entry});
			var title = entry + "(Flatmap)";
			tabManager.setTitle(data, title);
		}
	}
	
	//Resize the required drawing area
	var resizeMAPDrawingArea = function() {
	
		var contentHeight = window.innerHeight - document.getElementById("maptab_contents").offsetTop;
		mapContent.style.height = contentHeight + "px";
	}
	
	var processMessage = function(message) {
		switch(message.action) {
		case "query-data":
			break;
		case "flatmap-show":
			if (message.resource) {
				createFlatmap(message.resource);
			}
			break;
		case "scaffold-show":
			if (message.resource) {
				var annotation = message.data ? message.data.annotation : undefined;
				var species = message.data ? message.data.species : undefined;
				var organ = message.data ? message.data.organ : undefined;
				createOrganViewer(species, organ, annotation, message.resource);
			}
			break;
		case "data-viewer-show":
			if (message.resource) {
				var annotation = message.data ? message.data.annotation : undefined;
				createDataViewer(annotation, message.resource);
			}
			break;
		default:
			break;
		}

	}

	/**
	 * Initialise all the panels required for PJP to function correctly.
	 * Modules used include - {@link PJP.ModelsLoader}, {@link PJP.BodyViewer},
	 * {@link PJP.OrgansViewer}, {@link PJP.TissueViewer}, {@link PJP.CellPanel}
	 * and {@link PJP.ModelPanel}.
	 */
	var initialiseMain = function() {	
		if (moduleManager) {
			var channel = new (require('broadcast-channel')).default(channelName);
			channel.onmessage = processMessage;
			resizeMAPDrawingArea();
			moduleManager.addConstructor("Flatmap", FlatmapsModule, FlatmapsDialog ); 
			moduleManager.addConstructor("Data Viewer", BFCSVExporterModule, BFCSVExporterDialog );
			var tabContainment = document.getElementById("maptab_container");
			tabManager = new (require('./tabmanager').TabManager)(tabContainment, moduleManager);
			if (window.location.hash !== "") {
				tabManager.processHash(window.location.hash);
			} else {
				createFlatmap("NCBITaxon:9606");
			}
			moduleManager.serialiseDiv = false;
		    moduleManager.allowStateChange = true;   
		}
	}

	//initialise all required elements/objects
	var initialise = function() {
		moduleManager = new physiomeportal.ModuleManager();
		fdikbquery = new fdi_kb_query_module(parent);
		initialiseMain();
	}	

	initialise();

	//Resize when window size has changed
	window.onresize = function(event) {
		resizeMAPDrawingArea();
	}
}

window.document.addEventListener('DOMContentLoaded', main);
