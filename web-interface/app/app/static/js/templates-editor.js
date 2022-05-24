class TemplateEditor extends HTMLElement{get attrEditor(){return this.querySelector("#attr-editor")}get taxonomyEditor(){return this.querySelector(".mini-editor#taxonomy")}get checklistEditor(){return this.querySelector(".mini-editor#ena-import")}get nameEditor(){return this.querySelector(".mini-editor#name")}get subFilesEditor(){return this.querySelector(".mini-editor#files-check")}createSpacer(){const e=document.createElement("div");return e.classList.add("spacer"),e.ondragover=function(e){return e.preventDefault(),!1},e.ondrop=function(e){e.stopPropagation();e=dragSource.nextSibling;return this.parentElement.insertBefore(dragSource,this.nextSibling),this.parentElement.insertBefore(e,dragSource.nextSibling),dragSource.clearDragClasses(),TEMPLATE_EDITOR.renumberRows(),!1},e}appendBlankRow(){const e=document.createElement("editor-row");return e.index=this.querySelectorAll("editor-row.attr").length+1,e.classList.add("attr"),this.attrEditor.appendChild(e),this.attrEditor.appendChild(this.createSpacer()),e}renumberRows(){this.attrEditor.querySelectorAll("editor-row.attr").forEach((e,t)=>{e.index=t+1})}set taxonomyId(e){this.taxonomyEditor.querySelector("#taxonomy-id").value=e}set scientificName(e){this.taxonomyEditor.querySelector("#scientific-name").value=e}set commonName(e){this.taxonomyEditor.querySelector("#common-name").value=e}set name(e){this.nameEditor.querySelector("#template-name-field").value=e}set description(e){this.nameEditor.querySelector("#template-description-field").value=e}set enaChecklist(e){this.checklistEditor.querySelector("#ena-checklist").value=e}lockName(e){this.name=e;const t=new HiddenField("template_name");this.nameEditor.querySelector("#template-name-field").disabled=!0,t.setValue(e),this.nameEditor.appendChild(t.input)}lockEnaChecklist(e){this.enaChecklist=e,this.checklistEditor.querySelector("#ena-checklist").disabled=!0,this.checklistEditor.querySelector("#fetch-ena-button").disabled=!0;const t=new HiddenField("ena_checklist+0+ena_checklist");t.setValue(e),this.checklistEditor.appendChild(t.input)}setSubmissionFiles(e){e.forEach(i=>{i.is_active&&i.repos.forEach(e=>{const t=this.subFilesEditor.querySelector(`input[type='checkbox'][data-ftype='${i.filetype}'][data-repo='${e}']`);t.checked=!0})})}fillFromTemplate(e){this.lockName(e.name),this.taxonomyId=e.taxonomy.taxonomy_id,this.scientificName=e.taxonomy.scientific_name,this.commonName=e.taxonomy.common_name,this.description=e.short_description,e.ena_checklist&&this.lockEnaChecklist(e.ena_checklist),this.setSubmissionFiles(e.files),e.attributes.forEach(t=>{if(!t.is_fixed){let e=this.appendBlankRow();e.setFromAttribute(t)}})}deleteRow(t){this.attrEditor.querySelectorAll("editor-row.attr").forEach(e=>{e.generalName==t&&(e.nextSibling.remove(),e.remove())})}clear(){this.attrEditor.querySelectorAll("editor-row.attr").forEach(e=>{this.deleteRow(e.generalName)})}addAttribute(e){const t=this.appendBlankRow();t.setFromAttribute(e)}switchUploadFiles(t){let e;"gisaid"==t.dataset.repo&&"assembly"==t.dataset.ftype?e=get_gisaid_assembly_fields():"ena"==t.dataset.repo&&"read"==t.dataset.ftype&&(e=get_ena_read_fields()),e.forEach(e=>{t.checked?this.addAttribute(e):this.deleteRow(e.general_name)})}}customElements.define("template-editor",TemplateEditor),TEMPLATE_NAME&&fetch("/templates/json?name="+TEMPLATE_NAME).then(e=>e.json()).then(e=>{TEMPLATE_EDITOR.fillFromTemplate(e)});