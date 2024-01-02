import os
import shutil
import subprocess

# Получаем имя текущего пользователя
current_user = subprocess.getoutput('whoami')

# Пути для копирования

# Возвращает путь к файлу, где выполняется данный код.
script_directory = os.path.dirname(os.path.abspath(__file__))

# Возращзает путь к директории с конфигами
config_source = os.path.join(script_directory, '')

# Путь назначения для конфигов
config_destination = f'/home/{current_user}/.config/'

# Список директорий, которые нужно скопировать в домашнюю директорию
home_configs = ['zsh', 'tmux']

# Путь назначения для файлов, которые должны находиться в доме
home_path = f'/home/{current_user}/'

# Копирование нужных конфигов в дом
for directory_name in home_configs:
    source_directory = os.path.join(config_source, directory_name)
    for file_name in os.listdir(source_directory):
        source_file = os.path.join(source_directory, file_name)
        if os.path.isfile(source_file):
            shutil.copy(source_file, home_path)
            print(f"{directory_name} has been copied to {home_path}")

# Копирование остальных директорий
for dir_name in os.listdir(config_source):
# возаращает имена всех директорий и файлов в (config_source)
    source_dir = os.path.join(config_source, dir_name)
    # создаёт полный путь до директории с конфигом(/home/kirill/dotfiles/rofi)
    if os.path.isdir(source_dir) and dir_name not in ['zsh', 'tmux', 'apex-legend', '.git']:
    # проверяет является ли (source_dir) директорией 
    # и не является ли (dir_name) одной из не нужных директорий
        destination_dir = os.path.join(config_destination, dir_name)
        # путь назначения конфигов
        if os.path.exists(destination_dir):
        #проверяет существует ли уже такой путь(то-есть конфиг)
            if os.path.isdir(destination_dir):
            #если сущетсвует и ЯВЛЯЕТСЯ ДИРЕКТОРИЕЙ
                shutil.rmtree(destination_dir)
                #удаляется полностью
            else:
                os.remove(destination_dir)
                #если это прото файл, то он тоже удаляется
        shutil.copytree(source_dir, destination_dir)
        #ну и наконце-то он копирует все конфиги
        print(f"Config {dir_name} has been copied to {config_destination}")

print("Script was executed successfully...")
