import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

# Função para manuseio do currículo (selecionando o arquivo e copiando)
def enviar_curriculo():
    # Obtém os dados da interface
    unidade_selecionada = combo_unidade.get()
    funcao_selecionada = combo_funcoes.get()
    curriculo = curriculo_path.get()  # Caminho do arquivo selecionado
    
    if not unidade_selecionada or not funcao_selecionada or not curriculo:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return
    
    # Formar o caminho da pasta com base na unidade e função
    caminho_pasta = f"G:/Meu Drive/Currículos/{unidade_selecionada}/{funcao_selecionada}"

    # Verifica se a pasta existe, se não, cria a pasta
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)  # Cria a pasta, se não existir

    # Obter o nome do arquivo e o caminho do arquivo de origem
    nome_arquivo = os.path.basename(curriculo)  # Nome do arquivo sem o caminho
    caminho_destino = os.path.join(caminho_pasta, nome_arquivo)  # Caminho completo para destino

    try:
        # Tenta copiar o arquivo para o destino
        shutil.copy(curriculo, caminho_destino)
        messagebox.showinfo("Sucesso", f"Currículo copiado para {caminho_destino}")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao copiar o currículo: {e}")

def anexar_curriculo():
    # Abre o explorador de arquivos para o usuário selecionar o currículo
    caminho = filedialog.askopenfilename(
        title="Selecione o currículo", 
        filetypes=[("PDF", "*.pdf"), 
                  ("Word", "*.docx"), 
                  ("Imagens PNG", "*.png"),
                  ("Imagens JPG", "*.jpg"),
                  ("Imagens JPEG", "*.jpeg"),
                  ("Todos os arquivos", "*.*")]
    )
    if caminho:
        curriculo_path.set(caminho)  # Atualiza o campo com o caminho do arquivo

# Criação da janela principal
root = tk.Tk()
root.title("Envio de Currículos")

# Ajustando o tamanho da janela
root.geometry("400x350")

# Funções predefinidas para o menu suspenso
funcoes = ['Auxiliar Pizzaiolo', 'Pizzaiolo', 'Auxiliar Chapeiro', 'Chapeiro', 'Auxiliar Cozinha', 'Atendente', 'Operador de caixa', 'Estoquista', 'Gerente', 'Entregador']
unidades = ['Mocambinho', 'Promorar', 'Dirceu']

# Variável para armazenar o caminho do currículo
curriculo_path = tk.StringVar()

# Criando os widgets da interface
label_unidade = tk.Label(root, text="Selecione a Unidade:")
label_unidade.pack(pady=10)

combo_unidade = ttk.Combobox(root, values=unidades, state="readonly")
combo_unidade.pack(pady=10)

label_funcao = tk.Label(root, text="Selecione a Função:")
label_funcao.pack(pady=10)

combo_funcoes = ttk.Combobox(root, values=funcoes, state="readonly")
combo_funcoes.pack(pady=10)

label_curriculo = tk.Label(root, text="Anexar Currículo:")
label_curriculo.pack(pady=10)

botao_anexar = tk.Button(root, text="Selecionar Currículo", command=anexar_curriculo)
botao_anexar.pack(pady=10)

label_path = tk.Label(root, textvariable=curriculo_path)
label_path.pack(pady=10)

botao_enviar = tk.Button(root, text="Enviar Currículo", command=enviar_curriculo)
botao_enviar.pack(pady=20)

# Inicia a interface
root.mainloop()

