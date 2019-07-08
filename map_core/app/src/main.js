var physiomeportal = require('mapcoreintegratedwebapp').physiomeportal;
var FlatmapsDialog = require('mapcoreintegratedwebapp').FlatmapsDialog;
var FlatmapsModule = require('mapcoreintegratedwebapp').FlatmapsModule;
var BFCSVExporterDialog = require('mapcoreintegratedwebapp').BFCSVExporterDialog;
var BFCSVExporterModule = require('mapcoreintegratedwebapp').BFCSVExporterModule;
var Split = require('split.js').default;

main = function()  {
	var moduleManager = undefined;
	var UIIsReady = true;
	var nav_bar = document.querySelector(".nav");
	var parent = document.getElementById("MAPcorePortalArea");
	var flatmapsDialog = undefined;
	var channel = undefined;
	var hSplit = undefined;
	var vSplit = undefined
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
	
	var horizontalSplit = function() {
		hSplit = Split(['#one', '#two'], {
			elementStyle: (dimension, size, gutterSize) => ({
				'flex-basis': `calc(${size}% - ${gutterSize}px)`,
			}),
			gutterStyle: (dimension, gutterSize) => ({
				"border-style": "solid"
			}),
		})
	}
	
	var verticalSplit = function() {
		vSplit = Split(['#three', '#four'], {
			direction: 'vertical',
			elementStyle: (dimension, size, gutterSize) => ({
				'flex-basis': `calc(${size}% - ${gutterSize}px)`,
			}),
			gutterStyle: (dimension, gutterSize) => ({
				"cursor": 'row-resize',
				"border-style": "solid"
			}),
		})
	}
	
	var createOrgansViewer = function(manager) {
		horizontalSplit();
		var organsViewer = moduleManager.createModule("Organs Viewer");
		organsViewer.setName("Organs Viewer");
		var three = document.getElementById("three");
		var organsViewerDialog = new physiomeportal.OrgansViewerDialog(organsViewer, three);
		organsViewerDialog.hideCloseButton();
		organsViewerDialog.dock();
		organsViewerDialog.destroyModuleOnClose = true;
		moduleManager.manageDialog(organsViewerDialog);
		var eventNotifier =  new physiomeportal.EventNotifier();
		organsViewer.addNotifier(eventNotifier);
		eventNotifier.subscribe(this, selectionCallback(organsViewer));
		return organsViewer;
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
					} else if (source.typeName === "Organs Viewer") {
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
	}
	
	var updateWidgets = function() {
		var organsViewerItem = findItemWithTypeNameInManager(moduleManager, "Organs Viewer");
		var plotViewerItem = findItemWithTypeNameInManager(moduleManager, "Data Viewer");
		if (!organsViewerItem) {
			if (hSplit) {
				hSplit.destroy();
				hSplit = undefined;
			}
		}
		else {
			if (!hSplit) {
				horizontalSplit();
			}
			var module = organsViewerItem.getModule();
			var dialog = organsViewerItem.getDialog();
			dialog.destroyModuleOnClose = true;
			if (module.eventNotifiers.length == 0) {
				var eventNotifier =  new physiomeportal.EventNotifier();
				module.addNotifier(eventNotifier);
				eventNotifier.subscribe(this, selectionCallback(module));
			}
		}
		if (!plotViewerItem) {
			if (vSplit) {
				vSplit.destroy();
				vSplit = undefined;
			}
		}
		else {
			if (!vSplit) {
				verticalSplit();
			}
			var module = plotViewerItem.getModule();
			var dialog = plotViewerItem.getDialog();
			dialog.destroyModuleOnClose = true;
			if (module.eventNotifiers.length == 0) {
				var eventNotifier =  new physiomeportal.EventNotifier();
				module.addNotifier(eventNotifier);
				eventNotifier.subscribe(this, selectionCallback(module));
			}
		}
	}
	
	/**
		Process the hash
	 */
	var processHash = function() {
		moduleManager.deserialise(window.location.hash);
		// Then create or destory split
		updateWidgets();
	}

	/**
	 * Initialise all the panels required for PJP to function correctly.
	 * Modules used incude - {@link PJP.ModelsLoader}, {@link PJP.BodyViewer},
	 * {@link PJP.OrgansViewer}, {@link PJP.TissueViewer}, {@link PJP.CellPanel}
	 * and {@link PJP.ModelPanel}.
	 */
	var initialiseMain = function() {	
		if (moduleManager) {
			moduleManager.addConstructor("Flatmaps", FlatmapsModule, FlatmapsDialog ); 
			moduleManager.addConstructor("Data Viewer", BFCSVExporterModule, BFCSVExporterDialog );
			resizeMAPDrawingArea();
			var one = document.getElementById("one");
			var module = new FlatmapsModule();
			flatmapsDialog = new FlatmapsDialog(module, one, {flatmapEntry: "https://models.physiomeproject.org/workspace/585/rawfile/650adf9076538a4bf081609df14dabddd0eb37e7/Human_Body.pptx"});
			var eventNotifier =  new physiomeportal.EventNotifier();
			module.setName("Flatmaps");
			flatmapsDialog.setTitle("Flatmaps");
			flatmapsDialog.destroyModuleOnClose = true;
			flatmapsDialog.addNotifier(eventNotifier);
			flatmapsDialog.hideCloseButton();
			flatmapsDialog.dock();
			eventNotifier.subscribe(this, selectionCallback(flatmapsDialog));
			flatmapsDialog.initaliseBroadcastCallback();
			moduleManager.manageDialog(flatmapsDialog);
		    if (window.location.hash !== "") {
		    	processHash();
			}
		    moduleManager.allowStateChange = true;   
		}
	}

	var initialise = function() {
		moduleManager = new physiomeportal.ModuleManager();
		initialiseMain();
	}	

	initialise();
	
	window.onresize = function(event) {
		resizeMAPDrawingArea();
	}
}

window.document.addEventListener('DOMContentLoaded', main);