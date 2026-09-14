'''
27/05/2025 - Rodrigo Pasti
'''
from qiskit import *
from qiskit.visualization import plot_bloch_multivector, visualize_transition, plot_histogram
from qiskit_aer import Aer, AerSimulator
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import mathpyt



qc = QuantumCircuit(3,3)


#Set the initial state for each input
# [0,1] #|1> / [1,0] #|0>
qc.initialize([1,0], 0)
qc.initialize([1,0], 1)

#qc.rx(1.0, 0)
#qc.rz(1.0, 0)
qc.h(0)
qc.t(0)

# ==========================================
# NOVO: PLOTAR A ESFERA DE BLOCH AQUI
# Captura o estado logo após a porta H e antes de medir
estado_antes_da_medicao = Statevector(qc)
plot_bloch_multivector(estado_antes_da_medicao)
# ==========================================

qc.measure(0,0)
qc.measure(1,1)


#Draw using matplotlib
qc.draw('mpl')


#Running the circuit on the simulator
shots = 1000
backend = Aer.get_backend("statevector_simulator")
#noise_model = NoiseModel.from_backend("statevector_simulator")
#backend = AerSimulator(method='statevector_simulator', noise_model=noise_model)
compiled_circuit = transpile(qc,backend)
run_out = backend.run(compiled_circuit, shots=shots).result()
out_state_vector = run_out.get_statevector()
out_counts = run_out.get_counts()
#out_unitary_matrix = run_out.get_unitary()


print(out_counts)

probs = {state: count / shots for state, count in out_counts.items()}

# Display the result
print("Estimated probabilities from", shots, "shots:")
for state, prob in sorted(probs.items()):
    print(f"{state}: {prob:.4f}")



plot_histogram(out_counts)
#print(out_unitary_matrix)


plt.show()



