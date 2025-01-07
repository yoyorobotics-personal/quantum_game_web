#yoyorobotics 2025/1/2
#quantum art first test art generator interactive

import tkinter as tk
from tkinter import ttk

import io
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile

def generate_quantum_random_bits(n_qubits=8):
    qc = QuantumCircuit(n_qubits, n_qubits)
    qc.h(range(n_qubits))  # Apply Hadamard gate to all qubits
    qc.measure(range(n_qubits), range(n_qubits))  # Measure qubits

    backend = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(qc, backend)
    job = backend.run(compiled_circuit)
    result = job.result()
    counts = result.get_counts(qc)
    return list(counts.keys())[0]  # Return the most frequent bitstring

def run_game():
    return generate_quantum_random_bits()

