import numpy as np
from pytransform3d import rotations as pr
from numpy.testing import assert_array_almost_equal


def test_compact_axis_angle_from_quaternion():
    from dmp_fast import compact_axis_angle_from_quaternion as compact_axis_angle_from_quaternion_cython
    from pytransform3d.rotations import compact_axis_angle_from_quaternion as compact_axis_angle_from_quaternion_python

    q = np.array([-9.99988684e-01, -4.73967909e-03,  3.10305586e-04,  2.67831240e-04])
    axis_angle_python = compact_axis_angle_from_quaternion_python(q.copy())
    axis_angle_cython = compact_axis_angle_from_quaternion_cython(q.copy())

    q2 = np.array([9.89307860e-01,  1.45783469e-01, -4.06641953e-03,  7.76339940e-04])
    axis_angle_2_python = compact_axis_angle_from_quaternion_python(q2.copy())
    axis_angle_2_cython = compact_axis_angle_from_quaternion_cython(q2.copy())

    assert_array_almost_equal(axis_angle_python, axis_angle_cython)
    assert_array_almost_equal(axis_angle_2_python, axis_angle_2_cython)
