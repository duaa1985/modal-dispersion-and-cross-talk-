# modal-dispersion-and-cross-talk-
This is an implementation for calculation of dispersion and cross-talk
in large-core multimode fiber with and without mode dependent loss. In
this implimentation we uses different length of fiber, different core
diameter of fiber, and diferent coupling regaime to plot frequency
response and crosstalk in the fiber vs modulation bandwidth.
To plot different frequency response and cross-talk we have to follows following procedure
# Prerequisites
1. Install "numpy"

2. Install "scipy"

- To plot frequency response of the fiber without mode dependent loss
vs modulation bandwidth :

1.  Run `lossless_dispersion.py`, it will save the first order and
higher order frequency response of the fiber as file for different
length, diameter and radius of curvature.

2. Run `lossless_dispersion_plot.py`, it will plot graph between
frequency response a fiber and modulation bandwidth, using files which
are saved by `lossless_dispersion.py`.

- To plot cross-talk in multiplexed signal in fiber without mode dependent loss

1. Run `lossless_crosstalk.py`, it will save the first order and
higher order frequency response of the fiber as file for different
length, diameter and radius of curvature.

2.  Run `lossless_crosstalk_plot.py`, it will plot graph between
frequency response a fiber and modulation bandwidth, using file which
are saved by `lossy_crosstalk.py`.

- To plot frequency responseTo plot frequency response of the fiber
with mode dependent loss vs modulation bandwidth

 1. Run `propagationmatrix.py` to generate modal projection from lossy
section to lossless section and save it as a file.

2. Run `lossy_dispersion.py`, it will save the first order and higher
order frequency response of the fiber as file for different length,
diameter and radius of curvature.

3.  Run `lossy_dispersion_plot.py`, it will plot graph between
frequency response a fiber and modulation bandwidth, using files which
are saved by `lossy_dispersion.py`.

- To plot cross-talk in multiplexed signal in fiber without mode dependent loss

1. Run `propagationmatrix.py` to generate modal projection from lossy
section to lossess section and save it as a file.

2. Run `lossy_multiplexing_1km.py`, it will save the first order and
higher order frequency response of the fiber as file for different
length, diameter and radius of curvature.

3.  Run `lossy_crosstalk_plot.py`, it will plot graph between
frequency response a fiber and modulation bandwidth, using file which
are saved by 'lossy_multiplexing_1km.py'.

- To plot Bit error rate (BER) vs. signal to noise ratio (SNR)

1. Run `BER.py`, it save BER for different SNR at different frequency

2.  Run `BER_plot`, it average BER over different modulation bandwidth
and plot using files saved by `BER.py`





