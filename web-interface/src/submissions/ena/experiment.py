from .xml import XML
from xml.dom import minidom


class ExperimentSetXML(XML):

    def __init__(self, fname="experiment"):
        super().__init__(root="EXPERIMENT_SET", fname=fname)


    def experiment_xml(self, sample: "Sample") -> None:
        exp = self.create_element("EXPERIMENT")
        exp.setAttribute("alias",
                         sample.get_attribute_value("ena_experiment_name"))
        study = self.create_element("STUDY_REF")
        study.setAttribute("accession",
                           sample.get_attribute_value("ena_study"))
        return exp


    def add_sample(self, sample: "Sample") -> None:
        experiment_xml = self.experiment_xml(sample)
        self.append_element(experiment_xml)

"""
<EXPERIMENT_SET>
   <EXPERIMENT alias="exp_mantis_religiosa">
       <TITLE>The 1KITE project: evolution of insects</TITLE>
       <STUDY_REF accession="SRP017801"/>
       <DESIGN>
           <DESIGN_DESCRIPTION/>
           <SAMPLE_DESCRIPTOR accession="SRS462875"/>
           <LIBRARY_DESCRIPTOR>
               <LIBRARY_NAME/>
               <LIBRARY_STRATEGY>RNA-Seq</LIBRARY_STRATEGY>
               <LIBRARY_SOURCE>TRANSCRIPTOMIC</LIBRARY_SOURCE>
               <LIBRARY_SELECTION>cDNA</LIBRARY_SELECTION>
               <LIBRARY_LAYOUT>
                   <PAIRED NOMINAL_LENGTH="250" NOMINAL_SDEV="30"/>
               </LIBRARY_LAYOUT>
               <LIBRARY_CONSTRUCTION_PROTOCOL>Messenger RNA (mRNA) was isolated using the Dynabeads mRNA Purification Kit (Invitrogen, Carlsbad Ca. USA) and then sheared using divalent cations at 72*C. These cleaved RNA fragments were transcribed into first-strand cDNA using II Reverse Transcriptase (Invitrogen, Carlsbad Ca. USA) and N6 primer (IDT). The second-strand cDNA was subsequently synthesized using RNase H (Invitrogen, Carlsbad Ca. USA) and DNA polymerase I (Invitrogen, Shanghai China). The double-stranded cDNA then underwent end-repair, a single `A? base addition, adapter ligati on, and size selection on anagarose gel (250 * 20 bp). At last, the product was indexed and PCR amplified to finalize the library prepration for the paired-end cDNA.</LIBRARY_CONSTRUCTION_PROTOCOL>
           </LIBRARY_DESCRIPTOR>
       </DESIGN>
       <PLATFORM>
           <ILLUMINA>
               <INSTRUMENT_MODEL>Illumina HiSeq 2000</INSTRUMENT_MODEL>
           </ILLUMINA>
       </PLATFORM>
       <EXPERIMENT_ATTRIBUTES>
           <EXPERIMENT_ATTRIBUTE>
               <TAG>library preparation date</TAG>
               <VALUE>2010-08</VALUE>
           </EXPERIMENT_ATTRIBUTE>
       </EXPERIMENT_ATTRIBUTES>
   </EXPERIMENT>
</EXPERIMENT_SET>
"""
