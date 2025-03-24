
import numpy as np
import matplotlib.pyplot as plt


T = np.array([300, 310, 320, 330, 340])
P_s = np.array([5e5, 6e5, 7.2e5, 8.5e5, 1e6])

ln_P_s = np.log(P_s)
inv_T = 1 / T

pente, intercept = np.polyfit(inv_T, ln_P_s, 1)

plt.figure(figsize=(8, 5))
plt.plot(inv_T, ln_P_s, "o", label="Données expérimentales")
plt.plot(inv_T, pente * inv_T + intercept, "-", label=f"Ajustement linéaire\nPente = {pente:.2f}")
plt.xlabel("1/T (K⁻¹)")
plt.ylabel("ln(P_s)")
plt.title("Graphique de Clausius-Clapeyron")
plt.legend()
plt.grid()
plt.tight_layout()


plt.savefig("clausius_clapeyron_plot.pdf")
plt.show()

R = 8.314  # J·mol⁻¹·K⁻¹

L = -pente * R
print(f"Chaleur latente de vaporisation L ≈ {L:.2f} J·mol⁻¹")
