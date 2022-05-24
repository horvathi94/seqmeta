function string2XML(e){return(new window.DOMParser).parseFromString(e,"text/xml")}async function fetchEnaXml(e){return string2XML(await fetch("https://www.ebi.ac.uk/ena/browser/api/xml/"+e).then(e=>e.text()))}function clearEnaInfo(){const e=document.querySelector("#ena-info");e.querySelectorAll("p").forEach(e=>{e.remove()})}function appendEnaInfo(e,n){const r=document.querySelector("#ena-info"),t=document.createElement("p");t.innerHTML=`<strong>${e}:</strong>`+n,r.appendChild(t)}function updateType(e,n){e.querySelector(".cell.type>.attr.field.type_").value=n,changedAttributeType(e)}function cleanNameField(e){return clean=e.replace(/[ /-]/g,"_").replace(/[()]/g,"")}function field2Attribute(e){const n=Object.create(ATTRIBUTE),r=(n.ena_name=e.querySelector("NAME").innerHTML,e.querySelector("LABEL").innerHTML),t=(n.general_name=cleanNameField(n.ena_name),n.label=r.slice(0,1).toUpperCase()+r.slice(1).toLowerCase(),n.description=e.querySelector("DESCRIPTION").innerHTML,n.ena_requirement=e.querySelector("MANDATORY").innerHTML,e.querySelector("FIELD_TYPE").children[0]);let a;switch(t.tagName){case"TEXT_FIELD":const a=t.querySelector("REGEX_VALUE");null!==a&&(n.pattern=a.innerHTML);break;case"TEXT_AREA_FIELD":break;case"TEXT_CHOICE_FIELD":n.type_="select",n.options=Array.from(t.querySelectorAll("TEXT_VALUE")).map(e=>e.querySelector("VALUE").innerHTML)}const c=e.querySelector("UNITS");return c&&(n.ena_units=Array.from(c.querySelectorAll("UNIT")).map(e=>e.innerHTML)),n}function parseFieldGroup(e){let n,r;Array.from(e.querySelectorAll("FIELD")).forEach(e=>{r=TEMPLATE_EDITOR.appendBlankRow(),n=field2Attribute(e),r.setFromAttribute(n)})}async function parseXmlChecklist(){var e=document.querySelector("#ena-import > #ena-checklist").value;const n=await fetchEnaXml(e),r=n.querySelector(`CHECKLIST_SET > CHECKLIST[checklistType='Sample'][accession='${e}']`);if(null!==r)if(r.querySelector("IDENTIFIERS>PRIMARY_ID").innerHTML==e){const t=r.querySelector("DESCRIPTOR");clearEnaInfo(),appendEnaInfo("Label",t.querySelector("LABEL").innerHTML),appendEnaInfo("Name",t.querySelector("NAME").innerHTML),appendEnaInfo("Description",t.querySelector("DESCRIPTION").innerHTML),appendEnaInfo("Authority",t.querySelector("AUTHORITY").innerHTML),Array.from(r.querySelectorAll("FIELD_GROUP")).forEach(e=>{parseFieldGroup(e)})}else alert("Mismatch in accession number!");else alert("Mismatch in accession number!")}function fetchEnaData(){parseXmlChecklist()}