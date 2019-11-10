{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "def plot_data(X, y):\n",
    "    \"\"\"\n",
    "    Plots the data points X and y into a new figure.\n",
    "    Parameters\n",
    "    ----------\n",
    "    X : ndarray, shape (n_samples, n_features)\n",
    "        Training vectors, where n_samples is the number of samples and n_features is the number of features.\n",
    "    y : ndarray, shape (n_samples,)\n",
    "        Target values (class labels in classification).\n",
    "    \"\"\"\n",
    "    pos = np.nonzero(y == 1)\n",
    "    neg = np.nonzero(y == 0)\n",
    "    plt.plot(X[pos, 0], X[pos, 1], linestyle='', marker='+', color='k')\n",
    "    plt.plot(X[neg, 0], X[neg, 1], linestyle='', marker='o', color='y')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
