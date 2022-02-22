# matrix is strictly same size

from numpy import *

a = array(
    [
        ["Mon", 1, 2, 3, 4],
        ["Tues", 5, 6, 7, 8],
        ["Wed", 9, 10, 11, 12],
        ["Thurs", 13, 14, 15, 16],
        ["Fri", 17, 18, 19, 20],
    ]
)

m = reshape(a, (5, 5))
print(m)
