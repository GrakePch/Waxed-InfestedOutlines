import os
import json

# List of block IDs
block_ids = [
    "infested_chiseled_stone_bricks", "infested_cobblestone", "infested_cracked_stone_bricks", "infested_deepslate", "infested_mossy_stone_bricks", "infested_stone_bricks", "infested_stone", 
    "waxed_copper_block", "waxed_exposed_copper", "waxed_weathered_copper", "waxed_oxidized_copper"
]

copper_variants = [
    "chiseled_copper", "copper_bulb", "copper_door", "copper_grate", "copper_trapdoor", "cut_copper_slab", "cut_copper_stairs", "cut_copper"
]

copper_oxidation_stages = [
    "", "exposed_", "weathered_", "oxidized_"
]

# Generate block IDs for copper variants
for variant in copper_variants:
    for stage in copper_oxidation_stages:
        block_ids.append(f"waxed_{stage}{variant}")

# Output directory for JSON files
output_dir = "./assets/minecraft/items/"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Generate JSON files
for block_id in block_ids:
    file_name = f"{block_id}.json"
    file_path = os.path.join(output_dir, file_name)
    
    # JSON content
    content = {
        "model": {
            "type": "minecraft:model",
            "model": f"minecraft:item/{block_id}"
        }
    }
    
    # Write JSON to file
    with open(file_path, "w") as json_file:
        json.dump(content, json_file, indent=2)
        print(f"Generated: {file_path}")