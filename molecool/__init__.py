"""A Python package to visualize molecules given their Cartesian coordinates.
This was created for the Python Best Practices Workshop."""

# Add imports here
from .functions import canvas
from molecool.measure import calculate_distance, calculate_angle
from molecool.atom_data import atom_colors, atomic_weights
from molecool.visualization import draw_molecule
from molecool.molecules import bond_histogram, build_bond_list, compute_molecular_mass
from molecool.io import open_pdb
# from molecool import io --> this will also work

from ._version import __version__
