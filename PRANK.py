import pygame
import pyttsx3
import speech_recognition as sr

def stopwatch():
    c_time = pygame.time.get_ticks()
    e_time = c_time - s_time
    secs = int((e_time / 1000) % 60)
    mins = int((e_time / (1000 * 60)) % 60)
    font = pygame.font.SysFont('Calibri', 20, True, False)
    text = font.render("{:02d}:{:02d}".format(mins, secs), True, WHITE)
    screen.blit(text, (175, 180))
    pygame.display.update()

def pg0():
    screen.fill(WHITE)
    pygame.draw.ellipse(screen, GREEN, [112.5, 237.5, 175, 175], )
    font = pygame.font.SysFont('Calibri', 40, True, False)
    text = font.render("PRANK", True, WHITE)
    screen.blit(text, [128.5, 303])
    pygame.display.update()
    pygame.time.delay(1000)

def pg1():
    background_image = pygame.image.load("home_background.png")
    background_image = pygame.transform.scale(background_image, (400, 650))

    screen.blit(background_image, (0, 0))
    pygame.display.update()
def pg2():
    call_screen = pygame.image.load("call_background.png")
    call_screen = pygame.transform.scale(call_screen, (400, 650))
    screen.blit(call_screen, (0, 0))

    font = pygame.font.SysFont('Calibri', 50, True, False)
    text = font.render(whoCall, True, WHITE)
    screen.blit(text, loc)
    pygame.display.update()

def pg3():
    rest_screen = pygame.image.load("rest_background.png")
    rest_screen = pygame.transform.scale(rest_screen, (400, 650))
    screen.blit(rest_screen, (0, 0))
    font = pygame.font.SysFont('Calibri', 20, True, False)
    text = font.render(user_text, True, GREY)
    screen.blit(text, (43, 206))
def pg4():
    school_screen = pygame.image.load("school_background.png")
    school_screen = pygame.transform.scale(school_screen, (400, 650))
    screen.blit(school_screen, (0, 0))
    font = pygame.font.SysFont('Calibri', 20, True, False)
    text = font.render(user_text, True, GREY)
    screen.blit(text, (43, 206))
def pg5():
    company_screen = pygame.image.load("company_background.png")
    company_screen = pygame.transform.scale(company_screen, (400, 650))
    screen.blit(company_screen, (0, 0))
    font = pygame.font.SysFont('Calibri', 20, True, False)
    text = font.render(user_text, True, GREY)
    screen.blit(text, (43, 206))
def pg6():
    store_screen = pygame.image.load("store_background.png")
    store_screen = pygame.transform.scale(store_screen, (400, 650))
    screen.blit(store_screen, (0, 0))
    font = pygame.font.SysFont('Calibri', 20, True, False)
    text = font.render(user_text, True, GREY)
    screen.blit(text, (43, 206))
def pg7():
    emer_screen = pygame.image.load("emergency_background.png")
    emer_screen = pygame.transform.scale(emer_screen, (400, 650))
    screen.blit(emer_screen, (0, 0))
def pg8():
    impo_screen = pygame.image.load("important_background.png")
    impo_screen = pygame.transform.scale(impo_screen, (400, 650))
    screen.blit(impo_screen, (0, 0))



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (65, 198, 35)
RED = (255, 0, 0)
GREY = (71, 71, 71)

pygame.init()
engine = pyttsx3.init()

engine.setProperty('rate', engine.getProperty('rate') // 1.2)

r = sr.Recognizer()

size = (400, 650)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PRANK")
clock = pygame.time.Clock()

done = False

user_text = ""
message = ""
response = ""
message_spoken = False
page = 0
canPlay = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if page == 1:
                if pos[1]>80 and pos[0]>50 and pos[1]<230 and pos[0] <350:
                    page = 2
                    whoCall = "911"
                    loc = [160, 110]

                    message = "911, what is your emergency?"
                    response = "help is on the way"
                    s_time = pygame.time.get_ticks()

                elif pos[1]>250 and pos[1]<330 and pos[0]>50 and pos[0]<120:
                    page = 3
                    user_text = ""
                elif pos[1]>250 and pos[1]<330 and pos[0]>130 and pos[0]<200:
                    page = 4
                    user_text = ""
                elif pos[1]>250 and pos[1]<330 and pos[0]>210 and pos[0]<280:
                    page = 5
                    user_text = ""
                elif pos[1] > 250 and pos[1] < 330 and pos[0] > 285 and pos[0] < 350:
                    page = 6
                    user_text = ""

                elif pos[1] > 350 and pos[1] < 460 and pos[0] > 50 and pos[0] < 350:
                    page = 7
                elif pos[1] > 480 and pos[1] < 590 and pos[0] > 50 and pos[0] < 350:
                    page = 8

            elif page == 2:
                if pos[1] > 500 and pos[0] > 170 and pos[1] < 560 and pos[0] < 230:
                    page = 1
                    user_text = ""
                    canPlay = True

            elif page == 3:
                if pos[1] > 550 and pos[1] < 590 and pos[0] > 270 and pos[0] < 350:
                    page = 1
                    user_text = ""
                elif pos[1] > 280 and pos[1] < 350 and pos[0] > 40 and pos[0] < 210:
                    page = 2
                    whoCall = "Restaurant"
                    loc = [70, 110]
                    s_time = pygame.time.get_ticks()
                    if len(user_text) > 0:
                        message = "Hello welcome to " + user_text + " what can I get for you today?"
                    else:
                        message = "Hello welcome to our restaurant. What can I get for you today?"
                    response = "alright ill get that for you"
            elif page == 4:
                if pos[1] > 550 and pos[1] < 590 and pos[0] > 270 and pos[0] < 350:
                    page = 1
                    user_text = ""
                elif pos[1] > 280 and pos[1] < 350 and pos[0] > 40 and pos[0] < 210:
                    page = 2
                    whoCall = "School"
                    loc = [120, 110]
                    s_time = pygame.time.get_ticks()
                    if len(user_text) > 0:
                        message = "Hello welcome to " + user_text + " what can I do for you today?"
                    else:
                        message = "Hello welcome to our school. What can I do for you today?"
                    response = "we can help you with that"
            elif page == 5:
                if pos[1] > 550 and pos[1] < 590 and pos[0] > 270 and pos[0] < 350:
                    page = 1
                    user_text = ""
                elif pos[1] > 280 and pos[1] < 350 and pos[0] > 40 and pos[0] < 210:
                    page = 2
                    whoCall = "Company"
                    loc = [90, 110]
                    s_time = pygame.time.get_ticks()
                    if len(user_text) > 0:
                        message = "Hello welcome to " + user_text + " what can I get for you today?"
                    else:
                        message = "Hello welcome to our company. What can I get for you today?"
                    response = "we can help you with that"
            elif page == 6:
                if pos[1] > 550 and pos[1] < 590 and pos[0] > 270 and pos[0] < 350:
                    page = 1
                    user_text = ""
                elif pos[1] > 280 and pos[1] < 350 and pos[0] > 40 and pos[0] < 210:
                    page = 2
                    whoCall = "Store"
                    loc = [135, 110]
                    s_time = pygame.time.get_ticks()
                    if len(user_text) > 0:
                        message = "Hello welcome to " + user_text + " what can I get for you today?"
                    else:
                        message = "Hello welcome to our store. What can I help you with today?"
                    response = "we can help you with that"

            elif page == 7 or page == 8:
                if pos[1] > 550 and pos[1] < 590 and pos[0] > 270 and pos[0] < 350:
                    page = 1

        if page == 3 or page == 4 or page == 5 or page == 6:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.unicode.isprintable():
                    # Add printable characters to the user input string
                    user_text += event.unicode

    # Logo Page
    if page == 0:
        pg0()
        page = 1

    # Home
    if page == 1:
        pg1()

    # Call Screen

    if page == 2:
        pg2()

        if canPlay:
            engine.say(message)
            engine.runAndWait()
            canPlay = False

            with sr.Microphone() as source:
                # adjust for ambient noise
                r.adjust_for_ambient_noise(source)
                # listen for audio input from the user
                audio = r.listen(source)
                engine.say(response)
                engine.runAndWait()
        done = False

    # Restaurant
    elif page == 3:
        pg3()

    # School
    elif page == 4:
        pg4()

    # Company
    elif page == 5:
        pg5()

    # Store
    elif page == 6:
        pg6()

    # Emergency
    elif page == 7:
        pg7()

    # Important
    elif page == 8:
        pg8()

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
