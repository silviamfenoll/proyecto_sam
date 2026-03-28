#!/usr/bin/env nextflow
params.sam = null
process analyze_sam {

    input:
    path sam_file
    path "main.py"

    output:
    file "output_WT.txt"

    script:
    """
    uv run main.py ${sam_file} > output_WT.txt
    """
}   
workflow {
    analyze_sam(params.sam, file("main.py"))
}
