def exists_word(word, instance):
    search_result = []
    for i in range(len(instance)):
        file_data = instance.search(i)
        occurrence_lines = []
        lines = []
        for item in file_data["linhas_do_arquivo"]:
            lines.extend(item.splitlines())
        occurrence_lines = [{
            "linha": number}
            for number, line in enumerate(lines, start=1)
            if word.lower() in line.lower()]
        if occurrence_lines:
            search_result.append({
                "palavra": word,
                "arquivo": file_data["nome_do_arquivo"],
                "ocorrencias": occurrence_lines,
            })
    return search_result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
