# Função para buscar comentários da Steam
import requests

def buscar_reviews_steam(app_id, quantidade=10, idioma="portuguese"):
    url = f"https://store.steampowered.com/appreviews/{app_id}?json=1&num_per_page={quantidade}&language={idioma}&filter=recent"
    response = requests.get(url)
    data = response.json()
    
    comentarios = []
    if "reviews" in data:
        for review in data["reviews"]:
            comentarios.append(review["review"])
    
    return comentarios


print(buscar_reviews_steam(730))