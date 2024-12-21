#!/bin/bash

# ========================================================================
# Script: copiar_arquivos.sh
# Descrição: Copia o conteúdo de todos os arquivos com extensões especificadas
#            para um único arquivo de saída, adicionando um cabeçalho com o
#            caminho relativo e o nome de cada arquivo.
# Uso: ./copiar_arquivos.sh
# ========================================================================

# Configurações iniciais

# Define as extensões dos arquivos que você deseja copiar, sem o ponto.
EXTENSOES=("py" "css" "html")  # Adicione ou remova extensões conforme necessário

# Define o nome do arquivo de saída
ARQUIVO_SAIDA="personal_site.txt"

# Remove o arquivo de saída se ele já existir para evitar concatenações indesejadas
if [ -f "$ARQUIVO_SAIDA" ]; then
    rm "$ARQUIVO_SAIDA"
    echo "Arquivo de saída existente '$ARQUIVO_SAIDA' removido."
fi

# Função para copiar o conteúdo dos arquivos
copiar_arquivos() {
    local ext="$1"
    echo "Processando arquivos com a extensão: .$ext"

    # Encontra todos os arquivos com a extensão atual de forma recursiva
    find . -type f -iname "*.$ext" | while IFS= read -r arquivo; do
        # Remove o prefixo './' para obter o caminho relativo
        caminho_relativo="${arquivo#./}"

        # Adiciona o cabeçalho ao arquivo de saída
        echo "===== Caminho: $caminho_relativo =====" >> "$ARQUIVO_SAIDA"

        # Adiciona o conteúdo do arquivo ao arquivo de saída
        cat "$arquivo" >> "$ARQUIVO_SAIDA"

        # Adiciona uma linha em branco para separar os arquivos
        echo "" >> "$ARQUIVO_SAIDA"
    done
}

# Itera sobre cada extensão definida
for ext in "${EXTENSOES[@]}"; do
    copiar_arquivos "$ext"
done

echo "Todos os arquivos especificados foram copiados para '$ARQUIVO_SAIDA'."
