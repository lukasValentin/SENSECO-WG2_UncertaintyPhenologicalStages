'''
Created on Oct 26, 2021

@author: Lukas Graf (D-USYS, ETHZ)
'''

import glob
import numpy as np
import rasterio as rio
import pandas as pd
from pathlib import Path


def raster_statistics(
        raster_file: Path
    ) -> dict:
    """
    Extracts the min, max, mean and standard deviation of a
    single band raster (in case of a multi-band raster, the first
    band is used). We assume the raster has no missing values
    (NaNs).

    :param raster_file:
        file path to the raster file to be analyzed
    :return:
        dictionary with extracted descriptive statistics
    """

    # read first band into an array
    with rio.open(raster_file, 'r') as src:
        data = src.read(1)

    # analyze the statistics
    stats_dict = {}
    stats_dict['mean'] = np.mean(data)
    stats_dict['std'] = np.std(data)
    stats_dict['min'] = np.min(data)
    stats_dict['max'] = np.max(data)
    stats_dict['min-max'] = stats_dict['max'] - stats_dict['min']

    return stats_dict


if __name__ == '__main__':

    # define directory with raster results
    result_dir = Path('./../data/outputs')

    # define directory for saving the analysis results to
    output_dir = Path('./../data/analysis')

    # get lost of files and extract their meaning in terms of phenological metrics
    raster_files = glob.glob(result_dir.joinpath('*.tif').as_posix())
    raster_vars = ['_'.join(Path(x).name.split('_')[:-1]) for x in raster_files]

    # loop over files (i.e., phenological metrics) and extract their statistics
    # in terms of mean, standard deviation and min-max spread to quantify the
    # impact of radiometric uncertainty
    stats = {}
    for pheno_metric in zip(raster_files, raster_vars):
        res = {}
        res['metric'] = pheno_metric[1]
        res.update(raster_statistics(raster_file=pheno_metric[0]))
        stats[pheno_metric[1]] = res

    pheno_metrics = pd.DataFrame(stats).transpose()
    fname_res = result_dir.joinpath('phenological_metrics.csv')
    pheno_metrics.to_csv(fname_res, index=False)

        