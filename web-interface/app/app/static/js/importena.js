function string2XML(e){return(new window.DOMParser).parseFromString(e,"text/xml")}function fecthEnaXml(){return string2XML(rawXML)}function appendEnaInfo(e,r){const t=document.querySelector("#ena-info"),n=document.createElement("p");n.innerHTML=`<strong>${e}:</strong>`+r,t.appendChild(n)}function updateType(e,r){e.querySelector(".cell.type>.attr.field.type_").value=r,changedAttributeType(e)}function cleanNameField(e){return clean=e.replace(/[ /]/g,"_").replace(/[()]/g,"")}function field2AttributeRow(e){const r=insertNewAttribute();var t=e.querySelector("NAME").innerHTML;const n=e.querySelector("LABEL").innerHTML,c=(r.setName(cleanNameField(t)),r.setLabel(n.slice(0,1).toUpperCase()+n.slice(1).toLowerCase()),r.setDescription(e.querySelector("DESCRIPTION").innerHTML),r.setEnaRequirementLevel(e.querySelector("MANDATORY").innerHTML),r.setEnaName(t),e.querySelector("FIELD_TYPE").children[0]);let l;switch(c.tagName){case"TEXT_FIELD":r.setType("text");const l=c.querySelector("REGEX_VALUE");null!==l&&r.setPattern(l.innerHTML);break;case"TEXT_AREA_FIELD":r.setType("text");break;case"TEXT_CHOICE_FIELD":r.setType("select");var a=Array.from(c.querySelectorAll("TEXT_VALUE")).map(e=>e.querySelector("VALUE").innerHTML);console.log(a),r.setOptions(a)}}function parseFieldGroup(e){let r;Array.from(e.querySelectorAll("FIELD")).forEach(e=>{r=field2AttributeRow(e)})}function parseXmlChecklist(){var e="ERC000033";const r=fecthEnaXml(),t=r.querySelector(`CHECKLIST_SET > CHECKLIST[checklistType='Sample'][accession='${e}']`);if(null!==t)if(t.querySelector("IDENTIFIERS>PRIMARY_ID").innerHTML==e){const n=t.querySelector("DESCRIPTOR");appendEnaInfo("Label",n.querySelector("LABEL").innerHTML),appendEnaInfo("Name",n.querySelector("NAME").innerHTML),appendEnaInfo("Description",n.querySelector("DESCRIPTION").innerHTML),appendEnaInfo("Authority",n.querySelector("AUTHORITY").innerHTML),Array.from(t.querySelectorAll("FIELD_GROUP")).forEach(e=>{parseFieldGroup(e)})}else alert("Mismatch in accession number!");else alert("Mismatch in accession number!")}parseXmlChecklist();