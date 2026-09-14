'''
Template para circuito de um qubit
'''

from qiskit import *
from qiskit.visualization import plot_bloch_multivector, visualize_transition, plot_histogram
from qiskit_aer import Aer, AerSimulator
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import math

qc = QuantumCircuit(2,2)

# Set the initial state for each input
# [0,1] #|1> / [1,0] #|0>
qc.initialize([1,0], 0)
qc.initialize([1,0], 1)

qc.y(0)

# ==========================================
# NOVO: PLOTAR A ESFERA DE BLOCH AQUI
# Captura o estado logo após a porta H e antes de medir
estado_antes_da_medicao = Statevector(qc)
plot_bloch_multivector(estado_antes_da_medicao)
# ==========================================

qc.measure(0,0)
qc.measure(1,1)

# Draw using matplotlib
qc.draw('mpl')

# Running the circuit on the simulator
shots = 1000
backend = Aer.get_backend("statevector_simulator")
compiled_circuit = transpile(qc, backend)
run_out = backend.run(compiled_circuit, shots=shots).result()
out_state_vector = run_out.get_statevector()
out_counts = run_out.get_counts()

print(out_counts)

probs = {state: count / shots for state, count in out_counts.items()}

# Display the result
print("Estimated probabilities from", shots, "shots:")
for state, prob in sorted(probs.items()):
    # Espaços invisíveis que causavam erro corrigidos aqui
    print(f"{state}: {prob:.4f}")

plot_histogram(out_counts)

# Abre todas as imagens geradas (Circuito, Histograma e Esferas de Bloch)
plt.show()

'''
#Realizar os devidos imports
from qiskit import transpile, QuantumCircuit
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit_aer import Aer
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt


#Instanciar circuito quântico
qc = QuantumCircuit(1,1)


#Estado inicial de cada qubit -> [0,1] #|1> / [1,0] #|0>
initial_state_qubit0 = [1,0]
#Inicializar qubit (estado e índice do qubit)
qc.initialize(initial_state_qubit0, 0)


#Exibe o vetor de estados (colocar bloco de código como função)
state_vector = Statevector.from_instruction(qc)
print("State vector:")
print(state_vector)
for i, amp in enumerate(state_vector):
    print(f"|{format(i, f'{qc.num_qubits+1}b')}>: {amp.real:.3f} + {amp.imag:.3f}j")


#Aplicar portas quânticas
qc.z(0)

# ==========================================
# NOVO: PLOTAR A ESFERA DE BLOCH AQUI
# Pegamos o vetor de estados atual (após a porta X, antes de medir)
state_after_x = Statevector.from_instruction(qc)
# Criamos a figura da esfera de Bloch
plot_bloch_multivector(state_after_x)
# ==========================================

#Aplicar medição
qc.measure(0,0)

#Plotar circuito quântico
qc.draw('mpl')

#Executar o circuito
shots = 1000 #Nr de repetições do circuito
backend = Aer.get_backend("statevector_simulator") #Tipo de simulador
compiled_circuit = transpile(qc,backend) #Criar circuito para rodar
run_out = backend.run(compiled_circuit, shots=shots).result() #Rodar o circuito
out_counts = run_out.get_counts() #Pegar contagem da saída


#Plotar probabilidades por estado após medição
probs = {state: count / shots for state, count in out_counts.items()}

print("Estimated probabilities from", shots, "shots:")
for state, prob in sorted(probs.items()):
    print(f"{state}: {prob:.4f}")

plot_histogram(out_counts)

plt.show()


'''
