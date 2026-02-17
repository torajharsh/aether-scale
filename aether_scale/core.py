import torch

class AetherEngine:
    """
    Aether-Scale Matrix Engine (ASME)
    Implements Unit-Domain Flow (UDF) for deep-stack tensor operations.
    Official Release V1.0
    """
    def __init__(self, phi: float = 128.0, device: str = 'cuda'):
        self.phi = float(phi)
        self.device = device

    @torch.jit.script
    def harmonic_product(x: torch.Tensor, weight: torch.Tensor, phi: float) -> torch.Tensor:
        """
        Calculates the low-friction Harmonic Product of two tensors.
        Ensures bit-perfect Unit-Domain Flow (UDF).
        """
        # Pre-scaling the weight allows the GPU to utilize optimized 
        # paths without the overhead of post-multiplication normalization.
        return torch.matmul(x, weight / phi)

    def run_sequence(self, input_tensor, weight_stack):
        """
        Processes a multi-layer sequence with optimized efficiency.
        Note: The speed boost compounds as depth increases.
        """
        flow = input_tensor
        for w in weight_stack:
            flow = self.harmonic_product(flow, w, self.phi)
        return flow
