import numpy as np
import scipy.sparse as sp

um = np.genfromtxt("Movielens/um.txt")
uu = np.genfromtxt("Movielens/uu.txt")
ua = np.genfromtxt("Movielens/ua.txt")
uo = np.genfromtxt("Movielens/uo.txt")
mg = np.genfromtxt("Movielens/mg.txt")
mm = np.genfromtxt("Movielens/mm.txt")

U = 943
A = 8
O = 21
M = 1682
G = 18

um_ = sp.coo_matrix((np.ones(um.shape[0]), (um[:, 0], um[:, 1])), shape=(U, M)).toarray()
uu_ = sp.coo_matrix((np.ones(uu.shape[0]), (uu[:, 0], uu[:, 1])), shape=(U, U)).toarray()
ua_ = sp.coo_matrix((np.ones(ua.shape[0]), (ua[:, 0], ua[:, 1])), shape=(U, A)).toarray()
uo_ = sp.coo_matrix((np.ones(uo.shape[0]), (uo[:, 0], uo[:, 1])), shape=(U, O)).toarray()
mg_ = sp.coo_matrix((np.ones(mg.shape[0]), (mg[:, 0], mg[:, 1])), shape=(M, G)).toarray()
mm_ = sp.coo_matrix((np.ones(mm.shape[0]), (mm[:, 0], mm[:, 1])), shape=(M, M)).toarray()

umu = np.matmul(um_, um_.T) > 0
umu = sp.coo_matrix(umu)
sp.save_npz("Movielens/umu.npz", umu)

uau = np.matmul(ua_, ua_.T) > 0
uau = sp.coo_matrix(uau)
sp.save_npz("Movielens/uau.npz", uau)

uou = np.matmul(uo_, uo_.T) > 0
uou = sp.coo_matrix(uou)
sp.save_npz("Movielens/uou.npz", uou)

umg = np.matmul(um_, mg_) > 0
umgmu = np.matmul(umg, umg.T) >0
umgmu = sp.coo_matrix(umgmu)
sp.save_npz("Movielens/umgmu.npz", umgmu)

umm = np.matmul(um_, mm_) > 0
ummmu = np.matmul(umm, umm.T) > 0
ummmu = sp.coo_matrix(ummmu)
sp.save_npz("Movielens/ummmu.npz", ummmu)

mum = np.matmul(um_.T, um_) > 0
mum = sp.coo_matrix(mum)
sp.save_npz("Movielens/mum.npz", mum)

mgm = np.matmul(mg_, mg_.T) > 0
mgm = sp.coo_matrix(mgm)
sp.save_npz("Movielens/mp_matrix/mgm.npz", mgm)

muu = np.matmul(um_.T, uu_) > 0
muuum = np.matmul(muu, muu.T) > 0
muuum = sp.coo_matrix(muuum)
sp.save_npz("Movielens/muuum.npz", muuum)


