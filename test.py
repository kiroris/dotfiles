import os
import shutil
import subprocess

# Получаем имя текущего пользователя
current_user = subprocess.getoutput('whoami')

# Пути для копирования

# Возвращает путь к файлу, где выполняется данный код.
script_directory = os.path.dirname(os.path.abspath(__file__))

# Путь до конфига zsh
zsh_source = os.path.join(script_directory, 'zsh/')

# Путь назначения для файлов zsh
zsh_destination = f'/home/{current_user}/'

# Возвращает путь к директории с конфигами
config_source = os.path.join(script_directory, '')

# Путь назначения для конфигов
config_destination = f'/home/{current_user}/.config/'

# Директории, файлы из которых нужно переместить в домашнюю директорию
move_to_home = ['dir1', 'dir2']

# Копирование файлов zsh
for file_name in os.listdir(zsh_source):
    source_file = os.path.join(zsh_source, file_name)
    if os.path.isfile(source_file):
        shutil.copy(source_file, zsh_destination)
print("The zsh config has been copied...")

# Копирование остальных директорий
for dir_name in os.listdir(config_source):
    source_dir = os.path.join(config_source, dir_name)
    if os.path.isdir(source_dir):
        base_name = os.path.basename(source_dir)
        if base_name not in move_to_home and base_name not in ['zsh', 'tmux', 'apex-legend', '.git']:
            destination_dir = os.path.join(config_destination, base_name)
            if os.path.exists(destination_dir):
                if os.path.isdir(destination_dir):
                    shutil.rmtree(destination_dir)
                else:
                    os.remove(destination_dir)
            shutil.copytree(source_dir, destination_dir)
print("The rest of the configurations have been copied...")

# Перемещение файлов из директорий, указанных в move_to_home, в домашнюю директорию
for dir_name in move_to_home:
    source_dir = os.path.join(config_source, dir_name)
    if os.path.isdir(source_dir):
        for file_name in os.listdir(source_dir):
            source_file = os.path.join(source_dir, file_name)
            shutil.move(source_file, zsh_destination)
print("Files from specified directories moved to home directory...")

print("Script was executed successfully...")

