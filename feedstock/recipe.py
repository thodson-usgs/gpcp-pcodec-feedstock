import apache_beam as beam
import pandas as pd

from pangeo_forge_recipes.patterns import ConcatDim, FilePattern
from pangeo_forge_recipes.transforms import OpenURLWithFSSpec, OpenWithXarray, StoreToZarr

dates = [
    d.to_pydatetime().strftime('%Y%m%d')
    for d in pd.date_range("1996-10-01", "1999-02-01", freq="D")
]

def make_url(time):
    url_base = "https://storage.googleapis.com/pforge-test-data"
    return f"{url_base}/gpcp/v01r03_daily_d{time}.nc"


concat_dim = ConcatDim("time", dates, nitems_per_file=1)
pattern = FilePattern(make_url, concat_dim)


# FIXME[2]: Dynamic assignment of `target_path` (and `cache_path`)?
# from tempfile import TemporaryDirectory
# td = TemporaryDirectory()
target_path = "output.zarr"

recipe = (
    # FIXME[1]: `pattern_pruned`
    beam.Create(pattern.items())
    | OpenURLWithFSSpec()
    # FIXME[1]: `pattern_pruned`
    | OpenWithXarray(file_type=pattern.file_type)
    | StoreToZarr(
        # FIXME[2]: `target_path`
        target_url=target_path,
        combine_dims=pattern.combine_dim_keys,
    )
)
