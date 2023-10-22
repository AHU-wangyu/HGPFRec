import numpy as np
import scipy.sparse as sp
import torch
import os

def normalize_adj(adj):
    """Symmetrically normalize adjacency matrix."""
    adj = sp.coo_matrix(adj)
    rowsum = np.array(adj.sum(1))
    d_inv_sqrt = np.power(rowsum, -0.5).flatten()
    d_inv_sqrt[np.isinf(d_inv_sqrt)] = 0.
    d_mat_inv_sqrt = sp.diags(d_inv_sqrt)
    return adj.dot(d_mat_inv_sqrt).transpose().dot(d_mat_inv_sqrt).tocoo()


def sparse_mx_to_torch_sparse_tensor(sparse_mx):
    """Convert a scipy sparse matrix to a torch sparse tensor."""
    sparse_mx = sparse_mx.tocoo().astype(np.float32)
    indices = torch.from_numpy(
        np.vstack((sparse_mx.row, sparse_mx.col)).astype(np.int64))
    values = torch.from_numpy(sparse_mx.data)
    shape = torch.Size(sparse_mx.shape)
    return torch.sparse.FloatTensor(indices, values, shape)

def load_movielens():
    path = "../data/Movielens/mp_matrix/"
    umu = sp.load_npz(path + "umu.npz")
    uau = sp.load_npz(path + "uau.npz")
    uou = sp.load_npz(path + "uou.npz")
    umgmu = sp.load_npz(path + "umgmu.npz")
    ummmu = sp.load_npz(path + "ummmu.npz")
    mum = sp.load_npz(path + "mum.npz")
    mgm = sp.load_npz(path + "mgm.npz")
    muuum = sp.load_npz(path + "muuum.npz")

    umu = sparse_mx_to_torch_sparse_tensor(normalize_adj(umu))
    # uau = sparse_mx_to_torch_sparse_tensor(normalize_adj(uau))
    uou = sparse_mx_to_torch_sparse_tensor(normalize_adj(uou))
    umgmu = sparse_mx_to_torch_sparse_tensor(normalize_adj(umgmu))
    # ummmu = sparse_mx_to_torch_sparse_tensor(normalize_adj(ummmu))
    mum = sparse_mx_to_torch_sparse_tensor(normalize_adj(mum))
    mgm = sparse_mx_to_torch_sparse_tensor(normalize_adj(mgm))
    # muuum = sparse_mx_to_torch_sparse_tensor(normalize_adj(muuum))

    user_key = "user"
    item_key = "movie"
    meta_paths = {
        "user": [["umu"], ["uou"], ["umgmu"]],
        # , ["uau"], ["ummmu"]
        "movie": [["mum"], ["mgm"]],
        # , ["muuum"]
    }
    #     ,uau,ummmu
    # ,muuum
    return meta_paths,user_key,item_key,[umu,uou,umgmu],[mum,mgm]

def load_data(dataset):
    if dataset == "Movielens":
        data = load_movielens()
    return data

# if __name__ == '__main__':
#     load_movielens()