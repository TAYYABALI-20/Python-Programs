#Write a program for daraz or similar online shopping store

input('Greetings! Hopefully you are doing good Buddy. Press enter to continue.')
input("I'm a built-in scripted online shooping store. My job is to display and buy products according to your preferences. Press enter to continue.")
input('Welcome To Our Scripted Python Product Store! Press enter to continue.')

categories = str(
    input('Please enter the name of the category you are interested in to view our top in-demand products.\n'
          'Available categories:\n'
          '1. Mobile Phones\n'
          '2. Watches\n'
          '3. Cameras\n'
          '4. Laptops\n'
          '5. Headphones\n')).strip().lower()

#CATEGORY NO 1:

if categories in ['mobile phones', 'mobile phone', 'mobiles', 'mobile']:
    
    print('MOBILES\n')
    
    totalAmount = 0
    
    amountOfFirstMobile = 1299
    amountOfSecondMobile = 1999
    amountOfThirdMobile = 1599
    amountOfFourthMobile = 1449
    
    mobile_1 = ("Samsung Galaxy S25 Ultra", "The latest flagship with a stunning display and top-notch camera.")
    mobile_2 = ("iPhone 15 Pro Max", "Apple’s newest release with an advanced A16 Bionic chip and Pro camera system.")
    mobile_3 = ("Spark 7", "Affordable smartphone with a large display and long battery life.")
    mobile_4 = ("Infinix Hot 10", "Budget-friendly option with decent performance and battery life.")
    
    print(f'1. {mobile_1[0]} - ${amountOfFirstMobile}\n   {mobile_1[1]}\n')
    
    buy = input(f"Would you like to buy the {mobile_1[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        totalAmount = amountOfFirstMobile
        print(f'Your selected item, {mobile_1[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
    else:
        print(f"Thank you for considering the {mobile_1[0]}. We appreciate your time and hope to serve you again in the future.")

    shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()
        
    if shopping_done == 'yes':
        feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
        print(f'Thank you for your feedback, "{feedback_message}"')

    elif shopping_done == 'no':
        
        print(f'2. {mobile_2[0]} - ${amountOfSecondMobile}\n   {mobile_2[1]}\n')
    
        buy = input(f"Would you like to buy the {mobile_2[0]}? (yes/no): ").strip().lower()
    
        if buy == 'yes':
            totalAmount = amountOfFirstMobile + amountOfSecondMobile
            print(f'Your selected item, {mobile_2[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
        else:
            print(f"Thank you for considering the {mobile_2[0]}. We appreciate your time and hope to serve you again in the future.")

        shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()
        
        if shopping_done == 'yes':
            feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
            print(f'Thank you for your feedback, "{feedback_message}"')

        elif shopping_done == 'no':

            print(f'3. {mobile_3[0]} - ${amountOfThirdMobile}\n   {mobile_3[1]}\n')
    
            buy = input(f"Would you like to buy the {mobile_3[0]}? (yes/no): ").strip().lower()
    
            if buy == 'yes':
                totalAmount = amountOfFirstMobile + amountOfSecondMobile + amountOfThirdMobile
                print(f'Your selected item, {mobile_3[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
            else:
                print(f"Thank you for considering the {mobile_3[0]}. We appreciate your time and hope to serve you again in the future.")

            shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()
        
            if shopping_done == 'yes':
                feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
                print(f'Thank you for your feedback, "{feedback_message}"')

            elif shopping_done == 'no':

                print(f'4. {mobile_4[0]} - ${amountOfFourthMobile}\n   {mobile_4[1]}\n')
    
                buy = input(f"Would you like to buy the {mobile_4[0]}? (yes/no): ").strip().lower()
    
                if buy == 'yes':
                    totalAmount = amountOfFirstMobile + amountOfSecondMobile + amountOfThirdMobile + amountOfFourthMobile
                    print(f'Your selected item, {mobile_4[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
                else:
                    print(f"Thank you for considering the {mobile_4[0]}. We appreciate your time and hope to serve you again in the future.")
                
                shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()
                
                if shopping_done == 'yes':
                    feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
                    print(f'Thank you for your feedback, "{feedback_message}"')
                else:
                    print("We have a wide range of products in other categories too! Feel free to explore and find something you like.")

#CATEGORY NO 2:

elif categories in ['watches', 'watch']:
    
    print('WATCHES\n')

    totalAmount = 0
    
    amountOfFirstwatch = 2000
    amountOfSecondwatch = 799
    amountOfThirdwatch = 599
    amountOfFourthwatch = 1500

    watch_1 = ("Rolex Submariner", "Iconic dive watch with exceptional craftsmanship and design.")
    watch_2 = ("Omega Speedmaster", "Known as the Moonwatch, this timepiece has a storied history in space exploration.")
    watch_3 = ("Apple Watch Series 9", "The latest smartwatch from Apple with advanced health and fitness tracking.")
    watch_4 = ("Tag Heuer Carrera", "Elegant and sporty watch with a rich motor-racing heritage.")

    print(f'1. {watch_1[0]} - ${amountOfFirstwatch}\n   {watch_1[1]}\n')
    
    buy = input(f"Would you like to buy the {watch_1[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        totalAmount = amountOfFirstwatch
        print(f'Your selected item, {watch_1[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
    else:
        print(f"Thank you for considering the {watch_1[0]}. We appreciate your time and hope to serve you again in the future.")

    shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()
        
    if shopping_done == 'yes':
        feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
        print(f'Thank you for your feedback, "{feedback_message}"')

    elif shopping_done == 'no':

        print(f'2. {watch_2[0]} - ${amountOfSecondwatch}\n   {watch_2[1]}\n')
    
        buy = input(f"Would you like to buy the {watch_2[0]}? (yes/no): ").strip().lower()
    
        if buy == 'yes':
            totalAmount = amountOfFirstwatch + amountOfSecondwatch
            print(f'Your selected item, {watch_2[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
        else:
            print(f"Thank you for considering the {watch_1[0]}. We appreciate your time and hope to serve you again in the future.")

        shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()
        
        if shopping_done == 'yes':
            feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
            print(f'Thank you for your feedback, "{feedback_message}"')

    elif shopping_done == 'no':
        
        print(f'3. {watch_3[0]} - ${amountOfThirdwatch}\n   {watch_3[1]}\n')
    
        buy = input(f"Would you like to buy the {watch_3[0]}? (yes/no): ").strip().lower()
    
        if buy == 'yes':
            totalAmount = amountOfFirstwatch + amountOfSecondwatch + amountOfThirdwatch
            print(f'Your selected item, {watch_3[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
        else:
            print(f"Thank you for considering the {watch_1[0]}. We appreciate your time and hope to serve you again in the future.")

        if shopping_done == 'yes':
            feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
            print(f'Thank you for your feedback, "{feedback_message}"')

    elif shopping_done == 'no':

        print(f'4. {watch_4[0]} - ${amountOfFourthwatch}\n   {watch_4[1]}\n')
    
        buy = input(f"Would you like to buy the {watch_4[0]}? (yes/no): ").strip().lower()
    
        if buy == 'yes':
            totalAmount = amountOfFirstwatch + amountOfSecondwatch + amountOfThirdwatch + amountOfFourthwatch
            print(f'Your selected item, {watch_4[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
        else:
            print(f"Thank you for considering the {watch_1[0]}. We appreciate your time and hope to serve you again in the future.")

        if shopping_done == 'yes':
            feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
            print(f'Thank you for your feedback, "{feedback_message}"')
        else:
            print("We have a wide range of products in other categories too! Feel free to explore and find something you like.")

#CATEGORY NO 3:

elif categories in ['cameras', 'camera']:
    
    print('CAMERAS\n')

    totalAmount = 0
    
    amountOfFirstCamera = 5000
    amountOfSecondCamera = 2899
    amountOfThirdCamera = 3500
    amountOfFourthCamera = 4700

    camera_1 = ("Canon EOS R5", "Mirrorless camera with 45MP sensor and 8K video recording.")
    camera_2 = ("Sony Alpha a7 IV", "Full-frame mirrorless camera with excellent autofocus and video capabilities.")
    camera_3 = ("Nikon Z7 II", "High-resolution mirrorless camera with robust performance and 4K video.")
    camera_4 = ("Fujifilm X-T4", "APS-C mirrorless camera with in-body stabilization and versatile features.")

    print(f'1. {camera_1[0]} - ${amountOfFirstCamera}\n   {camera_1[1]}\n')
    
    buy = input(f"Would you like to buy {camera_1[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        totalAmount = amountOfFirstCamera
        print(f'Your selected item, {camera_1[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
    else:
        print(f"Thank you for considering the {camera_1[0]}. We appreciate your time and hope to serve you again in the future.")

    shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()
        
    if shopping_done == 'yes':
        feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
        print(f'Thank you for your feedback, "{feedback_message}"')

    elif shopping_done == 'no':

        print(f'2. {camera_2[0]} - ${amountOfSecondCamera}\n   {camera_2[1]}\n')
    
        buy = input(f"Would you like to buy {camera_2[0]}? (yes/no): ").strip().lower()
    
        if buy == 'yes':
            totalAmount = amountOfFirstCamera + amountOfSecondCamera
            print(f'Your selected item, {camera_2[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
        else:
            print(f"Thank you for considering the {camera_2[0]}. We appreciate your time and hope to serve you again in the future.")

        shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()
        
        if shopping_done == 'yes':
            feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
            print(f'Thank you for your feedback, "{feedback_message}"')

    elif shopping_done == 'no':

        print(f'3. {camera_3[0]} - ${amountOfThirdCamera}\n   {camera_3[1]}\n')
    
        buy = input(f"Would you like to buy {camera_3[0]}? (yes/no): ").strip().lower()
    
        if buy == 'yes':
            totalAmount = amountOfFirstCamera + amountOfSecondCamera + amountOfThirdCamera
            print(f'Your selected item, {camera_3[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
        else:
            print(f"Thank you for considering the {camera_3[0]}. We appreciate your time and hope to serve you again in the future.")

        shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()
        
        if shopping_done == 'yes':
            feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
            print(f'Thank you for your feedback, "{feedback_message}"')

    elif shopping_done == 'no':

        print(f'4. {camera_4[0]} - ${amountOfFourthCamera}\n   {camera_4[1]}\n')
    
        buy = input(f"Would you like to buy {camera_4[0]}? (yes/no): ").strip().lower()
    
        if buy == 'yes':
            totalAmount = amountOfFirstCamera + amountOfSecondCamera + amountOfThirdCamera + amountOfFourthCamera
            print(f'Your selected item, {camera_4[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
        else:
            print(f"Thank you for considering the {camera_4[0]}. We appreciate your time and hope to serve you again in the future.")
                
        shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()
                
        if shopping_done == 'yes':
            feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
            print(f'Thank you for your feedback, "{feedback_message}"')
        else:
            print("We have a wide range of products in other categories too! Feel free to explore and find something you like.")

#CATEGORY NO 4:

elif categories in ['laptops', 'laptop']:
    
    print('LAPTOPS\n')

    totalAmount = 0
    
    amountOfFirstLaptop = 4500
    amountOfSecondLaptop = 3899
    amountOfThirdLaptop = 4100
    amountOfFourthHeadphone = 3500

    laptop_1 = ("MacBook Pro 16-inch", "Powerful laptop with M1 Pro chip and exceptional display.")
    laptop_2 = ("Dell XPS 13", "Sleek, ultraportable laptop with a stunning 4K display and great performance.")
    laptop_3 = ("HP Spectre x360", "Convertible laptop with a stylish design and strong performance.")
    laptop_4 = ("Lenovo ThinkPad X1 Carbon", "Business laptop with robust build quality and excellent keyboard.")

    print(f'1. {laptop_1[0]} - ${amountOfFirstLaptop}\n   {laptop_1[1]}\n')
    
    buy = input(f"Would you like to buy {laptop_1[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        totalAmount = amountOfFirstLaptop
        print(f'Your selected item, {laptop_1[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
    else:
        print(f"Thank you for considering the {laptop_1[0]}. We appreciate your time and hope to serve you again in the future.")

    shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()

    if shopping_done == 'yes':
        feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
        print(f'Thank you for your feedback, "{feedback_message}"')

    elif shopping_done == 'no':

        print(f'2. {laptop_2[0]} - ${amountOfSecondLaptop}\n   {laptop_2[1]}\n')
    
        buy = input(f"Would you like to buy {laptop_2[0]}? (yes/no): ").strip().lower()
    
        if buy == 'yes':
            totalAmount = amountOfFirstLaptop + amountOfSecondLaptop
            print(f'Your selected item, {laptop_2[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
        else:
            print(f"Thank you for considering the {laptop_2[0]}. We appreciate your time and hope to serve you again in the future.")

        shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()

        if shopping_done == 'yes':
            feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
            print(f'Thank you for your feedback, "{feedback_message}"')

    elif shopping_done == 'no':

        print(f'3. {laptop_3[0]} - ${amountOfThirdLaptop}\n   {laptop_3[1]}\n')
    
        buy = input(f"Would you like to buy {laptop_3[0]}? (yes/no): ").strip().lower()
    
        if buy == 'yes':
            totalAmount = amountOfFirstLaptop + amountOfSecondLaptop + amountOfThirdLaptop
            print(f'Your selected item, {laptop_3[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
        else:
            print(f"Thank you for considering the {laptop_3[0]}. We appreciate your time and hope to serve you again in the future.")

        shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()

        if shopping_done == 'yes':
            feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
            print(f'Thank you for your feedback, "{feedback_message}"')

    elif shopping_done == 'no':

        print(f'4. {laptop_4[0]} - ${amountOfFourthHeadphone}\n   {laptop_4[1]}\n')
    
        buy = input(f"Would you like to buy {laptop_4[0]}? (yes/no): ").strip().lower()
    
        if buy == 'yes':
            totalAmount = amountOfFirstLaptop + amountOfSecondLaptop + amountOfThirdLaptop + amountOfFourthHeadphone
            print(f'Your selected item, {laptop_4[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
        else:
            print(f"Thank you for considering the {laptop_4[0]}. We appreciate your time and hope to serve you again in the future.")

        shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()

        if shopping_done == 'yes':
            feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
            print(f'Thank you for your feedback, "{feedback_message}"')
        else:
            print("We have a wide range of products in other categories too! Feel free to explore and find something you like.")

#CATEGORY NO 5:

elif categories in ['headphones', 'headphone']:
    
    print('LAPTOPS\n')

    totalAmount = 0
    
    amountOfFirstHeadphone = 500
    amountOfSecondHeadphone = 399
    amountOfThirdHeadphone = 299
    amountOfFourthLaptop = 400

    headphone_1 = ("Sony WH-1000XM5", "Industry-leading noise cancellation with exceptional sound quality.")
    headphone_2 = ("Bose QuietComfort 45", "Renowned for their comfort and superb noise-cancelling capabilities.")
    headphone_3 = ("Apple AirPods Max", "Premium over-ear headphones with high-fidelity audio and spatial audio.")
    headphone_4 = ("Sennheiser HD 660 S", "High-end open-back headphones for audiophiles seeking excellent sound clarity.")

    print(f'1. {headphone_1[0]} - ${amountOfFirstHeadphone}\n   {headphone_1[1]}\n')
    
    buy = input(f"Would you like to buy {headphone_1[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        totalAmount = amountOfFirstHeadphone
        print(f'Your selected item, {headphone_1[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
    else:
        print(f"Thank you for considering the {headphone_1[0]}. We appreciate your time and hope to serve you again in the future.")

    shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()

    if shopping_done == 'yes':
        feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
        print(f'Thank you for your feedback, "{feedback_message}"')

    elif shopping_done == 'no':

        print(f'2. {headphone_2[0]} - ${amountOfSecondHeadphone}\n   {headphone_2[1]}\n')
    
        buy = input(f"Would you like to buy {headphone_2[0]}? (yes/no): ").strip().lower()
    
        if buy == 'yes':
            totalAmount = amountOfFirstHeadphone + amountOfSecondHeadphone
            print(f'Your selected item, {headphone_2[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
        else:
            print(f"Thank you for considering the {headphone_2[0]}. We appreciate your time and hope to serve you again in the future.")

        shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()

        if shopping_done == 'yes':
            feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
            print(f'Thank you for your feedback, "{feedback_message}"')

    elif shopping_done == 'no':

        print(f'3. {headphone_3[0]} - ${amountOfThirdHeadphone}\n   {headphone_3[1]}\n')
    
        buy = input(f"Would you like to buy {headphone_3[0]}? (yes/no): ").strip().lower()
    
        if buy == 'yes':
            totalAmount = amountOfFirstHeadphone + amountOfSecondHeadphone + amountOfThirdHeadphone
            print(f'Your selected item, {headphone_3[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
        else:
            print(f"Thank you for considering the {headphone_3[0]}. We appreciate your time and hope to serve you again in the future.")

        shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()

        if shopping_done == 'yes':
            feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
            print(f'Thank you for your feedback, "{feedback_message}"')

    elif shopping_done == 'no':

        print(f'4. {headphone_4[0]} - ${amountOfFourthLaptop}\n   {headphone_4[1]}\n')
    
        buy = input(f"Would you like to buy {headphone_4[0]}? (yes/no): ").strip().lower()
    
        if buy == 'yes':
            totalAmount = amountOfFirstHeadphone + amountOfSecondHeadphone + amountOfThirdHeadphone + amountOfFourthLaptop
            print(f'Your selected item, {headphone_4[0]}, has been successfully purchased. Your total bill is ${totalAmount}\n')
        else:
            print(f"Thank you for considering the {headphone_4[0]}. We appreciate your time and hope to serve you again in the future.")

        shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()

        if shopping_done == 'yes':
            feedback_message = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback (you can include a rating out of 5 stars with *): ")
            print(f'Thank you for your feedback, "{feedback_message}"')
        else:
            print("We have a wide range of products in other categories too! Feel free to explore and find something you like.")

else:
    print("Sorry, we do not have the category you are looking for.")