const FIELD_TYPES=["text","select","date","template","file"],REQUIREMENT_LEVELS=["exclude","optional","recommended","mandatory"],FIXED_VALUES=["sample_name","ena_checklist"];let dragSource;const ATTR_EDITOR=document.querySelector("template-editor > #attr-editor");ATTRIBUTE={general_name:"",label:"",type_:"text",description:"",ena_requirement:"exclude",ena_name:"",ena_units:[],gisaid_requirement:"exclude",gisaid_name:"",gisaid_header:"",pattern:"",options:[],default:""};class EditorRow extends HTMLElement{constructor(){super(),this.cells={},0==this.children.length?this.initCells():this.readCells(),this.addEventListener("dragstart",this.handleDragStart),this.addEventListener("dragend",this.handleDragEnd),this.addEventListener("dragover",this.handleDragOver),this.addEventListener("dragenter",this.handleDragEnter),this.addEventListener("dragleave",this.handleDragLeave),this.addEventListener("drop",this.handleDrop)}connectedCallback(){Object.values(this.cells).forEach(e=>{this.appendChild(e)}),this.draggable=!0}wrapCell(e,t=[]){const l=EditorCell.create(e,t);return l.classList.add(e),l}readCells(){this.cells.removeCell=this.querySelector("editor-cell.remove"),this.cells.generalNameCell=this.querySelector("editor-cell.general_name"),this.cells.labelCell=this.querySelector("editor-cell.label"),this.cells.typeCell=this.querySelector("editor-cell.type_"),this.cells.enaCell=this.querySelector("editor-cell.ena"),this.cells.gisaidCell=this.querySelector("editor-cell.gisaid"),this.cells.paramsCell=this.querySelector("editor-cell.params"),this.cells.defaultCell=this.querySelector("editor-cell.default"),this.cells.descriptionCell=this.querySelector("editor-cell.description")}initCells(){this.cells.removeCell=this.wrapCell("remove",[this.removeButton]),this.cells.generalNameCell=this.wrapCell("general_name",[this.generalNameField]),this.cells.labelCell=this.wrapCell("label",[this.labelField]),this.cells.typeCell=this.wrapCell("type_",[this.typeField]),this.cells.enaCell=this.wrapCell("ena",this.enaFields),this.cells.gisaidCell=this.wrapCell("gisaid",this.gisaidFields),this.cells.paramsCell=this.wrapCell("params",[this.paramsField]),this.cells.defaultCell=this.wrapCell("default",[this.defaultField]),this.cells.descriptionCell=this.wrapCell("description",[this.descriptionField])}get removeButton(){const e=document.createElement("input");return e.type="button",e.classList.add("rmbutton"),e.value="X",e.onclick=function(){this.closest("padded-row").remove()},e}genName(e){return`attr+${this.index}+`+e}get generalNameField(){return new TextField(this.genName("general_name")).input}get labelField(){return new TextField(this.genName("label")).input}get typeField(){const e=new SelectField(this.genName("type_"),FIELD_TYPES);return e.input.onchange=function(){this.closest("attr-row").type=this.value},e.input}get paramsField(){let e;switch(this.type){case"text":(e=new TextField(this.genName("pattern"))).input.placeholder="Regex for input.";break;case"select":(e=new TextAreaField(this.genName("options"))).input.placeholder="Comma separated list of options.";break;case"template":(e=new TextField(this.genName("template"))).input.placeholder="Template for input.";break;case"date":case"file":(e=new TextField(name="junk")).input.placeholder="N/A",e.input.disabled=!0;break;default:return void console.log("Failed to create paramters cell.")}return e.input.onchange=function(){this.closest("attr-row").modifiedParams(this.value)},e.input}get defaultField(){let e;var t=this.genName("default");switch(this.type){case"text":(e=new TextField(t)).input.placeholder="Default value for field.";break;case"select":e=new SelectField(t,this.options);break;case"date":e=new DateField(t);break;case"template":case"file":(e=new TextField("junk")).input.placeholder="N/A",e.input.disabled=!0;break;default:return void console.log("Failed to create default cell.")}return e.input}createEnaUnitsField(e=[]){var t=this.genName("ena_units");let l;return 0==e.length?(l=new TextField(t)).input.placeholder="ENA unit.":l=new SelectField(t,options=e),l}get enaFields(){const e=new TextField(this.genName("ena_name")),t=(e.input.placeholder="ENA Checklist name.",new SelectField(this.genName("ena_requirement"),REQUIREMENT_LEVELS));t.input.onchange=function(){this.closest("attr-row").modifiedRequirements(this.value)};var l=this.createEnaUnitsField();return[e.input,t.input,l.input]}get gisaidFields(){const e=new TextField(this.genName("gisaid_name")),t=(e.input.placeholder="GISAID 2 row",new SelectField(this.genName("gisaid_requirement"),REQUIREMENT_LEVELS)),l=(t.input.onchange=function(){this.closest("attr-row").modifiedRequirements(this.value)},new TextField(this.genName("gisaid_header")));return l.input.placeholder="GISAID header.",[e.input,t.input,l.input]}get descriptionField(){const e=new TextAreaField(this.genName("description"));return e.input.placeholder="Short description of the field.",e.input}set index(t){this.dataset.index=t,Object.values(this.cells).forEach(e=>{e.index=t})}get index(){return this.dataset.index}get generalName(){return this.cells.generalNameCell.getValue("general_name")}set generalName(e){this.cells.generalNameCell.setValue("general_name",e)}set label(e){this.cells.labelCell.setValue("label",e)}set type(e){this.cells.typeCell.setValue("type_",e),this.cells.paramsCell.update([this.paramsField]),this.cells.defaultCell.update([this.defaultField])}get type(){return this.cells.typeCell.getValue("type_")}get options(){if("select"==this.type)return this.cells.paramsCell.getValue("options").split(",")}set options(e=[]){null!==e&&"select"==this.type&&(this.cells.paramsCell.setValue("options",e.join(",")),this.cells.defaultCell.update([this.defaultField]))}get pattern(){"text"==this.type&&this.cells.paramsCell.getValue("pattern")}set pattern(e=""){null!==e&&"text"==this.type&&(this.cells.paramsCell.setValue("pattern",e),this.cells.defaultCell.setPattern("default",e))}set description(e){this.cells.descriptionCell.setValue("description",e)}get maxRequirement(){const t=[];t.push(this.enaRequirement),t.push(this.gisaidRequirement);let l=REQUIREMENT_LEVELS[0];return REQUIREMENT_LEVELS.forEach(e=>{t.includes(e)&&(l=e)}),l}set enaName(e){this.cells.enaCell.setValue("ena_name",e)}get enaRequirement(){return this.cells.enaCell.getValue("ena_requirement")}set enaRequirement(e){this.cells.enaCell.setValue("ena_requirement",e)}set enaUnits(e){this.cells.enaCell.setValue("ena_units",e)}set gisaidName(e){this.cells.gisaidCell.setValue("gisaid_name",e)}get gisaidRequirement(){return this.cells.gisaidCell.getValue("gisaid_requirement")}set gisaidRequirement(e){this.cells.gisaidCell.setValue("gisaid_requirement",e)}set gisaidHeader(e){this.cells.gisaidCell.setValue("gisaid_header",e)}set default(e){this.cells.defaultCell.setValue("default",e)}verifyTemplate(e){const t=parseTemplateString(e);this.cells.paramsCell.toggleInvalid("template",!1),t.filter(e=>"var"==e.type).forEach(t=>{let l=!1;TEMPLATE_EDITOR.querySelectorAll("padded-row > attr-row").forEach(e=>{e.generalName==t.value&&(l=!0),FIXED_VALUES.includes(t.value)&&(l=!0)}),l||this.cells.paramsCell.toggleInvalid("template",!0)})}modifiedParams(e){switch(this.type){case"text":this.pattern=e;break;case"select":this.options=e.split(",");break;case"template":this.verifyTemplate(e);break;case"date":case"file":break;default:return}}modifiedRequirements(){switch(this.maxRequirement){case"exclude":case"optional":case"recommended":this.cells.removeCell.querySelector(".rmbutton").disabled=!1;break;case"mandatory":this.cells.removeCell.querySelector(".rmbutton").disabled=!0;break;default:return}}setFromAttribute(e){this.generalName=e.general_name,this.label=e.label,this.type=e.type_,this.enaName=e.ena_name,this.enaRequirement=e.ena_requirement,this.enaUnits=e.ena_units,this.gisaidName=e.gisaid_name,this.gisaidRequirement=e.gisaid_requirement,this.gisaidHeader=e.gisaid_header,this.pattern=e.pattern,this.options=e.options,this.template=e.template,this.default=e.default,this.description=e.description,this.modifiedRequirements()}handleDragStart(e){(dragSource=this).classList.add("moving"),e.dataTransfer.effectAllowed="move"}handleDragEnd(){this.classList.remove("moving"),dragSource=null}handleDragEnter(){this.classList.add("over")}handleDragLeave(){this.classList.remove("over")}handleDragOver(e){return e.preventDefault(),!1}clearDragClasses(){this.classList.remove("moving"),this.classList.remove("over")}handleDrop(e){if(e.stopPropagation(),this===dragSource)return!1;const t=dragSource.cloneNode(!0);return t.clearDragClasses(),t.index=this.index,this.index=dragSource.index,ATTR_EDITOR.replaceChild(t,this),ATTR_EDITOR.replaceChild(this,dragSource),this.clearDragClasses(),!1}}customElements.define("editor-row",EditorRow);