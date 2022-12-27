import apache_beam as beam
import pandas as pd

from pangeo_forge_recipes.patterns import ConcatDim, FilePattern, prune_pattern
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


# FIXME[1]: How is `--prune` going to work in runner?
# We can't have contributors calling `prune_pattern` themselves...
pattern_pruned = prune_pattern(pattern)

# FIXME[2]: Dynamic assignment of `target_path` (and `cache_path`)?
# from tempfile import TemporaryDirectory
# td = TemporaryDirectory()
target_path = "output.zarr"

recipe = (
    # FIXME[1]: `pattern_pruned`
    beam.Create(pattern_pruned.items())
    | OpenURLWithFSSpec()
    # FIXME[1]: `pattern_pruned`
    | OpenWithXarray(file_type=pattern_pruned.file_type)
    | StoreToZarr(
        # FIXME[2]: `target_path`
        target_url=target_path,
        combine_dims=pattern.combine_dim_keys,
    )
)
