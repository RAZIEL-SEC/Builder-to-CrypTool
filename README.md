# 🔐 CrypToolBuild

O **CrypTool Build** é uma interface de linha de comando (CLI) projetada para automatizar processos de compilação, ofuscação e empacotamento de projetos Python.

A ferramenta foi desenvolvida para facilitar a preparação de scripts Python para distribuição, oferecendo opções de configuração do processo de build e gerenciamento do ambiente de compilação.

## Uso integrado com as seguintes ferramentas:
Stealer: `https://github.com/RAZIEL-SEC/RzL-Stealer.git`

Obfuscador: `https://github.com/RAZIEL-SEC/RzL-CrypTool.git`

---

## 🙀 Funcionalidades Principais

- **🖥️ Interface CLI Interativa**
  - Menu intuitivo para facilitar o fluxo de trabalho.
  - Reduz a necessidade de editar configurações manualmente.

- **🛠️ Modo DEBUG (Console)**
  - Mantém a janela do terminal aberta.
  - Permite visualizar logs e mensagens de erro em tempo real.
  - Recomendado durante o desenvolvimento e testes.

- **📦 Modo de Distribuição**
  - Permite gerar uma versão empacotada do projeto.
  - Facilita a preparação do executável para disseminação.
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

### 1. Instalar o Python 3.10
```powershell
winget install Python.Python.3.10
```

### 2. Criar uma pasta para o projeto
```bash
mkdir Builder_CrypTool
cd Builder_CrypTool
```

### 3. Criar o ambiente virtual

```bash
py -3.10 -m venv .venv
```

### 4. Ativar o ambiente virtual

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No CMD:

```cmd
.venv\Scripts\activate
```

### 5. Clonar o repositório

```bash
git clone https://github.com/RAZIEL-SEC/Builder-to-CrypTool.git
cd Builder-to-CrypTool
```

### 6. Instalar as dependências

```bash
pip install -r requirements.txt
```
---

## ▶️ Executando o CrypToolBuild

Com o ambiente virtual ativado:

```bash
py -3.10 BuilderCT.py
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

---

## 📁 Estrutura do Projeto

Uma estrutura possível para o projeto:

```text
Builder-to-CrypTool/
│
├── CrypTool.py
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
python BuilderCT.py
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

## ⚠️ Aviso de Uso

O **CrypTool** é destinado à automação de processos de compilação, ofuscação e empacotamento de software.

O usuário é responsável por garantir que a ferramenta seja utilizada de acordo com as leis, políticas e permissões aplicáveis ao ambiente em que estiver sendo executada.

---

## 💡 Dica de Desenvolvimento

> **Utilize o Modo DEBUG durante o desenvolvimento.**
>
> O console aberto facilita a identificação de erros e permite acompanhar os logs do projeto. Depois de confirmar que tudo está funcionando corretamente, gere a versão final para disseminação.

---

## 👨‍💻 Autor

**Raziel Security**

- GitHub: `https://github.com/RAZIEL-SEC/`
- Repositório: `https://github.com/RAZIEL-SEC/Builder-to-CrypTool.git`

---

