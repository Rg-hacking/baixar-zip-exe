import requests
import os

BASE_URL = "https://www.gamingsteam.com.br/premium/"
PASTA = "downloads"

def baixar(numero):
    os.makedirs(PASTA, exist_ok=True)
    url = f"{BASE_URL}{numero}.zip"
    caminho = os.path.join(PASTA, f"{numero}.zip")

    try:
        r = requests.get(url, stream=True, timeout=15)

        if r.status_code == 404:
            print(f"{numero}.zip não existe")
            return

        r.raise_for_status()

        with open(caminho, "wb") as f:
            for chunk in r.iter_content(8192):
                if chunk:
                    f.write(chunk)

        print(f"Baixado: {numero}.zip")

    except Exception:
        print(f"Erro ao baixar {numero}.zip")

def main():
    print("Digite um número ou intervalo (ex: 1551360 ou 1551360-1551370)")
    entrada = input("> ").strip()

    if "-" in entrada:
        inicio, fim = map(int, entrada.split("-"))
        for n in range(inicio, fim + 1):
            baixar(n)
    else:
        baixar(int(entrada))

if __name__ == "__main__":
    main()
