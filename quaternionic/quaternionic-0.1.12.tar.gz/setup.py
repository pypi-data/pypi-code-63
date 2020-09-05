# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quaternionic']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.13,<2.0', 'scipy>=1.0,<2.0']

extras_require = \
{':implementation_name == "cpython"': ['numba>=0.50'],
 ':python_version < "3.8"': ['importlib-metadata>=1.0,<2.0'],
 'mkdocs:implementation_name == "cpython"': ['mkdocs>=1.1.2'],
 'mktheapidocs:implementation_name == "cpython"': ['mktheapidocs>=0.2'],
 'pymdown-extensions:implementation_name == "cpython"': ['pymdown-extensions>=8,<9']}

setup_kwargs = {
    'name': 'quaternionic',
    'version': '0.1.12',
    'description': 'Interpret numpy arrays as quaternionic arrays with numba acceleration',
    'long_description': '[![Test Status](https://github.com/moble/quaternionic/workflows/tests/badge.svg)](https://github.com/moble/quaternionic/actions)\n[![Test Coverage](https://codecov.io/gh/moble/quaternionic/branch/master/graph/badge.svg)](https://codecov.io/gh/moble/quaternionic)\n[![Documentation Status](https://readthedocs.org/projects/quaternionic/badge/?version=latest)](https://quaternionic.readthedocs.io/en/latest/?badge=latest)\n[![PyPI Version](https://img.shields.io/pypi/v/quaternionic?color=)](https://pypi.org/project/quaternionic/)\n[![Conda Version](https://img.shields.io/conda/vn/conda-forge/quaternionic.svg?color=)](https://anaconda.org/conda-forge/quaternionic)\n\n\n# Quaternionic arrays\n\nThis module subclasses numpy\'s array type, interpreting the array as an array of quaternions, and\naccelerating the algebra using numba.  This enables natural manipulations, like multiplying\nquaternions as `a*b`, while also working with standard numpy functions, as in `np.log(q)`.  There is\nalso basic initial support for symbolic manipulation of quaternions by creating quaternionic arrays\nwith sympy symbols as elements, though this is a work in progress.\n\nThis package has evolved from the [quaternion](https://github.com/moble/quaternion) package, which\nadds a quaternion dtype directly to numpy.  In some ways, that is a better approach because dtypes\nare built in to numpy, making it more robust than this package.  However, that approach has its own\nlimitations, including that it is harder to maintain, and requires much of the code to be written in\nC, which also makes it harder to distribute.  This package is written entirely in python code, but\nshould actually have comparable performance because it is compiled by numba.  Moreover, because the\ncore code is written in pure python, it is reusable for purposes other than the core purpose of this\npackage, which is to provide the numeric array type.\n\n\n# Installation\n\nBecause this package is pure python code, installation is very simple.  In particular, with\na reasonably modern installation, you can just run\n\n```bash\nconda install -c conda-forge quaternionic\n```\n\nor\n\n```bash\npip install quaternionic\n```\n\nThese will download and install the package.  You can also install the package from source if you\nhave `pip` version 10.0 or greater by running `pip install .`, or if you have `poetry` by running\n`poetry install`.\n\nNote that only python 3.6 or greater is supported.  (I have also tried to support PyPy3, although I\ncannot test this as `scipy` does not currently install.  Pull requests are welcome.)  In any case, I\nstrongly recommend installing by way of an environment manager — especially\n[conda](https://docs.anaconda.com/anaconda/install/), though other managers like `virtualenv` or\n`pipenv` should also work.\n\nFor development work, the best current option is [poetry](https://python-poetry.org/).  From the\ntop-level directory, you can run `poetry run <some command>` to run the command in an isolated\nenvironment.\n\n\n# Usage\n\n## Basic construction\n\nThe key function is `quaternionic.array`, which takes nearly the same arguments as `numpy.array`,\nexcept that whatever array will result must have a final axis of size 4 (and the `dtype` must be\n`float`).  As long as these conditions are satisfied, we can create new arrays or just reinterpret\nexisting arrays:\n\n```python\nimport numpy as np\nimport quaternionic\n\na = 1.0 - np.random.rand(17, 11, 4)  # Just some random numbers; last dimension is 4\nq1 = quaternionic.array(a)  # Reinterpret an existing array\nq2 = quaternionic.array([1.2, 2.3, 3.4, 4.5])  # Create a new array\n```\n\nIn this example, `q1` is an array of 187 (17*11) quaternions, just to demonstrate that any number of\ndimensions may be used, as long as the final dimension has size 4.\n\nHere, the original array `a` will still exist just as it was, and will behave just as a normal numpy\narray — including changing its values (which will change the values in `q1`), slicing, math, etc.\nHowever, `q1` will be another\n["view"](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html) into the same\ndata.  Operations on `q1` will be quaternionic.  For example, whereas `1/a` returns the element-wise\ninverse of each float in the array, `1/q1` returns the *quaternionic* inverse of each quaternion.\nSimilarly, if you multiply two quaternionic arrays, their product will be computed with the usual\nquaternion multiplication, rather than element-wise multiplication of floats as numpy usually\nperforms.\n\n## Algebra\n\nAll the usual quaternion operations are available, including\n\n  * Addition `q1 + q2`\n  * Subtraction `q1 - q2`\n  * Multiplication `q1 * q2`\n  * Division `q1 / q2`\n  * Scalar multiplication `q1 * s == s * q1`\n  * Scalar division `q1 / s` and `s / q1`\n  * Reciprocal `np.reciprocal(q1) == 1/q1`\n  * Exponential `np.exp(q1)`\n  * Logarithm `np.log(q1)`\n  * Square-root `np.sqrt(q1)`\n  * Conjugate `np.conjugate(q1) == np.conj(q1)`\n\nAll numpy [ufuncs](https://numpy.org/doc/stable/reference/ufuncs.html) that make sense for\nquaternions are supported.  When the arrays have different shapes, the usual numpy\n[broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) rules take effect.\n\n\n## Attributes\n\nIn addition to the basic numpy array features, we also have a number of extra properties that are\nparticularly useful for quaternions, including\n\n  * Methods to extract and/or set components\n    * `w`, `x`, `y`, `z`\n    * `i`, `j`, `k` (equivalent to `x`, `y`, `z`)\n    * `scalar`, `vector` (equivalent to `w`, [`x`, `y`, `z`])\n    * `real`, `imag` (equivalent to `scalar`, `vector`)\n  * Methods related to norms\n    * `abs` (square-root of sum of squares of components)\n    * `norm` (sum of squares of components)\n    * `modulus`, `magnitude` (equal to `abs`)\n    * `absolute_square`, `abs2`, `mag2` (equal to `norm`)\n    * `normalized`\n    * `inverse`\n  * Methods related to array infrastructure\n    * `ndarray` (the numpy array underlying the quaternionic array)\n    * `flattened` (all dimensions but last are flattened into one)\n    * `iterator` (iterate over all quaternions)\n\nNote that this package makes a distinction between `abs` and `norm` — the latter being equal to the\nsquare of the former.  This version of the norm is also known as the "Cayley" norm, commonly used\nwhen emphasizing the properties of an object in an algebra, as opposed to the "Euclidean" norm more\ncommon when emphasizing the properties of an object in a vector space — though of course, algebras\nare vector spaces with additional structure.  This choice agrees with the [Boost library\'s\nimplementation of\nquaternions](https://www.boost.org/doc/libs/1_74_0/libs/math/doc/html/math_toolkit/value_op.html),\nas well as this package\'s forerunner\n[quaternion](https://github.com/moble/quaternion/blob/99913120b1b2a8a5eb7769c29ee760a236d40880/quaternion.h#L115-L120).\nThis also agrees with the corresponding functions on the [C++ standard library\'s complex\nnumbers](http://www.cplusplus.com/reference/complex/norm/).  Because this may be confusing, a number\nof aliases are also provided that may be less confusing.  For example, some people find the pair\n`abs` and `abs2` (meaning the square of `abs`) to be more sensible.\n\n\n## Rotations\n\nThe most common application of quaternions is to representing rotations by means of unit\nquaternions.  Note that this package does not *restrict* quaternions to have unit norms, since it is\nusually better for numerical purposes not to do so.  For example, whereas rotation of a vector $v$\nby a quaternion is usually implemented as $R\\, v\\, \\bar{R}$, it is generally better to drop the\nassumption that the quaternion has unit magnitude and implement rotation as $R\\, v\\, R^{-1}$.  This\nis almost always more efficient, and more accurate.  That is what this package does by default\nwhenever rotations are involved.\n\nAlthough this package does not restrict to unit quaternions, there are several converters to and\nfrom other representations of rotations, including\n\n   * `to_rotation_matrix`, `from_rotation_matrix`\n   * `to_transformation_matrix` (for non-unit quaternions)\n   * `to_axis_angle`, `from_axis_angle` representation\n   * `to_euler_angles`, `from_euler_angles` (though using Euler angles is almost always a bad idea)\n   * `to_spherical_coordinates`, `from_spherical_coordinates`\n   * `to_angular_velocity`, `from_angular_velocity`\n\nNote that the last item relates to quaternion-valued functions of time.  Converting to an angular\nvelocity requires differentiation, while converting from angular velocity requires integration (as\nexplored in [this paper](https://arxiv.org/abs/1604.08139)).\n\nFor these converters, the "to" functions are properties on the individual arrays, whereas the "from"\nfunctions are "classmethod"s that take the corresponding objects as inputs.  For example, we could\nwrite\n\n```python\nq1 = quaternionic.array(np.random.rand(100, 4)).normalized\nm = q1.to_rotation_matrix\n```\n\nto obtain the matrix `m` *from* a quaternionic array `q1`.  (Here, `m` is actually a series of 100\n3x3 matrices corresponding to the 100 quaternions in `q1`.)  On the other hand, to obtain a\nquaternionic array from some matrix `m`, we would write\n\n```python\nq2 = quaternionic.array.from_rotation_matrix(m)\n```\n\nAlso note that, because the unit quaternions form a "double cover" of the rotation group (meaning\nthat quaternions `q` and `-q` represent the same rotation), these functions are not perfect inverses\nof each other.  In this case, for example, `q1` and `q2` may have opposite signs.  We can, however,\nprove that these quaternions represent the same rotations by measuring the "distance" between the\nquaternions as rotations:\n\n```python\nnp.max(quaternionic.distance.rotation.intrinsic(q1, q2))  # Typically around 1e-15\n```\n\n\n## Distance functions\n\nThe `quaternionic.distance` contains four distance functions:\n\n  * `rotor.intrinsic`\n  * `rotor.chordal`\n  * `rotation.intrinsic`\n  * `rotation.chordal`\n\nThe "rotor" distances do not account for possible differences in signs, meaning that rotor distances\ncan be large even when they represent identical rotations; the "rotation" functions just return the\nsmaller of the distance between `q1` and `q2` or the distance between `q1` and `-q2`.  So, for\nexample, either "rotation" distance between `q` and `-q` is always zero, whereas neither "rotor"\ndistance between `q` and `-q` will ever be zero (unless `q` is zero).  The "intrinsic" functions\nmeasure the geodesic distance within the manifold of *unit* quaternions, and is somewhat slower but\nmay be more meaningful; the "chordal" functions measure the Euclidean distance in the (linear) space\nof all quaternions, and is faster but its precise value is not necessarily as meaningful.\n\nThese functions satisfy some important conditions.  For each of these functions `d`, and for any\nnonzero quaternions `q1` and `q2`, and *unit* quaternions `q3` and `q4`, we have\n\n  * symmetry: `d(q1, q2) = d(q2, q1)`\n  * invariance: `d(q3*q1, q3*q2) = d(q1, q2) = d(q1*q4, q2*q4)`\n  * identity: `d(q1, q1) = 0`\n  * positive-definiteness:\n    * For rotor functions `d(q1, q2) > 0` whenever `q1 ≠ q2`\n    * For rotation functions `d(q1, q2) > 0` whenever `q1 ≠ q2` and `q1 ≠ -q2`\n\nNote that the rotation functions also satisfy both the usual identity property `d(q1, q1) = 0` and\nthe opposite-identity property `d(q1, -q1) = 0`.\n\nSee [Moakher (2002)](https://doi.org/10.1137/S0895479801383877) for a nice general discussion.\n\n\n## Interpolation\n\nFinally, there are also capabilities related to interpolation\n\n  * slerp (spherical linear interpolation)\n  * squad (spherical quadratic interpolation)\n\n\n# Related packages\n\nOther python packages with some quaternion features include\n\n  * [quaternion](https://github.com/moble/quaternion/) (core written in C; very fast; adds\n    quaternion `dtype` to numpy; named\n    [numpy-quaternion](https://pypi.org/project/numpy-quaternion/) on pypi due to name conflict)\n  * [clifford](https://github.com/pygae/clifford) (very powerful; more general geometric algebras)\n  * [rowan](https://github.com/glotzerlab/rowan) (many features; similar approach to this package;\n    no acceleration or overloading)\n  * [pyquaternion](http://kieranwynn.github.io/pyquaternion/) (many features; pure python; no\n    acceleration or overloading)\n  * [quaternions](https://github.com/mjsobrep/quaternions) (basic pure python package; no\n    acceleration; specialized for rotations only)\n  * [scipy.spatial.transform.Rotation.as\\_quat](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.as_quat.html)\n    (quaternion output for `Rotation` object)\n  * [mathutils](https://gitlab.com/ideasman42/blender-mathutils) (a Blender package with python\n    bindings)\n  * [Quaternion](https://pypi.org/project/Quaternion/) (extremely limited capabilities; unmaintained)\n\nAlso note that there is some capability to do symbolic manipulations of quaternions in these\npackages:\n\n  * [galgebra](https://github.com/pygae/galgebra) (more general geometric algebras; analogous to\n    `clifford`, but for symbolic calculations)\n  * [sympy.algebras.quaternion](https://docs.sympy.org/latest/modules/algebras.html)\n',
    'author': 'Michael Boyle',
    'author_email': 'michael.oliver.boyle@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/moble/quaternionic',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
