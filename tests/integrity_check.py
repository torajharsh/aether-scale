import torch
import time
from aether_scale.core import AetherEngine

def run_v1_0_validation(layers=100, dim=1024):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    phi = 128.0
    engine = AetherEngine(phi=phi, device=device)
    
    # Initialize Test Data
    x_init = torch.randn(dim, dim).to(device)
    weights = [torch.randn(dim, dim).to(device) for _ in range(layers)]

    print(f"--- ASME V1.0 Integrity Check ({layers} Layers) ---")

    # Standard Path (Re-normalization comparison)
    x_std = x_init
    for w in weights:
        x_std = (torch.matmul(x_std, w)) / phi

    # Aether-Scale Path
    x_asme = engine.run_sequence(x_init, weights)

    # Validation
    mse = torch.mean((x_std - x_asme)**2).item()
    print(f"Final Integrity MSE: {mse:.12f}")
    print(f"Status: {'PASSED' if mse < 1e-10 else 'FAILED'}")

if __name__ == "__main__":
    run_v1_0_validation()
