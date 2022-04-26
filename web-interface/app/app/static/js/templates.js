const TEMPLATE_EDITOR=document.querySelector("#template-editor"),FIELD_TYPES=["text","select","date","template"],REQUIREMENT_LEVELS=["exclude","optional","recommended","mandatory"],TEMPLATE_NAME=document.querySelector("#loaded-template-name").value;ATTRIBUTE={general_name:"",label:"",type_:"text",description:"",ena_requirement:"exclude",ena_name:"",gisaid_requirement:"exclude",gisaid_name:"",pattern:"",options:[],units:null,default:""};class AttributeRow{constructor(e){this.row=e,this.row.querySelectorAll(".cell").length||this.createCells()}getStatus(){return this.row.classList[1]}getIndex(){return this.row.getAttribute("index")}getCell(e){return this.row.querySelector("div.cell."+e)}getName(){return this.getCell("general_name").querySelector("input").value}setName(e){this.getCell("general_name").querySelector("input").value=e}setLabel(e){this.getCell("label").querySelector("input").value=e}setDescription(e){this.getCell("description").querySelector("textarea").value=e}getTemplate(){return"template"!=this.getType()?"":this.getCell("parameters").querySelector(".paramfield").value}setTemplate(e){"template"==this.getType()&&(this.getCell("parameters").querySelector(".paramfield").value=e,this.replaceDefaultField())}getPattern(){return"text"!=this.getType()?"":this.getCell("parameters").querySelector(".paramfield").value}setPattern(e){"text"==this.getType()&&(this.getCell("parameters").querySelector(".paramfield").value=e,this.replaceDefaultField())}getOptions(){return"select"!=this.getType()?[]:this.getCell("parameters").querySelector(".paramfield").value.split(",")}setOptions(e){"select"==this.getType()&&(this.getCell("parameters").querySelector(".paramfield").value=e.join(","),this.replaceDefaultField())}getType(){return this.getCell("type_").querySelector("select").value}setType(e){this.getCell("type_").querySelector("select").value=e,this.replaceParametersField(),this.replaceDefaultField()}getMaxRequirementLevel(){const t=[];t.push(this.getCell("ena").querySelector(".reqlevel").value),t.push(this.getCell("gisaid").querySelector(".reqlevel").value);let a="exclude";return REQUIREMENT_LEVELS.forEach(e=>{t.includes(e)&&(a=e)}),a}setEnaRequirementLevel(e){this.getCell("ena").querySelector(".reqlevel").value=e}setEnaName(e){this.getCell("ena").querySelector(".reqname").value=e}setGisaidRequirementLevel(e){this.getCell("gisaid").querySelector(".reqlevel").value=e}setGisaidName(e){this.getCell("gisaid").querySelector(".reqname").value=e}setDefault(e){this.getCell("default").querySelector(".defaultfield").value=e}setUnits(e){this.getCell("units").getElementsByTagName("input")[0].value=e}appendCell(e,t=[]){const a=document.createElement("div");a.classList.add("cell",e),t.forEach(e=>{a.appendChild(e)}),this.row.appendChild(a)}createCells(){this.appendCell("rm",this.createRemoveFields()),this.appendCell("general_name",[this.attrInput({name:"general_name",type:"text",pattern:"\\w+"})]),this.appendCell("label",[this.attrInput({name:"label",type:"text"})]),this.appendCell("type_",[this.createTypeField()]),this.appendCell("ena",this.createEnaFields()),this.appendCell("gisaid",this.createGisaidFields()),this.appendCell("parameters",[this.createParametersField()]),this.appendCell("units",[this.createUnitsField()]),this.appendCell("default",[this.createDefaultField()]),this.appendCell("description",[this.createDescriptionField()])}createTypeField(){const e=this.attrInput({name:"type_",type:"select",options:FIELD_TYPES});return e.onchange=function(){updateRow(this,"changed-type")},e}createRequirementFields(e){const t=this.attrInput({name:e+"_name",type:"text"}),a=(t.classList.add("reqname"),this.attrInput({name:e+"_requirement",type:"select",options:REQUIREMENT_LEVELS}));return a.onchange=function(){updateRow(this,"changed-requirement")},a.classList.add("reqlevel"),[t,a]}createEnaFields(){return this.createRequirementFields("ena")}createGisaidFields(){const e=this.createRequirementFields("gisaid"),t=this.attrInput({name:"gisaid_header",type:"text"});return t.classList.add("gisaidhead"),e.push(t),e}createParametersField(){let e;switch(this.getType()){case"text":(e=this.attrInput({name:"pattern",type:"text"})).placeholder="Regex for input.";break;case"select":(e=this.attrInput({name:"options",type:"textarea"})).placeholder="Comma separated list of options.";break;case"date":(e=this.attrInput({name:"junk",type:"text"})).placeholder="N/A",e.disabled=!0;break;case"template":(e=this.attrInput({name:"template",type:"text"})).placeholder="Template for input field."}return e.classList.add("paramfield"),e.onchange=function(){updateRow(this,"changed-parameters")},e}createDescriptionField(){const e=this.attrInput({name:"description",type:"textarea"});return e.placeholder="Short description.",e}createDefaultField(){let e;switch(this.getType()){case"text":(e=this.attrInput({name:"default",type:"text",pattern:this.getPattern()})).placeholder="Default value for field.";break;case"select":(e=this.attrInput({name:"default",type:"select",options:this.getOptions()})).placeholder="Default value for field.";break;case"date":e=this.attrInput({name:"default",type:"date"});break;case"template":(e=this.attrInput({name:"template",type:"text"})).placeholder="N/A.",e.disabled=!0}return e.classList.add("defaultfield"),e}createRemoveFields(){const e=document.createElement("input"),t=(e.setAttribute("type","button"),e.classList.add("rmbutton"),e.value="X",e.onclick=function(){updateRow(this,"remove")},this.attrInput({name:"deleted",type:"hidden"}));return t.classList.add("deleted"),t.value="0",[e,t]}createUnitsField(){return this.attrInput({name:"units",type:"text"})}attrInput({name:e="",type:t="",pattern:a="",options:l=[]}){var r=`attr+${this.getStatus()}+${this.getIndex()}+`+e;let i;switch(t){case"text":(i=new TextField(r)).setPattern(a);break;case"select":i=new SelectField(r,l);break;case"textarea":i=new TextAreaField(r);break;case"date":i=new DateField(r);break;case"hidden":i=new HiddenField(r)}return i.input}updateRemoveButton(){var e=this.getMaxRequirementLevel();const t=this.getCell("rm").querySelector(".rmbutton");t.disabled="mandatory"==e}replaceParametersField(){const e=this.getCell("parameters");var t=e.querySelector(".paramfield");e.replaceChild(this.createParametersField(),t)}replaceDefaultField(){const e=this.getCell("default");var t=e.querySelector(".defaultfield");e.replaceChild(this.createDefaultField(),t)}removeRow(){"registered"==this.getStatus()?(this.getCell("rm").querySelector(".deleted").value="1",this.row.classList.add("hide")):this.row.remove()}update(e){switch(console.log(`Updating with command=${e} in `+this.row),e){case"remove":this.removeRow();break;case"changed-type":this.setType(this.getType());break;case"changed-parameters":"text"==this.getType()&&this.setPattern(this.getPattern()),"select"==this.getType()&&this.setOptions(this.getOptions()),"template"==this.getType()&&validateTemplate(this.getCell("parameters").querySelector(".paramfield"));break;case"changed-requirement":this.updateRemoveButton()}}setFromAttribute(e){this.setName(e.general_name),this.setLabel(e.label),this.setType(e.type_),this.setPattern(e.pattern),this.setOptions(e.options),this.setTemplate(e.template),this.setDefault(e.default),this.setDescription(e.description),this.setEnaName(e.ena_name),this.setEnaRequirementLevel(e.ena_requirement),this.setGisaidName(e.gisaid_name),this.setGisaidRequirementLevel(e.gisaid_requirement),this.setUnits(e.units)}}function validateTemplate(e){const t=parseTemplateString(e.value);e.style.color="black",t.filter(e=>"var"==e.type).forEach(a=>{let l=!1;TEMPLATE_EDITOR.querySelectorAll(".row.attr").forEach(e=>{let t=new AttributeRow(e);console.log(t.getName()),t.getName()==a.value&&(l=!0)}),l||(e.style.color="red")})}function updateRow(e,t){const a=new AttributeRow(e.closest("div.row"));a.update(t)}function createBlankRow(e="new",t=0){"new"!=e||t||(t=TEMPLATE_EDITOR.querySelectorAll("div.row.new").length+1);const a=document.createElement("div");return a.classList.add("row","attr",e),a.setAttribute("index",t),a}function insertNewAttribute(e="new",t=0){e=createBlankRow(e,t),t=new AttributeRow(e);return TEMPLATE_EDITOR.appendChild(t.row),t}function fillFromTemplate(e){document.querySelector("#template-name-field").value=e.name;let t;e.attributes.forEach(e=>{(t=insertNewAttribute(status="registered",index=e.id)).setFromAttribute(e)})}TEMPLATE_NAME&&fetch("/templates/json?name="+TEMPLATE_NAME).then(e=>e.json()).then(e=>{fillFromTemplate(e)});