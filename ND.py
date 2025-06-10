import requests

def load_context():
    try:
        with open("kontekstas.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Konteksto failas nerastas."

def main():
    print("Ekspertas ruošiasi...")

    # 1. Įkeliamas kontekstas
    kontekstas = load_context()

    # 2. Vartotojo klausimas
    klausimas = input("Įveskite klausimą apie Anykščius: ")

    # 3. Promptas su kontekstu
    prompt = f"""
Tu esi Anykščių turizmo informacijos centro atstovas.
Atsakinėji trumpai (1–3 sakiniai), tik lietuvių kalba, mandagiai ir konkrečiai.

Atsakyk remdamasis TIK šiuo kontekstu:

----- KONTEKSTAS -----
{kontekstas}
-----------------------

KLAUSIMAS:
{klausimas}
    """

    # 4. Užklausa modeliui
    payload = {
        "model": "jobautomation/OpenEuroLLM-Lithuanian",
        "prompt": prompt,
        "stream": False,
    }

    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        if response.status_code == 200:
            result = response.json()
            print("\nExperto atsakymas:\n")
            print(result.get("response", "").strip())
        else:
            print(f"Klaida iš serverio: {response.status_code}")
    except Exception as e:
        print(f"Klaida siunčiant užklausą: {e}")

if __name__ == "__main__":
    main()
