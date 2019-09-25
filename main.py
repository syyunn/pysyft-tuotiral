import utils


def generate_computation_server(hook):
    """
    Generate computation_server that holds pointer sent from the local edges
    :return: computation_server
    """
    import syft
    server = syft.VirtualWorker(hook, id="c-server")

    return server


def main():
    hook, syft = utils.check_syft_sanity()
    server = generate_computation_server(hook)
    random_tensors = utils.generate_random_tensors(num_tensors=2, size=5)
    ptrs = utils.send_data_to_server(random_tensors, server)
    # z = utils.ptr_addition(ptrs, [0, 0])
    z_spot = ptrs[0] + ptrs[0]
    y_spot = ptrs[0] + ptrs[1]
    result = y_spot.get()

    import torch
    z = torch.add(ptrs[0], ptrs[1])
    z.get()

    pass

    location_boolean = (server == ptrs[0].location)
    tensor_id_at_server = ptrs[0].id_at_location
    ptr_owner = ptrs[0].owner
    local_worker = syft.local_worker
    owner_boolean = (ptr_owner == local_worker)
    pass

    ptrs_to_retrieve = ptrs + [z_spot]
    utils.retrieve_ptrs_from_server(ptrs_to_retrieve)
    pass


if __name__ == "__main__":
    main()
    pass
