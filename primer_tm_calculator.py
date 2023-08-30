from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq
import tkinter as tk
from tkinter import messagebox

MIXED_BASES = {'R': ['A', 'G'], 'Y': ['C', 'T'], 'S': ['G', 'C'], 'W': ['A', 'T'], 'K': ['G', 'T'], 'M': ['A', 'C'],
               'B': ['C', 'G', 'T'], 'D': ['A', 'G', 'T'], 'H': ['A', 'C', 'T'], 'V': ['A', 'C', 'G'], 'N': ['A', 'T', 'G', 'C']}

def expand_sequence(seq):
    expanded_seqs = [seq]
    for mixed_base in MIXED_BASES:
        new_seqs = []
        for seq in expanded_seqs:
            if mixed_base in seq:
                for base in MIXED_BASES[mixed_base]:
                    new_seqs.append(seq.replace(mixed_base, base, 1))
            else:
                new_seqs.append(seq)
        expanded_seqs = new_seqs
    return expanded_seqs

def calculate_tm_and_annealing():
    primer1 = primer1_entry.get()
    primer2 = primer2_entry.get()
    expanded_primers1 = expand_sequence(primer1)
    expanded_primers2 = expand_sequence(primer2)

    results = ""
    for primer1 in expanded_primers1:
        for primer2 in expanded_primers2:
            tm1 = mt.Tm_NN(Seq(primer1))
            tm2 = mt.Tm_NN(Seq(primer2))
            annealing_temp1 = tm1 - 5
            annealing_temp2 = tm2 - 5
            results += f"Primer1: {primer1}, Tm: {tm1}, Annealing Temperature: {annealing_temp1}\n"
            results += f"Primer2: {primer2}, Tm: {tm2}, Annealing Temperature: {annealing_temp2}\n"
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
