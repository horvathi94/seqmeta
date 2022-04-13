async function fetchTemplate(){const e=await fetch("/templates/json/"+TEMPLATE_ID);return e.json()}function createAttributeField(e,t="",a=!1){let l;switch(l=document.createElement("input"),e.type_){case"text":(l=document.createElement("input")).type="text",e.pattern&&(l.pattern=e.pattern),e.default&&(l.value=e.default);break;case"select":l=createSelectMenu(parseOptions(e.options)),e.default&&(l.value=e.default);break;case"date":(l=document.createElement("input")).type="date",e.default&&(l.value=e.default);break;case"template":(l=document.createElement("input")).type="text",l.placeholder=e.template,l.setAttribute("template-string",e.template)}return a?l.addEventListener("change",function(){changeAll(this)},!1):l.addEventListener("change",function(){updateTemplateFields()},!1),l.classList.add(e.type_),t&&(l.name=t+"+"+e.general_name),l}function changeAll(t){t.parentElement.parentElement.querySelectorAll(".sample.attr").forEach(e=>{e.querySelector(".attr.field").value=t.value}),updateTemplateFields()}function parseTemplateString(e){let t=[],a=!0;return[...e].forEach(e=>{a="["==e?(t.push({type:"var",value:""}),!1):"]"==e||(a&&t.push({type:"const",value:""}),t[t.length-1].value+=e,!1)}),t}function updateTemplateFields(e){let a,l,n;Array.from(document.querySelectorAll(".field.attr.template")).forEach(t=>{l=t.name.split("+").slice(0,-1).join("+"),(a=parseTemplateString(t.getAttribute("template-string"))).forEach(e=>{"const"==e.type?t.value+=e.value:(n=document.querySelector(`[name='${l}+${e.value}']`).value)?t.value+=n:t.value+="["+e.value+"]"})})}function createNewRow(e){const t=document.createElement("tr"),a=(t.classList.add("row",e.general_name),document.createElement("th")),l=(a.innerHTML=e.label,t.appendChild(a),document.createElement("td")),n=(l.appendChild(createAttributeField(e,sampleName="",isEditAll=!0)),t.appendChild(l),document.createElement("td"));return n.innerHTML=e.description,t.appendChild(n),t}async function addNewSample(t=!0){const e=await fetchTemplate(),a=document.querySelector("#sample-editor").tBodies[0];let l="";var n;t&&(n=a.rows[0].querySelectorAll(".attr.sample.new").length+1,l="sample+new+"+n);let r,c,i;e.attributes.forEach(e=>{r=a.querySelector(".row."+e.general_name),(i=createAttributeField(e,l)).classList.add("field","attr",e.general_name),(c=r.insertCell(r.cells.length-1)).classList.add("attr","sample",e.general_name),t&&c.classList.add("new"),c.appendChild(i)})}async function initSampleEditor(){const e=await fetchTemplate(),t=document.querySelector("#sample-editor").tBodies[0];let a;e.attributes.forEach(e=>{a=createNewRow(e),t.appendChild(a)})}initSampleEditor();