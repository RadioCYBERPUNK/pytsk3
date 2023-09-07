import pytsk3

# Especifique o caminho do dispositivo ou arquivo de imagem
device_path = '/dev/sda3'

# Abra o dispositivo ou imagem
img_info = pytsk3.Img_Info(device_path)

# Abra o sistema de arquivos
fs_info = pytsk3.FS_Info(img_info)

# Função para listar todos os arquivos, incluindo os apagados
def list_all_files(directory, prefix=''):
    for entry in directory:
        file_name = entry.info.name.name.decode('utf-8')
        full_path = prefix + '/' + file_name if prefix else file_name
        
        print("Nome:", file_name)
        print("Caminho:", full_path)
        print("Tamanho:", entry.info.meta.size)
        print("inode:", entry.info.meta.addr)
        # Verifique se o arquivo está apagado (inode = -1)
        if entry.info.meta.addr == -1:
            print("Estado: Apagado")
        else:
            print("Estado: Não apagado")

        print()

        if entry.info.meta.type == pytsk3.TSK_FS_META_TYPE_DIR:
            if file_name not in ['.', '..']:
                sub_directory = fs_info.open_dir(full_path)
                list_all_files(sub_directory, full_path)

# Chame a função para listar todos os arquivos a partir do diretório 
root_dir = fs_info.open_dir('/home/saturno/Documents')
list_all_files(root_dir)
