"""Implementation of Largest Triangle Three Bucket."""
import numpy as np


def lttb(x, y, threshold):
    """Compute downsampling of given series using Largest Triangle Three Buckets algorithm.

    :param x: abscissae of original sample
    :type x: sequence of floats
    :param y: ordinates of original sample
    :type y: sequence of floats
    :param threshold: number of required points required in the downsampled series. Should be
     greater than 2 and less or equal to length of the input data.
    :type threshold: float
    :returns: (downsampled_x, downsampled_y), abscissae and ordinates of downsampled series.
    :rtype: tuple of numpy.ndarray
    :raises ValueError: if x and y are not of the same length or threshold is not in the
     acceptable range.
    """
    # Handle edge cases
    if len(x) != len(y):
        raise ValueError('Both x and y need to have the same size')

    if threshold <= 2 or threshold > len(x):
        raise ValueError('Invalid threshold (should be > 2 and <= len(x)).')

    # Compute bucket size - note that it can be nonintegral number
    bucket_size = (len(x) - 2) / (threshold - 2)

    # Stack data into two-row matrix for easier access later on
    data = np.vstack([x, y])

    # Preallocate sample for result
    result = np.zeros((2, threshold))

    # The first point we base our triangles on is the first point in the data
    # It is also the first point in the output array
    left_point = data[:, 0]
    result[:, 0] = left_point

    # Instead of computing the edges of buckets dynamically, we compute them all beforehand
    # This prevents us from computing the same edge multiple times
    edges = ((np.arange(threshold) * bucket_size).astype(int) + 1).clip(1, len(x))

    # Compute all points except first and the last one
    for i in range(threshold-2):
        # Right (fixed) point is a center of mass of the next bucket, i.e. its coordinates
        # are equal to respective averages of coordinates of points in the bucket
        right_point = data[:, edges[i+1]:edges[i+2]].sum(axis=1) / (edges[i+2] - edges[i+1])

        # Areas of triangles are computed using determinants (usual formula for an area of
        # a triangle). We can instruct numpy to compute them all at once - this is done
        # by arranging all possible determinants along third axis. Other axes hold
        # data for coordinates of points and a row of ones.
        squares = np.ones((edges[i+1]-edges[i], 3, 3))
        squares[:, 1, 0:2] = left_point
        squares[:, 2, 0:2] = right_point
        squares[:, 0, 0:2] = data[:, edges[i]:edges[i+1]].T
        areas = 0.5 * np.abs(np.linalg.det(squares))
        idx = areas.argmax()
        left_point = data[:, edges[i] + idx]
        result[:, i+1] = left_point

    result[:, -1] = right_point
    return result[0, :], result[1, :]
