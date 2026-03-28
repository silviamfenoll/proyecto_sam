#proyecto_sam

## DESCRIPTION
This project has a Python script "main.py" which analyzes SAM files:
- It sums up the total number of alligned reads.
- It sums up how many reads have MAPQ = 60
- It calculates the percentage of reads with MAPQ = 60

## REQUISITES
- Python 3
- UV
- Nextflow
- rich library

## INSTALATION
1. Clone the repository
https://github.com/silviamfenoll/proyecto_sam.git
2. Install uv dependencies
```bash
uv install
```

## USE
Run the Python script
```bash
uv run main.py path/to/WT.sam
```

Run the script using Nextflow
```bash
nextflow run main.nf --sam path/to/WT.sam
```
This will generate an output.txt file with the results.



## INCLUDED FILES
main.py Python script
pyproject.toml Dependencies managed by UV
main.nf Nextflow workflow
README.md
