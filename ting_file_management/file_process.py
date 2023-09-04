import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    new_file = txt_importer(path_file)
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] is path_file:
            return None
    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas":   len(new_file),
        "linhas_do_arquivo": new_file,
    }
    instance.enqueue(file_data)
    print(str(file_data))


def remove(instance):
    if not len(instance):
        print("Não há elementos")
        return
    file_data = instance.dequeue()
    print(f"Arquivo {file_data['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        file_info = instance.search(position)
        print(str(file_info))
    except IndexError:
        sys.stderr.write("Posição inválida")
