import numpy as np
import torch

def torch_matmul(A, B):
    """PyTorch matmul 구현"""
    return torch.matmul(A,B)

def numpy_matmul(A, B):
    """NumPy matmul 구현"""
    return np.matmul(A,B)


def main():
    tensor1 = torch.randn(1024,1024)
    tensor2 = torch.randn(1024,1024)
    
    torch_result = torch.matmul(tensor1, tensor2)

    numpy_matmul_result = numpy_matmul(tensor1.numpy(), tensor2.numpy())

    if torch.allclose(torch_result, torch.from_numpy(numpy_matmul_result)):
        print("Success")
    else: 
        print("Failure")


if __name__ == "__main__":
    main()
