# -Cycloconverter
# Simple Cycloconverter Simulation

input_frequency = 50  # Hz

print("--- CYCLOCONVERTER ---")
print("Input Frequency:", input_frequency, "Hz")

while True:
    print("\nSelect Output Frequency")
    print("1. 25 Hz")
    print("2. 20 Hz")
    print("3. 10 Hz")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        output_frequency = 25
        print("Output Frequency:", output_frequency, "Hz")

    elif choice == "2":
        output_frequency = 20
        print("Output Frequency:", output_frequency, "Hz")

    elif choice == "3":
        output_frequency = 10
        print("Output Frequency:", output_frequency, "Hz")

    elif choice == "4":
        print("Cycloconverter stopped.")
        break

    else:
        print("Invalid choice!")
