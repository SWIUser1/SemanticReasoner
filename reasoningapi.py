import sys
import os
import time
from prettytable import PrettyTable
import pandas as pd
from owlready2 import *


if __name__ == "__main__":
    time_dict = {}
    owlready2.reasoning.JAVA_MEMORY = 8000

    # gva = get_ontology("file:///mnt/c/Users/gopis/Desktop/django/semrec/ontology/gva.nt").load()
    # skos = get_ontology("http://www.w3.org/2004/02/skos/core#").load()

    for i in os.listdir('variants'):
        gva = get_ontology("file:///home/swiadmin/GVA/ontology/gva.nt").load()
        skos = get_ontology("http://www.w3.org/2004/02/skos/core#").load()
        print("Currently Running {} file".format(i))
        variant_ont = get_ontology("file:///home/swiadmin/SemanticReasoner/variants/{}".format(i)).load()

        with gva :
            class UnknownPhenotype(gva.Variant): pass

            class MAFVariant(gva.Variant): pass
            class NMAFVariant(gva.Variant): pass
            class PSDamaging(gva.Variant): pass
            class UnknownClinvar(gva.Variant): pass
            class KnownPhenotype(gva.Variant): pass
            class UncertainSignificance1(gva.Variant):
                equivalent_to = [KnownPhenotype & MAFVariant  & UnknownClinvar ]
                
            class UncertainSignificance2(gva.Variant) :
                equivalent_to =  [UnknownClinvar & UnknownPhenotype]

            class PathogenicClinvar(gva.Variant): pass
            class Pathogenic1(gva.Variant):
                equivalent_to = [KnownPhenotype & MAFVariant &  PathogenicClinvar]

            class Pathogenic2(gva.Variant):
                equivalent_to = [UnknownPhenotype &   PathogenicClinvar]

            class ClinVarLikelyPathogenic(gva.Variant): pass
            class LikelyPathogenic1(gva.Variant):
                equivalent_to = [KnownPhenotype & MAFVariant &  ClinVarLikelyPathogenic]

            class LikelyPathogenic2(gva.Variant):
                equivalent_to = [UnknownPhenotype &  ClinVarLikelyPathogenic]

            class ClinVarLikelyBenign(gva.Variant): pass
            class LikelyBenign1(gva.Variant):
                equivalent_to = [KnownPhenotype & MAFVariant &  ClinVarLikelyBenign]

            class LikelyBenign2(gva.Variant):
                equivalent_to = [UnknownPhenotype &  ClinVarLikelyBenign]

            class ClinVarBenign(gva.Variant): pass
            class PSBT(gva.Variant): pass
            class Benign(gva.Variant):
                equivalent_to = [ ClinVarBenign]
            
            class NovelGene(gva.Variant):
                equivalent_to = [UnknownPhenotype & NMAFVariant ]
            

            Imp().set_as_rule("""Variant(?v), hasObservation(?v , ?obs),hasCategory(?obs, ?cat),hasCategory(?cat,?grp),prefLabel(?grp, ?lbl), stringEqualIgnoreCase(?lbl,"Phenotype Match"),hasScore(?obs, ?score), equal(?score, 0.0) -> UnknownPhenotype(?v)""",[gva,skos])
            Imp().set_as_rule("""Variant(?v), hasObservation(?v , ?obs), hasCategory(?obs, ?cat), hasCategory(?cat,?grp),prefLabel(?grp, ?lbl), stringEqualIgnoreCase(?lbl,"Frequency of Variants"),isAbout(?obs,?sem),prefLabel(?sem, ?semlbl), stringEqualIgnoreCase(?semlbl,"Very Rare Allele Frequency Variant") -> MAFVariant(?v)""",[gva,skos])
            Imp().set_as_rule("""Variant(?v), hasObservation(?v , ?obs), hasCategory(?obs, ?cat), hasCategory(?cat,?grp),prefLabel(?grp, ?lbl), stringEqualIgnoreCase(?lbl,"Frequency of Variants"),isAbout(?obs,?sem),prefLabel(?sem, ?semlbl), stringEqualIgnoreCase(?semlbl,"Rare Allele Frequency Variant") -> MAFVariant(?v)""",[gva,skos])
            Imp().set_as_rule("""Variant(?v), hasObservation(?v , ?obs), hasCategory(?obs, ?cat), hasCategory(?cat,?grp),prefLabel(?grp, ?lbl), stringEqualIgnoreCase(?lbl,"Frequency of Variants"),isAbout(?obs,?sem),prefLabel(?sem, ?semlbl), stringEqualIgnoreCase(?semlbl,"Low Allele Frequency Variant") -> MAFVariant(?v)""",[gva,skos])
            Imp().set_as_rule("""Variant(?v), hasObservation(?v , ?obs), hasCategory(?obs, ?cat), hasCategory(?cat,?grp),prefLabel(?grp, ?lbl), stringEqualIgnoreCase(?lbl,"Frequency of Variants"),isAbout(?obs,?sem),prefLabel(?sem, ?semlbl), stringEqualIgnoreCase(?semlbl,"Slightly High Allele Frequency Variant") -> MAFVariant(?v)""",[gva,skos])
            Imp().set_as_rule("""Variant(?v), hasObservation(?v , ?obs), hasCategory(?obs, ?cat), hasCategory(?cat,?grp),prefLabel(?grp, ?lbl), stringEqualIgnoreCase(?lbl,"Frequency of Variants"),isAbout(?obs,?sem),prefLabel(?sem, ?semlbl), stringEqualIgnoreCase(?semlbl,"Novel Allele Frequency Variant") -> MAFVariant(?v)""",[gva,skos])
            Imp().set_as_rule("""Variant(?v), hasObservation(?v , ?obs), hasCategory(?obs, ?cat), hasCategory(?cat,?grp),prefLabel(?grp, ?lbl), stringEqualIgnoreCase(?lbl,"Clinvar Details"),isAbout(?obs,?sem),prefLabel(?sem, ?semlbl), stringEqualIgnoreCase(?semlbl,"ClinVar Uncertain Significance") -> UnknownClinvar(?v)""",[gva,skos])
            Imp().set_as_rule("""Variant(?v), hasObservation(?v , ?obs), hasCategory(?obs, ?cat), hasCategory(?cat,?grp),prefLabel(?grp, ?lbl), stringEqualIgnoreCase(?lbl,"Clinvar Details"),isAbout(?obs,?sem),prefLabel(?sem, ?semlbl), stringEqualIgnoreCase(?semlbl,"ClinVar Unknown") -> UnknownClinvar(?v)""",[gva,skos])
            Imp().set_as_rule("""Variant(?v), hasObservation(?v , ?obs), hasCategory(?obs, ?cat), hasCategory(?cat,?grp),prefLabel(?grp, ?lbl), stringEqualIgnoreCase(?lbl,"Clinvar Details"),isAbout(?obs,?sem),prefLabel(?sem, ?semlbl), stringEqualIgnoreCase(?semlbl,"ClinVar Conflicting Interpretations of Pathogenicity") -> UnknownClinvar(?v)""",[gva,skos])
            Imp().set_as_rule("""Variant(?v), hasObservation(?v , ?obs),hasCategory(?obs, ?cat),hasCategory(?cat,?grp),prefLabel(?grp, ?lbl), stringEqualIgnoreCase(?lbl,"Phenotype Match"),hasScore(?obs, ?score), greaterThan(?score, 0.0) -> KnownPhenotype(?v)""",[gva,skos])
            Imp().set_as_rule("""Variant(?v), hasObservation(?v , ?obs), hasCategory(?obs, ?cat), hasCategory(?cat,?grp),prefLabel(?grp, ?lbl), stringEqualIgnoreCase(?lbl,"Clinvar Details"),isAbout(?obs,?sem),prefLabel(?sem, ?semlbl), stringEqualIgnoreCase(?semlbl,"ClinVar Pathogenic") -> PathogenicClinvar(?v)""",[gva,skos])
            Imp().set_as_rule("""Variant(?v), hasObservation(?v , ?obs), hasCategory(?obs, ?cat), hasCategory(?cat,?grp),prefLabel(?grp, ?lbl), stringEqualIgnoreCase(?lbl,"Clinvar Details"),isAbout(?obs,?sem),prefLabel(?sem, ?semlbl), stringEqualIgnoreCase(?semlbl,"ClinVar Likely Pathogenic") -> ClinVarLikelyPathogenic(?v)""",[gva,skos])
            Imp().set_as_rule("""Variant(?v), hasObservation(?v , ?obs), hasCategory(?obs, ?cat), hasCategory(?cat,?grp),prefLabel(?grp, ?lbl), stringEqualIgnoreCase(?lbl,"Clinvar Details"),isAbout(?obs,?sem),prefLabel(?sem, ?semlbl), stringEqualIgnoreCase(?semlbl,"ClinVar Likely Benign") -> ClinVarLikelyBenign(?v)""",[gva,skos])
            Imp().set_as_rule("""Variant(?v), hasObservation(?v , ?obs), hasCategory(?obs, ?cat), hasCategory(?cat,?grp),prefLabel(?grp, ?lbl), stringEqualIgnoreCase(?lbl,"Clinvar Details"),isAbout(?obs,?sem),prefLabel(?sem, ?semlbl), stringEqualIgnoreCase(?semlbl,"ClinVar Benign") -> ClinVarBenign(?v)""",[gva,skos])
            Imp().set_as_rule("""Variant(?v), hasObservation(?v , ?obs), hasCategory(?obs, ?cat), hasCategory(?cat,?grp),prefLabel(?grp, ?lbl), stringEqualIgnoreCase(?lbl,"Frequency of Variants"),isAbout(?obs,?sem),prefLabel(?sem, ?semlbl), stringEqualIgnoreCase(?semlbl,"Novel Allele Frequency Variant") -> NMAFVariant(?v)""",[gva,skos])

        try:

            to = time.time()
            sync_reasoner_pellet([variant_ont],infer_property_values = True, infer_data_property_values = True)
            time_dict[i] = time.time() - to
        except Exception:
            time_dict[i] = "Error"
            print("Unexpected error:", sys.exc_info()[0])
        print(time_dict[i])
        gva.destroy()

    # storing dictionary as csv
    pd.DataFrame.from_dict(data=time_dict, orient='index').to_csv('results.csv', header=False)

    # Row count from Excel
    row_count = [3902,1265,1931,4114,3891]

    # Initializing the Table
    Table = PrettyTable(["Filename", "No. of Variants", "Reasoning Time"])

    idx = 0
    for v,t in time_dict.items():
        Table.add_row([v,row_count[idx],t])
        idx += 1

    #print Table
    print(Table)
    
