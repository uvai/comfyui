#!/usr/bin/env python3
"""
download_gdrive.py

A Python script to download files from Google Drive using `gdown`,
showing a progress bar and checking if a file already exists before downloading.
If the target folder doesn't exist, it will be created automatically.
"""

import os
import gdown

# ------------------------------------------------------------------------------
# 1) Define the files to download as a list of dictionaries:
#    Each entry has:
#       "url"      : The Google Drive share URL
#       "folder"   : Where to store the downloaded file
#       "filename" : The final filename to use on disk
#
#   NOTE: We specify the filename ourselves because older `gdown` versions
#         don't provide a simple way to retrieve the Drive "title" in Python.
# ------------------------------------------------------------------------------
FILES = [
	# {
	# 	# "url": "https://drive.google.com/file/d/1O6HfxHHbau_vgrLi0WyJ8ZDyAwv4sv0R/view?usp=sharing",
	# 	# "folder": "/workspace/ComfyUI/models/loras",
	# 	# "filename": "clip_l.safetensors"
	# },
	# {
	# 	# "url": "https://drive.google.com/file/d/1N7l_0U2ceiwRVNogPCoKjrHFNmx_2huV/view?usp=sharing",
	# 	# "folder": "/workspace/storage/stable_diffusion/models/ckpt",
	# 	# "filename": "pornmasterAmateur_sdxlV1VAE.safetensors"
	# },
	# {
	# 	# "url": "https://drive.google.com/file/d/1g_cyxEmO0FDfaa7JcFG392GxYKcQNgMX/view?usp=sharing",
	# 	# "folder": "/workspace/storage/stable_diffusion/models/loras",
	# 	# "filename": "KUTits_PONY.safetensors"
	# },
	{#JOAN
		"url": "https://drive.google.com/file/d/1iDnHmvENV60FUziu2qia9cY_leI-ISmC/view?usp=sharing",
		"folder": "/workspace/storage/stable_diffusion/models/lora",
		"filename": "joan_v1_epoch40.safetensors"
	},
	{#tittydrop
		"url": "https://drive.google.com/file/d/1YE8_KF4rMHe3UmGKDZPC0x9N-avLn2Tq/view?usp=sharing",
		"folder": "/workspace/storage/stable_diffusion/models/lora",
		"filename": "breast_drop_v2_170.safetensors"
	},
	{#cowgirl
		"url": "https://drive.google.com/file/d/1RX36SDRGhYqpIt1P9VhcwmFflIlm7V--/view?usp=sharing",
		"folder": "/workspace/storage/stable_diffusion/models/lora",
		"filename": "pov_cowgirlposition_hunyuan_V3.safetensors"
	},
	{#edgeofreality
		"url": "https://drive.google.com/file/d/1hj2_korPlDPAnF1BElzyDKE6864cAecY/view?usp=sharing",
		"folder": "/workspace/storage/stable_diffusion/models/lora",
		"filename": "edge_of_reality_ep30_25200stp_lora_theaidoctor.safetensors"
	},
	{#vintage
		"url": "https://drive.google.com/file/d/1b55oYWLTRd5qwi11Yn3vn61crQ-icbrv/view?usp=sharing",
		"folder": "/workspace/storage/stable_diffusion/models/lora",
		"filename": "vintage_e60_512.safetensors"
	},
	
	# Add more entries as needed...
	
]

def main():
	"""
	Download files from Google Drive into specified folders, showing a progress bar.
	If the file already exists in the target folder, skip re-downloading it.
	"""
	for item in FILES:
		
		print(f"Debug: Processing item - {filename}")
		
		url = item["url"]
		folder = item["folder"]
		filename = item["filename"]

		print(f"\nProcessing: {url}")
		print(f"Target folder: {folder}")
		print(f"Final filename: {filename}")

		# 1. Ensure the target folder exists
		if os.path.exists(folder) and not os.path.isdir(folder):
			print(f"  ❌ Error: '{folder}' exists but is not a directory. Skipping.")
			continue
		os.makedirs(folder, exist_ok=True)

		# 2. Build the full path where the file should be saved
		target_path = os.path.join(folder, filename)

		# 3. Check if the file already exists
		if os.path.isfile(target_path):
			print(f"  ✅ File already exists: {target_path}. Skipping download.")
			continue

		# 4. Download with a progress bar (quiet=False)
		#    `fuzzy=True` lets gdown parse the share URL automatically.
		print(f"  Downloading to: {target_path}")
		downloaded_filepath = gdown.download(
			url=url,
			output=target_path,
			quiet=False,   # Show progress bar
			fuzzy=True
		)

		# 5. Verify the download
		if downloaded_filepath is None:
			print(f"  ❌ Download failed for: {url}")
		else:
			print(f"  ✅ Saved file to: {downloaded_filepath}")

	print("\nAll downloads complete!")


if __name__ == "__main__":
	main()