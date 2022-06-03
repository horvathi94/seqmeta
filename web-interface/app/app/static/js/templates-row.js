const FIELD_TYPES=["text","select","date","template"],REQUIREMENT_LEVELS=["exclude","optional","recommended","mandatory"],FIXED_VALUES=["sample_name","ena_checklist"];let dragSource;const ATTR_EDITOR=TEMPLATE_EDITOR.querySelector("#attr-editor");let EMPTY_ATTRIBUTE;async function fetchEmptyAttribute(){const e=await fetch("/templates/attributes?for=empty");var t=await e.json();EMPTY_ATTRIBUTE=t[0]}fetchEmptyAttribute();class EditorRow extends HTMLElement{constructor(){super(),this.cells={},0==this.children.length?this.initCells():this.readCells(),this.addEventListener("dragstart",this.handleDragStart),this.addEventListener("dragend",this.handleDragEnd),this.addEventListener("dragover",this.handleDragOver),this.addEventListener("dragenter",this.handleDragEnter),this.addEventListener("dragleave",this.handleDragLeave),this.addEventListener("drop",this.handleDrop)}connectedCallback(){Object.values(this.cells).forEach(e=>{this.appendChild(e)}),this.draggable=!0}wrapCell(e,t=[]){const l=EditorCell.create(e,t);return l.classList.add(e),l}readCells(){this.cells.removeCell=this.querySelector("editor-cell.remove"),this.cells.generalNameCell=this.querySelector("editor-cell.general_name"),this.cells.labelCell=this.querySelector("editor-cell.label"),this.cells.typeCell=this.querySelector("editor-cell.type_"),this.cells.enaCell=this.querySelector("editor-cell.ena"),this.cells.gisaidCell=this.querySelector("editor-cell.gisaid"),this.cells.paramsCell=this.querySelector("editor-cell.params"),this.cells.defaultCell=this.querySelector("editor-cell.default"),this.cells.descriptionCell=this.querySelector("editor-cell.description")}initCells(){this.cells.removeCell=this.wrapCell("remove",[this.removeButton]),this.cells.generalNameCell=this.wrapCell("general_name",[this.generalNameField,this.hasFixedNameField,this.uniqueCheck,this.mustBeUniqueField,this.isMandatoryField]),this.cells.labelCell=this.wrapCell("label",[this.labelField]),this.cells.typeCell=this.wrapCell("type_",[this.typeField]),this.cells.enaCell=this.wrapCell("ena",this.enaFields),this.cells.gisaidCell=this.wrapCell("gisaid",this.gisaidFields),this.cells.paramsCell=this.wrapCell("params",[this.paramsField]),this.cells.defaultCell=this.wrapCell("default",[this.defaultField]),this.cells.descriptionCell=this.wrapCell("description",[this.descriptionField])}get removeButton(){const e=document.createElement("input");return e.type="button",e.classList.add("rmbutton"),e.value="X",e.onclick=function(){const e=this.closest("editor-row");e.nextSibling.remove(),e.remove()},e}enableRemove(){this.cells.removeCell.querySelector(".rmbutton").disabled=!1}disableRemove(){this.cells.removeCell.querySelector(".rmbutton").disabled=!0}get isMandatoryField(){const e=document.createElement("input");return e.type="hidden",e.name=this.genName("is_mandatory"),e}get isMandatory(){return this.cells.generalNameCell.getValue("is_mandatory")}set isMandatory(e){this.cells.generalNameCell.setValue("is_mandatory",+e),e?this.disableRemove():this.enableRemove()}get uniqueCheck(){const e=document.createElement("input");return e.type="checkbox",e.name=this.genName("is_unique"),e}get mustBeUniqueField(){const e=document.createElement("input");return e.type="hidden",e.name=this.genName("must_be_unique"),e}set isUnique(e){this.cells.generalNameCell.fetchField("is_unique").checked=e}get isUnique(){return this.cells.generalNameCell.fetchField("is_unique").checked}get mustBeUnique(){return this.cells.generalNameCell.getValue("must_be_unique")}set mustBeUnique(e){const t=this.cells.generalNameCell;t.setValue("must_be_unique",+e),e&&(this.isUnique=!0,t.lockField("is_unique"))}genName(e){return`attr+${this.index}+`+e}get generalNameField(){const e=document.createElement("input");return e.type="text",e.name=this.genName("general_name"),e}get hasFixedNameField(){const e=document.createElement("input");return e.type="hidden",e.name=this.genName("has_fixed_name"),e}get labelField(){const e=document.createElement("input");return e.type="text",e.name=this.genName("label"),e}get typeField(){const e=createSelectMenu(FIELD_TYPES);return e.name=this.genName("type_"),e.onchange=function(){this.closest("editor-row").type=this.value},e}get paramsField(){let e=document.createElement("input");switch(e.type="text",this.type){case"text":e.name=this.genName("pattern"),e.placeholder="Regex for input.";break;case"select":(e=document.createElement("textarea")).name=this.genName("options"),e.placeholder="Comma separated list of options.";break;case"template":e.name=this.genName("template"),e.placeholder="Template for input.";break;case"date":case"file":e.name="junk",e.placeholder="N/A",e.disabled=!0;break;default:return void console.log("Failed to create paramters cell.")}return e.onchange=function(){this.closest("editor-row").modifiedParams(this.value)},e}get defaultField(){let e=document.createElement("input");switch(this.type){case"text":e.type="text",e.placeholder="Default value for field.";break;case"select":e=createSelectMenu(this.options);break;case"date":e.type="date";break;case"template":case"file":return e.type="text",e.name="junk",e.placeholder="N/A",e.disabled=!0,e;default:return void console.log("Failed to create default cell.")}return e.name=this.genName("default"),e}createEnaUnitsField(e=[]){let t=document.createElement("input");return t.type="text",t.name=this.genName("ena_units"),t.placeholder="ENA unit.",t.value=e.join(","),t}createRepoNameField(e){const t=document.createElement("input");return t.type="text",t.name=this.genName(e+"_name"),t.placeholder="Field name",t}createRepoReqField(e){const t=createSelectMenu(REQUIREMENT_LEVELS);return t.name=this.genName(e+"_requirement"),t.onchange=function(){this.closest("editor-row").modifiedRequirements(this.value)},t}get enaFields(){return[this.createRepoNameField("ena"),this.createRepoReqField("ena"),this.createEnaUnitsField()]}get gisaidFields(){var e=this.createRepoNameField("gisaid"),t=this.createRepoReqField("gisaid");const l=document.createElement("input");return l.type="text",l.name=this.genName("gisaid_header"),l.placeholder="GISAID first header",[e,t,l]}get descriptionField(){const e=document.createElement("textarea");return e.name=this.genName("description"),e.placeholder="Short description of the field.",e}set index(t){this.dataset.index=t,Object.values(this.cells).forEach(e=>{e.index=t})}get index(){return this.dataset.index}get generalName(){return this.cells.generalNameCell.getValue("general_name")}set generalName(e){this.cells.generalNameCell.setValue("general_name",e)}lockGeneralNameField(){this.cells.generalNameCell.lockField("general_name")}get hasFixedName(){return this.cells.generalNameCell.getValue("has_fixed_name")}set hasFixedName(e){console.log(`Setting ${this.generalName} hasFixedname: `+e),this.cells.generalNameCell.setValue("has_fixed_name",+e),e&&this.lockGeneralNameField()}get label(){return this.cells.labelCell.getValue("label")}set label(e){this.cells.labelCell.setValue("label",e)}set type(e){this.cells.typeCell.setValue("type_",e),this.cells.paramsCell.update([this.paramsField]),this.cells.defaultCell.update([this.defaultField])}get type(){return this.cells.typeCell.getValue("type_")}get options(){if("select"==this.type)return this.cells.paramsCell.getValue("options").split(",")}set options(e=[]){null!==e&&"select"==this.type&&(this.cells.paramsCell.setValue("options",e.join(",")),this.cells.defaultCell.update([this.defaultField]))}get pattern(){"text"==this.type&&this.cells.paramsCell.getValue("pattern")}set pattern(e=""){null!==e&&"text"==this.type&&(this.cells.paramsCell.setValue("pattern",e),this.cells.defaultCell.setPattern("default",e))}get template(){return this.cells.paramsCell.getValue("template")}set template(e){"template"==this.type&&null!==e&&(this.cells.paramsCell.setValue("template",e),this.verifyTemplate(this.template))}get description(){return this.cells.descriptionCell.getValue("description")}set description(e){this.cells.descriptionCell.setValue("description",e)}get maxRequirement(){const t=[];t.push(this.enaRequirement),t.push(this.gisaidRequirement);let l=REQUIREMENT_LEVELS[0];return REQUIREMENT_LEVELS.forEach(e=>{t.includes(e)&&(l=e)}),l}get enaName(){return this.cells.enaCell.getValue("ena_name")}set enaName(e){this.cells.enaCell.setValue("ena_name",e)}get enaRequirement(){return this.cells.enaCell.getValue("ena_requirement")}set enaRequirement(e){this.cells.enaCell.setValue("ena_requirement",e)}get enaUnits(){return this.cells.enaCell.getValue("ena_units").split(",")}set enaUnits(e){this.cells.enaCell.setValue("ena_units",e)}get gisaidName(){return this.cells.gisaidCell.getValue("gisaid_name")}set gisaidName(e){this.cells.gisaidCell.setValue("gisaid_name",e)}get gisaidRequirement(){return this.cells.gisaidCell.getValue("gisaid_requirement")}set gisaidRequirement(e){this.cells.gisaidCell.setValue("gisaid_requirement",e)}get gisaidHeader(){return this.cells.gisaidCell.getValue("gisaid_header")}set gisaidHeader(e){this.cells.gisaidCell.setValue("gisaid_header",e)}get default(){return this.cells.defaultCell.getValue("default")}set default(e){this.cells.defaultCell.setValue("default",e)}verifyTemplate(e){if(e){const t=parseTemplateString(e);this.cells.paramsCell.toggleInvalid("template",!1),t.filter(e=>"var"==e.type).forEach(t=>{let l=!1;TEMPLATE_EDITOR.querySelectorAll("editor-row").forEach(e=>{e.generalName==t.value&&(l=!0),FIXED_VALUES.includes(t.value)&&(l=!0)}),l||this.cells.paramsCell.toggleInvalid("template",!0)})}}modifiedParams(e){switch(this.type){case"text":this.pattern=e;break;case"select":this.options=e.split(",");break;case"template":this.verifyTemplate(e);break;case"date":case"file":break;default:return}}modifiedRequirements(){switch(this.maxRequirement){case"exclude":case"optional":case"recommended":this.enableRemove();break;case"mandatory":this.disableRemove();break;default:return}}setFromAttribute(e){this.generalName=e.general_name,this.label=e.label,this.type=e.type_,this.enaName=e.ena_name,this.enaRequirement=e.ena_requirement,this.enaUnits=e.ena_units,this.gisaidName=e.gisaid_name,this.gisaidRequirement=e.gisaid_requirement,this.gisaidHeader=e.gisaid_header,this.pattern=e.pattern,this.options=e.options,this.template=e.template,this.default=e.default,this.description=e.description,this.modifiedRequirements(),this.isMandatory=e.is_mandatory,this.hasFixedName=e.has_fixed_name,this.isUnique=e.is_unique,this.mustBeUnique=e.must_be_unique}getAttr(){const e=Object.create(EMPTY_ATTRIBUTE);return e.general_name=this.generalName,e.label=this.label,e.type_=this.type,e.description=this.description,e.ena_requirement=this.enaRequirement,e.ena_name=this.enaName,e.ena_units=this.enaUnits,e.gisaid_requirement=this.gisaidRequirement,e.gisaid_name=this.gisaidName,e.gisaid_header=this.gisaidHeader,e.pattern=this.pattern,e.options=this.options,e.default=this.default,e.has_fixed_name=this.hasFixedName,e.is_unique=this.isUnique,e.must_be_unique=this.mustBeUnique,e.is_mandatory=this.isMandatory,e}handleDragStart(e){(dragSource=this).classList.add("moving"),e.dataTransfer.effectAllowed="move"}handleDragEnd(){this.classList.remove("moving"),dragSource=null}handleDragEnter(){this.classList.add("over")}handleDragLeave(){this.classList.remove("over")}handleDragOver(e){return e.preventDefault(),!1}clearDragClasses(){this.classList.remove("moving"),this.classList.remove("over")}handleDrop(e){if(e.stopPropagation(),this===dragSource)return!1;const t=document.createElement("editor-row");return t.setFromAttribute(dragSource.getAttr()),t.index=this.index,this.index=dragSource.index,ATTR_EDITOR.replaceChild(t,this),ATTR_EDITOR.replaceChild(this,dragSource),this.clearDragClasses(),!1}}customElements.define("editor-row",EditorRow);