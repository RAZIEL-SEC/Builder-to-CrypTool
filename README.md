# 🚀 CrypToolBuild

O **CrypTool Build** é uma interface de linha de comando (CLI) projetada para automatizar processos de compilação, ofuscação e empacotamento de projetos Python.

A ferramenta foi desenvolvida para facilitar a preparação de scripts Python para distribuição, oferecendo opções de configuração do processo de build e gerenciamento do ambiente de compilação.

---

## ✨ Funcionalidades Principais

- **🖥️ Interface CLI Interativa**
  - Menu intuitivo para facilitar o fluxo de trabalho.
  - Reduz a necessidade de editar configurações manualmente.

- **🛠️ Modo DEBUG (Console)**
  - Mantém a janela do terminal aberta.
  - Permite visualizar logs e mensagens de erro em tempo real.
  - Recomendado durante o desenvolvimento e testes.

- **📦 Modo de Distribuição**
  - Permite gerar uma versão empacotada do projeto.
  - Facilita a preparação do executável para distribuição.
  - Totalmente em background e sem janelas.

- **📚 Gerenciamento de Dependências**
  - Auxilia no empacotamento das bibliotecas utilizadas pelo projeto.
  - Pode trabalhar com bibliotecas como `cryptography` e `opencv`.

- **🧹 Limpeza Automática do Workspace**
  - Gerencia diretórios como `build/` e `dist/`.
  - Ajuda a evitar conflitos causados por arquivos de builds anteriores.

---

## 📋 Requisitos

Para utilizar o CrypToolBuild, recomenda-se:

- **Python:** `3.10` (RECOMENDADO) ou superior
- **Sistema Operacional:** Windows
- **Ambiente virtual:** `venv`
- Ferramentas de compilação necessárias para dependências que utilizam extensões nativas

---

## 🛠️ Instalação e Uso

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-projeto.git](https://github.com/RAZIEL-SEC/Builder-to-CrypTool.git
cd Builder-to-CrypTool
```

### 2. Criar o ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual

No PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

No CMD:

```cmd
venv\Scripts\activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando o CrypToolBuild

Com o ambiente virtual ativado:

```bash
python CrypTool.py
```

---

## 🔄 Fluxo de Trabalho Recomendado

### 1. Configurar o arquivo

Defina o script `.py` que será utilizado como entrada do processo de compilação.

### 2. Testar em DEBUG

Utilize o **Modo DEBUG** para verificar o funcionamento do projeto e identificar possíveis erros.

### 3. Selecionar as configurações

Escolha as opções de build disponíveis na interface do CrypToolBuild.

### 4. Compilar

Inicie o processo de compilação e aguarde sua conclusão.

### 5. Verificar o resultado

Os arquivos gerados poderão ser encontrados na pasta:

```text
dist/
```

---

## 📦 Dependências

As dependências do projeto devem ser declaradas no arquivo:

```text
requirements.txt
```

Entre as bibliotecas que podem ser utilizadas pelo projeto estão:

| Biblioteca | Finalidade |
|---|---|
| `cryptography` | Recursos de criptografia |
| `opencv-python` | Processamento de imagens |
| `requests` | Comunicação HTTP |
| `psutil` | Informações e gerenciamento de processos e sistema |

> A lista acima deve ser ajustada de acordo com as dependências realmente utilizadas pelo projeto.

---

## 📁 Estrutura do Projeto

Uma estrutura possível para o projeto:

```text
CrypToolBuild/
│
├── Professional_Builder_Pro.py
├── requirements.txt
├── README.md
│
├── build/
│   └── arquivos temporários
│
├── dist/
│   └── arquivos gerados
│
└── venv/
    └── ambiente virtual
```

---

## 🧹 Limpeza do Workspace

Caso seja necessário remover arquivos gerados por builds anteriores, no PowerShell:

```powershell
Remove-Item -Recurse -Force build, dist
```

Depois, execute novamente o processo de compilação.

---

## 🐛 Solução de Problemas

### O programa não inicia

Execute diretamente pelo Python para visualizar as mensagens de erro:

```bash
python Professional_Builder_Pro.py
```

### Problemas com dependências

Atualize o `pip`:

```bash
python -m pip install --upgrade pip
```

Depois reinstale as dependências:

```bash
pip install -r requirements.txt --upgrade
```

### Problemas durante o build

Limpe os diretórios antigos:

```powershell
Remove-Item -Recurse -Force build, dist
```

E execute novamente o processo.

---

## 🔐 Boas Práticas

- ✅ Teste o projeto antes da distribuição.
- ✅ Utilize um ambiente virtual para isolar dependências.
- ✅ Mantenha o `requirements.txt` atualizado.
- ✅ Não armazene senhas, tokens ou chaves privadas no código.
- ✅ Mantenha backups do código-fonte.
- ✅ Utilize a ferramenta somente em sistemas autorizados.

---

## ⚠️ Aviso de Uso

O **CrypToolBuild** é destinado à automação de processos de compilação, ofuscação e empacotamento de software.

O usuário é responsável por garantir que a ferramenta seja utilizada de acordo com as leis, políticas e permissões aplicáveis ao ambiente em que estiver sendo executada.

---

## 💡 Dica de Desenvolvimento

> **Utilize o Modo DEBUG durante o desenvolvimento.**
>
> O console aberto facilita a identificação de erros e permite acompanhar os logs do projeto. Depois de confirmar que tudo está funcionando corretamente, gere a versão final para distribuição.

---

## 📄 Licença

Defina aqui a licença utilizada pelo projeto.

Exemplo:

```text
MIT License
```

---

## 👨‍💻 Autor

**Seu Nome**

- GitHub: `https://github.com/seu-usuario`
- Repositório: `https://github.com/seu-usuario/seu-projeto`

---

⭐ Se este projeto for útil para você, considere deixar uma estrela no repositório!
