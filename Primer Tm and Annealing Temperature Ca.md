# Primer Tm and Annealing Temperature Calculator

This Python script calculates the Tm (melting temperature) and annealing temperature of PCR primers. It uses the Nearest-Neighbor (NN) method for Tm calculation, which is currently the most accurate method because it considers the influence of neighboring base pairs in the primer sequence on the Tm value. 

The script also considers mixed bases in the primer sequence and calculates the Tm and annealing temperature for each possible sequence combination. 

The results are displayed in a GUI created using the Tkinter library.

## Dependencies

- Python 3.10
- Biopython
- Tkinter

## Installation

1. Clone this repository to your local machine.
2. Install the necessary Python packages. If you don't have them installed already, you can install them using pip:

```bash
pip install biopython
```

## Usage

1. Run the script using Python 3.10.

```bash
python primer_tm_calculator.py
```

2. Enter your primer sequences in the GUI that pops up. 

3. Click the "Calculate" button to calculate the Tm and annealing temperatures. The results will be displayed in a new window.

## Contribution

Contributions are always welcome! Please read the contribution guidelines first.

