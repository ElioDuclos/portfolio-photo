from PIL import Image
import os

def optimize_jpg(input_folder, output_folder, quality=85):
    """
    Optimise tous les fichiers JPG d'un dossier en réduisant leur taille tout en maintenant une bonne qualité.
    :param input_folder: Dossier contenant les fichiers JPG d'entrée
    :param output_folder: Dossier où enregistrer les fichiers JPG optimisés
    :param quality: Qualité de l'image (1-100, plus élevé signifie meilleure qualité)
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            try:
                with Image.open(input_path) as img:
                    img = img.convert("RGB")  # Assurer un format compatible
                    img.save(output_path, "JPEG", quality=quality, optimize=True)
                    print(f"Image optimisée enregistrée : {output_path}")
            except Exception as e:
                print(f"Erreur lors de l'optimisation de {filename} : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    input_folder = "/workspaces/portfolio-photo/photos/Architecture"  # Remplacez par le chemin de votre dossier d'images
    output_folder = "images_optimisees"
    optimize_jpg(input_folder, output_folder, quality=20)
    
