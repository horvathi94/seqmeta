SAMPLE_ATTRIBUTE={general_name:"",label:"",description:"",type_:"text"};class SampleEditor{constructor(e){this.table=e,this.head=this.table.tHead,this.tab=this.table.tBodies[0],this._template=null,this.lastIndex=0}get template(){return this._template}set template(e){this._template=e,this._template.attributes.forEach(e=>{this.appendBlankRow(e)})}createLabelCell(e){const t=document.createElement("th");return t.textContent=e,t}createDescriptionCell(e){const t=document.createElement("td");return t.textContent=e,t}createEditAllCell(e){const t=document.createElement("td");t.classList.add("editall");let a;return"sample_name"==e.general_name?t.textContent="Must be unique.":("file"==e.type_?a=createEditAllFileField(e):(a=createAttributeField(e)).onchange=function(){this.closest("tr").querySelectorAll("td.sample").forEach(e=>{e.querySelector(".attrfield").value=this.value}),SAMPLE_EDITOR.updateSampleTemplate(this)},t.appendChild(a)),t}appendBlankRow(e){const t=this.tab.insertRow();t.dataset.generalName=e.general_name,t.appendChild(this.createLabelCell(e.label)),t.appendChild(this.createEditAllCell(e)),t.appendChild(this.createDescriptionCell(e.description))}stretchHeader(){const e=this.head.querySelector("#samples-header-cell");e.style.display||(e.colSpan=parseInt(e.colSpan)+1),e.style.display=""}getRow(e){return this.tab.querySelector(`tr[data-general-name='${e}']`)}get currentIndex(){return this.lastIndex+1}addAttributeCell(e,t=null){const a=this.getRow(e.general_name).insertCell(this.lastIndex+2);a.classList.add("sample"),"template"==e.type_&&a.classList.add("template"),a.dataset.sample=this.currentIndex;var l=`sample+${this.currentIndex}+`+e.general_name,e=createAttributeField(e,l,t);a.appendChild(e)}addSample(l=null){this.template.attributes.forEach(t=>{let e=null;var a;null!==l&&("sample_name"==t.general_name?e=l.name:"short_description"==t.general_name?e=l.short_description:0<l.attributes.length&&null!==(a=l.attributes.find(e=>e.general_name==t.general_name))&&(e=a.value)),this.addAttributeCell(t,e)}),this.stretchHeader(),this.lastIndex++}checkSample(t){let a=0;return this.getRow("sample_name").querySelectorAll("td.sample>input.attrfield").forEach(e=>{e.value==t&&(a=parseInt(e.name.split("+")[1]))}),a}addSampleFromFile(e){const t=e.name.split(".")[0];e=t.split("_")[0];if(!this.checkSample(e)){const a=JSON.parse(JSON.stringify(BLANK_SAMPLE));a.name=e,SAMPLE_EDITOR.addSample(a)}}updateTemplate(e){const t=e.querySelector(".attrfield"),a=e.dataset.sample,l=parseTemplateString(t.dataset.templateString);l.filter(e=>"const"!=e.type).forEach(e=>{let t=e.value;"sample_name"==e.value&&(t="name"),e.fieldValue=this.getRow(t).querySelector(`td.sample[data-sample='${a}']`).querySelector(".attrfield").value}),t.value=constructStringFromTemplate(l)}updateSampleTemplate(e){const t=e.closest("td");let a="td.sample.template";t.classList.contains("editall")||(a+=`[data-sample='${t.dataset.sample}']`),this.tab.querySelectorAll(a).forEach(e=>{this.updateTemplate(e)})}}function addBlankSample(){const l=parseInt(SAMPLE_EDITOR.rows[1].querySelectorAll("td.sample").length)+1;return TEMPLATE.attributes.forEach(e=>{const t=SAMPLE_EDITOR.querySelector(`tr[data-general-name='${e.general_name}']`),a=t.insertCell(t.cells.length-1);a.classList.add("sample"),a.dataset.sample=l,a.appendChild(createAttributeField(e))}),l}function newSample(){SAMPLE_EDITOR.addSample()}async function initTable(){const t=document.querySelector("#template-name").value,e=(SAMPLE_EDITOR.template=await fetch(`/templates/json?name=${t}&use=sample_editor`).then(e=>e.json()).then(e=>e),document.querySelector("#sample-names").value.split(","));e&&e.forEach(e=>{e&&fetch(`/samples/json?name=${e}&template_name=`+t).then(e=>e.json()).then(e=>SAMPLE_EDITOR.addSample(e))})}const table=document.querySelector("#sample-editor"),SAMPLE_EDITOR=new SampleEditor(table);initTable();