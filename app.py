import streamlit as st
from PIL import Image
import os

# Configuration de la page
st.set_page_config(
    page_title="Portfolio Photographique",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="expanded"
)



# Styles CSS personnalisés avec design moderne
st.markdown("""
    <style>
        /* Reset du thème et styles globaux */
        [data-testid="stAppViewContainer"], 
        [data-testid="stHeader"] {
            background-color: #ffffff;
            color: #1a1a1a;
        }
        
        [data-testid="stToolbar"] {
            right: 2rem;
        }
        
        /* Barre latérale */
        [data-testid="stSidebar"] {
            background-color: #1a1a1a;
            padding-top: 2rem;
        }
        
        [data-testid="stSidebar"] [data-testid="stMarkdown"] {
            color: #ffffff;
        }

        [data-testid="stSidebarNav"] {
            background-color: #1a1a1a;
        }

        [data-testid="stSidebarNav"] .css-17lntkn {
            color: #ffffff;
        }
        
        /* En-têtes */
        h1 {
            color: #1a1a1a !important;
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: 700;
            font-size: 2.5rem;
            margin-bottom: 2rem;
            text-align: center;
            padding: 2rem 0;
        }
        
        h2 {
            color: #333 !important;
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: 600;
            margin: 1.5rem 0;
        }
        
        h3 {
            color: #444 !important;
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: 500;
        }

        p {
            color: #2e2e2e !important;
        }
        
        /* Conteneurs et blocs */
        .block-container {
            padding: 3rem 1rem !important;
            max-width: 100%;
        }
        
        /* Images */
        .stImage {
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        
        .stImage:hover {
            transform: translateY(-5px);
        }
        
        /* Légendes */
        .caption {
            color: #666;
            font-style: italic;
            padding: 0.5rem;
            text-align: center;
            font-size: 0.9rem;
        }
        
        /* Boutons */
        .stButton button {
            background-color: #1a1a1a !important;
            color: white !important;
            border: none !important;
            border-radius: 4px;
            padding: 0.5rem 1rem;
            font-weight: 500;
            transition: background-color 0.3s ease;
        }
        
        .stButton button:hover {
            background-color: #333 !important;
            border: none !important;
        }
        
        /* Sélecteurs et inputs */
        .stSelectbox {
            margin-bottom: 2rem;
        }

        .stSelectbox > div > div {
            background-color: white;
            color: #1a1a1a;
        }
        
        /* Séparateurs */
        hr {
            border: none;
            height: 2px;
            background: linear-gradient(to right, transparent, #1a1a1a, transparent);
            margin: 2rem 0;
        }
        
        /* Grille de la galerie */
        .gallery-grid > div {
            background-color: white;
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 2rem;
            background-color: #1a1a1a;
            color: white;
            margin-top: 3rem;
        }
        
        /* Contact info */
        .contact-info {
            background-color: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }
        
        /* Profile image */
        .profile-image {
            border-radius: 50%;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Expander */
        .streamlit-expanderHeader {
            background-color: white;
            color: #1a1a1a;
        }
    </style>
""", unsafe_allow_html=True)

# Fonction pour charger les images
def load_images(folder_path):
    images = []
    valid_extensions = ['.jpg', '.jpeg', '.png']
    try:
        for filename in os.listdir(folder_path):
            if any(filename.lower().endswith(ext) for ext in valid_extensions):
                images.append({
                    'path': os.path.join(folder_path, filename),
                    'name': os.path.splitext(filename)[0]
                })
    except Exception as e:
        st.warning(f"Erreur lors du chargement des images : {str(e)}")
    return images

# Sidebar avec logo/nom du photographe
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: white;'>📸</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: white;'>Elio Duclos", unsafe_allow_html=True)
    st.markdown("---")
    menu = ["Accueil", "Galerie", "À propos"]
    choice = st.selectbox("", menu)
    st.markdown("---")
    st.markdown("<div style='position: fixed; bottom: 0; padding: 1rem; color: white;'>© 2025 Elio Duclos</div>", unsafe_allow_html=True)

# Contenu principal
if choice == "Accueil":
    st.title("Capturer l'instant, révéler l'émotion")
    
    try:
        cover_image = Image.open("20240413-001905-Elio-Duclos (1).jpg")
        st.image(cover_image, use_container_width=True)
    except:
        st.image("https://via.placeholder.com/1200x600?text=Ajoutez+une+image+de+couverture", use_container_width=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ## Ma Vision
        
        Je suis un photographe passionné par la capture de moments authentiques et d'émotions sincères. 
        Mon approche combine la technique avec une sensibilité artistique unique, créant des images qui racontent des histoires intemporelles.
        """)
    
    with col2:
        st.markdown("""
        ### Spécialités
        - 📸 Mariage/Portraits
        - 🌅 Paysages
        - 🏛️ Architecture
        - 🌆 Urbain
        """)

elif choice == "Galerie":
    st.title("Portfolio")
    
    categories = ["Portraits", "Paysages", "Architecture", "Street"]
    selected_category = st.selectbox("Explorer", categories)
    
    # Configuration de l'affichage en grille
    gallery = st.container()
    with gallery:
        try:
            folder_path = f"photos/{selected_category}"
            cols = st.columns(3)
            images = load_images(folder_path)
            
            if not images:
                st.info(f"Ajoutez vos photos dans le dossier {folder_path}")
            
            # On utilise session_state pour garder la trace de l'image sélectionnée
            if 'selected_image' not in st.session_state:
                st.session_state.selected_image = None
            
            for idx, image_info in enumerate(images):
                with cols[idx % 3]:
                    try:
                        img = Image.open(image_info['path'])
                        # On crée un container cliquable pour chaque image
                        image_container = st.container()
                        with image_container:
                            # L'image elle-même devient cliquable
                            if st.image(img, use_container_width=True):
                                st.session_state.selected_image = image_info['path']
                        st.markdown(f"<p class='caption'>{image_info['name']}</p>", unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Erreur lors du chargement de l'image {image_info['name']}")
    

        except Exception as e:
            st.error(f"Erreur lors du chargement de la galerie : {str(e)}")

elif choice == "À propos":
    st.title("À propos")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            profile_image = Image.open("photo_cv.jpg")
            st.image(profile_image, width=300, clazz="profile-image")
        except:
            print('ouiii')
            st.image("https://via.placeholder.com/300x300?text=Photo+de+profil", width=300)
    
    with col2:
        st.markdown("""
        ## Elio Duclos
        
        Photographe professionnel basé à Gif-sur-Yvette. Spécialisé dans la capture de moments authentiques 
        et la création d'images qui racontent des histoires uniques.
        
        Mon approche combine créativité, technique et émotion pour créer des images qui restent.
        
        ### Parcours
        - 10 ans d'expérience en photographie
        - Formation à CentraleSupélec
        - Expositions : [Galeries/Lieux]
        """)
        
        st.markdown("""
        <div class='contact-info'>
        <h3>Contact</h3>
        
        - 📧 elioduclos@gmail.com
        - 📱 +33 7 81 25 78 30
        - 📸 A venir
        </div>
        """, unsafe_allow_html=True)