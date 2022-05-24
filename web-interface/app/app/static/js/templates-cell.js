class EditorCell extends HTMLElement{constructor(){super(),this.inpfields=[],this.index=0}set fields(e){this.inpfields=Array.from(e)}get fields(){return this.inpfields}addFields(){this.fields.forEach(e=>{this.appendChild(e)})}set index(i){Array.from(this.classList).includes("remove")||this.fields.forEach(e=>{let t=e.name.split("+");t[1]=i,e.name=t.join("+")})}static create(e,t){const i=document.createElement("editor-cell");return i.fields=t,i.addFields(),i}fetchField(t){let i=null;return this.fields.forEach(e=>{e.name.split("+")[2]==t&&(i=e)}),i}getValue(e){e=this.fetchField(e);if(null!==e)return e.value}setValue(e,t){const i=this.fetchField(e);null!==i&&(i.value=t)}setPattern(e,t){const i=this.fetchField(e);null!==i&&(""!=t?i.pattern=t:i.removeAttribute("pattern"))}toggleInvalid(e,t=!0){const i=this.fetchField(e);null!==i&&i.classList.toggle("invalid",t)}clear(){this.fields.forEach(e=>e.remove()),this.inpfields=[]}update(e=[]){this.clear(),this.fields=e,this.addFields()}}customElements.define("editor-cell",EditorCell);