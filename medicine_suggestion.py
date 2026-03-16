import csv
from datetime import datetime

# Symptom to medicine mapping
medicine_db = {
    "fever": ["Paracetamol", "Crocin"],
    "cold": ["Cetirizine", "Sinarest"],
    "headache": ["Aspirin", "Ibuprofen"],
    "cough": ["Benadryl", "Dextromethorphan"],
    "stomach pain": ["Buscopan", "Drotin"],
    "vomiting": ["Ondansetron", "Domperidone"],
    "rashes": ["Framycetin Skin Cream"],
    "fungal infection": ["Cotrimoxazole Tab"],
    "indigestion": ["Dried Aluminium Hydroxide", "Magnesium Hydroxide & Activated Dimethicone", "Rantidine Hydrochloride tab"],
    "swelling": ["Diclofenac gel", "Ibuprofen"],
    "uti": ["Norfloxacin tab", "Uclean syrup"],
    "acidity": ["Omeprazole tab"],
    "weakness": ["VIT C", "VIT B"]
}

def suggest_medicines(symptoms):
    suggestions = []
    for symptom in symptoms:
        symptom = symptom.lower().strip()
        meds = medicine_db.get(symptom, ["No suggestion available"])
        suggestions.append((symptom, meds))
    return suggestions

def save_to_csv(user_name, suggestions):
    filename = "medicine_suggestions_log.csv"
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        for symptom, meds in suggestions:
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                user_name,
                symptom,
                ", ".join(meds)
            ])

def main():
    print("Welcome to the Medicine Suggestion System")
    user_name = input("Enter your name: ").strip()
    symptoms_input = input("Enter your symptoms separated by commas: ")
    symptoms = symptoms_input.split(",")
    
    suggestions = suggest_medicines(symptoms)
    
    print(f"\nHello {user_name}, here are your suggested medicines:")
    for symptom, meds in suggestions:
        print(f"- {symptom.title()}: {', '.join(meds)}")
    
    save_to_csv(user_name, suggestions)
    print("\nYour input has been saved to 'medicine_suggestions_log.csv'")

if __name__ == "__main__":
    main()
