from __future__ import print_function
import numpy as np
import h5py
from sklearn.model_selection import train_test_split


def load_one_file(file_num):
	file_name = 'A0' + str(file_num) + 'T_slice.mat'
	cur_data = h5py.File(file_name, 'r')
	X = np.copy(cur_data['image'])[:, 0:22, :]
	y = np.copy(cur_data['type'])[0,0:X.shape[0]:1]
	y = np.asarray(y)
	print('Data loaded from' + file_name + ':')
	print(X.shape)
	print(y.shape)
	
	return X,y

#split data into testdata(#test_size) + rest(train + val)
def split_test(test_size, X, y):
	X_rest, X_test, y_rest, y_test = train_test_split(X, y, test_size = test_size)

	return X_rest, X_test, y_rest, y_test

#split data into val data + train data
def split_val(val_size, X, y):
	X_rest, X_val, y_rest, y_val = train_test_split(X, y, test_size = val_size)

	return X_rest, X_val, y_rest, y_val


def self_train_val_test(file_num, test_size, val_size):
		X_ori, y_ori = load_one_file(file_num)
		X, y = remove_nan(X_ori, y_ori)
		X_rest1, X_test, y_rest1, y_test = split_test(test_size, X, y)
		X_rest2, X_val, y_rest2, y_val = split_val(val_size, X_rest1, y_rest1)

		X_train = X_rest2
		y_train = y_train2

		return X_train, X_val, X_test, y_train, y_val, y_test

