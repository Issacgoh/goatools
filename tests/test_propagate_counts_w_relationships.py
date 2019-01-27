#!/usr/bin/env python
"""Test propagate_counts up relationships as well as parent-child links."""

import sys
import os
# from itertools import combinations
# import collections as cx

from goatools.go_enrichment import GOEnrichmentStudy
from goatools.base import get_godag
from goatools.test_data.genes_NCBI_10090_ProteinCoding import GENEID2NT as GeneID2nt_mus
from goatools.test_data.nature3102_goea import get_geneid2symbol
from goatools.associations import get_assoc_ncbi_taxids

def test_pc_w_rels(prt=sys.stdout):
    """Test P-value calculations."""
    results_r0 = _get_results(propagate_counts=True, relationships=False, prt=prt)
    results_r1 = _get_results(propagate_counts=True, relationships=True, prt=prt)
    _chk_results(results_r0, results_r1, prt)

def _chk_results(results_r0, results_r1, prt):
    """Test propagate_counts up relationships as well as parent-child links."""
    prt.write('TBD: Compare results')
    pass

def _get_results(propagate_counts, relationships, prt=sys.stdout):
    """Run a GOEA. Return results"""
    taxid = 10090 # Mouse study
    file_obo = os.path.join(os.getcwd(), "go-basic.obo")
    obo_dag = get_godag(file_obo, prt, loading_bar=None)
    geneids_pop = set(GeneID2nt_mus.keys())
    assoc_geneid2gos = get_assoc_ncbi_taxids([taxid], loading_bar=None)
    geneids_study = get_geneid2symbol("nbt.3102-S4_GeneIDs.xlsx")
    goeaobj = GOEnrichmentStudy(
        geneids_pop,
        assoc_geneid2gos,
        obo_dag,
        propagate_counts=propagate_counts,
        alpha=0.05,
        methods=['fdr_bh'])
    return goeaobj.run_study(geneids_study, prt=prt)


if __name__ == '__main__':
    test_pc_w_rels()