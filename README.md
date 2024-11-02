<p align="center">
  <img alt="Kali MC" src="kali_mc/ui/res/splash-kali.png">
</p>

**Software for calculating IORT treatments with a LIAC HWL linac, based on precalculated Monte Carlo dose distributions in water.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fradiofisica-hgugm%2Fkali_mc%2Fmain%2Fpyproject.toml)
[![Documentation Status](https://readthedocs.org/projects/kali-mc/badge/?version=latest)](https://kali-mc.readthedocs.io/en/latest/?badge=latest)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14009300.svg)](https://doi.org/10.5281/zenodo.14009299)


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

## Documentation:
[https://kali-mc.readthedocs.io/](https://kali-mc.readthedocs.io/)
