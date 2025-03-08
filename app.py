from flask import Flask, render_template, request, redirect, url_for, flash
import os
import shutil

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Para usar flash messages

# Função para manuseio do currículo (selecionando o arquivo e copiando)
def enviar_curriculo(unidade_selecionada, funcao_selecionada, curriculo):
    caminho_pasta = f"G:/Meu Drive/Currículos/{unidade_selecionada}/{funcao_selecionada}"

    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)  # Cria a pasta, se não existir

    # Obter o nome do arquivo e o caminho do arquivo de origem
    nome_arquivo = os.path.basename(curriculo)  # Nome do arquivo sem o caminho
    caminho_destino = os.path.join(caminho_pasta, nome_arquivo)  # Caminho completo para destino

    try:
        shutil.copy(curriculo, caminho_destino)  # Copia o arquivo para o destino
        return f"Currículo copiado para {caminho_destino}"
    except Exception as e:
        return f"Falha ao copiar o currículo: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        unidade_selecionada = request.form.get("unidade")
        funcao_selecionada = request.form.get("funcao")
        curriculo = request.files["curriculo"]

        if not unidade_selecionada or not funcao_selecionada or not curriculo:
            flash("Por favor, preencha todos os campos.")
            return redirect(url_for("index"))

        # Salva o arquivo temporariamente
        caminho_temporal = os.path.join("uploads", curriculo.filename)
        curriculo.save(caminho_temporal)

        # Processa o currículo
        resultado = enviar_curriculo(unidade_selecionada, funcao_selecionada, caminho_temporal)

        flash(resultado)
        return redirect(url_for("index"))
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
