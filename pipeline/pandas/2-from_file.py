#!/usr/bin/env python3
import pandas as pd
"""loads data from a file as a pd.DataFrame"""


def from_file(filename, delimiter):
    """
    Args:
        -filename is the file to load from
        -delimiter is the column separator
    Returns:
        -the loaded pd.DataFrame
    """
    return pd.read_csv(filename, delimiter=delimiter)
