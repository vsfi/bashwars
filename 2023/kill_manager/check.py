import random
import time
from multiprocessing import Process
import subprocess

questions_list = ["Ну как там?\n", "Че как дела?\n", "Сроки сможешь сказать?\n", "Обозначь ситуацию\n", "Что по задаче?\n",
                  "Коллеги, актуализируйте статусы по задачам\n", "Чё там?\n", "Ну как там?!\n", "Прошу решить в приоритете\n"]


def drop_ssh():
    stdout = open("/stdout.log", "w")
    stdout.write("Работяг то за что? ")
    stdout.close()
    kill_sh = subprocess.check_output(['sh', '-c', "killall -9 sh"])


def loop_spam():
    while 1:
        stdout = open("/stdout.log", "w")
        stdout.write(random.choice(questions_list))
        stdout.close()
        time.sleep(120)


def loop_check():
    taskComplete = False
    while 1:
        checkKillAll = "ps aux | grep -v grep | grep py_files| awk '{print $1}'"
        outputCheckKillAll = subprocess.check_output(
            ['sh', '-c', checkKillAll])
        if outputCheckKillAll.decode('utf-8').strip() == "":
            drop_ssh()

        checkManagerKillCommand = "ps aux | grep -v grep | grep manager | grep -v check | wc -l"  # 0
        outputcheckManagerKillCommand = subprocess.check_output(
            ['sh', '-c', checkManagerKillCommand])
        checkRabotyagaKillCommand = "ps aux | grep -v grep | grep rabotyaga | grep -v check | wc -l"  # 10
        outputcheckRabotyagaKillCommand = subprocess.check_output(
            ['sh', '-c', checkRabotyagaKillCommand])

        if outputcheckManagerKillCommand.decode('utf-8').strip() == "0" and outputcheckRabotyagaKillCommand.decode('utf-8').strip() == "10" and taskComplete == False:
            stdout = open("/stdout.log", "w")
            stdout.write("Покажи коллегам флаг: Ну че, успел таски написать?")
            stdout.close()
            taskComplete = True
        time.sleep(2)


def main():
    Process(target=loop_spam).start()
    Process(target=loop_check).start()


if __name__ == '__main__':
    main()
