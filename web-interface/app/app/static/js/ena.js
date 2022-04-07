const rawXML=`
<CHECKLIST_SET>
<CHECKLIST accession="ERC000033" checklistType="Sample">
<IDENTIFIERS>
<PRIMARY_ID>ERC000033</PRIMARY_ID>
</IDENTIFIERS>
<DESCRIPTOR>
<LABEL>ENA virus pathogen reporting standard checklist</LABEL>
<NAME>ENA virus pathogen reporting standard checklist</NAME>
<DESCRIPTION>Minimum information about a virus pathogen. A checklist for reporting metadata of virus pathogen samples associated with genomic data. This minimum metadata standard was developed by the COMPARE platform for submission of virus surveillance and outbreak data (such as Ebola) as well as virus isolate information.</DESCRIPTION>
<AUTHORITY>ENA</AUTHORITY>
<FIELD_GROUP restrictionType="Any number or none of the fields">
<NAME>Human surveillance data</NAME>
<DESCRIPTION>Information associated with a human influenza surveillance sample.</DESCRIPTION>
<FIELD>
<LABEL>subject exposure</LABEL>
<NAME>subject exposure</NAME>
<DESCRIPTION>Exposure of the subject to infected human or animals, such as poultry, wild bird or swine. If multiple exposures are applicable, please state them separated by semicolon. Example: poultry; wild bird</DESCRIPTION>
<FIELD_TYPE>
<TEXT_FIELD/>
</FIELD_TYPE>
<MANDATORY>optional</MANDATORY>
<MULTIPLICITY>multiple</MULTIPLICITY>
</FIELD>
<FIELD>
<LABEL>subject exposure duration</LABEL>
<NAME>subject exposure duration</NAME>
<DESCRIPTION>Duration of the exposure of the subject to an infected human or animal. If multiple exposures are applicable, please state their duration in the same order in which you reported the exposure in the field 'subject exposure'. Example: 1 day; 0.33 days</DESCRIPTION>
<FIELD_TYPE>
<TEXT_FIELD/>
</FIELD_TYPE>
<MANDATORY>optional</MANDATORY>
<MULTIPLICITY>multiple</MULTIPLICITY>
</FIELD>
<FIELD>
<LABEL>type exposure</LABEL>
<NAME>type exposure</NAME>
<DESCRIPTION>Setting within which the subject is exposed to animals, such as farm, slaughterhouse, food preparation. If multiple exposures are applicable, please state their type in the same order in which you reported the exposure in the field 'subject exposure'. Example: backyard flock; confined animal feeding operation</DESCRIPTION>
<FIELD_TYPE>
<TEXT_FIELD/>
</FIELD_TYPE>
<MANDATORY>optional</MANDATORY>
<MULTIPLICITY>multiple</MULTIPLICITY>
</FIELD>
<FIELD>
<LABEL>personal protective equipment</LABEL>
<NAME>personal protective equipment</NAME>
<DESCRIPTION>Use of personal protective equipment, such as gloves, gowns, during any type of exposure. Example: mask</DESCRIPTION>
<FIELD_TYPE>
<TEXT_FIELD/>
</FIELD_TYPE>
<MANDATORY>optional</MANDATORY>
<MULTIPLICITY>multiple</MULTIPLICITY>
</FIELD>
<FIELD>
<LABEL>hospitalisation</LABEL>
<NAME>hospitalisation</NAME>
<DESCRIPTION>Was the subject confined to a hospital as a result of virus infection or problems occurring secondary to virus infection?</DESCRIPTION>
<FIELD_TYPE>
<TEXT_CHOICE_FIELD>
<TEXT_VALUE>
<VALUE>no</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>yes</VALUE>
</TEXT_VALUE>
</TEXT_CHOICE_FIELD>
</FIELD_TYPE>
<MANDATORY>optional</MANDATORY>
<MULTIPLICITY>multiple</MULTIPLICITY>
</FIELD>
<FIELD>
<LABEL>illness duration</LABEL>
<NAME>illness duration</NAME>
<DESCRIPTION>The number of days the illness lasted. Example: 4</DESCRIPTION>
<FIELD_TYPE>
<TEXT_FIELD/>
</FIELD_TYPE>
<MANDATORY>optional</MANDATORY>
<MULTIPLICITY>multiple</MULTIPLICITY>
</FIELD>
<FIELD>
<LABEL>illness symptoms</LABEL>
<NAME>illness symptoms</NAME>
<DESCRIPTION>The symptoms that have been reported in relation to the illness, such as cough, diarrhea, fever, headache, malaise, myalgia, nausea, runny_nose, shortness_of_breath, sore_throat. If multiple exposures are applicable, please state them separated by semicolon.</DESCRIPTION>
<FIELD_TYPE>
<TEXT_AREA_FIELD/>
</FIELD_TYPE>
<MANDATORY>optional</MANDATORY>
<MULTIPLICITY>multiple</MULTIPLICITY>
</FIELD>
</FIELD_GROUP>
<FIELD_GROUP restrictionType="Any number or none of the fields">
<NAME>Collection event information</NAME>
<FIELD>
<LABEL>collection date</LABEL>
<NAME>collection date</NAME>
<DESCRIPTION>The date of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid ISO8601 compliant times: 2008-01-23T19:23:10+00:00; 2008-01-23T19:23:10; 2008-01-23; 2008-01; 2008.</DESCRIPTION>
<FIELD_TYPE>
<TEXT_FIELD>
<REGEX_VALUE>(^[12][0-9]{3}(-(0[1-9]|1[0-2])(-(0[1-9]|[12][0-9]|3[01])(T[0-9]{2}:[0-9]{2}(:[0-9]{2})?Z?([+-][0-9]{1,2})?)?)?)?(/[0-9]{4}(-[0-9]{2}(-[0-9]{2}(T[0-9]{2}:[0-9]{2}(:[0-9]{2})?Z?([+-][0-9]{1,2})?)?)?)?)?$)|(^not collected$)|(^not provided$)|(^restricted access$)</REGEX_VALUE>
</TEXT_FIELD>
</FIELD_TYPE>
<MANDATORY>recommended</MANDATORY>
<MULTIPLICITY>multiple</MULTIPLICITY>
</FIELD>
<FIELD>
<LABEL>geographic location (country and/or sea)</LABEL>
<NAME>geographic location (country and/or sea)</NAME>
<DESCRIPTION>The geographical origin of the sample as defined by the country or sea. Country or sea names should be chosen from the INSDC country list (http://insdc.org/country.html).</DESCRIPTION>
<FIELD_TYPE>
<TEXT_CHOICE_FIELD>
<TEXT_VALUE>
<VALUE>Afghanistan</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Albania</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Algeria</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>American Samoa</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Andorra</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Angola</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Anguilla</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Antarctica</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Antigua and Barbuda</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Arctic Ocean</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Argentina</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Armenia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Aruba</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Ashmore and Cartier Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Atlantic Ocean</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Australia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Austria</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Azerbaijan</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Bahamas</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Bahrain</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Baker Island</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Baltic Sea</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Bangladesh</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Barbados</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Bassas da India</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Belarus</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Belgium</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Belize</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Benin</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Bermuda</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Bhutan</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Bolivia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Borneo</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Bosnia and Herzegovina</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Botswana</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Bouvet Island</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Brazil</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>British Virgin Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Brunei</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Bulgaria</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Burkina Faso</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Burundi</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Cambodia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Cameroon</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Canada</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Cape Verde</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Cayman Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Central African Republic</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Chad</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Chile</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>China</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Christmas Island</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Clipperton Island</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Cocos Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Colombia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Comoros</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Cook Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Coral Sea Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Costa Rica</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Cote d'Ivoire</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Croatia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Cuba</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Curacao</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Cyprus</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Czech Republic</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Democratic Republic of the Congo</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Denmark</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Djibouti</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Dominica</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Dominican Republic</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>East Timor</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Ecuador</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Egypt</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>El Salvador</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Equatorial Guinea</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Eritrea</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Estonia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Ethiopia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Europa Island</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Falkland Islands (Islas Malvinas)</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Faroe Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Fiji</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Finland</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>France</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>French Guiana</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>French Polynesia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>French Southern and Antarctic Lands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Gabon</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Gambia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Gaza Strip</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Georgia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Germany</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Ghana</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Gibraltar</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Glorioso Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Greece</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Greenland</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Grenada</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Guadeloupe</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Guam</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Guatemala</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Guernsey</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Guinea</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Guinea-Bissau</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Guyana</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Haiti</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Heard Island and McDonald Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Honduras</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Hong Kong</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Howland Island</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Hungary</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Iceland</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>India</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Indian Ocean</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Indonesia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Iran</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Iraq</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Ireland</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Isle of Man</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Israel</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Italy</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Jamaica</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Jan Mayen</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Japan</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Jarvis Island</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Jersey</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Johnston Atoll</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Jordan</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Juan de Nova Island</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Kazakhstan</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Kenya</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Kerguelen Archipelago</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Kingman Reef</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Kiribati</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Kosovo</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Kuwait</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Kyrgyzstan</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Laos</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Latvia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Lebanon</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Lesotho</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Liberia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Libya</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Liechtenstein</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Lithuania</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Luxembourg</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Macau</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Macedonia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Madagascar</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Malawi</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Malaysia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Maldives</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Mali</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Malta</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Marshall Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Martinique</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Mauritania</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Mauritius</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Mayotte</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Mediterranean Sea</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Mexico</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Micronesia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Midway Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Moldova</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Monaco</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Mongolia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Montenegro</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Montserrat</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Morocco</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Mozambique</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Myanmar</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Namibia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Nauru</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Navassa Island</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Nepal</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Netherlands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>New Caledonia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>New Zealand</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Nicaragua</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Niger</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Nigeria</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Niue</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Norfolk Island</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>North Korea</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>North Sea</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Northern Mariana Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Norway</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Oman</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Pacific Ocean</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Pakistan</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Palau</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Palmyra Atoll</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Panama</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Papua New Guinea</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Paracel Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Paraguay</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Peru</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Philippines</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Pitcairn Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Poland</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Portugal</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Puerto Rico</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Qatar</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Republic of the Congo</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Reunion</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Romania</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Ross Sea</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Russia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Rwanda</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Saint Helena</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Saint Kitts and Nevis</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Saint Lucia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Saint Pierre and Miquelon</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Saint Vincent and the Grenadines</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Samoa</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>San Marino</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Sao Tome and Principe</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Saudi Arabia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Senegal</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Serbia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Seychelles</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Sierra Leone</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Singapore</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Sint Maarten</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Slovakia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Slovenia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Solomon Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Somalia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>South Africa</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>South Georgia and the South Sandwich Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>South Korea</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Southern Ocean</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Spain</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Spratly Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Sri Lanka</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Sudan</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Suriname</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Svalbard</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Swaziland</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Sweden</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Switzerland</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Syria</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Taiwan</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Tajikistan</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Tanzania</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Tasman Sea</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Thailand</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Togo</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Tokelau</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Tonga</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Trinidad and Tobago</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Tromelin Island</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Tunisia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Turkey</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Turkmenistan</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Turks and Caicos Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Tuvalu</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>USA</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Uganda</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Ukraine</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>United Arab Emirates</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>United Kingdom</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Uruguay</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Uzbekistan</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Vanuatu</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Venezuela</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Viet Nam</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Virgin Islands</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Wake Island</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Wallis and Futuna</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>West Bank</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Western Sahara</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Yemen</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Zambia</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>Zimbabwe</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>not applicable</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>not collected</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>not provided</VALUE>
</TEXT_VALUE>
<TEXT_VALUE>
<VALUE>restricted access</VALUE>
</TEXT_VALUE>
</TEXT_CHOICE_FIELD>
</FIELD_TYPE>
<MANDATORY>mandatory</MANDATORY>
<MULTIPLICITY>multiple</MULTIPLICITY>
</FIELD>
<FIELD>
<LABEL>geographic location (latitude)</LABEL>
<NAME>geographic location (latitude)</NAME>
<DESCRIPTION>The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in WGS84 system</DESCRIPTION>
<UNITS>
<UNIT>DD</UNIT>
</UNITS>
<FIELD_TYPE>
<TEXT_FIELD>
<REGEX_VALUE>(^[+-]?[0-9]+.?[0-9]{0,8}$)|(^not collected$)|(^not provided$)|(^restricted access$)</REGEX_VALUE>
</TEXT_FIELD>
</FIELD_TYPE>
<MANDATORY>recommended</MANDATORY>
<MULTIPLICITY>multiple</MULTIPLICITY>
</FIELD>
<FIELD>
<LABEL>geographic location (longitude)</LABEL>
<NAME>geographic location (longitude)</NAME>
<DESCRIPTION>The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in WGS84 system</DESCRIPTION>
<UNITS>
<UNIT>DD</UNIT>
</UNITS>
<FIELD_TYPE>
<TEXT_FIELD>
<REGEX_VALUE>(^[+-]?[0-9]+.?[0-9]{0,8}$)|(^not collected$)|(^not provided$)|(^restricted access$)</REGEX_VALUE>
</TEXT_FIELD>
</FIELD_TYPE>
<MANDATORY>recommended</MANDATORY>
<MULTIPLICITY>multiple</MULTIPLICITY>
</FIELD>
<FIELD>
<LABEL>geographic location (region and locality)</LABEL>
<NAME>geographic location (region and locality)</NAME>
<DESCRIPTION>The geographical origin of the sample as defined by the specific region name followed by the locality name.</DESCRIPTION>
<FIELD_TYPE>
<TEXT_FIELD/>
</FIELD_TYPE>
<MANDATORY>recommended</MANDATORY>
<MULTIPLICITY>multiple</MULTIPLICITY>
</FIELD>
</FIELD_GROUP>
</DESCRIPTOR>
</CHECKLIST>
</CHECKLIST_SET>
`;function appendInfo(E,T){E=E.charAt(0).toUpperCase()+E.slice(1);const L=document.querySelector("#ena-checklist-info"),A=document.createElement("dt"),U=document.createElement("dd");A.innerHTML=E,U.innerHTML=T,L.appendChild(A),L.appendChild(U)}function changedKeep(E){E.getAttribute("name").replace("ommit","inpfield");const T=document.querySelector();E.checked?T.value=1:T.value=0}function replaceIndices(E,T){Array.from(E.children).forEach(E=>{Array.from(E.children).forEach(E=>{E.setAttribute("name",E.name.replace("+0+",`+${T}+`))})})}function createDefaultValSelect(E){const L=document.createElement("select"),T=document.createElement("option");return T.innerHTML="---------",T.value="",L.add(T),E.options.forEach(E=>{let T=document.createElement("option");T.innerHTML=E,T.value=E,L.add(T)}),L}function replaceDefaultValField(E,T,L){let A=E.querySelector(`[name='inpfield+${T}+default']`),U=null;"select"==L.type?U=createDefaultValSelect(L):"text"==L.type&&null!==L.regex?A.setAttribute("pattern",L.regex):"textarea"==L.type&&(U=document.createElement("textarea")),null!==U&&(U.setAttribute("name",A.getAttribute("name")),A.parentNode.replaceChild(U,A))}function setRowValues(E,T,L){E.querySelector(`[name='inpfield+${T}+enalabel']`).value=L.name,E.querySelector(`[name='inpfield+${T}+description']`).value=L.description,E.querySelector(`[name='inpfield+${T}+importance']`).value=L.importance;const A=E.querySelector(`[name='ommit+${T}+ena']`),U=E.querySelector(`[name='inpfield+${T}+ena']`);"mandatory"==L.importance?(U.value=1,A.disabled=!0,A.checked=!0):"recommended"==L.importance&&(U.value=1,A.checked=!0),replaceDefaultValField(E,T,L.default)}function addNewRow(E=null){const T=document.querySelector("#fields-editor-tab").tBodies[0],L=T.querySelector("tr.template").cloneNode(!0);var A=T.rows.length-1;L.classList.remove("template"),replaceIndices(L,A),T.appendChild(L),null!==E&&setRowValues(L,A,E)}function parseDefaultValue(E){E=E.querySelector(":scope > FIELD_TYPE").children[0];let T={type:"text",regex:null,options:[]};return"TEXT_CHOICE_FIELD"==E.tagName?(T.type="select",T.options=Array.from(E.children).map(E=>E.children[0].innerHTML)):"TEXT_AREA_FIELD"==E.tagName?T.type="textarea":"TEXT_FIELD"==E.tagName&&0<E.children.length&&"REGEX_VALUE"==E.children[0].tagName&&(T.regex=E.children[0].innerHTML),T}function parseAttr(E){return{name:E.querySelector(":scope > NAME").innerHTML,importance:E.querySelector(":scope > MANDATORY").innerHTML,description:E.querySelector(":scope > DESCRIPTION").innerHTML,default:parseDefaultValue(E)}}function handleChecklist(E,T){var T=`/CHECKLIST_SET/CHECKLIST[@checklistType='Sample' and @accession='${T}']`,T=(appendInfo("primary id",E.evaluate(T+"/IDENTIFIERS/PRIMARY_ID",E,null,XPathResult.STRING_TYPE,null).stringValue),T+"/DESCRIPTOR"),L=(appendInfo("label",E.evaluate(T+"/LABEL",E,null,XPathResult.STRING_TYPE,null).stringValue),E.evaluate(T+"/NAME",E,null,XPathResult.STRING_TYPE,null).stringValue),L=(appendInfo("name",L),E.evaluate(T+"/DESCRIPTION",E,null,XPathResult.STRING_TYPE,null).stringValue),L=(appendInfo("name",L),E.evaluate(T+"/AUTHORITY",E,null,XPathResult.STRING_TYPE,null).stringValue),T=(appendInfo("authority",L),E.getElementsByTagName("FIELD_GROUP"));let A,U,V;Array.from(T).forEach(E=>{A=null===(A=E.querySelector(":scope > NAME"))?"N/A":A.innerHTML,U=null===(U=E.querySelector(":scope > DESCRIPTION"))?"N/A":U.innerHTML,appendInfo(A,U),V=E.querySelectorAll(":scope > FIELD"),Array.from(V).forEach(E=>{addNewRow(parseAttr(E))})})}function fetchXML(){const E=document.querySelector("#ena-checklist-accession").value;handleChecklist(xml=(new window.DOMParser).parseFromString(rawXML,"text/xml"),E)}