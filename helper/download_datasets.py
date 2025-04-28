import os

import kaggle

print("*****************************************")
print("Downloading datasets from Kaggle...")
print("*****************************************")
print("\n")

if not os.path.exists(os.path.expanduser("~/.kaggle/kaggle.json")):
    print(
        "Kaggle API credentials not found. Please set up your Kaggle API credentials."
    )

    print(
        "You can find instructions here: https://www.kaggle.com/docs/api#getting-started-installation-&-authentication"
    )

    exit(1)

datasets = [
    "berkeleyearth/climate-change-earth-surface-temperature-data",
    "bigironsphere/gpcc-monthly-precipitation-dataset-05x05",
    "jarredpriester/global-sea-level-rise",
    "ulrikthygepedersen/co2-emissions-by-country",
    "nsidcorg/daily-sea-ice-extent-data",
]

base_folder = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "imports", "data"
)

os.makedirs(base_folder, exist_ok=True)

print(f"Base folder for datasets: {base_folder}")

for dataset in datasets:
    print("------------------------")
    print(f"Downloading {dataset}...")
    print("------------------------")

    dataset_name = dataset.partition("/")[2]  # exclude the username

    dataset_folder = os.path.join(base_folder, dataset_name)

    if os.path.exists(dataset_folder):
        print(
            f"Dataset {dataset} already exists in {dataset_folder}. Skipping download."
        )
        continue

    os.makedirs(dataset_folder, exist_ok=True)

    print(f"Downloading {dataset}...")

    try:
        kaggle.api.dataset_download_files(dataset, path=dataset_folder, unzip=True)
        print(f"Downloaded {dataset} to {dataset_folder}")
    except Exception as e:
        print(f"Failed to download {dataset}: {e}")

print("\n")
print("*****************************************")
print("All downloads complete.")
print("*****************************************")
