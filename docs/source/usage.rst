Usage
======
This section describe the general usage of the software.
Follow the next subsections to calculate a treatment, generate a report and send it to a R&V system  with Kali MC.


.. _kali-screemshot:
.. image:: figures/kali-screenshot.png
    :align: center
    :width: 100 %

The software shows absorbed dose distributions in water, pre-calculated with penEasy 2020 :footcite:p:`sempauPENELOPEbasedSystemAutomated2011`,
based in PENELOPE 2018 :footcite:p:`nuclearenergyagencyPENELOPE2018Code2019`.

Additionally, it

Applicator
-------------
Choose between the available applicator diameters (3, 4, 5, 6, 7, 8, 9, 10 and 12 cm) and bevel endings (0º, 15º, 30º and
45º).

.. _kali-applicator:
.. image:: figures/kali-applicator.png
    :align: center
    :width: 35 %


Prescription
-------------
Enter the prescribed dose in cGy and the desire depth in cm (depth of the 90% isodose).

.. _kali-prescription:
.. image:: figures/kali-prescription.png
    :align: center
    :width: 35 %

Energy selection
-----------------
Choose the desired energy comparing its R\ :sub:`90`\  with the prescribed treatment depth.

.. _kali-energies:
.. image:: figures/kali-energies.png
    :align: center
    :width: 35 %

|

.. note::
    If rescaling factors are enabled in ``local_conf.py``, the associated factors will show next to the R\ :sub:`90` \
    values.

MU calculation
-----------------
Once the diameter and the bevel of the applicator and the desired energy are selected, it is necessary to enter the
current atmospheric pressure in hPa.
This is needed since the monitor system of the linac does not perform a pressure correction and undesirable deviations
in output can be observed if not corrected.

For that purpose, the atmospheric pressure at the time of calibration of the equipment (Pref) must be recorded.
It is possible to modify this parameter customizing the configuration file ``local_conf.py`` (see Configuration file
section).

The following expression is used for calculating Monitor Units:

.. math::
   UM = round((D * P_{now} * resc. factor) / (cGy/UM * (presc. isodose / 100) * P_{ref})

where:

D
    Prescribed Dose in cGy
Pnow
    Current atmospheric pressure (hPa)
resc. factor
    Rescaling factor, if activated, otherwise resc. factor=1

cGy/UM
    Output factor at zmax for the current applicator and energy combination in cGy per MU.
prescr. isodose
    Prescription isodose, non-editable, 90% isodose.
Pref
    Atmospheric pressure (hPa) at calibration time.

.. _kali-calculation:
.. image:: figures/kali-calculation.png
    :align: center
    :width: 35 %


|


.. footbibliography::