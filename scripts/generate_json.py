import json

if __name__ == '__main__':
    with open('transforms_val.json', 'r') as f:
        original_data = json.load(f)

    folder_path = './val/'
    new_frames = []

    for i in range(72):
        file_path = f'{folder_path}image_{i}.json'
        with open(file_path, 'r') as file:
            transform_matrix = json.load(file)
            print(transform_matrix)

        new_frame = {
            "file_path": f"./val/{i}",
            "rotation": original_data["frames"][i]["rotation"],
            "transform_matrix": transform_matrix
        }
        new_frames.append(new_frame)
    #
    original_data["frames"] = new_frames

    with open('new_transforms_val.json', 'w') as f:
        json.dump(original_data, f, indent=4)