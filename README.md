# Kali MC
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Documentation Status](https://readthedocs.org/projects/kali-mc/badge/?version=latest)](https://kali-mc.readthedocs.io/en/latest/?badge=latest)

Software for calculating IORT treatments with a LIAC HWL linac, based on precalculated Monte Carlo dose distributions in water.

![3D applicator setup](kali_mc/ui/res/splash-kali.png?raw=true "3D applicator setup")

## Main Features:
- Visualize absorbed dose distributions of all combinations of applicators and energies
- Calculate monitor units (MU) with measured output factors at zmax
- Pressure correction available
- Rescaling factors can be added for desired combinations
- Report generation in pdf
- Send data as RTPlan to Record and Verify software (only tested with MOSAIQ)

## Limitations:
- The software is intended for educational purposes
- The Monte Carlo model was fitted to the data accquired at Gregorio Marañón hospital, Madrid.
  Different linacs may show dosimetric differences.
