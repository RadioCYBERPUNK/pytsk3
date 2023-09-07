# radioCYBERPUNKpytsk3
LABORATORIO PYTSK3 FORENSIC 

O pytsk3 é uma poderosa biblioteca Python projetada para auxiliar profissionais de computação forense e investigadores digitais na análise e recuperação de metadados de sistemas de arquivos em dispositivos de armazenamento. Com essa ferramenta, os especialistas podem acessar informações detalhadas sobre arquivos, diretórios e a estrutura do sistema de arquivos, permitindo a reconstrução de eventos e trilhas de atividades em investigações forenses.

Durante um laboratório dedicado à recuperação de metadados usando o pytsk3, foram realizados testes em um ambiente controlado para explorar as funcionalidades dessa biblioteca em diversos cenários. Os resultados demonstraram a eficácia do pytsk3 na extração de informações valiosas, mesmo em casos onde os metadados do sistema de arquivos estavam ausentes ou danificados.

As principais funcionalidades do pytsk3 incluem:

    Recuperação de Metadados: O pytsk3 permite que os investigadores acessem informações sobre arquivos, como nome, tamanho, data de criação, data de modificação e proprietário.

    Data Carving: Essa biblioteca é capaz de realizar data carving, uma técnica de recuperação de dados não estruturados, identificando assinaturas de arquivos em setores de armazenamento, o que é essencial quando os metadados estão indisponíveis.

    Suporte a Sistemas de Arquivos Diversos: O pytsk3 é compatível com uma variedade de sistemas de arquivos, incluindo NTFS, FAT, HFS+, ext2/3/4, entre outros.

    Interface Python Amigável: A integração do pytsk3 com Python torna a programação e a automação de tarefas de análise forense mais acessíveis.

O laboratório demonstrou como o pytsk3 pode ser uma ferramenta valiosa em investigações forenses, permitindo aos examinadores recuperar metadados de maneira eficaz, mesmo em cenários desafiadores. Vale ressaltar que o uso do pytsk3 deve ser feito de acordo com as leis e regulamentações locais, garantindo a integridade das evidências e o respeito aos direitos individuais durante investigações digitais. Para obter mais informações sobre o pytsk3 e seu código-fonte, você pode visitar o repositório oficial no GitHub.

O objeto entry.info.meta em pytsk3 contém várias variáveis que fornecem informações sobre um arquivo ou diretório em um sistema de arquivos. Aqui estão algumas das variáveis disponíveis em meta:

Exemplo: entry.info.meta.inode

atime: Data de último acesso (Access Time). ( exemplo: entry.info.meta.atime)
block_count: Número de blocos alocados para o arquivo.
block_size: Tamanho do bloco de armazenamento do sistema de arquivos.
ctime: Data de criação/mudança de metadados (Change Time).
gid: ID do grupo do arquivo (Group ID).
inode: Número do inode do arquivo.
mode: Modo de acesso (permissões) do arquivo.
mtime: Data de última modificação do conteúdo (Modification Time).
name: Nome do arquivo.
seq: Número de sequência do arquivo.
size: Tamanho do arquivo em bytes.
type: Tipo de entrada (arquivo, diretório, link simbólico, etc.).
uid: ID do usuário proprietário do arquivo (User ID).

