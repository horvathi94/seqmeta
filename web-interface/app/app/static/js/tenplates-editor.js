const TEMPLATE_EDITOR=document.querySelector("#template-editor");class PaddedRow extends HTMLElement{}customElements.define("padded-row",PaddedRow);const editor=new TemplateEditor(TEMPLATE_EDITOR);editor.appendChild(new PaddedRow),editor.appendChild(new PaddedRow);