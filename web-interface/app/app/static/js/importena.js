function string2XML(e){return(new window.DOMParser).parseFromString(e,"text/xml")}function fecthEnaXml(){return string2XML(rawXML)}function appendEnaInfo(e,r){const n=document.querySelector("#ena-info"),t=document.createElement("p");t.innerHTML=`<strong>${e}:</strong>`+r,n.appendChild(t)}function updateType(e,r){e.querySelector(".cell.type>.attr.field.type_").value=r,changedAttributeType(e)}function cleanNameField(e){return clean=e.replace(/[ /]/g,"_").replace(/[()]/g,"")}function field2Attribute(e){const r=new TemplateAttribute,n=(r.name=e.querySelector("NAME").innerHTML,e.querySelector("LABEL").innerHTML),t=(r.label=n.slice(0,1).toUpperCase()+n.slice(1).toLowerCase(),r.description=e.querySelector("DESCRIPTION").innerHTML,r.ena_requirement=e.querySelector("MANDATORY").innerHTML,e.querySelector("FIELD_TYPE").children[0]);switch(t.tagName){case"TEXT_FIELD":var c=t.querySelector("REGEX_VALUE");null!==c&&(r.pattern=c.innerHTML);break;case"TEXT_AREA_FIELD":break;case"TEXT_CHOICE_FIELD":r.type_="select",r.options=Array.from(t.querySelectorAll("TEXT_VALUE")).map(e=>e.querySelector("VALUE").innerHTML)}return r}function parseFieldGroup(e){let r;Array.from(e.querySelectorAll("FIELD")).forEach(e=>{r=field2Attribute(e),console.log(r)})}function parseXmlChecklist(){var e="ERC000033";const r=fecthEnaXml(),n=r.querySelector(`CHECKLIST_SET > CHECKLIST[checklistType='Sample'][accession='${e}']`);if(null!==n)if(n.querySelector("IDENTIFIERS>PRIMARY_ID").innerHTML==e){const t=n.querySelector("DESCRIPTOR");appendEnaInfo("Label",t.querySelector("LABEL").innerHTML),appendEnaInfo("Name",t.querySelector("NAME").innerHTML),appendEnaInfo("Description",t.querySelector("DESCRIPTION").innerHTML),appendEnaInfo("Authority",t.querySelector("AUTHORITY").innerHTML),Array.from(n.querySelectorAll("FIELD_GROUP")).forEach(e=>{parseFieldGroup(e)})}else alert("Mismatch in accession number!");else alert("Mismatch in accession number!")}