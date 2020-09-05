import setuptools

setuptools.setup(
    name='voxelmorph',
    version='0.1',
    license='gpl-3.0',
    description='Image Registration with Convolutional Networks',
    url='https://github.com/voxelmorph/voxelmorph',
    keywords=['deformation', 'registration', 'imaging', 'cnn', 'mri'],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'scikit-image',
        'h5py',
        'numpy',
        'scipy',
        'nibabel',
        'neurite',
    ]
)
