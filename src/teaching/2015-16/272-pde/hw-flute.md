title: Flute and Birds Optional Problem
{%- from get_file('course_info.j2') import course %}
breadcrumb: index.html|{{course.title}}

[[static/mixed.wav|This file]] contains a mix of two audio clips: One of birds
chirping, and the other of a flute. Your task is to remove the chirping birds,
and recover (as well as you can) the original clip of the flute alone. (I would
need to see an algorithm and/or code, as well as the final result.)

I will measure the error as follows: Convert your wave file to a vector, and
normalise it to have length 1. (If your WAV file is stereo, both channels will
be averaged to convert it to mono.) I will take the original wave file for the
flute and convert it to a vector (again normalised to have length 1). The error
will be half the distance between the above two normalised vectors. (The
distance (as measured above) between the mixed clip and the original flute
sample is about 0.2578. My code currently reduces this distance to 0.0446, at
which point the birds are essentially inaudible, with very little
"artifacting". See if you can do better!)

I'd recommend using Matlab, [Octave] or [SciPy]/[NumPy] to do this. If you
choose to use Matlab/Octave, a few functions you'll find helpful are `wavread`,
`wavwrite`, `fft` and `ifft`. If you use a different language, don't reinvent the
wheel: find a library that read wave files and Fourier transforms functions. 

[Octave]: http://www.gnu.org/software/octave
[SciPy]: http://www.scipy.org/
[NumPy]: http://www.numpy.org/
