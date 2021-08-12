# 𝑃(𝑋=4|𝑀𝐴)
import math
# print()
p4_A = math.exp(-1) * (1/math.sqrt(2*math.pi))
p4_B = math.exp(0) * (1/math.sqrt(2*math.pi))

pA_4 = p4_A * (1/2) / (p4_A + p4_B)
pB_4 = p4_B * (1/2) / (p4_A + p4_B)

print(pA_4)
print(pB_4)