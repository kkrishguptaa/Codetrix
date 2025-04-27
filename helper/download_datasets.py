import os

import kaggle

datasets = [
    "berkeleyearth/climate-change-earth-surface-temperature-data",
    "bigironsphere/gpcc-monthly-precipitation-dataset-05x05",
    "jarredpriester/global-sea-level-rise",
    "ulrikthygepedersen/co2-emissions-by-country",
    "nsidcorg/daily-sea-ice-extent-data",
]

# Folder where all datasets will be stored
# ../data
base_folder = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "data"
)

# Ensure base folder exists
os.makedirs(base_folder, exist_ok=True)

# Download each dataset
for dataset in datasets:
    # if folder already exists, skip download
    # Create a subfolder for each dataset
    dataset_name = dataset.split("/")[-1]
    dataset_folder = os.path.join(base_folder, dataset_name)

    # Check if the dataset folder already exists
    if os.path.exists(dataset_folder):
        print(
            f"Dataset {dataset} already exists in {dataset_folder}. Skipping download."
        )
        continue
    # Create the dataset folder
    os.makedirs(dataset_folder, exist_ok=True)

    # Download the dataset using Kaggle API
    print(f"Downloading {dataset}...")
    try:
        kaggle.api.dataset_download_files(dataset, path=dataset_folder, unzip=True)
        print(f"Downloaded {dataset} to {dataset_folder}")
    except Exception as e:
        print(f"Failed to download {dataset}: {e}")

print("All downloads complete.")
