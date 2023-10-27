import os
import shutil
import subprocess

# Получаем имя текущего пользователя
current_user = subprocess.getoutput('whoami')

# Пути для копирования

#возвращает путь к файлу, где выполняется данный код.
script_directory = os.path.dirname(os.path.abspath(__file__))

#путь до конфига zsh
zsh_source = os.path.join(script_directory, 'zsh/')

#путь нзначения для файлов zsh
zsh_destination = f'/home/{current_user}/'

#возращзает путь к директории с конфигами
config_source = os.path.join(script_directory, '')

#путь назначения для конфигов
config_destination = f'/home/{current_user}/.config/'

#Копирование файлов zsh
for file_name in os.listdir(zsh_source):
    source_file = os.path.join(zsh_source, file_name)
    if os.path.isfile(source_file):
        shutil.copy(source_file, zsh_destination)
print("The zsh config has been copied...")

# Копирование остальных директорий
for dir_name in os.listdir(config_source):
# возаращает имена всех директорий и файлов в (config_source)
    source_dir = os.path.join(config_source, dir_name)
    # создаёт полный путь до директории с конфигом(/home/kirill/dotfiles/rofi)
    if os.path.isdir(source_dir) and dir_name not in ['zsh', 'apex-legend']:
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
print("The rest of the configurations have been copied...")

print("Script was executed successfully...")
