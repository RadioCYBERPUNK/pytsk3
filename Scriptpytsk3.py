
import subprocess

def obter_informacoes_hd():
    try:
        # Execute o comando lsblk para obter informações sobre discos rígidos
        resultado = subprocess.check_output(["lsblk", "-o", "NAME,SIZE,TYPE,MOUNTPOINT", "-n", "-l"], universal_newlines=True)

        # Divida as informações em discos individuais com base em linhas em branco
        discos = resultado.strip().split('\n')

        informacoes_discos = []

        for disco in discos:
            disco_info = {}
            # Divida as informações de cada disco em colunas
            colunas = disco.strip().split()
            if len(colunas) >= 3:
                disco_info['NAME'] = colunas[0]
                disco_info['SIZE'] = colunas[1]
                disco_info['TYPE'] = colunas[2]
                disco_info['MOUNTPOINT'] = colunas[3] if len(colunas) >= 4 else ""
            informacoes_discos.append(disco_info)

        return informacoes_discos
    except subprocess.CalledProcessError as e:
        print("Erro ao obter informações do disco rígido:", e)
        return []

# Obtenha informações sobre os discos rígidos e imprima
informacoes_discos = obter_informacoes_hd()
if informacoes_discos:
    for i, disco_info in enumerate(informacoes_discos):
        print(f"Disco {i + 1}:")
        for chave, valor in disco_info.items():
            print(f"{chave}: {valor}")
        print("\n")
else:
    print("Nenhuma informação de disco encontrada.")
