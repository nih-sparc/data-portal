var TabData = function() {
	this.buttonElem = undefined;
	this.contentElem = undefined;
	this.textElem = undefined;
	this.module = undefined;
	this.dialog = undefined;
} 

exports.TabManager = function(containerIn, moduleManagerIn ) {
	const container = containerIn;
	const maptab = document.querySelector(".maptab");
	const contents = document.querySelector(".maptab-contents");
	const moduleManager = moduleManagerIn;
	const tabData = [];
	const _this = this;
	
	
	const toggleActiveElement = function(targetData) {
		for (let i = 0; i < tabData.length; i++) {
			let data = tabData[i];
			data.contentElem.className = data.contentElem.className.replace(" active", "");
			data.buttonElem.className = data.buttonElem.className.replace(" active", "");
		}
		targetData.contentElem.className += " active";
		targetData.buttonElem.className += " active";
	}
	
	const destroyElement = function(targetData) {
		if (targetData) {
			targetData.dialog.close();
		}
	}
	
	const addDialog = function(module) {
		let data = new TabData();
		data.contentElem = document.createElement("div");
		data.contentElem.className = "maptabcontent active";
		data.buttonElem = document.createElement("div");
		data.buttonElem.classList = "tablinks active";
		data.textElem = document.createElement("div");
		data.buttonElem.appendChild(data.textElem);
		let closeButton = document.createElement("button");
		closeButton.innerHTML = "&times;";
		closeButton.onclick = function() {destroyElement(data)};
		data.buttonElem.appendChild(closeButton);
		data.buttonElem.onclick = function() {toggleActiveElement(data)};
		return data;
	}
	
	const dialogDestroyed = function(data) {
		return function(myInstance) {
			if (data) {
				data.contentElem.parentNode.removeChild(data.contentElem);
				data.buttonElem.parentNode.removeChild(data.buttonElem);
				let index = tabData.indexOf(data);
				if (index > -1) {
					tabData.splice(index, 1);
					if (tabData.length > 0) {
						if (index == 0)
							toggleActiveElement(tabData[0]);
						else
							toggleActiveElement(tabData[index - 1]);
					}
				}
			}
		}
	}
	
	this.processHash = function(hash) {
		const parser = new (require('mapcoreintegratedwebapp').physiomeportal.FragmentParser)();
		const settings = parser.parseString(hash);
		for (let i = 0; i < settings.length; i++) {
			let setting = settings[i];
			if (setting.dialog) {
				let data = _this.createDialog(setting.dialog);
				data.module.importSettings(setting);
			}
		}
		
	}
	
	this.createDialog = function(type, options) {
		let newModule = moduleManager.createModule(type);
		if (newModule) {
			let data = addDialog(newModule);
			data.module = newModule;
			let newDialog =  moduleManager.createDialog(newModule, data.contentElem, options)
			if (newDialog) {
				newDialog.setTitle(type);
				newDialog.destroyModuleOnClose = true;
				contents.appendChild(data.contentElem);
				maptab.appendChild(data.buttonElem);
				moduleManager.manageDialog(newDialog);
				newDialog.dock();
				newDialog.showCloseButton();
				newDialog.beforeCloseCallbacks.push(dialogDestroyed(data));
				newDialog.hideTitlebar();
				data.dialog = newDialog;
				data.textElem.innerHTML = type;
				tabData.push(data);
				toggleActiveElement(data);
				return data;
			}
		}
		return undefined;
	}

}

