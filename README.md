# :construction: :stop_sign: Do not delete :stop_sign: :construction:
## :bulb: This feedstock is used for testing https://github.com/pangeo-forge/pangeo-forge-runner



# gpcp-from-gcs-feedstock

Pangeo Forge feedstock for gpcp-from-gcs.

- This feedstock uses the same data as fetched by the [official `gpcp-feedstock` here](https://github.com/pangeo-forge/gpcp-feedstock/blob/78ebfa39faafbb3eb352b3cdc0856d4b1a722b95/feedstock/recipe.py#L11-L19).
- Rather than sourcing these data from https://www.ncei.noaa.gov, this feedstock pulls from a cache of these data on Pangeo Forge's GCS.
- The cached input data are stored under the key `gs://pforge-test-data/gpcp/` and are all publicly accessible.
- In the GCS cache, the original paths have been shortened for readability and predictability. (In the original paths, inclusion of a
"created on" date makes progamatically determining a given path impossible without listing the source file server. The "created on" date has been
removed for the GCS cache, so that the source paths can be determined more easily in this feedstock's recipe.)
- As of writing, the date range used in this feedstock has been constrained to about 1/10th of the total volume of data used for the official
`gpcp-feedstock`. This is done to keep the volume of data moved by, and runtime of, tests as efficient as possible. All of the data used for the
official feedstock are cached in `gs://pforge-test-data/gpcp/`, however, so the date range could be adjusted if desired.
