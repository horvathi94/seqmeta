const TEMPLATE_NAME=document.querySelector("#template-name").value,SAMPLE_NAME_ATTR={general_name:"name",label:"Sample name",description:"Unique name to differentiate between registered samples.",pattern:"\\w+",type_:"sample_name",value:""},SHORT_DESCRIPTION_ATTR={general_name:"short_description",label:"Short description",description:"A short description to more easily identify the sample.",type_:"text",value:""};function createAttributeField(e,t=""){let a=document.createElement("input");switch(e.type_){case"text":a.type="text",e.pattern&&(a.pattern=e.pattern);break;case"select":a=createSelectMenu(e.options);break;case"date":a.type="date";break;case"template":a.type="text",a.placeholder=e.template,a.dataset.templateString=e.template,a.classList.add("template");break;case"file":a.type="text";break;case"sample_name":a.type="text",a.pattern=e.pattern}return a.name=t,e.value?a.value=e.value:a.value=e.default,a.classList.add("attrfield",e.general_name),"template"!=e.type_&&a.addEventListener("change",function(){SAMPLE_EDITOR.updateSampleTemplate(this)},!1),a}function createEditAllField(e){let t;return"sample_name"==e.type_?(t=document.createElement("p")).textContent="Must be unique.":"file"==e.type_?(t=document.createElement("p")).textContent="Upload files separatly.":(t=createAttributeField(e)).addEventListener("change",function(){this.closest("tr").querySelectorAll("td.sample").forEach(e=>{e.querySelector(".attrfield").value=this.value}),updateTemplateFields()},!1),t}function createTextCell(e,t=[],a="td"){const l=document.createElement(a),n=(l.classList.add(t),document.createElement("p"));return n.innerHTML=e,l.appendChild(n),l}function createEditAllCellOld(e){const t=document.createElement("td");t.classList.add("editall");e=createEditAllField(e);return t.appendChild(e),t}function createAttributeRowOld(e){const t=document.createElement("tr");return t.classList.add(e.general_name),t.appendChild(createTextCell(e.label,classList=["title"],element="th")),t.appendChild(createEditAllCell(e)),t.appendChild(createTextCell(e.description,classList=["description"],element="td")),t}function initTableOld(){SAMPLE_EDITOR.appendChild(createAttributeRow(SAMPLE_NAME_ATTR)),SAMPLE_EDITOR.appendChild(createAttributeRow(SHORT_DESCRIPTION_ATTR)),fetch("/templates/json?name="+TEMPLATE_NAME).then(e=>e.json()).then(e=>{e.attributes.forEach(e=>{SAMPLE_EDITOR.appendChild(createAttributeRow(e))})})}function insertSampleCell(e,t=0){const a=SAMPLE_EDITOR.querySelector("tr."+e.general_name),l=a.insertCell(a.cells.length-1);l.classList.add("sample",e.general_name),l.dataset.sample=t,"template"==e.type_&&l.classList.add("template");t=`sample+${t}+`+e.general_name,e=createAttributeField(e,t);l.appendChild(e)}async function addSample(e=null,t=0){const a=document.querySelector("#samples-header-cell");a.style.display||(a.colSpan=parseInt(a.colSpan)+1);let l=!(a.style.display=""),n,r={...SAMPLE_NAME_ATTR},s={...SHORT_DESCRIPTION_ATTR};0==t&&(t=parseInt(SAMPLE_EDITOR.rows[1].querySelectorAll("td.sample").length)+1),null!==e&&(n=await fetch(`/samples/json?template_name=${TEMPLATE_NAME}&name=`+e).then(e=>e.json()).then(e=>e),r.value=n.name,s.value=n.short_description,l=!1),insertSampleCell(r,t),insertSampleCell(s,t),await fetch("/templates/json?name="+TEMPLATE_NAME).then(e=>e.json()).then(e=>{e.attributes.forEach(e=>{l||(e.value=n.attributes[e.general_name]),insertSampleCell(e,t)})})}async function loadSample(e){}async function loadSamples(e){e.forEach((e,t)=>{addSample(name=e,id=t+1)}),updateTemplateFields()}