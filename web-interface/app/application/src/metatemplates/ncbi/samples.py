from ..base.excel_gen import ExcelGenerator

class NcbiSample(ExcelGenerator):

    tempfilename = "last_generated_ncbi.xlsx";
    attachement_prefix = "ncbi";
    extension = "xlsx";
    filename = f"samples.{extension}";

    @classmethod
    def populate(cls, ws, samples):
        for indx, sample in enumerate(samples):
            i = indx+13;
            ws[f"A{i}"] = sample["sample_name"];
            ws[f"B{i}"] = sample["sample_title"];
            ws[f"D{i}"] = sample["organism"];
            ws[f"E{i}"] = sample["collected_by"];
            ws[f"F{i}"] = sample["collection_date"];
            ws[f"G{i}"] = sample["geo_loc_name"];
            ws[f"H{i}"] = sample["host"];
            ws[f"I{i}"] = sample["host_disease"];
            ws[f"J{i}"] = sample["isolate"];
            ws[f"K{i}"] = sample["isolation_source"];
            ws[f"L{i}"] = sample["antiviral_treatment_agent"];
            ws[f"M{i}"] = sample["collection_device"];
            ws[f"N{i}"] = sample["collection_method"];
            ws[f"O{i}"] = sample["date_of_prior_antiviral_treat"];
            ws[f"P{i}"] = sample["date_of_prior_sars_cov_2_infection"];
            ws[f"Q{i}"] = sample["date_of_prior_sars_cov_2_vaccination"];
            ws[f"R{i}"] = sample["exposure_event"];
            ws[f"S{i}"] = sample["geo_loc_exposure"];
            ws[f"T{i}"] = sample["gisaid_accession"];
            ws[f"U{i}"] = sample["gisaid_virusname"];
            ws[f"V{i}"] = sample["host_age"];
            ws[f"W{i}"] = sample["host_anatomical_material"];
            ws[f"X{i}"] = sample["host_anatomical_part"];
            ws[f"Y{i}"] = sample["host_body_product"];
            ws[f"Z{i}"] = sample["host_disease_outcome"];
            ws[f"AA{i}"] = sample["host_health_state"];
            ws[f"AB{i}"] = sample["host_recent_travel_loc"];
            ws[f"AC{i}"] = sample["host_recent_travel_return_date"];
            ws[f"AD{i}"] = sample["host_sex"];
            #ws[f"AE{i}"] = sample["host_specimen_voucher"];
            ws[f"AF{i}"] = sample["host_subject_id"];
            ws[f"AG{i}"] = sample["lat_lon"];
            ws[f"AH{i}"] = sample["passage_method"];
            ws[f"AI{i}"] = sample["passage_number"];
            ws[f"AJ{i}"] = sample["prior_sars_cov_2_antiviral_treat_view"];
            ws[f"AK{i}"] = sample["prior_sars_cov_2_infection_view"];
            ws[f"AL{i}"] = sample["prior_sars_cov_2_vaccination_view"];
            ws[f"AM{i}"] = sample["purpose_of_sampling"];
            ws[f"AN{i}"] = sample["purpose_of_sequencing"];
            ws[f"AO{i}"] = sample["sars_cov_2_diag_gene_name_1"];
            ws[f"AP{i}"] = sample["sars_cov_2_diag_gene_name_2"];
            ws[f"AQ{i}"] = sample["sars_cov_2_diag_pcr_ct_value_1"];
            ws[f"AR{i}"] = sample["sars_cov_2_diag_pcr_ct_value_2"];
            ws[f"AS{i}"] = sample["sequenced_by"];
            ws[f"AT{i}"] = sample["vaccine_received"];
            ws[f"AU{i}"] = sample["virus_isolate_of_prior_infection"];
            ws[f"AV{i}"] = sample["description"];




    @classmethod
    def write(cls, samples):
        wb, ws = cls.create_worksheet("SARS-CoV-2");
        cls.populate(ws, samples);
        cls.save_excel(wb, cls.get_tempfile());
        wb.close();
