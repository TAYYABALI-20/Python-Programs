#Write a program for daraz or similar online shopping store

input('Greetings! Hopefully you are doing good Buddy. Press enter to continue.')

input("I'm a built-in scripted online shooping store. My job is to display and buy products according to your preferences. Press enter to continue.")

input('Welcome To Our Scripted Python Product Store! Press enter to continue.')

categories = str(
    input('Please enter the name of the category you are interested in to view our top in-demand products.\n'
          'Available categories:\n'
          '1. Mobile Phones\n'
          '2. Watches\n'
          '3. Video Games\n'
          '4. Gadgets\n'
          '5. Laptops\n'
          '6. Tablets\n'
          '7. Headphones\n'
          '8. Cameras\n'
          '9. Smart Home Devices\n')).strip().lower()

#CATEGORY NO 1:

if categories in ['mobile phones', 'mobile phone', 'mobiles', 'mobile']:
    
    print('MOBILES\n')
    
    mobile_1 = ("Samsung Galaxy S25 Ultra", "$1,299", "The latest flagship with a stunning display and top-notch camera.")
    
    mobile_2 = ("iPhone 15 Pro Max", "$1,399", "Apple’s newest release with an advanced A16 Bionic chip and Pro camera system.")
    
    mobile_3 = ("Spark 7", "$199", "Affordable smartphone with a large display and long battery life.")
    
    mobile_4 = ("Infinix Hot 10", "$149", "Budget-friendly option with decent performance and battery life.")
    
    print(f'1. {mobile_1[0]} - {mobile_1[1]}\n   {mobile_1[2]}\n')
    
    buy = input(f"Would you like to buy the {mobile_1[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {mobile_1[0]}, has been successfully purchased. Your total bill is {mobile_1[1]}\n')

    else:
        print(f"Thank you for considering the {mobile_1[0]}. We appreciate your time and hope to serve you again in the future.")

    shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()
        
    if shopping_done == 'yes':
        feedbackMessage = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback.")
        print(f'Thank you for your feedback, {feedbackMessage}')

    elif shopping_done == 'no':
        
        print(f'2. {mobile_2[0]} - {mobile_2[1]}\n   {mobile_2[2]}\n')
    
        buy = input(f"Would you like to buy the {mobile_2[0]}? (yes/no): ").strip().lower()
    
        if buy == 'yes':
            print(f'Your selected item, {mobile_2[0]}, has been successfully purchased. Your total bill is {mobile_2[1]}\n')

        else:
            print(f"Thank you for considering the {mobile_2[0]}. We appreciate your time and hope to serve you again in the future.")

        shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()
        
        if shopping_done == 'yes':
            feedbackMessage = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback.")
            print(f'Thank you for your feedback, {feedbackMessage}')

        elif shopping_done == 'no':

            print(f'3. {mobile_3[0]} - {mobile_3[1]}\n   {mobile_3[2]}\n')
    
            buy = input(f"Would you like to buy the {mobile_3[0]}? (yes/no): ").strip().lower()
    
            if buy == 'yes':
                print(f'Your selected item, {mobile_3[0]}, has been successfully purchased. Your total bill is {mobile_3[1]}\n')

            else:
                print(f"Thank you for considering the {mobile_3[0]}. We appreciate your time and hope to serve you again in the future.")

            shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()
        
            if shopping_done == 'yes':
                feedbackMessage = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback.")
                print(f'Thank you for your feedback, {feedbackMessage}')

            elif shopping_done == 'no':

                print(f'4. {mobile_4[0]} - {mobile_4[1]}\n   {mobile_4[2]}\n')
    
                buy = input(f"Would you like to buy the {mobile_4[0]}? (yes/no): ").strip().lower()
    
                if buy == 'yes':
                    print(f'Your selected item, {mobile_4[0]}, has been successfully purchased. Your total bill is {mobile_4[1]}\n')

                else:
                    print(f"Thank you for considering the {mobile_4[0]}. We appreciate your time and hope to serve you again in the future.")
                
                shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()
                
                if shopping_done == 'yes':
                    feedbackMessage = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback.")
                    print(f'Thank you for your feedback, {feedbackMessage}')

                else:
                    print("We have a wide range of products in other categories too! Feel free to explore and find something you like.")

#CATEGORY NO 2:

elif categories in ['watches', 'watch']:
    
    print('WATCHES\n')

    watch_1 = ("Rolex Submariner", "$8,100", "Iconic dive watch with exceptional craftsmanship and design.")
    
    watch_2 = ("Omega Speedmaster", "$6,500", "Known as the Moonwatch, this timepiece has a storied history in space exploration.")
    
    watch_3 = ("Apple Watch Series 9", "$399", "The latest smartwatch from Apple with advanced health and fitness tracking.")
    
    watch_4 = ("Tag Heuer Carrera", "$5,000", "Elegant and sporty watch with a rich motor-racing heritage.")

    print(f'1. {watch_1[0]} - {watch_1[1]}\n   {watch_1[2]}\n')
    
    buy = input(f"Would you like to buy the {watch_1[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {watch_1[0]}, has been successfully purchased. Your total bill is {watch_1[1]}\n')

    else:
        print(f"Thank you for considering the {watch_1[0]}. We appreciate your time and hope to serve you again in the future.")

    shopping_done = input("Is your shopping done? (yes/no): ").strip().lower()
        
    if shopping_done == 'yes':
        feedbackMessage = input("Thank you for shopping with us! We appreciate your business. Please leave a feedback.")
        print(f'Thank you for your feedback, {feedbackMessage}')

    elif shopping_done == 'no':

        print(f'2. {watch_2[0]} - {watch_2[1]}\n   {watch_2[2]}\n')
    
        buy = input(f"Would you like to buy the {watch_2[0]}? (yes/no): ").strip().lower()
    
        if buy == 'yes':
            print(f'Your selected item, {watch_2[0]}, has been successfully purchased. Your total bill is {watch_2[1]}\n')

        print(f'3. {watch_3[0]} - {watch_3[1]}\n   {watch_3[2]}\n')
    
        buy = input(f"Would you like to buy the {watch_3[0]}? (yes/no): ").strip().lower()
    
        if buy == 'yes':
            print(f'Your selected item, {watch_3[0]}, has been successfully purchased. Your total bill is {watch_3[1]}\n')

        print(f'4. {watch_4[0]} - {watch_4[1]}\n   {watch_4[2]}\n')
    
        buy = input(f"Would you like to buy the {watch_4[0]}? (yes/no): ").strip().lower()
    
        if buy == 'yes':
            print(f'Your selected item, {watch_4[0]}, has been successfully purchased. Your total bill is {watch_4[1]}\n')

#CATEGORY NO 3:

elif categories in ['video games', 'video game', 'games', 'game']:
    
    print('VIDEO GAMES\n')

    game_1 = ("The Legend of Zelda: Tears of the Kingdom", "$59.99", "Highly anticipated sequel with expansive open-world exploration.")
    
    game_2 = ("Elden Ring", "$59.99", "Action RPG developed by FromSoftware with a vast and intricate world.")
    
    game_3 = ("Cyberpunk 2077", "$49.99", "Open-world RPG set in a dystopian future, known for its immersive narrative.")
    
    game_4 = ("God of War Ragnarok", "$69.99", "Epic continuation of the God of War series with stunning visuals and gameplay.")

    print(f'1. {game_1[0]} - {game_1[1]}\n   {game_1[2]}\n')
    
    buy = input(f"Would you like to buy {game_1[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {game_1[0]}, has been successfully purchased. Your total bill is {game_1[1]}\n')

    print(f'2. {game_2[0]} - {game_2[1]}\n   {game_2[2]}\n')
    
    buy = input(f"Would you like to buy {game_2[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {game_2[0]}, has been successfully purchased. Your total bill is {game_2[1]}\n')

    print(f'3. {game_3[0]} - {game_3[1]}\n   {game_3[2]}\n')
    
    buy = input(f"Would you like to buy {game_3[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {game_3[0]}, has been successfully purchased. Your total bill is {game_3[1]}\n')

    print(f'4. {game_4[0]} - {game_4[1]}\n   {game_4[2]}\n')
    
    buy = input(f"Would you like to buy {game_4[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {game_4[0]}, has been successfully purchased. Your total bill is {game_4[1]}\n')

#CATEGORY NO 4:

elif categories in ['gadgets', 'gadget']:
    
    print('GADGETS\n')
   
    gadget_1 = ("Apple AirPods Pro 2", "$249", "Noise-cancelling earbuds with superior sound quality and spatial audio.")
    
    gadget_2 = ("Samsung Galaxy Buds Pro", "$199", "High-quality wireless earbuds with active noise cancellation.")
    
    gadget_3 = ("DJI Mini 3 Pro Drone", "$759", "Compact and powerful drone with advanced features and 4K video recording.")
    
    gadget_4 = ("Amazon Echo Show 10", "$249.99", "Smart display with Alexa and a rotating screen to follow you around the room.")

    print(f'1. {gadget_1[0]} - {gadget_1[1]}\n   {gadget_1[2]}\n')
    
    buy = input(f"Would you like to buy {gadget_1[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {gadget_1[0]}, has been successfully purchased. Your total bill is {gadget_1[1]}\n')

    print(f'2. {gadget_2[0]} - {gadget_2[1]}\n   {gadget_2[2]}\n')
    
    buy = input(f"Would you like to buy {gadget_2[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {gadget_2[0]}, has been successfully purchased. Your total bill is {gadget_2[1]}\n')

    print(f'3. {gadget_3[0]} - {gadget_3[1]}\n   {gadget_3[2]}\n')
    
    buy = input(f"Would you like to buy {gadget_3[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {gadget_3[0]}, has been successfully purchased. Your total bill is {gadget_3[1]}\n')

    print(f'4. {gadget_4[0]} - {gadget_4[1]}\n   {gadget_4[2]}\n')
    
    buy = input(f"Would you like to buy {gadget_4[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {gadget_4[0]}, has been successfully purchased. Your total bill is {gadget_4[1]}\n')

#CATEGORY NO 5:

elif categories in ['laptops', 'laptop']:
    
    print('LAPTOPS\n')

    laptop_1 = ("MacBook Pro 16-inch", "$2,499", "Powerful laptop with M1 Pro chip and exceptional display.")
    
    laptop_2 = ("Dell XPS 13", "$1,299", "Sleek, ultraportable laptop with a stunning 4K display and great performance.")
    
    laptop_3 = ("HP Spectre x360", "$1,499", "Convertible laptop with a stylish design and strong performance.")
    
    laptop_4 = ("Lenovo ThinkPad X1 Carbon", "$1,799", "Business laptop with robust build quality and excellent keyboard.")

    print(f'1. {laptop_1[0]} - {laptop_1[1]}\n   {laptop_1[2]}\n')
    
    buy = input(f"Would you like to buy {laptop_1[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {laptop_1[0]}, has been successfully purchased. Your total bill is {laptop_1[1]}\n')

    print(f'2. {laptop_2[0]} - {laptop_2[1]}\n   {laptop_2[2]}\n')
    
    buy = input(f"Would you like to buy {laptop_2[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {laptop_2[0]}, has been successfully purchased. Your total bill is {laptop_2[1]}\n')

    print(f'3. {laptop_3[0]} - {laptop_3[1]}\n   {laptop_3[2]}\n')
    
    buy = input(f"Would you like to buy {laptop_3[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {laptop_3[0]}, has been successfully purchased. Your total bill is {laptop_3[1]}\n')

    print(f'4. {laptop_4[0]} - {laptop_4[1]}\n   {laptop_4[2]}\n')
    
    buy = input(f"Would you like to buy {laptop_4[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {laptop_4[0]}, has been successfully purchased. Your total bill is {laptop_4[1]}\n')

#CATEGORY NO 6:

elif categories in ['tablets', 'tablet']:
    
    print('TABLETS\n')

    tablet_1 = ("Apple iPad Pro", "$1,099", "High-performance tablet with M1 chip and Liquid Retina display.")
    
    tablet_2 = ("Samsung Galaxy Tab S8", "$849", "Android tablet with a vibrant display and powerful hardware.")
    
    tablet_3 = ("Amazon Fire HD 10", "$149", "Affordable tablet with a 10-inch display and Alexa integration.")
    
    tablet_4 = ("Microsoft Surface Pro 9", "$999", "Versatile 2-in-1 device with powerful performance and a detachable keyboard.")

    print(f'1. {tablet_1[0]} - {tablet_1[1]}\n   {tablet_1[2]}\n')
    
    buy = input(f"Would you like to buy {tablet_1[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {tablet_1[0]}, has been successfully purchased. Your total bill is {tablet_1[1]}\n')

    print(f'2. {tablet_2[0]} - {tablet_2[1]}\n   {tablet_2[2]}\n')
    
    buy = input(f"Would you like to buy {tablet_2[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {tablet_2[0]}, has been successfully purchased. Your total bill is {tablet_2[1]}\n')

    print(f'3. {tablet_3[0]} - {tablet_3[1]}\n   {tablet_3[2]}\n')
    
    buy = input(f"Would you like to buy {tablet_3[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {tablet_3[0]}, has been successfully purchased. Your total bill is {tablet_3[1]}\n')

    print(f'4. {tablet_4[0]} - {tablet_4[1]}\n   {tablet_4[2]}\n')
    
    buy = input(f"Would you like to buy {tablet_4[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {tablet_4[0]}, has been successfully purchased. Your total bill is {tablet_4[1]}\n')

#CATEGORY NO 7:

elif categories in ['headphones', 'headphone']:
    
    print('HEADPHONES\n')

    headphone_1 = ("Sony WH-1000XM5", "$399", "Industry-leading noise cancellation with exceptional sound quality.")
    
    headphone_2 = ("Bose QuietComfort 45", "$329", "Renowned for their comfort and superb noise-cancelling capabilities.")
    
    headphone_3 = ("Apple AirPods Max", "$549", "Premium over-ear headphones with high-fidelity audio and spatial audio.")
    
    headphone_4 = ("Sennheiser HD 660 S", "$499", "High-end open-back headphones for audiophiles seeking excellent sound clarity.")

    print(f'1. {headphone_1[0]} - {headphone_1[1]}\n   {headphone_1[2]}\n')
    
    buy = input(f"Would you like to buy {headphone_1[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {headphone_1[0]}, has been successfully purchased. Your total bill is {headphone_1[1]}\n')

    print(f'2. {headphone_2[0]} - {headphone_2[1]}\n   {headphone_2[2]}\n')
    
    buy = input(f"Would you like to buy {headphone_2[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {headphone_2[0]}, has been successfully purchased. Your total bill is {headphone_2[1]}\n')

    print(f'3. {headphone_3[0]} - {headphone_3[1]}\n   {headphone_3[2]}\n')
    
    buy = input(f"Would you like to buy {headphone_3[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {headphone_3[0]}, has been successfully purchased. Your total bill is {headphone_3[1]}\n')

    print(f'4. {headphone_4[0]} - {headphone_4[1]}\n   {headphone_4[2]}\n')
    
    buy = input(f"Would you like to buy {headphone_4[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {headphone_4[0]}, has been successfully purchased. Your total bill is {headphone_4[1]}\n')

#CATEGORY NO 8:

elif categories in ['cameras', 'camera']:
    
    print('CAMERAS\n')

    camera_1 = ("Canon EOS R5", "$3,899", "Mirrorless camera with 45MP sensor and 8K video recording.")
    
    camera_2 = ("Sony Alpha a7 IV", "$2,499", "Full-frame mirrorless camera with excellent autofocus and video capabilities.")
    
    camera_3 = ("Nikon Z7 II", "$2,999", "High-resolution mirrorless camera with robust performance and 4K video.")
    
    camera_4 = ("Fujifilm X-T4", "$1,699", "APS-C mirrorless camera with in-body stabilization and versatile features.")

    print(f'1. {camera_1[0]} - {camera_1[1]}\n   {camera_1[2]}\n')
    
    buy = input(f"Would you like to buy {camera_1[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {camera_1[0]}, has been successfully purchased. Your total bill is {camera_1[1]}\n')

    print(f'2. {camera_2[0]} - {camera_2[1]}\n   {camera_2[2]}\n')
    
    buy = input(f"Would you like to buy {camera_2[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {camera_2[0]}, has been successfully purchased. Your total bill is {camera_2[1]}\n')

    print(f'3. {camera_3[0]} - {camera_3[1]}\n   {camera_3[2]}\n')
    
    buy = input(f"Would you like to buy {camera_3[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {camera_3[0]}, has been successfully purchased. Your total bill is {camera_3[1]}\n')

    print(f'4. {camera_4[0]} - {camera_4[1]}\n   {camera_4[2]}\n')
    
    buy = input(f"Would you like to buy {camera_4[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {camera_4[0]}, has been successfully purchased. Your total bill is {camera_4[1]}\n')

#CATEGORY NO 9:

elif categories in ['smart home devices', 'smart home', 'smart home device', 'smart devices', 'smart device']:
    
    print('SMART HOME DEVICES\n')

    smart_home_1 = ("Google Nest Hub Max", "$229", "Smart display with Google Assistant and built-in camera for video calls.")
    
    smart_home_2 = ("Amazon Echo Dot (4th Gen)", "$49.99", "Compact smart speaker with Alexa and improved sound quality.")
    
    smart_home_3 = ("Philips Hue Smart Bulbs", "$199 (Starter Kit)", "Customizable smart lighting system controllable via app or voice.")
    
    smart_home_4 = ("Ring Video Doorbell 4", "$199.99", "Advanced video doorbell with enhanced motion detection and video quality.")

    print(f'1. {smart_home_1[0]} - {smart_home_1[1]}\n   {smart_home_1[2]}\n')
    
    buy = input(f"Would you like to buy {smart_home_1[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {smart_home_1[0]}, has been successfully purchased. Your total bill is {smart_home_1[1]}\n')

    print(f'2. {smart_home_2[0]} - {smart_home_2[1]}\n   {smart_home_2[2]}\n')
    
    buy = input(f"Would you like to buy {smart_home_2[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {smart_home_2[0]}, has been successfully purchased. Your total bill is {smart_home_2[1]}\n')

    print(f'3. {smart_home_3[0]} - {smart_home_3[1]}\n   {smart_home_3[2]}\n')
    
    buy = input(f"Would you like to buy {smart_home_3[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {smart_home_3[0]}, has been successfully purchased. Your total bill is {smart_home_3[1]}\n')

    print(f'4. {smart_home_4[0]} - {smart_home_4[1]}\n   {smart_home_4[2]}\n')
    
    buy = input(f"Would you like to buy {smart_home_4[0]}? (yes/no): ").strip().lower()
    
    if buy == 'yes':
        print(f'Your selected item, {smart_home_4[0]}, has been successfully purchased. Your total bill is {smart_home_4[1]}\n')

else:
    print("Sorry, we do not have the category you are looking for.")