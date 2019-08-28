var FlatmapsDialog = require('mapcoreintegratedwebapp').FlatmapsDialog;
var FlatmapsModule = require('mapcoreintegratedwebapp').FlatmapsModule;
var PlotsvyDialog = require('mapcoreintegratedwebapp').PlotsvyDialog;
var PlotsvyModule = require('mapcoreintegratedwebapp').PlotsvyModule;
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
	var mapContentPanel = document.querySelector("#mapcore_content_panel");
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
			if (organ)
				title = organ + " " + title;
			data.module.setName(title);
			tabManager.setTitle(data, title);

			return data;
		}
		return undefined;
	}
	
	var createDataViewer = function(organ,  annotation, url, channelNames) {
		if (tabManager) {
			var options = {"url":url};
			var title = annotation + "(Data)";
			var data = tabManager.createDialog("Data Viewer", options)
			if (organ)
				title = organ + " " + title;
			data.module.setName(title);
			tabManager.setTitle(data, title);
			return data;
		}
	}
	
	var createFlatmap = function(species, entry) {
		if (tabManager) {
			var data = tabManager.createDialog("Flatmap", {flatmapEntry: entry});
			var title = entry + "(Flatmap)";
			if (species)
				title = species + " " + title;
			data.module.setName(title);
			tabManager.setTitle(data, title);
		}
	}
	
	//Resize the required drawing area
	var resizeMAPDrawingArea = function() {
		var height = Math.ceil(window.innerHeight * 0.9);
		var searchContainer = document.querySelector("#mapcore_search_results_container");
		var searchContainerOptimalHeight = 860;
		var searchHeight = searchContainerOptimalHeight + (searchContainer.offsetTop - parent.offsetTop);
		if (searchHeight > height)
			height = searchHeight;
		parent.style.height = height + "px";
		var height = parent.clientHeight;
		var top = mapContent.offsetTop - parent.offsetTop;
		var contentHeight = height - top;
		mapContent.style.height = contentHeight + "px";
	}
	
	//Messages come in from various module, this method determine what to do with them
	var processMessage = function(message) {
		switch(message.action) {
		case "query-data":
			break;
		case "flatmap-show":
			if (message.resource) {
				var species = message.data ? message.data.species : undefined;
				var index = message.resource.indexOf('NCBITaxon');
				if (index > -1)
					createFlatmap(species, message.resource.slice(index));
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
				var organ = message.data ? message.data.organ : undefined;
				var annotation = message.data ? message.data.annotation : undefined;
				createDataViewer(organ, annotation, message.resource);
			}
			break;
		case "image-show":
			if (message.resource) {
				window.open(message.resource, '_blank');
			}
			break;
		default:
			break;
		}
	}

	var fullscreenToggle = function() {
		if (parent.requestFullscreen) {
			parent.requestFullscreen();
		} else if (parent.mozRequestFullScreen) { /* Firefox */
			parent.mozRequestFullScreen();
		} else if (parent.webkitRequestFullscreen) { /* Chrome, Safari and Opera */
			parent.webkitRequestFullscreen();
		} else if (parent.msRequestFullscreen) { /* IE/Edge */
			parent.msRequestFullscreen();
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
			moduleManager.addConstructor("Data Viewer", PlotsvyModule, PlotsvyDialog );
			var tabContainment = document.getElementById("maptab_container");
			tabManager = new (require('./tabmanager').TabManager)(tabContainment, moduleManager);
			if (window.location.hash !== "") {
				tabManager.processHash(window.location.hash);
			} else {
				createFlatmap("Human", "NCBITaxon:9606");
			}
		}
	}

	//initialise all required elements/objects
	var initialise = function() {
		moduleManager = new physiomeportal.ModuleManager();
		moduleManager.serialiseDiv = false;
	    moduleManager.allowStateChange = true;  
		fdikbquery = new fdi_kb_query_module(parent);
		initialiseMain();
		document.getElementById("fullscreen-button").onclick = fullscreenToggle;
		resizeMAPDrawingArea();
	}	

	initialise();

	//Resize when window size has changed
	window.onresize = function(event) {
		resizeMAPDrawingArea();
	}
}

window.document.addEventListener('DOMContentLoaded', main);
