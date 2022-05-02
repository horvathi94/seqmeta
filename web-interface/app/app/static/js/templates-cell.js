class AttrCell extends HTMLElement{constructor(){super(),this.inpfields=[],this.index=0}set fields(e){this.inpfields=Array.from(e)}get fields(){return this.inpfields}addFields(){this.fields.forEach(e=>{this.appendChild(e)})}set index(l){this.fields.forEach(e=>{let t=e.name.split("+");t[1]=l,e.name=t.join("+")})}static create(e,t){const l=document.createElement("attr-cell");return l.fields=t,l.addFields(),l}fetchField(t){let l=null;return this.fields.forEach(e=>{e.name.split("+")[2]==t&&(l=e)}),l}getValue(e){e=this.fetchField(e);if(null!==e)return e.value}setValue(e,t){const l=this.fetchField(e);null!==l&&(l.value=t)}setPattern(e,t){const l=this.fetchField(e);null!==l&&(l.pattern=t)}toggleInvalid(e,t=!0){const l=this.fetchField(e);null!==l&&l.classList.toggle("invalid",t)}clear(){this.fields.forEach(e=>e.remove()),this.inpfields=[]}update(e=[]){this.clear(),this.fields=e,this.addFields()}}customElements.define("attr-cell",AttrCell);