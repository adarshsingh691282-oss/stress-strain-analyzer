import numpy as np
import matplotlib.pyplot as plt

def analyze_stress_strain():
    """
    Models an engineering stress-strain curve for structural metal and calculates key properties.
    """
    # Synthetic engineering strain data from 0 to 0.2 (20% elongation)
    strain = np.linspace(0, 0.20, 500)
    
    # Material parameters (Structural Steel)
    E = 200e3         # Young's Modulus in MPa (200 GPa)
    sigma_y = 250.0   # Yield strength in MPa
    sigma_uts = 450.0 # Ultimate tensile strength in MPa
    strain_uts = 0.12 # Strain at UTS
    
    stress = np.zeros_like(strain)
    for i, eps in enumerate(strain):
        if eps <= sigma_y / E:
            # Elastic region: Hooke's Law (sigma = E * epsilon)
            stress[i] = E * eps
        elif eps <= strain_uts:
            # Plastic region / Strain hardening
            progress = (eps - (sigma_y / E)) / (strain_uts - (sigma_y / E))
            stress[i] = sigma_y + (sigma_uts - sigma_y) * (progress ** 0.5)
        else:
            # Necking region
            progress = (eps - strain_uts) / (0.20 - strain_uts)
            stress[i] = sigma_uts - (sigma_uts - 220) * (progress ** 2)

    print("--- Material Mechanical Properties ---")
    print(f"Young's Modulus (E): {E/1e3:.1f} GPa")
    print(f"Yield Strength: {sigma_y:.1f} MPa")
    print(f"Ultimate Tensile Strength (UTS): {sigma_uts:.1f} MPa")

    # Plotting Stress-Strain Curve
    plt.figure(figsize=(8, 5))
    plt.plot(strain * 100, stress, color='crimson', lw=2.5, label='Engineering Stress-Strain')
    plt.axhline(sigma_y, color='blue', linestyle='--', alpha=0.7, label=f'Yield Strength ({sigma_y} MPa)')
    plt.axhline(sigma_uts, color='darkgreen', linestyle='--', alpha=0.7, label=f'UTS ({sigma_uts} MPa)')
    
    plt.title('Engineering Stress-Strain Curve (Tensile Test)', fontsize=12, fontweight='bold')
    plt.xlabel('Engineering Strain (%)')
    plt.ylabel('Engineering Stress (MPa)')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    plt.savefig("stress_strain_plot.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    analyze_stress_strain()
