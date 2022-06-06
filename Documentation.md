# SeqMeta v2.0

## What is SeqMeta

SeqMeta is a platform where you can store and manage sequencing data. It was designed to be run on a local machine and accessed trough the web browser.


## Setting up SeqMeta

SeqMeta is a Flask application in Python3.8, containerized in with Docker. The image for the container can be built directly by using the *Dockerfile*.
To setup your instance of the application use Docker to create a container. Customize any environment variables using the *.env* file.
Environment variables:
- **WEBIN_CLI_USER**: username of the Webin-CLI, this is required for uploading to ENA
- **WEBIN_CLI_PASSWORD**: password of the Webin-CLI, this is also required for uploading to ENA
- **HOST_PORT**: the number of the port on the host machine, which will be binded to the running port of the application. Use this port to access the web interface.
- **APP_SAMPLES_DIR**: the directory on the local machine, which is binded to the container and where all files are stored. Use this to obtain persistent data.


## Components of SeqMeta

### Sample templates

Sample templates contain all fields necessary to register a sample, these can be created and edited in the *Templates* tab of the interface.

#### Creating and editing a sample template

A sample template has main attributes and field attributes. The main attributes describe the sample template and all samples that will be associated with the template, while the field attributes contain fields that will be available when editing samples.

| Name | Description | Requirement |
| :--- | :---: | ---: |
| **Template name** | Unique name for the template to easily identify it. Once saved this value can not be changed! | mandatory |
| **Short description** | A short description about the template for identifiability. | recommended |
| **ENA checklist** | ENA checklist which is used when submitting data to ENA. You can also get all fields from a specific checklist by hitting the **GET** button, after typing in the checklist identifier. | mandatory if the template is meant for ENA submissions |
| **Taxonomy ID\*** | Species-rank taxon from the NCBI Taxonomy database. | mandatory |
| **Scientific name\*** | Scientific name of the sample. | mandatory |
| **Common name\*** | Common name of the sample. | recommended if available in the taxonomy database |
| **GISAID assembly** | If the sample is meant to be uploaded to GISAID. Checking this field also adds the necessary fields to the field editor. | mandatory for GISAID submissions |
| **ENA reads** | If the sequencing reads of the sample are meant to be uploaded to SRA trough ENA. Checking this field also adds the necessary fields to the field editor. | mandatory for read submission to ENA |

 \* These values can be easily fetched from the ENA servers by using the search option. This feature makes use of ENA's taxonomy service (https://ena-docs.readthedocs.io/en/latest/faq/taxonomy.html)


Field attributes describe the fields that will appear in the sample editor. A field has multiple values associated to it.
| Field | Description | Notes |
| :--- | :---: | ---: |
| **General name** | Unique identifier of the field, this value is only used by the program and does not show up in any submission. | Unique values within a template, can only contain letter and underscore (_) character. There is a list of values, which can not be used. |
| **Label** | Label that is shown in the sample editor | |
| **Type** | Type of the field | Options presented in detail in the followings. | 
| **ENA field name** | Name of the field in ENA submission (attribute) | This value is completed if importing from ENA checklist. Please follow the ENA documentation and checklist descriptions when manually completing|
| **ENA requirement** | Requirement level of the field in ENA submission. | This value is completed if importing from ENA checklist. Please follow the ENA documentation and checklist descriptions when manually completing. |
| **ENA unit** | Units of measurement of the field. | This value is completed if importing from ENA checklist. Please follow the ENA documentation and checklist descriptions when manually completing |
| **GISAID field name** | Name of the field in GISAID submission, shows up in the seccond row of the submission excel | Please adhere to the values in the GISAID batch submission excel documents. |
| **GISAID requirement** | Requirement level of the field in GISAID submission. | Please adhere to the values in the GISAID batch submission excel documents. |
| **GISAID header** | Header value in the  GISAID submission, shows up in the first row of the batch submission excel. | Please adhere to the values in the GISAID batch submission excel document. |
| **Parameters** | Constraints or options of the field | These are described in more detail later. | |
| **Default** | Default value for the field. When selected all new samples added in the sample editor will have this value. | |
| **Description** | Description of the field. | |



Field types:
| Type | Description | Parameters | Deafault |
| :--- | :---: | ---: | ---: |
| **Text** | Creates a text input field. | Regex for the field | Write default text. |
| **Select** | Creates a dropdown menu. | Comma separated list of options. | Select default option. | 
| **Date** | Creates a date input field | N/A | Select default date value. |
| **Template** | Creates a template field, which can contain values from other fields of the sample. A more detailed explenation on how to write templates is provided later. | Template | N/A |
| **File** | These can only be created by selecting the file fields. These create file upload fields. | N/A | N/A |


### Samples


## Using SeqMeta
