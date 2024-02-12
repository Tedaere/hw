import os
from forest import Forest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def scatter_data(x, y, file_name, xlabel, ylabel):
    fig = plt.figure()
    ax1 = fig.add_subplot()

    ax1.scatter(x, y)
    
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.grid(True)
    ax1.legend()
    
    cwd = os.getcwd()
    plt.savefig(os.path.join(cwd, file_name +'.png'))


def make_hist(data, file_name, xlabel, ylabel, n_bins):
    fig, axs = plt.subplots(1, 1)
    axs.hist(data, bins=n_bins)
    axs.set_xlabel(xlabel)
    axs.set_ylabel(ylabel)
    
    cwd = os.getcwd()
    plt.savefig(os.path.join(cwd, file_name +'.png'))


f = pd.read_csv("sdss_redshift.csv")
danfot = ['u', 'g', 'r', 'i', 'z']
data = np.array(f[danfot])
res = np.array(f['redshift'])

data_train, data_test, res_train, res_test = train_test_split(data, res, test_size=0.35, random_state=42)
depth = int(random.random() * depth_scaler * len(data))
forest = RandomForest(20, data_train, res_train, depth)
predictm = forest.predict(data_test)

otkolonen_train = res_train - predictm
train_std = np.std(otkolonen_train)
train_mean = np.mean(otkolonen_train)

predictm = forest.predict(data_test)

otkolonen_test = res_test - predictm

test_std = np.std(otkolonen_test)
test_mean = np.mean(otkolonen_test)
dic = {
        'train': str(train_std),
        'test': str(test_std)
    }
with open('redhsift.json', 'w') as file:
    json.dump(dic, file)
with open('redhsift.json', 'r') as file:
    c = json.load(file)

predictm = forest.predict(data)
scatter_data(range(len(data)), res - predictm, "redhift", "Элемент выборки", "Отклонение от истины")

file = pd.read_csv("sdss.csv")
data = file[danfot]

file['redshift'] = forest.predict(data)
file.to_csv('sdss_predict.csv')
