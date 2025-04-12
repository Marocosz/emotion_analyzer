from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time

# Defina o caminho correto para o driver do Edge
service = Service(executable_path="msedgedriver.exe")  # Altere para o seu caminho correto
options = Options()

# Definindo um User-Agent para evitar bloqueio por automação
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

driver = webdriver.Edge(service=service, options=options)

# Acessar a URL
urls = ['https://www.amazon.com.br/Controle-Dualshock-PlayStation-4-Preto/dp/B07FN1MZBH/?_encoding=UTF8&pd_rd_w=n0K2B&content-id=amzn1.sym.52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_p=52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_r=6QXRJGD63Z2Q34H4EZ7D&pd_rd_wg=V1vWA&pd_rd_r=1b8dbf41-ec68-4928-8e8e-4ff9ce6a04c9&ref_=pd_hp_d_btf_crs_zg_bs_7791985011',
        'https://www.amazon.com.br/PlayStation-DualSense-Controle-sem-fio/dp/B0CQKLS4RP/?_encoding=UTF8&pd_rd_w=n0K2B&content-id=amzn1.sym.52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_p=52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_r=6QXRJGD63Z2Q34H4EZ7D&pd_rd_wg=V1vWA&pd_rd_r=1b8dbf41-ec68-4928-8e8e-4ff9ce6a04c9&ref_=pd_hp_d_btf_crs_zg_bs_7791985011',
        'https://www.amazon.com.br/PlayStation%C2%AE5-Slim-Edi%C3%A7%C3%A3o-Digital-Jogos/dp/B0CYJBWGH5/?_encoding=UTF8&pd_rd_w=n0K2B&content-id=amzn1.sym.52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_p=52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_r=6QXRJGD63Z2Q34H4EZ7D&pd_rd_wg=V1vWA&pd_rd_r=1b8dbf41-ec68-4928-8e8e-4ff9ce6a04c9&ref_=pd_hp_d_btf_crs_zg_bs_7791985011',
        'https://www.amazon.com.br/Base-Carregamento-Do-Dualsense-PlayStation/dp/B09JH4PD8Q/?_encoding=UTF8&pd_rd_w=n0K2B&content-id=amzn1.sym.52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_p=52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_r=6QXRJGD63Z2Q34H4EZ7D&pd_rd_wg=V1vWA&pd_rd_r=1b8dbf41-ec68-4928-8e8e-4ff9ce6a04c9&ref_=pd_hp_d_btf_crs_zg_bs_7791985011',
        'https://www.amazon.com.br/Headphone-HV-H2232d-Ilumina%C3%A7%C3%A3o-Microfone-Conector/dp/B07N78G8GB/?_encoding=UTF8&pd_rd_w=n0K2B&content-id=amzn1.sym.52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_p=52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_r=6QXRJGD63Z2Q34H4EZ7D&pd_rd_wg=V1vWA&pd_rd_r=1b8dbf41-ec68-4928-8e8e-4ff9ce6a04c9&ref_=pd_hp_d_btf_crs_zg_bs_7791985011',
        'https://www.amazon.com.br/Ajust%C3%A1vel-Velocidade-Refor%C3%A7ado-Ergon%C3%B4mico-Antideslizante/dp/B0DNDGKMRT/?_encoding=UTF8&pd_rd_w=n0K2B&content-id=amzn1.sym.52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_p=52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_r=6QXRJGD63Z2Q34H4EZ7D&pd_rd_wg=V1vWA&pd_rd_r=1b8dbf41-ec68-4928-8e8e-4ff9ce6a04c9&ref_=pd_hp_d_btf_crs_zg_bs_7791985011',
        'https://www.amazon.com.br/Headset-Ouvido-HV-H2002d-Microfone-Falante/dp/B0BTJC5BGR/?_encoding=UTF8&pd_rd_w=n0K2B&content-id=amzn1.sym.52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_p=52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_r=6QXRJGD63Z2Q34H4EZ7D&pd_rd_wg=V1vWA&pd_rd_r=1b8dbf41-ec68-4928-8e8e-4ff9ce6a04c9&ref_=pd_hp_d_btf_crs_zg_bs_7791985011',
        'https://www.amazon.com.br/Headphone-Ouvido-HV-H2002d-Microfone-Falante/dp/B07Y2G7VX5/?_encoding=UTF8&pd_rd_w=n0K2B&content-id=amzn1.sym.52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_p=52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_r=6QXRJGD63Z2Q34H4EZ7D&pd_rd_wg=V1vWA&pd_rd_r=1b8dbf41-ec68-4928-8e8e-4ff9ce6a04c9&ref_=pd_hp_d_btf_crs_zg_bs_7791985011',
        'https://www.amazon.com.br/Controle-sem-fio-Xbox-Preto/dp/B088GJR4B9/?_encoding=UTF8&pd_rd_w=n0K2B&content-id=amzn1.sym.52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_p=52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_r=6QXRJGD63Z2Q34H4EZ7D&pd_rd_wg=V1vWA&pd_rd_r=1b8dbf41-ec68-4928-8e8e-4ff9ce6a04c9&ref_=pd_hp_d_btf_crs_zg_bs_7791985011',
        'https://www.amazon.com.br/Assassins-Creed-Shadows-PlayStation-5/dp/B0DQ1SMWHR/?_encoding=UTF8&pd_rd_w=n0K2B&content-id=amzn1.sym.52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_p=52e74d21-088e-4a9d-888d-8b14bf95d4ae&pf_rd_r=6QXRJGD63Z2Q34H4EZ7D&pd_rd_wg=V1vWA&pd_rd_r=1b8dbf41-ec68-4928-8e8e-4ff9ce6a04c9&ref_=pd_hp_d_btf_crs_zg_bs_7791985011']

listas_comentarios = []


for url in urls:
    driver.get(url)

    divs_externas = driver.find_elements(By.CLASS_NAME, 'card-padding')

    for div in divs_externas:
        # Agora busca dentro de cada div externa
        divs_internas = div.find_elements(By.CLASS_NAME, "a-expander-content")
        
        for interna in divs_internas:
            listas_comentarios.append(interna.text)
            


        
    
print(len(listas_comentarios))
print(listas_comentarios[0])


# Fechar o driver
driver.quit()
