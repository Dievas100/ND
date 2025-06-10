import requests

def main():
    print("Ekspertas ruošiasi pokalbiui...")

    promptas = input("Įveskite klausimą apie Anykščius: ")

    system_prompt = """
Tu esi Anykščių turizmo informacijos centro specialistas.
Atsakinėji tik lietuviškai, trumpai (1–3 sakiniai), mandagiai, pozityviai, ir konkrečiai.
Nesugalvok faktų – naudok tik pateiktą informaciją.
    """

    payload = {
        "model": "jobautomation/OpenEuroLLM-Lithuanian",
        "prompt": f"{system_prompt}\nKlausimas: {promptas}",
        "stream": False,
    }

    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        if response.status_code == 200:
            result = response.json()
            print("\nAnykščių turizmo ekspertas:\n")
            print(result.get("response", "").strip())
        else:
            print(f"Klaida iš serverio: {response.status_code}")
    except Exception as e:
        print(f"Klaida siunčiant užklausą: {e}")

if __name__ == "__main__":
    main()
