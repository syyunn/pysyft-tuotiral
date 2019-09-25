def check_syft_sanity():
    """
    Check import-sanity of syft-framework and return torch-Hook,
    an overriding  method of torch
    :return: TorchHook Instance
    """
    try:
        import sys
        import syft
        import torch
        from torch.nn import Parameter
        import torch.nn as nn
        import torch.nn.functional as F

        hook = syft.TorchHook(torch)

        return hook, syft

    except ImportError:
        print("Import-Error occurred.")

        return -1


def generate_random_tensors(num_tensors, size=5):
    """
    Generate random-torch-tensor where each element \in [0,1) w/ given size
    :return: num_tensors * torch-random-tensor
    """
    import torch
    rand_tensors = [torch.rand(size) for i in range(num_tensors)]

    return rand_tensors


def send_data_to_server(data, server):
    """
    Generate pointers that represents sending data to server
    :return: Pointers that are pointing data to server
    """
    ptrs = []
    for datum in data:
        ptr = datum.send(server)
        ptrs.append(ptr)
    return ptrs


def ptr_addition(ptrs, permute_idxs):
    """
    Add ptrs w/ the given permutation idx
    :return: result of ptr addition
    """

    init = ptrs[permute_idxs[0]]

    for idx in permute_idxs[1:]:
        init += ptrs[idx]

    return init


def retrieve_ptrs_from_server(ptrs):
    try:
        for ptr in ptrs:
            ptr.get()
        return 1
    except NameError:
        return -1
