class EditorCell extends HTMLElement{constructor(){super(),this.inpfields=[],this.index=0}set fields(a){this.inpfields=Array.from(a)}get fields(){return this.inpfields}addFields(){this.fields.forEach(a=>{this.appendChild(a)})}set index(a){Array.from(this.classList).includes("remove")||this.fields.forEach(b=>{let c=b.name.split("+");c[1]=a,b.name=c.join("+")})}static create(a,b){const c=document.createElement("editor-cell");return c.fields=b,c.addFields(),c}fetchField(a){let b=null;return this.fields.forEach(c=>{if(c.name.split("+")[2]==a)return void(b=c)}),b}getValue(a){const b=this.fetchField(a);return null===b?void 0:b.value}setValue(a,b){const c=this.fetchField(a);null===c||(c.value=b)}setPattern(a,b){const c=this.fetchField(a);return null===c?void 0:""==b?void c.removeAttribute("pattern"):void(c.pattern=b)}toggleInvalid(a,b=!0){const c=this.fetchField(a);null===c||c.classList.toggle("invalid",b)}clear(){this.fields.forEach(a=>a.remove()),this.inpfields=[]}update(a=[]){this.clear(),this.fields=a,this.addFields()}}customElements.define("editor-cell",EditorCell);