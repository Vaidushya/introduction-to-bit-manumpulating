# Implementing a Logic Circuit using Bit Manipulation
def logic_circuit(A, B, C):
    and1 = A & B
    or1 = B | C
    and2 = B & C
    and3 = or1 & and2
    Q = and1 | and3
    
    return int(Q)

# Testing with inputs A=1, B=1, C=0
print(f"Output Q: {logic_circuit(1, 1, 0)}")
