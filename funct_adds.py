""" FUNCTIONALITY ADDITIONS """


from termcolor import colored
from pyfiglet import Figlet
from os import system
from os import name as sys_name
import time


def clear_screen():
    """ Clear the screen in depends on operating system (Windows, Linux or iOS).
        It was copied from internet,  I will find out how it works in future (_=system is unknown for me) :)"""
    if sys_name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


def show_info(info):
    if info == "white" or info == "black":
        print('')
    else:
        print(colored(info, "red"))


def whose_turn(info):
    if info == "white":
        return "black"
    else:
        return "white"


def start_game_screen():
    """ Show start screen. Use pyfigled and termcolor modules"""
    
    f = Figlet(font="standard")
    print(colored(f.renderText("              CHECKERS"), "green"))
    time.sleep(1)  # Used time module for program delay
    f = Figlet(font="doom")
    print(colored(f.renderText("May The  Best Win"), "red"))
    time.sleep(3)


def who_is_winner(bl_paw_nm, whi_paw_nm):
    f = Figlet(font="small")
    if len(bl_paw_nm) == 0:
        print(colored(f.renderText("The Winner are Whites"), "magenta"))
    elif len(whi_paw_nm) == 0:
        print(colored(f.renderText("The Winner are Blacks"), "magenta"))
    else:
        print(colored(f.renderText("    Nobody Wins"), "magenta"))


def end_game_screen(bl_paw_nm, whi_paw_nm):
    time.sleep(2)
    clear_screen()
    start_game_screen()
    who_is_winner(bl_paw_nm, whi_paw_nm)
    answer = input(colored("       Do You want play again [Y]es/[N]o ? ", "green"))
    return answer


def goodbye_screen():
    """Shows goodbye screen"""
    
    clear_screen()
    start_game_screen()
    f = Figlet(font="standard")
    print(colored(f.renderText('       GOODBYE!'), "magenta"))
    time.sleep(2)


def choose_players():
    f = Figlet(font="small")
    print(colored(f.renderText("   Choose Opponent: "), "cyan"))
    print(colored(f.renderText("        1.  Human"), "magenta"))
    print(colored(f.renderText("        2.  Computer"), "magenta"))
    second_player = input()
    if second_player == "1":
        return "human"
    elif second_player == "2":
        return "computer"
    time.sleep(1)
    