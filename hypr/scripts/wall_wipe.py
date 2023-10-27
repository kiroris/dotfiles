import os

def get_next_filename(folder_path, current_index):
    files = sorted(os.listdir(folder_path))
    if current_index >= len(files):
        current_index = 0
    return files[current_index], (current_index + 1) % len(files)

def main():
    folder_path = '/home/kirill/.config/hypr/wallpapers'  # Замените на реальный путь к вашей папке
    state_file = '/dev/shm/state.txt'

    if not os.path.exists(state_file):
        current_index = 0
    else:
        with open(state_file, 'r') as f:
            current_index = int(f.read().strip())

    next_filename, next_index = get_next_filename(folder_path, current_index)

    command = f"swww img ~/.config/hypr/wallpapers/{next_filename} --transition-type wipe --transition-duration 3 "
    os.system(command)

    with open(state_file, 'w') as f:
        f.write(str(next_index))

if __name__ == '__main__':
    main()

