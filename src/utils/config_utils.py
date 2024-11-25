import yaml
import os

def load_config():
    """YAML dosyasını yükler."""
    # Proje kök dizinini bul
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    
    # Config dosyasının tam yolunu oluştur
    config_path = os.path.join(project_root, "config.yaml")
    
   # if not os.path.exists(config_path):
    #    raise FileNotFoundError(f"Config dosyası bulunamadı: {config_path}")
    
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config

