import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "AmmasDoughyDelights"

backend = "backend/src/main/java/com/ammasdoughy/backend"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"{backend}/AmmasDoughyDelightsApplication.java",
    f"{backend}/controller/ProductController.java",
    f"{backend}/controller/ContactController.java",
    f"{backend}/model/Product.java",
    f"{backend}/model/ContactMessage.java",
    f"{backend}/repository/ProductRepository.java",
    f"{backend}/repository/ContactRepository.java",
    f"{backend}/service/ProductService.java",
    f"{backend}/service/ContactService.java",
    f"backend/src/main/resources/application.properties",
    f"backend/Dockerfile",
    f"backend/pom.xml",
    f"frontend/public/index.html",
    f"frontend/src/App.js",
    f"frontend/src/index.js",
    f"frontend/src/styles.css",
    f"frontend/Dockerfile",
    f"frontend/package.json",
    f"deployment/docker-compose.yml",
    f"deployment/k8s/backend-deployment.yml",
    f"deployment/k8s/backend-service.yml",
    f"deployment/k8s/frontend-deployment.yml",
    f"deployment/k8s/frontend-service.yml",
    f"deployment/k8s/ingress.yml",
    "README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
