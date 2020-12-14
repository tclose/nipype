from nipype.interfaces.base import traits
from .mrtrix3.reconst import (
    ConstrainedSphericalDeconvolutionInputSpec,
    ConstrainedSphericalDeconvolution)

# Remove algorithm attribute from the input spec
class SS3TConstrainedSphericalDeconvolutionInputSpec(
    ConstrainedSphericalDeconvolutionInputSpec):

    # Disable the algorithm trait as it isn't required for ss3t_csd
    algorithm = traits.Any()


class SS3TConstrainedSphericalDeconvolution(ConstrainedSphericalDeconvolution):
    """
    Estimate fibre orientation distributions from diffusion data using spherical deconvolution

    This interface supersedes :py:class:`.EstimateFOD`.
    The old interface has contained a bug when using the CSD algorithm as opposed to the MSMT CSD
    algorithm, but fixing it could potentially break existing workflows. The new interface works
    the same, but does not populate the following inputs by default:

    * ``gm_odf``
    * ``csf_odf``
    * ``max_sh``

    Example
    -------

    >>> import nipype.interfaces.mrtrix3 as mrt
    >>> fod = mrt.SS3TConstrainedSphericalDeconvolution()
    >>> fod.inputs.in_file = 'dwi.mif'
    >>> fod.inputs.wm_txt = 'wm.txt'
    >>> fod.inputs.wm_txt = 'gm.txt'
    >>> fod.inputs.wm_txt = 'csf.txt'
    >>> fod.inputs.grad_fsl = ('bvecs', 'bvals')
    >>> fod.cmdline
    'ss3t_csd_beta1 -fslgrad bvecs bvals dwi.mif wm.txt wm.mif gm.txt gm.mif csf.txt csf.mif'
    >>> fod.run()  # doctest: +SKIP
    """

    _cmd = "ss3t_csd_beta1"
    input_spec = SS3TConstrainedSphericalDeconvolutionInputSpec
