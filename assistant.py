import speech_recognition as sr
import pyttsx3
from datetime import datetime


# ==========================================
# INITIALIZATION
# ==========================================

listener = sr.Recognizer()


# ==========================================
# TEXT TO SPEECH
# ==========================================

def talk(text):

    print("Assistant:", text)

    try:

        # Create a new engine every time
        # so speech works on every cycle.
        engine = pyttsx3.init()

        voices = engine.getProperty("voices")

        if len(voices) > 1:
            engine.setProperty(
                "voice",
                voices[1].id
            )

        engine.setProperty(
            "rate",
            150
        )

        engine.say(text)
        engine.runAndWait()
        engine.stop()

    except Exception as e:

        print("Text-to-speech error:", e)


# ==========================================
# SELECT LANGUAGE
# ==========================================

def select_language():

    # --------------------------------------
    # ASK LANGUAGE
    # --------------------------------------

    talk(
        "Please choose the language you want to use."
    )

    print()
    print("==============================")
    print("Choose Language")
    print("==============================")
    print("1. English")
    print("2. Hindi")
    print("3. Telugu")
    print("4. Tamil")
    print("5. Marathi")

    # --------------------------------------
    # GET LANGUAGE OPTION
    # --------------------------------------

    while True:

        try:

            option = int(
                input("\nEnter an option: ")
            )

            if option in [1, 2, 3, 4, 5]:
                break

            print(
                "Please choose a number from 1 to 5."
            )

        except ValueError:

            print(
                "Please enter a valid number."
            )

    # --------------------------------------
    # LANGUAGE CODES
    # --------------------------------------

    languages = {
        1: "en-IN",
        2: "hi-IN",
        3: "te-IN",
        4: "ta-IN",
        5: "mr-IN"
    }

    # --------------------------------------
    # LANGUAGE NAMES
    # --------------------------------------

    language_names = {
        1: "English",
        2: "Hindi",
        3: "Telugu",
        4: "Tamil",
        5: "Marathi"
    }

    language = languages[option]
    language_name = language_names[option]

    # --------------------------------------
    # CONFIRM LANGUAGE
    # --------------------------------------

    talk(
        "You have selected "
        + language_name
        + "."
    )

    # --------------------------------------
    # ASK USER TO SPEAK
    # --------------------------------------

    talk(
        "You may speak now."
    )

    return language, language_name


# ==========================================
# TAKE USER SPEECH
# ==========================================

def take_command(language, language_name):

    try:

        with sr.Microphone() as source:

            print()
            print("Listening...")

            listener.adjust_for_ambient_noise(
                source,
                duration=1
            )

            voice = listener.listen(
                source
            )

        print("Recognizing...")

        # ----------------------------------
        # SPEECH TO TEXT
        # ----------------------------------

        command = listener.recognize_google(
            voice,
            language=language
        )

        command = command.strip()

        # ----------------------------------
        # CURRENT DATE AND TIME
        # ----------------------------------

        current_time = datetime.now().strftime(
            "%d-%b-%Y %H:%M:%S"
        )

        # ----------------------------------
        # PRINT USER SPEECH
        # ----------------------------------

        print()
        print("You:", command)

        # ----------------------------------
        # SAVE TO OUTPUT.TXT
        # ----------------------------------

        with open(
            "output.txt",
            "a",
            encoding="utf-8"
        ) as file:

            file.write("\n")
            file.write(
                "========================================\n"
            )

            file.write(
                "Time: "
                + current_time
                + "\n"
            )

            file.write(
                "Language: "
                + language_name
                + "\n"
            )

            file.write(
                "You said: "
                + command
                + "\n"
            )

            file.write(
                "========================================\n"
            )

        return command.lower()

    # --------------------------------------
    # COULD NOT UNDERSTAND
    # --------------------------------------

    except sr.UnknownValueError:

        talk(
            "Sorry, I could not understand you."
        )

        return ""

    # --------------------------------------
    # SPEECH SERVICE ERROR
    # --------------------------------------

    except sr.RequestError:

        talk(
            "Sorry, there is a problem "
            "with the speech recognition service."
        )

        return ""

    # --------------------------------------
    # OTHER ERROR
    # --------------------------------------

    except Exception as e:

        print("Error:", e)

        return ""


# ==========================================
# LISTEN FOR CONTINUE / STOP
# ==========================================

def listen_continue_stop():

    try:

        with sr.Microphone() as source:

            print()
            print(
                "Listening for continue or stop..."
            )

            listener.adjust_for_ambient_noise(
                source,
                duration=1
            )

            voice = listener.listen(
                source
            )

        print("Recognizing...")

        response = listener.recognize_google(
            voice,
            language="en-IN"
        )

        response = response.strip().lower()

        # ----------------------------------
        # DEBUG
        # ----------------------------------

        print(
            "Continue/Stop response:",
            response
        )

        return response

    # --------------------------------------
    # COULD NOT UNDERSTAND
    # --------------------------------------

    except sr.UnknownValueError:

        print(
            "Could not understand response."
        )

        return ""

    # --------------------------------------
    # SPEECH SERVICE ERROR
    # --------------------------------------

    except sr.RequestError:

        talk(
            "Sorry, there is a problem "
            "with the speech recognition service."
        )

        return ""

    # --------------------------------------
    # OTHER ERROR
    # --------------------------------------

    except Exception as e:

        print("Error:", e)

        return ""


# ==========================================
# ASK CONTINUE OR STOP
# ==========================================

def ask_continue():

    while True:

        # ----------------------------------
        # ASK USER
        # ----------------------------------

        talk(
            "Do you want to continue or stop?"
        )

        # ----------------------------------
        # LISTEN
        # ----------------------------------

        response = listen_continue_stop()

        # ----------------------------------
        # STOP
        # ----------------------------------

        if (
            response == "stop"
            or response == "no"
            or response == "exit"
            or response == "quit"
            or response == "goodbye"
            or "stop" in response
        ):

            talk(
                "Okay. Goodbye!"
            )

            return False

        # ----------------------------------
        # CONTINUE
        # ----------------------------------

        if (
            response == "continue"
            or response == "yes"
            or response == "yeah"
            or response == "yep"
            or "continue" in response
        ):

            talk(
                "Okay. Let's continue."
            )

            return True

        # ----------------------------------
        # NOTHING UNDERSTOOD
        # ----------------------------------

        if response == "":

            talk(
                "I could not understand you."
            )

        else:

            talk(
                "Please say continue or stop."
            )


# ==========================================
# MAIN PROGRAM
# ==========================================

talk(
    "Hello. I am your voice assistant."
)


# ==========================================
# MAIN LOOP
# ==========================================

while True:

    # ======================================
    # STEP 1
    # SELECT LANGUAGE
    # ======================================

    language, language_name = select_language()


    # ======================================
    # STEP 2
    # USER SPEAKS
    # ======================================

    command = take_command(
        language,
        language_name
    )


    # --------------------------------------
    # If speech was not recognized,
    # start again from language selection.
    # --------------------------------------

    if command == "":
        continue


    # ======================================
    # STEP 3
    # ASK CONTINUE OR STOP
    # ======================================

    should_continue = ask_continue()


    # ======================================
    # STEP 4
    # STOP
    # ======================================

    if not should_continue:

        break


    # ======================================
    # STEP 5
    # CONTINUE
    #
    # The loop goes back to STEP 1.
    # ======================================

    print()
    print(
        "----------------------------------------"
    )
    print(
        "Starting a new session..."
    )
    print(
        "----------------------------------------"
    )
    print()


# ==========================================
# PROGRAM ENDED
# ==========================================

print()
print("Program ended.")