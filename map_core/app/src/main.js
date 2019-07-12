var physiomeportal = require('mapcoreintegratedwebapp').physiomeportal;
var FlatmapsDialog = require('mapcoreintegratedwebapp').FlatmapsDialog;
var FlatmapsModule = require('mapcoreintegratedwebapp').FlatmapsModule;
var BFCSVExporterDialog = require('mapcoreintegratedwebapp').BFCSVExporterDialog;
var BFCSVExporterModule = require('mapcoreintegratedwebapp').BFCSVExporterModule;

main = function()  {
	var tabManager = undefined;
	var moduleManager = undefined;
	var UIIsReady = true;
	var nav_bar = document.querySelector(".nav");
	var parent = document.getElementById("MAPcorePortalArea");
	var mapContent = document.querySelector(".maptab-contents");
	var flatmapsDialog = undefined;
	var channel = undefined;
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
	
	
	var createOrgansViewer = function(manager) {
		var data = tabManager.createDialog("Organ Viewer");
		data.module.loadOrgansFromURL("https://mapcore-bucket1.s3-us-west-2.amazonaws.com/ISAN/scaffold/stellate/stellate_metadata.json", 
			"human", "nervous", "stellate",
			"https://mapcore-bucket1.s3-us-west-2.amazonaws.com/ISAN/scaffold/stellate/stellate_view.json");
		return data;
	}
	
	var createPlotViewer = function(manager) {
		verticalSplit();
		var bfModule = new BFCSVExporterModule();
		var four = document.getElementById("four");
		var bfDialog = new BFCSVExporterDialog(bfModule, four);
		bfDialog.setTitle("Chart");
		bfDialog.destroyModuleOnClose = true;
		bfDialog.hideCloseButton();
		bfDialog.dock();
		moduleManager.manageDialog(bfDialog);
		return bfModule;
	}
	
	var selectionCallback = function(source) {
		return function(event) {
			if (event.eventType === physiomeportal.EVENT_TYPE.SELECTED) {
				if (event.identifiers.length > 0) {
					if (source === flatmapsDialog) {
						var annotation = event.identifiers[0];
						if (annotation.data.part) {
							if (annotation.data.part == "Lungs" || annotation.data.part == "Liver" || 
								(annotation.data.part == "Stellate Ganglia")) {
								var organsViewer = findModulesWithTypeNameInManager(moduleManager, "Organs Viewer");
								if (organsViewer === undefined) 
									organsViewer = createOrgansViewer();
								if (organsViewer) {
									if (annotation.data.part == "Stellate Ganglia")
										organsViewer.loadOrgansFromURL("static/stellate/stellate.json", "human", "nervous", "stellate",
											"static/stellate/stellate_view.json");
									else if (annotation.data.part == "Lungs")
										organsViewer.loadOrgans("human", "Respiratory", "Lungs");
									else if (annotation.data.part == "Liver")
										organsViewer.loadOrgans("human", "Digestive", "Liver");
								}
							}
						}
					} else if (source.typeName === "Organ Viewer") {
						var plotViewer = findModulesWithTypeNameInManager(moduleManager, "Data Viewer");
						if (plotViewer === undefined) 
							plotViewer = createPlotViewer();
						if (plotViewer)
							plotViewer.openCSV("static/Sample_1_18907001_channel_1.csv");
					}
				}
			}
		}
	}

	var resizeMAPDrawingArea = function() {
		var h = window.innerHeight;
		var myHeight = h - parent.offsetTop;
		parent.style.height = myHeight + "px";
		var contentHeight = myHeight - mapContent.offsetTop;
		mapContent.style.height = contentHeight + "px";
	}

	/**
	 * Initialise all the panels required for PJP to function correctly.
	 * Modules used incude - {@link PJP.ModelsLoader}, {@link PJP.BodyViewer},
	 * {@link PJP.OrgansViewer}, {@link PJP.TissueViewer}, {@link PJP.CellPanel}
	 * and {@link PJP.ModelPanel}.
	 */
	var initialiseMain = function() {	
		if (moduleManager) {
			resizeMAPDrawingArea();
			moduleManager.addConstructor("Flatmap", FlatmapsModule, FlatmapsDialog ); 
			moduleManager.addConstructor("Data Viewer", BFCSVExporterModule, BFCSVExporterDialog );
			var tabContainment = document.getElementById("maptab-container");
			tabManager = new (require('./tabmanager').TabManager)(tabContainment, moduleManager);
			if (window.location.hash !== "") {
				tabManager.processHash(window.location.hash);
			} else {
				var data = tabManager.createDialog("Flatmap", {flatmapEntry: "https://models.physiomeproject.org/workspace/585/rawfile/650adf9076538a4bf081609df14dabddd0eb37e7/Human_Body.pptx"});
				createOrgansViewer();
			}
			moduleManager.serialiseDiv = false;
		    moduleManager.allowStateChange = true;   
		}
	}

	var initialise = function() {
		moduleManager = new physiomeportal.ModuleManager();
		tabManager = new (require('./tabmanager').TabManager)();
		initialiseMain();
	}	

	initialise();
	
	window.onresize = function(event) {
		resizeMAPDrawingArea();
	}
}

window.document.addEventListener('DOMContentLoaded', main);