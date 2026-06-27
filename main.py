# Rule-Based Expert System

print("=== Medical Expert System ===")

fever = input("Do you have fever (yes/no)? ").lower()
cough = input("Do you have cough (yes/no)? ").lower()
headache = input("Do you have headache (yes/no)? ").lower()

print("--- Inference Process ---")

# Rule 1
if fever == "yes" and cough == "yes":
    print("Rule Applied: Fever + Cough - Flu")
    print("Inference: You may have Flu")

    # Rule 2
    print("Rule Applied: Flu - Consult Doctor")
    print("Recommendation: Consult Doctor")

# Rule 3
elif fever == "yes" and headache == "yes":
    print("Rule Applied: Fever + Headache - Viral Infection")
    print("Inference: You may have Viral Infection")

    # Rule 4
    print("Rule Applied: Viral Infection - Take Rest")
    print("Recommendation: Take Rest and Drink Water")

else:
    print("No matching disease found.")
    print("Recommendation: Monitor symptoms and consult a doctor if needed.")

print("Thank you for using the Expert System!")