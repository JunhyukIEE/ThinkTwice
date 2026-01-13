"""
Patch PyTorch to use CPU for lgamma operations to avoid RTX 4090 JIT compilation issues.
This is a workaround for PyTorch 1.12.1 + CUDA 11.3 not supporting sm_89 architecture.
"""

import torch
import warnings

# Save original lgamma function
_original_lgamma = torch.lgamma

def patched_lgamma(input):
    """
    Wrapper for torch.lgamma that moves tensor to CPU if on CUDA,
    computes lgamma, then moves back to original device.
    """
    if input.is_cuda:
        device = input.device
        # Compute on CPU to avoid nvrtc compilation issues
        result = _original_lgamma(input.cpu())
        return result.to(device)
    else:
        return _original_lgamma(input)

# Replace torch.lgamma with patched version
torch.lgamma = patched_lgamma
torch.Tensor.lgamma = lambda self: patched_lgamma(self)
torch.Tensor.lgamma_ = lambda self: self.copy_(patched_lgamma(self))

print("[RTX4090_PATCH] Applied CPU fallback for torch.lgamma to avoid sm_89 compilation issues")