Custom data sources
=====================
Since version ``v.1.3.0``, the software supports custom data sources. To use this feature, **copy** the ``data`` folder
to the desired location and modify its contents there.

.. danger::
    Do not modify the data folder directly. At startup, Kali MC checks the integrity of the original
    data. If these files are modified, the application will not start.

To enable custom data sources the parameter *enable_external_data* has to be enabled in the ``local_conf.py`` file,
together with the path to the customized data in *external_data_path*.

Modifying the original data
-----------------------------
The files in the ``data`` folder are numpy .npz files. In order to modify them, a python installation with the numpy
package needs to be available.

Output factors
##################
The following code modifies the output factor of the 8 cm applicator (C\ :sub:`8`\):

.. code-block:: python

   import numpy as np

   # Load the OF_C8.npz file. OF -> Output factors
   npzfile = r'path-to-your-custom-data/OF_C8.npz'  # Change path-to-your-custom-data with your data path
   OFs = np.load(npzfile, allow_pickle=True)['OFs']


.. code-block:: python

   # Check existing output factors
   OFs
   array([[1.16 , 1.165, 1.153, 1.141],
       [1.166, 1.182, 1.168, 1.142],
       [1.203, 1.22 , 1.215, 1.178],
       [1.27 , 1.27 , 1.245, 1.236]])


The different energies ``[6, 8, 10, 12]`` correspond to columns in the output factors (OFs) and the bevels
``[0, 15, 30, 45]`` correspond to rows.
For example, if we would like to modify the output factor of C\ :sub:`8`\B\ :sub:`45` \ and 10 MeV:

.. code-block:: python

        OFs[3, 2] = 1.5  # Assign 1.5 to the corresponding item in OF.

.. code-block:: python

   # Check the modified item in the array
   OFs
   array([[1.16 , 1.165, 1.153, 1.141],
       [1.166, 1.182, 1.168, 1.142],
       [1.203, 1.22 , 1.215, 1.178],
       [1.27 , 1.27 , 1.5  , 1.236]])

Finally, save the data to the npz file.

.. code-block:: python

   np.savez(npzfile, OFs=OFs)

R90 values
#################
The procedure is almost the same as in the previous section:

.. code-block:: python

   import numpy as np

   # Load the OF_C8.npz file. OF -> Output factors
   npzfile = r'path-to-your-custom-data/R90_C8.npz'  # Change path-to-your-custom-data with your data path
   R90s = np.load(npzfile, allow_pickle=True)['R90']

.. code-block:: python

   # Check existing R90s
   R90s
   array([[1.46, 1.35, 1.1 , 0.72],
       [1.86, 1.72, 1.43, 0.93],
       [2.36, 2.17, 1.81, 1.24],
       [2.78, 2.57, 2.17, 1.53]])

Modify desired item:

.. code-block:: python

   R90s[0,2] = 0.95

Verify that the R90s array is modified accordingly:

.. code-block:: python

   R90s
   array([[1.46, 1.35, 0.95, 0.72],
       [1.86, 1.72, 1.43, 0.93],
       [2.36, 2.17, 1.81, 1.24],
       [2.78, 2.57, 2.17, 1.53]])

Save the data to the npz file.

.. code-block:: python

   np.savez(npzfile, R90s=R90s)

Rescaling factors
##################
Rescaling factors are saved in ``data/rescale_factors.npy``

.. code-block:: python

   npyfile = r'path-to-your-custom-data/rescale_factors.npy'
   r_factors = np.load(npyfile, allow_pickle=True)

All the rescaling factors are stored in the same numpy array, the different energies [6, 8, 10, 12] correspond to
columns, while the order of rows is as follows:

.. code-block:: python

   r_factors
   array([[1.03, 1.05, 1.05, 1.05],  # C12B0
       [1.05, 1.05, 1.08, 0.  ],     # C12B15
       [0.  , 0.  , 0.  , 0.  ],     # C12B30
       [0.  , 0.  , 0.  , 0.  ],     # C12B45
       ....
       [1.  , 1.  , 1.  , 1.  ],     # C3B40
       [1.  , 1.  , 1.  , 1.  ],     # C3B15
       [1.  , 1.  , 1.  , 1.  ],     # C3B30
       [1.  , 1.  , 1.  , 1.  ]])    # C3B45

.. warning::

   If *rescale_factors* parameter is enabled in ``local_conf.py`` and null rescaling factors are stored, the corresponding
   applicator/bevel/energy will be effectively disabled.
