const TEMPLATE_EDITOR=document.querySelector("#template-editor"),FIELD_TYPES=["text","select","date","template","file"],REQUIREMENT_LEVELS=["exclude","optional","recommended","mandatory"],FIXED_VALUES=["sample_name","ena_checklist"],TEMPLATE_NAME=document.querySelector("#template-name-field").value;ATTRIBUTE={general_name:"",label:"",type_:"text",description:"",ena_requirement:"exclude",ena_name:"",ena_units:[],gisaid_requirement:"exclude",gisaid_name:"",gisaid_header:"",pattern:"",options:[],default:""};class AttrRow extends HTMLElement{constructor(){super(),this.cells={},0==this.children.length?this.initCells():this.readCells()}wrapCell(e,t=[]){const l=AttrCell.create(e,t);return l.classList.add(e),l}readCells(){this.cells.removeCell=this.querySelector("attr-cell.remove"),this.cells.generalNameCell=this.querySelector("attr-cell.general_name"),this.cells.labelCell=this.querySelector("attr-cell.label"),this.cells.typeCell=this.querySelector("attr-cell.type_"),this.cells.enaCell=this.querySelector("attr-cell.ena"),this.cells.gisaidCell=this.querySelector("attr-cell.gisaid"),this.cells.paramsCell=this.querySelector("attr-cell.params"),this.cells.defaultCell=this.querySelector("attr-cell.default"),this.cells.descriptionCell=this.querySelector("attr-cell.description")}initCells(){this.cells.removeCell=this.wrapCell("remove",[this.removeButton]),this.cells.generalNameCell=this.wrapCell("general_name",[this.generalNameField]),this.cells.labelCell=this.wrapCell("label",[this.labelField]),this.cells.typeCell=this.wrapCell("type_",[this.typeField]),this.cells.enaCell=this.wrapCell("ena",this.enaFields),this.cells.gisaidCell=this.wrapCell("gisaid",this.gisaidFields),this.cells.paramsCell=this.wrapCell("params",[this.paramsField]),this.cells.defaultCell=this.wrapCell("default",[this.defaultField]),this.cells.descriptionCell=this.wrapCell("description",[this.descriptionField])}get removeButton(){const e=document.createElement("input");return e.type="button",e.classList.add("rmbutton"),e.value="X",e.onclick=function(){this.closest("padded-row").remove()},e}genName(e){return`attr+${this.index}+`+e}get generalNameField(){return new TextField(this.genName("general_name")).input}get labelField(){return new TextField(this.genName("label")).input}get typeField(){const e=new SelectField(this.genName("type_"),FIELD_TYPES);return e.input.onchange=function(){this.closest("attr-row").type=this.value},e.input}get paramsField(){let e;switch(this.type){case"text":(e=new TextField(this.genName("pattern"))).input.placeholder="Regex for input.";break;case"select":(e=new TextAreaField(this.genName("options"))).input.placeholder="Comma separated list of options.";break;case"template":(e=new TextField(this.genName("template"))).input.placeholder="Template for input.";break;case"date":case"file":(e=new TextField(name="junk")).input.placeholder="N/A",e.input.disabled=!0;break;default:return void console.log("Failed to create paramters cell.")}return e.input.onchange=function(){this.closest("attr-row").modifiedParams(this.value)},e.input}get defaultField(){let e;var t=this.genName("default");switch(this.type){case"text":(e=new TextField(t)).input.placeholder="Default value for field.";break;case"select":e=new SelectField(t,this.options);break;case"date":e=new DateField(t);break;case"template":case"file":(e=new TextField("junk")).input.placeholder="N/A",e.input.disabled=!0;break;default:return void console.log("Failed to create default cell.")}return e.input}createEnaUnitsField(e=[]){var t=this.genName("ena_units");let l;return 0==e.length?(l=new TextField(t)).input.placeholder="ENA unit.":l=new SelectField(t,options=e),l}get enaFields(){const e=new TextField(this.genName("ena_name"));e.input.placeholder="ENA Checklist name.";var t=new SelectField(this.genName("ena_requirement"),REQUIREMENT_LEVELS),l=this.createEnaUnitsField();return[e.input,t.input,l.input]}get gisaidFields(){const e=new TextField(this.genName("gisaid_name"));e.input.placeholder="GISAID 2 row";var t=new SelectField(this.genName("gisaid_requirement"),REQUIREMENT_LEVELS);const l=new TextField(this.genName("gisaid_header"));return l.input.placeholder="GISAID header.",[e.input,t.input,l.input]}get descriptionField(){const e=new TextAreaField(this.genName("description"));return e.input.placeholder="Short description of the field.",e.input}connectedCallback(){Object.values(this.cells).forEach(e=>{this.appendChild(e)})}set index(t){this.dataset.index=t,Object.values(this.cells).forEach(e=>{e.index=t})}get index(){return this.dataset.index}get generalName(){return this.cells.generalNameCell.getValue("general_name")}set generalName(e){this.cells.generalNameCell.setValue("general_name",e)}set label(e){this.cells.labelCell.setValue("label",e)}set type(e){this.cells.typeCell.setValue("type_",e),this.cells.paramsCell.update([this.paramsField]),this.cells.defaultCell.update([this.defaultField])}get type(){return this.cells.typeCell.getValue("type_")}get options(){if("select"==this.type)return this.cells.paramsCell.getValue("options").split(",")}set options(e=[]){null!==e&&"select"==this.type&&(this.cells.paramsCell.setValue("options",e.join(",")),this.cells.defaultCell.update([this.defaultField]))}get pattern(){"text"==this.type&&this.cells.paramsCell.getValue("pattern")}set pattern(e=""){null!==e&&"text"==this.type&&(this.cells.paramsCell.setValue("pattern",e),this.cells.defaultCell.setPattern("default",e))}set description(e){this.cells.descriptionCell.setValue("description",e)}set enaName(e){this.cells.enaCell.setValue("ena_name",e)}set enaRequirement(e){this.cells.enaCell.setValue("ena_requirement",e)}set enaUnits(e){this.cells.enaCell.setValue("ena_units",e)}set gisaidName(e){this.cells.gisaidCell.setValue("gisaid_name",e)}set gisaidRequirement(e){this.cells.gisaidCell.setValue("gisaid_requirement",e)}set gisaidHeader(e){this.cells.gisaidCell.setValue("gisaid_header",e)}set default(e){this.cells.defaultCell.setValue("default",e)}verifyTemplate(e){const t=parseTemplateString(e);this.cells.paramsCell.toggleInvalid("template",!1),t.filter(e=>"var"==e.type).forEach(t=>{let l=!1;TEMPLATE_EDITOR.querySelectorAll("padded-row > attr-row").forEach(e=>{e.generalName==t.value&&(l=!0),FIXED_VALUES.includes(t.value)&&(l=!0)}),l||this.cells.paramsCell.toggleInvalid("template",!0)})}modifiedParams(e){switch(this.type){case"text":this.pattern=e;break;case"select":this.options=e.split(",");break;case"template":this.verifyTemplate(e);break;case"date":case"file":break;default:return}}setFromAttribute(e){this.generalName=e.general_name,this.label=e.label,this.type=e.type_,this.enaName=e.ena_name,this.enaRequirement=e.ena_requirement,this.enaUnits=e.ena_units,this.gisaidName=e.gisaid_name,this.gisaidRequirement=e.gisaid_requirement,this.gisaidHeader=e.gisaid_header,this.pattern=e.pattern,this.options=e.options,this.template=e.template,this.default=e.default,this.description=e.description}}class PaddedRow extends HTMLElement{constructor(){super(),this.row=this.querySelector("attr-row"),this.row||(this.row=document.createElement("attr-row"))}connectedCallback(){0==this.children.length&&this.appendChild(this.row)}set index(e){this.row.index=e}get index(){return this.row.index}setFromAttribute(e){this.row.setFromAttribute(e)}}function appendBlankRow(){const e=document.createElement("padded-row");return e.index=TEMPLATE_EDITOR.querySelectorAll("padded-row.attr").length+1,e.classList.add("attr"),TEMPLATE_EDITOR.appendChild(e),e}function updateTaxonomyFields({taxonomy_id:e="",scientific_name:t="",common_name:l=""}){const a=document.querySelector("div#taxonomy");a.querySelector("#taxonomy-id").value=e,a.querySelector("#scientific-name").value=t,a.querySelector("#common-name").value=l}function fillFromTemplate(e){document.querySelector("#template-name-field").disabled=!0;let t=new HiddenField("template_name");t.setValue(e.name),document.querySelector("#name-field").appendChild(t.input);let l;if(e.attributes.forEach(e=>{e.ena_units=[e.ena_units],(l=appendBlankRow()).setFromAttribute(e)}),e.ena_checklist){const a=document.querySelector("div#ena-import"),i=(a.querySelector("#fetch-ena-button").disabled=!0,a.querySelector("#ena-checklist"));i.disabled=!0,i.value=e.ena_checklist,(t=new HiddenField("ena_checklist+0+ena_checklist")).setValue(e.ena_checklist),a.appendChild(t.input)}updateTaxonomyFields(e.taxonomy)}customElements.define("attr-row",AttrRow),customElements.define("padded-row",PaddedRow),TEMPLATE_NAME&&fetch("/templates/json?name="+TEMPLATE_NAME).then(e=>e.json()).then(e=>{fillFromTemplate(e)});