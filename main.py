
import speech
from command import ai_response 

def main():
    while True:
        print("\nWaiting for your command...")
        command = speech.listen() 
        
        if command:
            print(f"Command received: {command}")
            response = ai_response(command)
            print(f"AI: {response}")
            
            
            if "exit" in command.lower() or "bye" in command.lower(): 
                print("Exiting.")
                break
        else:
            print("No command detected or an error occurred. Retrying...")

if __name__ == "__main__":
    main()