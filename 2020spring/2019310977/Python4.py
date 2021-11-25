{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "![http://feng.li/](logo.png)Brought to you by [Dr. Feng Li](http://feng.li)\n",
    "\n",
    "**{Other Formats Available: [PDF](http://feng.li/python) | [HTML](http://feng.li/python) | [SLIDES](http://feng.li/python)}**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Major Python modules for Data Wrangling\n",
    "\n",
    "## `NumPy`\n",
    "\n",
    "`NumPy` is short for Numerical Python, is the foundational package for scientific computing in Python. It contains among other things:\n",
    "\n",
    "- a powerful N-dimensional array object\n",
    "- sophisticated (broadcasting) functions\n",
    "- tools for integrating C/C++ and Fortran code\n",
    "- useful linear algebra, Fourier transform, and random number capabilities\n",
    "\n",
    "Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases. \n",
    "\n",
    "- [NumPy Reference](http://docs.scipy.org/doc/numpy/reference/)\n",
    "- [NumPy User Guide](http://docs.scipy.org/doc/numpy/user/index.html)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## `SciPy` \n",
    "\n",
    "`SciPy` is a collection of packages addressing a number of different standard problem domains in scientific computing. Here is a sampling of the packages included:\n",
    "\n",
    "- `scipy.integrate` : numerical integration routines and differential equation solvers.\n",
    "- `scipy.linalg` : linear algebra routines and matrix decompositions extending beyond those provided in `numpy.linalg`.\n",
    "- `scipy.optimize` : function optimizers (minimizers) and root finding algorithms.\n",
    "- `scipy.signal` : signal processing tools.\n",
    "- `scipy.sparse` : sparse matrices and sparse linear system solvers.\n",
    "- `scipy.special` : wrapper around SPECFUN, a Fortran library implementing many common mathematical functions, such as the gamma function.\n",
    "- `scipy.stats` : standard continuous and discrete probability distributions (density functions, samplers, continuous distribution functions), various statistical tests, and more descriptive statistics.\n",
    "- `scipy.weave` : tool for using inline C++ code to accelerate array computations.\n",
    "\n",
    "- `scipy.cluster` :\tClustering algorithms\n",
    "- `scipy.fftpack` : Fast Fourier Transform routines\n",
    "- `scipy.integrate` : Integration and ordinary differential equation solvers\n",
    "- `scipy.interpolate` : Interpolation and smoothing splines\n",
    "- `scipy.ndimage` : N-dimensional image processing\n",
    "optimize \tOptimization and root-finding routines\n",
    "- `scipy.spatial` : Spatial data structures and algorithms\n",
    "\n",
    "[SciPy Reference Guide](http://docs.scipy.org/doc/scipy/reference/)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## `pandas`\n",
    "\n",
    "`pandas` provides rich data structures and functions designed to make working with structured data fast, easy, and expressive. It is, as you will see, one of the critical in-gredients enabling Python to be a powerful and productive data analysis environment. pandas combines the high performance array-computing features of `NumPy` with the flexible data manipulation capabilities of spreadsheets and relational databases (such as SQL). It provides sophisticated indexing functionality to make it easy to reshape, slice and dice, perform aggregations, and select subsets of data.\n",
    "\n",
    "pandas consists of the following things\n",
    "\n",
    "- A set of labeled array data structures, the primary of which are Series and DataFrame\n",
    "- Index objects enabling both simple axis indexing and multi-level / hierarchical axis indexing\n",
    "- An integrated group by engine for aggregating and transforming data sets\n",
    "- Date range generation (date_range) and custom date offsets enabling the implementation of customized frequencies\n",
    "- Input/Output tools: loading tabular data from flat files (CSV, delimited, Excel 2003), and saving and loading pandas objects from the fast and efficient PyTables/HDF5 format.\n",
    "- Memory-efficient “sparse” versions of the standard data structures for storing data that is mostly missing or mostly constant (some fixed value)\n",
    "- Moving window statistics (rolling mean, rolling standard deviation, etc.)\n",
    "- Static and moving window linear and panel regression\n",
    "\n",
    "[pandas Documentation](http://pandas.pydata.org/pandas-docs/version/0.17.0/)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## `statsmodels`\n",
    "\n",
    "The `statsmodels` is a Python module that provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests, and statistical data exploration. An extensive list of result statistics are available for each estimator. The results are tested against existing statistical packages to ensure that they are correct. \n",
    "\n",
    "The `statsmodels` module covers the following topics\n",
    "\n",
    "- Linear Regression Models\n",
    "- Plotting\n",
    "- Discrete Choice Models\n",
    "- Nonparametric Statistics\n",
    "- Generalized Linear Models\n",
    "- Robust Regression\n",
    "- Statistics\n",
    "- Time Series Analysis\n",
    "- State space models"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Linear Algebra （线性代数）\n",
    "\n",
    "Linear algebra can be done conveniently via `scipy.linalg`. When SciPy is built using the optimized ATLAS LAPACK and BLAS libraries, it has very fast linear algebra capabilities. If you dig deep enough, all of the raw lapack and blas libraries are available for your use for even more speed. In this section, some easier-to-use interfaces to these routines are described.\n",
    "\n",
    "All of these linear algebra routines expect an object that can be converted into a 2-dimensional array. The output of these routines is also a two-dimensional array."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Matrices and n-dimensional array （矩阵和多维数组）"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2],\n",
       "       [3, 4]])"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "from scipy import linalg\n",
    "A = np.array([[1,2],[3,4]])\n",
    "A"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-2. ,  1. ],\n",
       "       [ 1.5, -0.5]])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "linalg.inv(A) # inverse of a matrix逆"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[5, 6]])"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b = np.array([[5,6]]) #2D array\n",
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[5],\n",
       "       [6]])"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 5, 12],\n",
       "       [15, 24]])"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A*b #not matrix multiplication!对应元素相乘"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[17],\n",
       "       [39]])"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A.dot(b.T) #matrix multiplication"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([5, 6])"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b = np.array([5,6]) #1D array\n",
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([5, 6])"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.T  #not matrix transpose!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([17, 39])"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A.dot(b)  #does not matter for multiplication"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Solving linear system （求解线性方程组）"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2],\n",
       "       [3, 4]])"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "from scipy import linalg\n",
    "A = np.array([[1,2],[3,4]])\n",
    "A"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[5],\n",
       "       [6]])"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b = np.array([[5],[6]])\n",
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-4. ],\n",
       "       [ 4.5]])"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "linalg.inv(A).dot(b) #slow"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.],\n",
       "       [ 0.]])"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A.dot(linalg.inv(A).dot(b))-b #check"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-4. ],\n",
       "       [ 4.5]])"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.linalg.solve(A,b) #fastAX=B"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.],\n",
       "       [ 0.]])"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A.dot(np.linalg.solve(A,b))-b #check"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Determinant （行列式）"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.0"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "from scipy import linalg\n",
    "A = np.array([[1,2],[2,4]])\n",
    "linalg.det(A)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Least-squares problems and pseudo-inverses （最小二乘和广义逆）"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from scipy import linalg\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "c1, c2 = 5.0, 2.0\n",
    "i = np.r_[1:11]\n",
    "xi = 0.1*i\n",
    "yi = c1*np.exp(-xi) + c2*xi\n",
    "zi = yi + 0.05 * np.max(yi) * np.random.randn(len(yi))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "A = np.c_[np.exp(-xi)[:, np.newaxis], xi[:, np.newaxis]]\n",
    "c, resid, rank, sigma = linalg.lstsq(A, zi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "xi2 = np.r_[0.1:1.0:100j]\n",
    "yi2 = c[0]*np.exp(-xi2) + c[1]*xi2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(xi,zi,'x',xi2,yi2)\n",
    "plt.axis([0,1.1,3.0,5.5])\n",
    "plt.xlabel('$x_i$')\n",
    "plt.title('Data fitting with linalg.lstsq')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Eigenvalues and eigenvectors （特征向量和特征值）"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(-0.3722813232690143+0j) (5.372281323269014+0j)\n",
      "[-0.82456484  0.56576746]\n",
      "[-0.41597356 -0.90937671]\n",
      "[1. 1.]\n",
      "5.551115123125783e-17\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from scipy import linalg\n",
    "A = np.array([[1,2],[3,4]])\n",
    "la,v = linalg.eig(A)\n",
    "l1,l2 = la\n",
    "print(l1, l2)  #eigenvalues\n",
    "\n",
    "print(v[:,0])  #first eigenvector\n",
    "\n",
    "print(v[:,1])  #second eigenvector\n",
    "\n",
    "print(np.sum(abs(v**2),axis=0)) #eigenvectors are unitary\n",
    "\n",
    "v1 = np.array(v[:,0]).T\n",
    "print(linalg.norm(A.dot(v1)-l1*v1)) #check the computation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Singular Value Decomposition (SVD) （奇异值分解）"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from scipy import linalg\n",
    "A = np.array([[1,2,3],[4,5,6]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "M,N = A.shape\n",
    "U,s,Vh = linalg.svd(A)\n",
    "Sig = linalg.diagsvd(s,M,N)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-0.3863177 , -0.92236578],\n",
       "       [-0.92236578,  0.3863177 ]])"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "U, Vh = U, Vh\n",
    "U"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[9.508032  , 0.        , 0.        ],\n",
       "       [0.        , 0.77286964, 0.        ]])"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Sig"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-0.42866713, -0.56630692, -0.7039467 ],\n",
       "       [ 0.80596391,  0.11238241, -0.58119908],\n",
       "       [ 0.40824829, -0.81649658,  0.40824829]])"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Vh"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 2., 3.],\n",
       "       [4., 5., 6.]])"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "U.dot(Sig.dot(Vh)) #check computation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## QR decomposition （QR分解）\n",
    "\n",
    "The command for QR decomposition is `linalg.qr`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## LU decomposition （LU分解）\n",
    "    \n",
    "The SciPy command for this decomposition is `linalg.lu`.  If the intent for performing LU decomposition is for solving linear systems then the command `linalg.lu_factor` should be used followed by repeated applications of the command `linalg.lu_solve` to solve the system for each new right-hand-side."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Cholesky decomposition （乔列斯基分解）\n",
    "\n",
    "The command `linalg.cholesky` computes the cholesky factorization. For using Cholesky factorization to solve systems of equations there are also `linalg.cho_factor` and `linalg.cho_solve` routines that work similarly to their LU decomposition counterparts."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Statistical Distributions （统计分布函数）\n",
    "\n",
    "A large number of probability distributions as well as a growing library of statistical functions are available in `scipy.stats`. See http://docs.scipy.org/doc/scipy/reference/stats.html for a complete list."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "Generate random numbers from normal distribution:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "from scipy.stats import norm\n",
    "r = norm.rvs(loc=0, scale=1, size=1000)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "Calculate a few first moments:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "mean, var, skew, kurt = norm.stats(moments='mvsk')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Linear regression model （线性回归模型）\n",
    "\n",
    "This example computes a least-squares regression for two sets of measurements."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'slope': 0.1655523906392262, 'intercept': 0.4465727634738072}\n",
      "{'p_value': 0.5038418263161998, 'r-squared': 0.06}\n"
     ]
    }
   ],
   "source": [
    "from scipy import stats\n",
    "import numpy as np\n",
    "x = np.random.random(10)\n",
    "y = np.random.random(10)\n",
    "slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)\n",
    "print({'slope':slope,'intercept':intercept})\n",
    "print({'p_value':p_value,'r-squared':round(r_value**2,2)})"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Optimization （优化）\n",
    "\n",
    "The `minimize` function provides a common interface to unconstrained and constrained minimization algorithms for multivariate scalar functions in `scipy.optimize`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Optimization terminated successfully.\n",
      "         Current function value: 0.000000\n",
      "         Iterations: 339\n",
      "         Function evaluations: 571\n",
      "[1. 1. 1. 1. 1.]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from scipy.optimize import minimize\n",
    "\n",
    "## Define the function\n",
    "def rosen(x):\n",
    "    \"\"\"The Rosenbrock function\"\"\"\n",
    "    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)\n",
    "\n",
    "x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])\n",
    "\n",
    "## Calling the minimize() function\n",
    "res = minimize(rosen, x0, method='nelder-mead',\n",
    "               options={'xtol': 1e-8, 'disp': True})\n",
    "print(res.x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Generalized Linear Models"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "import statsmodels.api as sm\n",
    "import statsmodels.formula.api as smf\n",
    "star98 = sm.datasets.star98.load_pandas().data\n",
    "formula = 'SUCCESS ~ LOWINC + PERASIAN + PERBLACK + PERHISP + PCTCHRT + \\\n",
    "           PCTYRRND + PERMINTE*AVYRSEXP*AVSALK + PERSPENK*PTRATIO*PCTAF'\n",
    "dta = star98[['NABOVE', 'NBELOW', 'LOWINC', 'PERASIAN', 'PERBLACK', 'PERHISP',\n",
    "              'PCTCHRT', 'PCTYRRND', 'PERMINTE', 'AVYRSEXP', 'AVSALK',\n",
    "              'PERSPENK', 'PTRATIO', 'PCTAF']].copy()\n",
    "endog = dta['NABOVE'] / (dta['NABOVE'] + dta.pop('NBELOW'))\n",
    "del dta['NABOVE']\n",
    "dta['SUCCESS'] = endog"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table class=\"simpletable\">\n",
       "<caption>Generalized Linear Model Regression Results</caption>\n",
       "<tr>\n",
       "  <th>Dep. Variable:</th>        <td>SUCCESS</td>     <th>  No. Observations:  </th>  <td>   303</td> \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Model:</th>                  <td>GLM</td>       <th>  Df Residuals:      </th>  <td>   282</td> \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Model Family:</th>        <td>Binomial</td>     <th>  Df Model:          </th>  <td>    20</td> \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Link Function:</th>         <td>logit</td>      <th>  Scale:             </th> <td>  1.0000</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Method:</th>                <td>IRLS</td>       <th>  Log-Likelihood:    </th> <td> -127.33</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Date:</th>            <td>Fri, 27 Mar 2020</td> <th>  Deviance:          </th> <td>  8.5477</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Time:</th>                <td>20:53:19</td>     <th>  Pearson chi2:      </th>  <td>  8.48</td> \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>No. Iterations:</th>          <td>4</td>        <th>                     </th>     <td> </td>   \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Covariance Type:</th>     <td>nonrobust</td>    <th>                     </th>     <td> </td>   \n",
       "</tr>\n",
       "</table>\n",
       "<table class=\"simpletable\">\n",
       "<tr>\n",
       "              <td></td>                <th>coef</th>     <th>std err</th>      <th>z</th>      <th>P>|z|</th>  <th>[0.025</th>    <th>0.975]</th>  \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Intercept</th>                <td>    0.4037</td> <td>   25.036</td> <td>    0.016</td> <td> 0.987</td> <td>  -48.665</td> <td>   49.472</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>LOWINC</th>                   <td>   -0.0204</td> <td>    0.010</td> <td>   -1.982</td> <td> 0.048</td> <td>   -0.041</td> <td>   -0.000</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>PERASIAN</th>                 <td>    0.0159</td> <td>    0.017</td> <td>    0.910</td> <td> 0.363</td> <td>   -0.018</td> <td>    0.050</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>PERBLACK</th>                 <td>   -0.0198</td> <td>    0.020</td> <td>   -1.004</td> <td> 0.316</td> <td>   -0.058</td> <td>    0.019</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>PERHISP</th>                  <td>   -0.0096</td> <td>    0.010</td> <td>   -0.951</td> <td> 0.341</td> <td>   -0.029</td> <td>    0.010</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>PCTCHRT</th>                  <td>   -0.0022</td> <td>    0.022</td> <td>   -0.103</td> <td> 0.918</td> <td>   -0.045</td> <td>    0.040</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>PCTYRRND</th>                 <td>   -0.0022</td> <td>    0.006</td> <td>   -0.348</td> <td> 0.728</td> <td>   -0.014</td> <td>    0.010</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>PERMINTE</th>                 <td>    0.1068</td> <td>    0.787</td> <td>    0.136</td> <td> 0.892</td> <td>   -1.436</td> <td>    1.650</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>AVYRSEXP</th>                 <td>   -0.0411</td> <td>    1.176</td> <td>   -0.035</td> <td> 0.972</td> <td>   -2.346</td> <td>    2.264</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>PERMINTE:AVYRSEXP</th>        <td>   -0.0031</td> <td>    0.054</td> <td>   -0.057</td> <td> 0.954</td> <td>   -0.108</td> <td>    0.102</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>AVSALK</th>                   <td>    0.0131</td> <td>    0.295</td> <td>    0.044</td> <td> 0.965</td> <td>   -0.566</td> <td>    0.592</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>PERMINTE:AVSALK</th>          <td>   -0.0019</td> <td>    0.013</td> <td>   -0.145</td> <td> 0.885</td> <td>   -0.028</td> <td>    0.024</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>AVYRSEXP:AVSALK</th>          <td>    0.0008</td> <td>    0.020</td> <td>    0.038</td> <td> 0.970</td> <td>   -0.039</td> <td>    0.041</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>PERMINTE:AVYRSEXP:AVSALK</th> <td> 5.978e-05</td> <td>    0.001</td> <td>    0.068</td> <td> 0.946</td> <td>   -0.002</td> <td>    0.002</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>PERSPENK</th>                 <td>   -0.3097</td> <td>    4.233</td> <td>   -0.073</td> <td> 0.942</td> <td>   -8.606</td> <td>    7.987</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>PTRATIO</th>                  <td>    0.0096</td> <td>    0.919</td> <td>    0.010</td> <td> 0.992</td> <td>   -1.792</td> <td>    1.811</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>PERSPENK:PTRATIO</th>         <td>    0.0066</td> <td>    0.206</td> <td>    0.032</td> <td> 0.974</td> <td>   -0.397</td> <td>    0.410</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>PCTAF</th>                    <td>   -0.0143</td> <td>    0.474</td> <td>   -0.030</td> <td> 0.976</td> <td>   -0.944</td> <td>    0.916</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>PERSPENK:PCTAF</th>           <td>    0.0105</td> <td>    0.098</td> <td>    0.107</td> <td> 0.915</td> <td>   -0.182</td> <td>    0.203</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>PTRATIO:PCTAF</th>            <td>   -0.0001</td> <td>    0.022</td> <td>   -0.005</td> <td> 0.996</td> <td>   -0.044</td> <td>    0.044</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>PERSPENK:PTRATIO:PCTAF</th>   <td>   -0.0002</td> <td>    0.005</td> <td>   -0.051</td> <td> 0.959</td> <td>   -0.010</td> <td>    0.009</td>\n",
       "</tr>\n",
       "</table>"
      ],
      "text/plain": [
       "<class 'statsmodels.iolib.summary.Summary'>\n",
       "\"\"\"\n",
       "                 Generalized Linear Model Regression Results                  \n",
       "==============================================================================\n",
       "Dep. Variable:                SUCCESS   No. Observations:                  303\n",
       "Model:                            GLM   Df Residuals:                      282\n",
       "Model Family:                Binomial   Df Model:                           20\n",
       "Link Function:                  logit   Scale:                          1.0000\n",
       "Method:                          IRLS   Log-Likelihood:                -127.33\n",
       "Date:                Fri, 27 Mar 2020   Deviance:                       8.5477\n",
       "Time:                        20:53:19   Pearson chi2:                     8.48\n",
       "No. Iterations:                     4                                         \n",
       "Covariance Type:            nonrobust                                         \n",
       "============================================================================================\n",
       "                               coef    std err          z      P>|z|      [0.025      0.975]\n",
       "--------------------------------------------------------------------------------------------\n",
       "Intercept                    0.4037     25.036      0.016      0.987     -48.665      49.472\n",
       "LOWINC                      -0.0204      0.010     -1.982      0.048      -0.041      -0.000\n",
       "PERASIAN                     0.0159      0.017      0.910      0.363      -0.018       0.050\n",
       "PERBLACK                    -0.0198      0.020     -1.004      0.316      -0.058       0.019\n",
       "PERHISP                     -0.0096      0.010     -0.951      0.341      -0.029       0.010\n",
       "PCTCHRT                     -0.0022      0.022     -0.103      0.918      -0.045       0.040\n",
       "PCTYRRND                    -0.0022      0.006     -0.348      0.728      -0.014       0.010\n",
       "PERMINTE                     0.1068      0.787      0.136      0.892      -1.436       1.650\n",
       "AVYRSEXP                    -0.0411      1.176     -0.035      0.972      -2.346       2.264\n",
       "PERMINTE:AVYRSEXP           -0.0031      0.054     -0.057      0.954      -0.108       0.102\n",
       "AVSALK                       0.0131      0.295      0.044      0.965      -0.566       0.592\n",
       "PERMINTE:AVSALK             -0.0019      0.013     -0.145      0.885      -0.028       0.024\n",
       "AVYRSEXP:AVSALK              0.0008      0.020      0.038      0.970      -0.039       0.041\n",
       "PERMINTE:AVYRSEXP:AVSALK  5.978e-05      0.001      0.068      0.946      -0.002       0.002\n",
       "PERSPENK                    -0.3097      4.233     -0.073      0.942      -8.606       7.987\n",
       "PTRATIO                      0.0096      0.919      0.010      0.992      -1.792       1.811\n",
       "PERSPENK:PTRATIO             0.0066      0.206      0.032      0.974      -0.397       0.410\n",
       "PCTAF                       -0.0143      0.474     -0.030      0.976      -0.944       0.916\n",
       "PERSPENK:PCTAF               0.0105      0.098      0.107      0.915      -0.182       0.203\n",
       "PTRATIO:PCTAF               -0.0001      0.022     -0.005      0.996      -0.044       0.044\n",
       "PERSPENK:PTRATIO:PCTAF      -0.0002      0.005     -0.051      0.959      -0.010       0.009\n",
       "============================================================================================\n",
       "\"\"\""
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mod1 = smf.glm(formula=formula, data=dta, family=sm.families.Binomial()).fit()\n",
    "mod1.summary()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Autoregressive Moving Average (ARMA)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "::\n",
      "\n",
      "    Number of Observations - 309 (Annual 1700 - 2008)\n",
      "    Number of Variables - 1\n",
      "    Variable name definitions::\n",
      "\n",
      "        SUNACTIVITY - Number of sunspots for each year\n",
      "\n",
      "    The data file contains a 'YEAR' variable that is not returned by load.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from scipy import stats\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import statsmodels.api as sm\n",
    "from statsmodels.graphics.api import qqplot\n",
    "\n",
    "print(sm.datasets.sunspots.NOTE)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "Let's first make the time series plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "dta = sm.datasets.sunspots.load_pandas().data\n",
    "dta.index = pd.Index(sm.tsa.datetools.dates_from_range('1700', '2008'))\n",
    "del dta[\"YEAR\"]\n",
    "dta.plot(figsize=(12,8));"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "The ACF and PACF"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x576 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = plt.figure(figsize=(12,8))\n",
    "ax1 = fig.add_subplot(211)\n",
    "fig = sm.graphics.tsa.plot_acf(dta.values.squeeze(), lags=40, ax=ax1)\n",
    "ax2 = fig.add_subplot(212)\n",
    "fig = sm.graphics.tsa.plot_pacf(dta, lags=40, ax=ax2)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Fit an ARIMA model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\ProgramData\\Anaconda3\\lib\\site-packages\\statsmodels\\tsa\\base\\tsa_model.py:162: ValueWarning: No frequency information was provided, so inferred frequency A-DEC will be used.\n",
      "  % freq, ValueWarning)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "const                49.659374\n",
      "ar.L1.SUNACTIVITY     1.390656\n",
      "ar.L2.SUNACTIVITY    -0.688571\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "arma_mod20 = sm.tsa.ARMA(dta, (2,0)).fit(disp=False)\n",
    "print(arma_mod20.params)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\ProgramData\\Anaconda3\\lib\\site-packages\\statsmodels\\tsa\\base\\tsa_model.py:162: ValueWarning: No frequency information was provided, so inferred frequency A-DEC will be used.\n",
      "  % freq, ValueWarning)\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "arma_mod30 = sm.tsa.ARMA(dta, (3,0)).fit(disp=False)\n",
    "resid = arma_mod30.resid\n",
    "stats.normaltest(resid)\n",
    "fig = plt.figure(figsize=(12,8))\n",
    "ax = fig.add_subplot(111)\n",
    "fig = qqplot(resid, line='q', ax=ax, fit=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's then do some predictions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1990-12-31    167.047459\n",
      "1991-12-31    140.993103\n",
      "1992-12-31     94.859271\n",
      "1993-12-31     46.861087\n",
      "1994-12-31     11.242765\n",
      "1995-12-31     -4.721154\n",
      "1996-12-31     -1.166832\n",
      "1997-12-31     16.185714\n",
      "1998-12-31     39.021869\n",
      "1999-12-31     59.449851\n",
      "2000-12-31     72.170143\n",
      "2001-12-31     75.376823\n",
      "2002-12-31     70.436540\n",
      "2003-12-31     60.731701\n",
      "2004-12-31     50.201925\n",
      "2005-12-31     42.076150\n",
      "2006-12-31     38.114390\n",
      "2007-12-31     38.454719\n",
      "2008-12-31     41.963867\n",
      "2009-12-31     46.869322\n",
      "2010-12-31     51.423293\n",
      "2011-12-31     54.399758\n",
      "2012-12-31     55.321745\n",
      "Freq: A-DEC, dtype: float64\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'DataFrame' object has no attribute 'ix'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-50-2270d5205ba2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpredict_sunspots\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mfig\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0max\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msubplots\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfigsize\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m8\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[0max\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdta\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mix\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'1950'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mplot\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0max\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0max\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[0mfig\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0marma_mod30\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mplot_predict\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'1990'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'2012'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdynamic\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0max\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0max\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mplot_insample\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mFalse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\pandas\\core\\generic.py\u001b[0m in \u001b[0;36m__getattr__\u001b[1;34m(self, name)\u001b[0m\n\u001b[0;32m   5272\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_info_axis\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_can_hold_identifiers_and_holds_name\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   5273\u001b[0m                 \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 5274\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mobject\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__getattribute__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   5275\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   5276\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__setattr__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m->\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'DataFrame' object has no attribute 'ix'"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAsoAAAHWCAYAAABuaq89AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAATLElEQVR4nO3dX4jld3nH8c9j1lTQqNDdgmQTE+immgYhdkgtXqiYliQXmxsrCYhVgnvTKK0iRBSVeFWlCEL8s6WSKmgavdBFVlKwKYoYyYa0wUQCS7RmiZD4LzeiMe3Ti5nKOHl25+x65sxm83rBwvzO+c6ZB/Jl5p3f/Ob8qrsDAAD8ruft9gAAAHA2EsoAADAQygAAMBDKAAAwEMoAADAQygAAMNg2lKvqs1X1eFV97yTPV1V9oqqOV9UDVfXq5Y8JAACrtcgZ5duTXHOK569NcmDj36Ekn/r9xwIAgN21bSh39zeT/OwUS65P8rled0+Sl1bVy5Y1IAAA7IZlXKN8YZJHNx2f2HgMAACetfYs4TVqeGy8L3ZVHcr65Rl54Qtf+GeveMUrlvDlAQDg5O67776fdPe+0/28ZYTyiSQXbTren+SxaWF3H05yOEnW1tb62LFjS/jyAABwclX132fyecu49OJIkrduvPvFa5I82d0/XsLrAgDArtn2jHJVfTHJ65PsraoTST6U5PlJ0t2fTnI0yXVJjif5ZZK379SwAACwKtuGcnffuM3zneRvlzYRAACcBdyZDwAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAYLhXJVXVNVD1fV8aq6ZXj+4qq6u6rur6oHquq65Y8KAACrs20oV9V5SW5Lcm2Sy5PcWFWXb1n2gSR3dveVSW5I8sllDwoAAKu0yBnlq5Ic7+5HuvupJHckuX7Lmk7y4o2PX5LkseWNCAAAq7dngTUXJnl00/GJJH++Zc2Hk/xbVb0zyQuTXL2U6QAAYJcscka5hsd6y/GNSW7v7v1Jrkvy+ap6xmtX1aGqOlZVx5544onTnxYAAFZkkVA+keSiTcf788xLK25KcmeSdPd3krwgyd6tL9Tdh7t7rbvX9u3bd2YTAwDACiwSyvcmOVBVl1bV+Vn/Y70jW9b8KMkbk6SqXpn1UHbKGACAZ61tQ7m7n05yc5K7knw/6+9u8WBV3VpVBzeWvSfJO6rqv5J8Mcnbunvr5RkAAPCsscgf86W7jyY5uuWxD276+KEkr13uaAAAsHvcmQ8AAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGC4VyVV1TVQ9X1fGquuUka95cVQ9V1YNV9YXljgkAAKu1Z7sFVXVektuS/GWSE0nuraoj3f3QpjUHkrwvyWu7++dV9Uc7NTAAAKzCImeUr0pyvLsf6e6nktyR5Pota96R5Lbu/nmSdPfjyx0TAABWa5FQvjDJo5uOT2w8ttllSS6rqm9X1T1Vdc2yBgQAgN2w7aUXSWp4rIfXOZDk9Un2J/lWVV3R3b/4nReqOpTkUJJcfPHFpz0sAACsyiJnlE8kuWjT8f4kjw1rvtrdv+nuHyR5OOvh/Du6+3B3r3X32r59+850ZgAA2HGLhPK9SQ5U1aVVdX6SG5Ic2bLmK0nekCRVtTfrl2I8ssxBAQBglbYN5e5+OsnNSe5K8v0kd3b3g1V1a1Ud3Fh2V5KfVtVDSe5O8t7u/ulODQ0AADuturdebrwaa2trfezYsV352gAAPHdU1X3dvXa6n+fOfAAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADBYKJSr6pqqeriqjlfVLadY96aq6qpaW96IAACwetuGclWdl+S2JNcmuTzJjVV1+bDugiTvSvLdZQ8JAACrtsgZ5auSHO/uR7r7qSR3JLl+WPeRJB9N8qslzgcAALtikVC+MMmjm45PbDz2W1V1ZZKLuvtrS5wNAAB2zSKhXMNj/dsnq56X5ONJ3rPtC1UdqqpjVXXsiSeeWHxKAABYsUVC+USSizYd70/y2KbjC5JckeQ/quqHSV6T5Mj0B33dfbi717p7bd++fWc+NQAA7LBFQvneJAeq6tKqOj/JDUmO/P+T3f1kd+/t7ku6+5Ik9yQ52N3HdmRiAABYgW1DubufTnJzkruSfD/Jnd39YFXdWlUHd3pAAADYDXsWWdTdR5Mc3fLYB0+y9vW//1gAALC73JkPAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABkIZAAAGQhkAAAZCGQAABguFclVdU1UPV9XxqrpleP7dVfVQVT1QVd+oqpcvf1QAAFidbUO5qs5LcluSa5NcnuTGqrp8y7L7k6x196uSfDnJR5c9KAAArNIiZ5SvSnK8ux/p7qeS3JHk+s0Luvvu7v7lxuE9SfYvd0wAAFitRUL5wiSPbjo+sfHYydyU5Ou/z1AAALDb9iywpobHelxY9ZYka0led5LnDyU5lCQXX3zxgiMCAMDqLXJG+USSizYd70/y2NZFVXV1kvcnOdjdv55eqLsPd/dad6/t27fvTOYFAICVWCSU701yoKourarzk9yQ5MjmBVV1ZZLPZD2SH1/+mAAAsFrbhnJ3P53k5iR3Jfl+kju7+8GqurWqDm4s+1iSFyX5UlX9Z1UdOcnLAQDAs8Ii1yinu48mObrlsQ9u+vjqJc8FAAC7yp35AABgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYCCUAQBgIJQBAGAglAEAYLBQKFfVNVX1cFUdr6pbhuf/oKr+deP571bVJcseFAAAVmnbUK6q85LcluTaJJcnubGqLt+y7KYkP+/uP07y8ST/sOxBAQBglRY5o3xVkuPd/Uh3P5XkjiTXb1lzfZJ/2fj4y0neWFW1vDEBAGC1FgnlC5M8uun4xMZj45rufjrJk0n+cBkDAgDAbtizwJrpzHCfwZpU1aEkhzYOf11V31vg6/PcsjfJT3Z7CM469gUT+4KJfcHkT87kkxYJ5RNJLtp0vD/JYydZc6Kq9iR5SZKfbX2h7j6c5HCSVNWx7l47k6E5d9kXTOwLJvYFE/uCSVUdO5PPW+TSi3uTHKiqS6vq/CQ3JDmyZc2RJH+z8fGbkvx7dz/jjDIAADxbbHtGubufrqqbk9yV5Lwkn+3uB6vq1iTHuvtIkn9O8vmqOp71M8k37OTQAACw0xa59CLdfTTJ0S2PfXDTx79K8ten+bUPn+Z6nhvsCyb2BRP7gol9weSM9kW5QgIAAJ7JLawBAGCw46Hs9tdMFtgX766qh6rqgar6RlW9fDfmZLW22xeb1r2pqrqq/GX7c8Ai+6Kq3rzxPePBqvrCqmdk9Rb4OXJxVd1dVfdv/Cy5bjfmZHWq6rNV9fjJ3n641n1iY888UFWv3u41dzSU3f6ayYL74v4ka939qqzf7fGjq52SVVtwX6SqLkjyriTfXe2E7IZF9kVVHUjyviSv7e4/TfJ3Kx+UlVrw+8UHktzZ3Vdm/U0GPrnaKdkFtye55hTPX5vkwMa/Q0k+td0L7vQZZbe/ZrLtvujuu7v7lxuH92T9/bs5ty3y/SJJPpL1/3H61SqHY9cssi/ekeS27v55knT34yuekdVbZF90khdvfPySPPMeEJxjuvubGe7jscn1ST7X6+5J8tKqetmpXnOnQ9ntr5kssi82uynJ13d0Is4G2+6LqroyyUXd/bVVDsauWuT7xWVJLquqb1fVPVV1qjNKnBsW2RcfTvKWqjqR9XfueudqRuMsdrr9sdjbw/0elnb7a84pC/83r6q3JFlL8rodnYizwSn3RVU9L+uXZ71tVQNxVljk+8WerP8q9fVZ/+3Tt6rqiu7+xQ7Pxu5ZZF/cmOT27v7HqvqLrN/v4Yru/t+dH4+z1Gk3506fUT6d21/nVLe/5pyyyL5IVV2d5P1JDnb3r1c0G7tnu31xQZIrkvxHVf0wyWuSHPEHfee8RX+OfLW7f9PdP0jycNbDmXPXIvvipiR3Jkl3fyfJC5LsXcl0nK0W6o/NdjqU3f6aybb7YuNX7J/JeiS73vC54ZT7oruf7O693X1Jd1+S9WvXD3b3sd0ZlxVZ5OfIV5K8IUmqam/WL8V4ZKVTsmqL7IsfJXljklTVK7Meyk+sdErONkeSvHXj3S9ek+TJ7v7xqT5hRy+9cPtrJgvui48leVGSL238beePuvvgrg3NjltwX/Acs+C+uCvJX1XVQ0n+J8l7u/unuzc1O23BffGeJP9UVX+f9V+vv82JuHNbVX0x65dg7d24Nv1DSZ6fJN396axfq35dkuNJfpnk7du+pj0DAADP5M58AAAwEMoAADAQygAAMBDKAAAwEMoAADAQygAAMBDKAAAwEMoAADD4P4fzu2ZTW1i9AAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 864x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "predict_sunspots = arma_mod30.predict('1990', '2012', dynamic=True)\n",
    "print(predict_sunspots)\n",
    "fig, ax = plt.subplots(figsize=(12, 8))\n",
    "ax = dta.ix['1950':].plot(ax=ax)\n",
    "fig = arma_mod30.plot_predict('1990', '2012', dynamic=True, ax=ax, plot_insample=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Lab\n",
    "\n",
    "Use the data from cycle in the U.S. unemployment rate to model the rrends and cycles in unemployment.\n",
    "\n",
    "```python\n",
    "from pandas_datareader.data import DataReader\n",
    "endog = DataReader('UNRATE', 'fred', start='1954-01-01')\n",
    "```"
   ]
  }
 ],
 "metadata": {
  "celltoolbar": "Slideshow",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
