import tkinter as tk
from tkinter import messagebox
from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq
import itertools

MIXED_BASES = {'R': ['A', 'G'], 'Y': ['C', 'T'], 'S': ['G', 'C'], 'W': ['A', 'T'], 'K': ['G', 'T'], 'M': ['A', 'C'],
               'B': ['C', 'G', 'T'], 'D': ['A', 'G', 'T'], 'H': ['A', 'C', 'T'], 'V': ['A', 'C', 'G'], 'N': ['A', 'T', 'G', 'C']}

def expand_sequence(seq):
    seq = seq.upper()
    for base in MIXED_BASES:
        if base in seq:
            return list(itertools.product(*[MIXED_BASES[base] if b == base else b for b in seq]))
    return [seq]

def calculate_tm_and_annealing():
    primer1 = primer1_entry.get()
    primer2 = primer2_entry.get()

    expanded_primers1 = expand_sequence(primer1)
    expanded_primers2 = expand_sequence(primer2)

    tm1_values = [mt.Tm_NN(Seq(''.join(primer))) for primer in expanded_primers1]
    tm2_values = [mt.Tm_NN(Seq(''.join(primer))) for primer in expanded_primers2]

    avg_tm1 = sum(tm1_values) / len(tm1_values)
    avg_tm2 = sum(tm2_values) / len(tm2_values)

    avg_annealing_temp1 = avg_tm1 - 5
    avg_annealing_temp2 = avg_tm2 - 5

    results = ""
    for i, primer in enumerate(expanded_primers1):
        results += f"Primer1: {''.join(primer)}, Tm: {tm1_values[i]}, Annealing Temperature: {tm1_values[i] - 5}\n"
    for i, primer in enumerate(expanded_primers2):
        results += f"Primer2: {''.join(primer)}, Tm: {tm2_values[i]}, Annealing Temperature: {tm2_values[i] - 5}\n"
    results += f"Primer1 Average Tm: {avg_tm1}, Average Annealing Temperature: {avg_annealing_temp1}\n"
    results += f"Primer2 Average Tm: {avg_tm2}, Average Annealing Temperature: {avg_annealing_temp2}\n"
    messagebox.showinfo("Results", results)

root = tk.Tk()
root.title("Primer Tm and Annealing Temperature Calculator")

primer1_label = tk.Label(root, text="Primer 1: ")
primer1_label.pack()
primer1_entry = tk.Entry(root)
primer1_entry.pack()

primer2_label = tk.Label(root, text="Primer 2: ")
primer2_label.pack()
primer2_entry = tk.Entry(root)
primer2_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_tm_and_annealing)
calculate_button.pack()

root.mainloop()
