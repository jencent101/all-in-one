from tabulate import tabulate
from PIL import ImageGrab
from win32api import GetSystemMetrics
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
from rich.prompt import Prompt
from rich.panel import Panel
from rich import print as pprint
import numpy as np
import cv2, subprocess, calendar, datetime, os, webbrowser
import googletrans, gtts, speech_recognition as sr
import playsound, mechanize, socket, time, struct

logo = """
    ***** *   *      (*) *****      **
    *   * *   *          *   *     * *
    ***** *   *       *  *   *       *
    *   * *** ***  @  *  *   *  @  ***** . PY

    use help command for first use ^_^
    """
print('=' * 50)
print(logo)
print('=' * 50)

author = "Jencent Dizon"
link = "https://github.com/yamada__101"
print("\nAuthor: " + author + "\nLink: " + link)

commands = [
    ['\nCommands', '\n\tUsage'],
    ['help', 'use this for help command'],
    ['help --secret', 'use this for more commands'],
    ['exit', 'to exit program'],
    ['ctrl + c', 'exit the program'],
    ['calculator', 'to use a calculator'],
    ['calendar', 'to open the calendar console'],
    ['notepad', 'open a notepad'],
    ['cmd', 'open a command prompt'],
    ['powershell', 'open a powershell'],
    ['bash', 'open git bash'],
    ['time', 'the time now'],
    ['goto', 'goto your favorite site automatic'],
    ['leap', "to show a year if it's a leapyear"],
    ['makedir', 'create a directory'],
    ['deldir', 'deleting the directory'],
    ['makeTXT', 'create .txt file'],
    ['readTXT', 'read the .txt file'],
    ['addTXT', 'add some text to .txt file'],
    ['delTXT', 'delete the .txt file'],
    ['pwd', 'print current directory'],
    ['clear', 'clear screen'],
    ]

help_advance = [
    ['\nCommands', '\n\tUsage'],
    ['ping', 'use to ping a site'],
    ['osk', 'on-screen keyboard'],
    ['ai --freefb', 'use to autologin to freefb'],
    ['ai --messenger', 'use to autologin to messenger'],
    ['ai --github', 'use to autologin to Github'],
    ['sc -record', 'start screen recorder'],
    ['con. string', 'converting string to binary'],
    ['Chrome -mp3', 'play your mp3 on chrome'],
    ['Chrome -mp4', 'play your mp4 on chrome'],
    ['tts', 'convert text to any languages'],
    ['sts', 'convert speech/voice to any languages'],
    ]

# BASIC COMMANDS #
def HELP():
    print(tabulate(commands, headers='firstrow'))
def HELPSECRET():
    print(tabulate(help_advance, headers='firstrow'))
def EXIT():
    exit()
def CALCULATOR():
    calc = subprocess.getoutput("calc")
def CALENDAR():
    year = int(input("Year: "))
    month = int(input("Month: "))
    CALENDAR = calendar.month(year, month)
    print(CALENDAR)
def NOTEPAD():
    ntpd = subprocess.getoutput("notepad")
def CMD():
    cmd = subprocess.getoutput("start")
def POWERSHELL():
    ps = subprocess.getoutput("start powershell.exe")
def BASH():
    p = subprocess.Popen("C:\Program Files\Git\git-bash.exe")
def TIME():
    Year = datetime.datetime.now().strftime("%Y")
    Month = datetime.datetime.now().strftime("%m")
    Day = datetime.datetime.now().strftime("%d")
    print("Year: " + Year + " Month: " + Month + " Day: " + Day)
def GOTO():
    print("use + sign between spaces")
    chromedir= 'C:/Program Files/Microsoft/Edge/Application/msedge.exe %s'
    fsite = input("Enter a site: ")
    webbrowser.get(chromedir).open("https://google.com/?q=" + fsite)
def LEAPYEAR():
    year = int(input("Year: "))
    is_leapyear = calendar.isleap(year)
    if is_leapyear == True:
        print("This year is a leap year")
    elif is_leapyear == False:
        print("This year is not a leap year")
    else:
        print("Invalid Year")
def MKDIR():
    path = input("Path: ")
    create_dir = os.mkdir(path)
def DDIR():
    path = input("Path: ")
    del_dir = os.rmdir(path)
def WTXT():
    print("example: c:/users/admin/desktop/hello.txt")
    path = input("Path: ")
    f = open(path, "w+")
    for i in range(1):
        mtxt = input("Enter a sample text: ")
        f.write(mtxt + "\n")
    f.close()
def RTXT():
    print("example: c:/users/admin/desktop/hello.txt")
    path = input("Path: ")
    with open(path, "r") as f:
        rtxt = f.read()
        print(rtxt)
def ATXT():
    print("example: c:/users/admin/desktop/hello.txt")
    path = input("Path: ")
    f = open(path, "a+")
    for i in range(1):
        atxt = input("Add some text: ")
        f.write(atxt + '\n')
    f.close()
def DTXT():
    path = input("Path: ")
    f = os.remove(path)
    print(path + " Removed Successfully")
def PWD():
    pwd = os.system("echo The current directory is: %CD%")
    print(pwd)
def CLEAR():
    clear_screen = os.system('cls')

# ADVANCE COMMANDS #
def PING():
    site = input("Site: ")
    pingSite = os.system("ping " + site)
    print(pingSite)
def ONSCREENKEYBOARD():
    os.system("%windir%\system32\osk.exe")
def FREEFB():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    logo = Panel.fit("[bold lightblue] Free Facebook autologin", border_style="blue")
    pprint(logo)
    username = Prompt.ask("[green][*] [cyan]Enter your email or username")
    password = getpass("[*] Enter your password: ")
    driver = webdriver.Chrome("C:\\Users\\Jencent\\.wdm\\drivers\\chromedriver\\win32\\89.0.4389.23\\chromedriver.exe")
    driver.get("https://free.facebook.com/login")
    username_txtbox = driver.find_element_by_id("m_login_email")
    username_txtbox.send_keys(username)
    time.sleep(2)
    password_txtbox = driver.find_element_by_name("pass")
    password_txtbox.send_keys(password)
    time.sleep(2)
    login_btn = driver.find_element_by_name("login")
    login_btn.submit()
    time.sleep(1)
    pprint("[green][+] Login Successfully")
def MESSENGER():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    logo = Panel.fit("[bold blue] Messenger autologin ", border_style="magenta")
    pprint(logo)
    username = Prompt.ask("[green][*] [cyan]Enter your email or username")
    password = getpass("[*] Enter your password: ")
    driver = webdriver.Chrome("C:\\Users\\Jencent\\.wdm\\drivers\\chromedriver\\win32\\89.0.4389.23\\chromedriver.exe")
    driver.get("https://www.messenger.com/login")
    username_txtbox = driver.find_element_by_id("email")
    username_txtbox.send_keys(username)
    time.sleep(2)
    password_txtbox = driver.find_element_by_id("pass")
    password_txtbox.send_keys(password)
    time.sleep(2)
    login_btn = driver.find_element_by_id("loginbutton")
    login_btn.submit()
    pprint("[green][+] Login Successfully")
def GITHUB():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    logo = Panel.fit("[bold blue] GitHub autologin ", border_style="green")
    pprint(logo)
    username = Prompt.ask("[green][*] [cyan]Enter your email or username")
    password = getpass("[*] Enter your password: ")
    driver = webdriver.Chrome("C:\\Users\\Jencent\\.wdm\\drivers\\chromedriver\\win32\\89.0.4389.23\\chromedriver.exe")
    driver.get("https://github.com/login")
    username_txtbox = driver.find_element_by_id("login_field")
    username_txtbox.send_keys(username)
    time.sleep(2)
    password_txtbox = driver.find_element_by_id("password")
    password_txtbox.send_keys(password)
    time.sleep(2)
    login_btn = driver.find_element_by_name("commit")
    login_btn.submit()
    pprint("[green][+] Login Successfully")
def BINARYCONVERTER():
    a_string = input("Enter a String : ")
    a_byte_array = bytearray(a_string, "utf8")
    for byte in a_byte_array:
        binary_representation = bin(byte)
        print(binary_representation)
def SCREENRECORD():
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    file_name = f'{time_stamp}.mp4'
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))
    while True:
        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow("Secret Capture", img_final)
        captured_video.write(img_final)
        if cv2.waitKey(10) == ord("q"):
            break
def MP3():
    chromedir= 'C:/Program Files/Microsoft/Edge/Application/msedge.exe %s'
    mp3file = input("mp3 file: ")
    webbrowser.get(chromedir).open(mp3file)
def MP4():
    chromedir= 'C:/Program Files/Microsoft/Edge/Application/msedge.exe %s'
    mp4file = input("mp4 file: ")
    webbrowser.get(chromedir).open(mp4file)
def TEXT2SPEECH():
    say = input('Enter a message: ')
    print("Select language")
    print(googletrans.LANGUAGES)
    languages = input('Choose a language: ')
    translator = googletrans.Translator()
    translated = translator.translate(say, dest=languages)
    print(translated.text)
def SPEECH2SPEECH():
    all_languages = googletrans.LANGUAGES
    print(all_languages)
    my_lang = str(input("Your language: "))
    her_lang = str(input("His/Her language: "))
    translator = googletrans.Translator()
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Speak Now")
            voice = recognizer.listen(source)
            text = recognizer.recognize_google(voice, language=my_lang)
            print(text)
    except:
        input("Press Enter to continue.")
        pass
    translated = translator.translate(text, dest=her_lang)
    print(translated.text)
    converted = gtts.gTTS(translated.text, lang=her_lang)
    converted.save('japanese.mp3')
    playsound.playsound("japanese.mp3")

try:
    while True:
        # basic commands
        user = input("$:-> ")
        if user == "help":
            HELP()
        elif user == 'help --secret':
            HELPSECRET()
        elif user == "exit":
            EXIT()
        elif user == "calculator":
            CALCULATOR()
        elif user == "calendar":
            CALENDAR()
        elif user == "notepad":
            NOTEPAD()
        elif user == 'cmd':
            CMD()
        elif user == 'powershell':
            POWERSHELL()
        elif user == 'bash':
            BASH()
        elif user == "time":
            TIME()
        elif user == "goto":
            GOTO()
        elif user == "leap":
            LEAPYEAR()
        elif user == "makedir":
            MKDIR()
        elif user == "deldir":
            DDIR()
        elif user == "makeTXT":
            WTXT()
        elif user == "readTXT":
            RTXT()
        elif user == "addTXT":
            ATXT()
        elif user == "delTXT":
            DTXT()
        elif user == "pwd":
            PWD()
        elif user == "clear":
            CLEAR()
        
        # advance commands
        elif user == "ping":
            PING()
        elif user == "osk":
            ONSCREENKEYBOARD()
        elif user == "ai --freefb":
            FREEFB()
        elif user == "ai --messenger":
            MESSENGER()
        elif user == "ai --github":
            GITHUB()
        elif user == "sc -record":
            SCREENRECORD()
        elif user == "con. string":
            BINARYCONVERTER()
        elif user == "Chrome -mp3":
            MP3()
        elif user == "Chrome -mp4":
            MP4()
        elif user == "tts":
            TEXT2SPEECH()
        elif user == "sts":
            SPEECH2SPEECH()
        else:
            print("Use help command")
except (KeyboardInterrupt, IndexError, 
        ConnectionError, Exception, 
        TypeError) as e:
    print("Exiting program...")
    input("Press Enter to continue.")
    print(e)
