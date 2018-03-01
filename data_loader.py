import numpy as np
import h5py

def data_loader(datapath, num_of_file):
	#loading 1 file for now
	X, y = None, None
	for i in range(1, num_of_file + 1):
		curpath = datapath + '/A0' + str(i) + 'T_slice.mat'
		curFile = h5py.File(curpath, 'r')
		curX = np.copy(curFile['image'])
		cury = np.copy(curFile['type'])
		cury = cury[0, 0:curX.shape[0]:1]
		cury = np.asarray(cury, dtype=np.int32)
		if i == 1:
			X = curX
			y = cury
		else:
			X = np.concatenate([X, curX])
			y = np.concatenate([np.asarray(y), np.asarray(cury)])
	# y = y[0, 0:X.shape[0]:1]
	# y = np.asarray(y, dtype=np.int32)		
		
	return X, y
		
# A01T = h5py.File('./project_datasets/A01T_slice.mat', 'r')
# X = np.copy(A01T['image'])
# y = np.copy(A01T['type'])
# y = y[0,0:X.shape[0]:1]
# y = np.asarray(y, dtype=np.int32)

X, y = data_loader('./project_datasets', 1)
print(X.shape)
print(y.shape)