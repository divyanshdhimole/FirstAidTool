print("\nFIRST-AID SUGGESTION TOOL")
print("\nSelect the type of minor injury:")
print("1. Cut or Scrape")
print("2. Burn")
print("3. Bruise")
print("4. Insect Bite")
print("5. Nosebleed")
print("6. Sprain")

choice = input("\nEnter your choice (1-6): ")

if choice == "1":
    print(" CUT OR SCRAPE ")
    print("1. Wash your hands thoroughly")
    print("2. Stop bleeding by applying gentle pressure with clean cloth")
    print("3. Clean the wound with water")
    print("4. Apply antibiotic ointment")
    print("5. Cover with a sterile bandage")
    print("\n Seek medical help if bleeding doesn't stop or wound is deep")

elif choice == "2":
    print(" BURN ")
    print("1. Cool the burn under running water for 10-20 minutes")
    print("2. Remove any jewelry or tight clothing near the burn")
    print("3. Cover with sterile, non-stick bandage")
    print("4. Take over-the-counter pain reliever if needed")
    print("5. Do NOT apply ice, butter, or ointments")
    print("\n Seek medical help for burns larger than 3 inches or on face/hands")

elif choice == "3":
    print("\n BRUISE ")
    print("1. Apply ice pack wrapped in cloth for 15-20 minutes")
    print("2. Elevate the bruised area if possible")
    print("3. Rest the affected area")
    print("4. After 48 hours, apply warm compress to improve circulation")
    print("5. Take over-the-counter pain reliever if needed")
    print("\n Seek medical help if bruise is very large or painful")

elif choice == "4":
    print(" INSECT BITE ")
    print("1. Remove stinger if present (scrape, don't pinch)")
    print("2. Wash area with soap and water")
    print("3. Apply cold compress to reduce swelling")
    print("4. Apply anti-itch cream or calamine lotion")
    print("5. Avoid scratching the bite")
    print("\n Seek immediate help if difficulty breathing or severe swelling occurs")

elif choice == "5":
    print(" NOSEBLEED ")
    print("1. Sit upright and lean slightly forward")
    print("2. Pinch the soft part of nose for 10 minutes")
    print("3. Breathe through your mouth")
    print("4. Apply cold compress to bridge of nose")
    print("5. Avoid lying down or tilting head back")
    print("\n Seek medical help if bleeding continues after 20 minutes")

elif choice == "6":
    print(" SPRAIN ")
    print("1. Rest the injured area")
    print("2. Ice: Apply ice pack for 15-20 minutes every 2-3 hours")
    print("3. Compression: Wrap with elastic bandage (not too tight)")
    print("4. Elevation: Keep injured area raised above heart level")
    print("5. Avoid using the injured area for 48-72 hours")
    print("\n Seek medical help if severe pain, can't bear weight, or visible deformity")

else:
    print("\n Invalid choice! Please run the program again and select 1-6.")

