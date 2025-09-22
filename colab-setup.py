import subprocess
import platform
import sys
import os
from Libraries.config_manager import set_openai, set_hackclub, set_ollama, set_rag_model, set_openai_api_key, get_openai_api_key, enable_voice, enable_devmode, set_db_clear, enable_mcp, get_config, update_config
from Libraries.filepicker import select_config_dir
from model.modelbuilder import build

# Define the virtual environment name and the library to install
VENV_NAME = ".genv"
requirements_file = "model/requirements.txt"
pip_executable = "pip"

def should_install_bitsandbytes():
    system = platform.system()      # 'Darwin', 'Linux', 'Windows'
    machine = platform.machine()    # 'arm64', 'x86_64', etc.
    return not (system == 'Darwin' and machine == 'arm64')

def create_and_install():
    # Install from requirements.txt
    print(f"📦 Installing packages from '{requirements_file}'...")
    try:
        subprocess.run([pip_executable, "install", "-r", requirements_file], check=True)
        subprocess.run([pip_executable, "install", "langchain-openai"], check=True)
        print(f"✅ Packages from '{requirements_file}' installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        sys.exit(1)

    # Conditionally install bitsandbytes
    if should_install_bitsandbytes():
        print("🧠 Detected supported system for bitsandbytes. Installing...")
        try:
            subprocess.run([pip_executable, "install", "bitsandbytes>0.37.0"], check=True)
            print("✅ bitsandbytes installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install bitsandbytes: {e}")
    else:
        print("⚠️ Skipping bitsandbytes: Not supported on Apple Silicon macOS.")

def install_ollama():
    """Automatically install Ollama on Linux"""
    print("🔧 Installing Ollama automatically...")
    try:
        subprocess.run(['bash', '-c', 'curl -sSL https://ollama.com/install.sh | sh'], check=True)
        print("✅ Ollama installed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Ollama: {e}")
        return False

def pull_ollama_models():
    """Pull required Ollama models"""
    print("📥 Pulling WizardLM2 7B model, this may take a while...")
    try:
        subprocess.run(['ollama', 'pull', 'wizardlm2:7b'], check=True)
        print("✅ wizardlm2:7b pulled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to pull wizardlm2:7b: {e}")
        sys.exit(1)
    
    print("📥 Pulling nomic-embed-text for RAG...")
    try:
        subprocess.run(['ollama', 'pull', 'nomic-embed-text:latest'], check=True)
        print("✅ nomic-embed-text:latest pulled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to pull nomic-embed-text:latest: {e}")
        sys.exit(1)

def build_gizmo_model():
    """Build the custom gizmo model"""
    print("🔨 Building gizmo model...")
    try:
        build(SYSTEM_FILE='model/system.txt', SKILLS_FILE='model/skills.txt', MODELFILE='model/Modelfile', MODEL_NAME='gizmo', BASE_MODEL='wizardlm2:7b')
        print("✅ gizmo model built successfully.")
    except Exception as e:
        print(f"❌ Failed to build gizmo model: {e}")
        sys.exit(1)

def configure_system():
    """Configure the system settings"""
    print("⚙️ Configuring system settings...")
    
    # Set Ollama as the main model
    set_openai(False)
    set_hackclub(False)
    set_ollama()
    print("✅ Ollama set as primary model.")
    
    # Set RAG to use Ollama
    set_rag_model("ollama")
    print("✅ RAG configured to use Ollama.")
    
    # Disable voice
    enable_voice(False)
    print("✅ Voice disabled.")
    
    # Enable MCP (assuming this is desired for functionality)
    enable_mcp(True)
    print("✅ MCP enabled.")

if __name__ == "__main__":
    print("Its...")
    print("                ██████╗ ██╗███████╗███╗   ███╗ ██████╗ ")
    print(" ʕ 0 ᴥ 0ʔ      ██╔════╝ ██║╚══███╔╝████╗ ████║██╔═══██╗")
    print(" |      |      ██║  ███╗██║  ███╔╝ ██╔████╔██║██║   ██║")
    print(" |      |      ██║   ██║██║ ███╔╝  ██║╚██╔╝██║██║   ██║")
    print(" |      |      ╚██████╔╝██║███████╗██║ ╚═╝ ██║╚██████╔╝")
    print("+--------+      ╚═════╝ ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ")
    print("Welcome to the automated gizmo installer for Linux with Ollama!")
    print("This script will automatically:")
    print("- Install Ollama")
    print("- Download required models (WizardLM2 7B and nomic-embed-text)")
    print("- Configure Ollama as the primary model")
    print("- Set up RAG with Ollama")
    print("- Disable voice features")
    print("- Install all required Python packages")
    print()
    
    # Check if we're on Linux
    if platform.system() != 'Linux':
        print("⚠️ Warning: This automated setup is designed for Linux systems.")
        print("Current system detected:", platform.system())
        continue_anyway = input("Do you want to continue anyway? (Y/N): ").upper()
        if continue_anyway != 'Y':
            print("Setup cancelled.")
            sys.exit(0)
    
    print("🚀 Starting automated installation...")
    
    # Step 1: Install Ollama
    if not install_ollama():
        print("❌ Failed to install Ollama. Please install manually and run again.")
        sys.exit(1)
    
    # Step 2: Configure system settings
    configure_system()
    
    # Step 3: Install Python packages
    print("📦 Installing Python packages...")
    create_and_install()
    
    # Step 4: Pull Ollama models
    pull_ollama_models()
    
    # Step 5: Build gizmo model
    build_gizmo_model()
    
    print()
    print("🎉 Setup complete!")
    print("✅ Ollama installed and configured")
    print("✅ Models downloaded (wizardlm2:7b, nomic-embed-text:latest)")
    print("✅ Gizmo model built")
    print("✅ RAG configured with Ollama")
    print("✅ Voice disabled")
    print("✅ Python packages installed")
    print()
    print("Your system is now ready to use. Run gizmo.py to start!")
    print("Configuration has been saved to config.json - you can modify settings there if needed.")