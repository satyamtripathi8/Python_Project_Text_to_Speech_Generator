from gtts import gTTS
import pygame
import re

def get_user_input():
    return input("Enter the text you want to convert to speech: ")

def select_language():
    print("Available languages:")
    print("1--> English (en)")
    print("2-->Spanish (es)")
    print("3--> Hindi (hi)")
    print("4--> French (fr)")
    print("5--> Chinese (zh)")
    print("6--> Korean (ko)")
    
    language_choice = input("Enter the number corresponding to the desired language: ")

    if language_choice == '1':
        return 'en'
    elif language_choice == '2':
        return 'es'
    elif language_choice == '3':
        return 'hi'
    elif language_choice == '4':
        return 'fr'
    elif language_choice == '5':
        return 'zh'
    elif language_choice == '6':
        return 'ko'
    # Add more conditions for additional languages

    print("Invalid choice. Defaulting to English.")
    return 'en'

def generate_file_name(text):
    cleaned_text = re.sub(r'\W+', '', text)
    return f"{cleaned_text}.mp3"

def save_to_file(obj, file_name):
    obj.save(file_name)

def play_audio(file_name):
    pygame.mixer.init() 
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    pygame.event.wait()

def main():
    user_input = get_user_input()
    language_input = select_language()
    file_name = generate_file_name(user_input)

    try:
        obj = gTTS(text=user_input, lang=language_input, slow=False)
    except ValueError as e:
        print(f"Error: {e}")
        return

    save_to_file(obj, file_name)
    print(f"Speech saved to {file_name}")

    play_option = input("Do you want to play the generated speech? (yes/no): ").lower()
    if play_option == 'yes':
        play_audio(file_name)

if __name__ == "__main__":
    pygame.init()  
    main()
