import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

def plot_decision_regions(X, y, classifier, resolution=0.02, test_idx=None, xlabel=None, ylabel=None):
    # set up colours and markets
    markers = ['x', 'o', '^', 'v']
    colors = ['red', 'blue', 'grey', 'cyan']
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # predict each point in 2d feature space and plot as regions of classes
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(
        np.arange(x1_min, x1_max, resolution),
        np.arange(x2_min, x2_max, resolution)
    )
    Z = classifier.predict(np.stack([xx1.ravel(), xx2.ravel()], axis=1))
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)

    # plot observation
    for i, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha = 0.8,
            c=colors[i],
            marker=markers[i],
            label=cl
        )
        
    if test_idx:
        X_test, y_test = X[test_idx, :], y[test_idx]

        plt.scatter(
            X_test[:, 0],
            X_test[:, 1],
            c='',
            alpha=1,
            label='test set',
            s=100,
            linewidth=1,
            edgecolors='black'
        )

    plt.legend(loc='best')
    if ylabel:
        plt.ylabel(ylabel)
    
    if xlabel:
        plt.xlabel(xlabel)
