from argparse import ArgumentParser
from multiprocessing import Process
import os
import subprocess

from engine.engine import Game

#P1F = 'python_skeleton/birai.py'
#p2s = ['player.py']
#P1F = 'python_skeleton/bipot.py'
#p2s = ['player.py', 'birai.py']
#threesome = ['bipot','player','birai']
robin = ['birai','ogcp']
pairings = []

for i, x in enumerate(robin):
    for y in robin[:i]:
        pairings.append((y,x))

#p2s = list(filter(lambda x: x.endswith('.py'), os.listdir('python_skeleton/')))+['player.py']*2

NUM_CORES = 20
NUM_GAMES = 15
PROCESS_MULT = 20
NUM_ROUNDS = 1000

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--docker", action="store_true", help="Running in containers")
    return parser.parse_args()


def run_game_engine(i, p1, p2):
    """
    Runs the game engine process.
    """
    i1 = 54000 + i * 2
    i2 = i1 + 1
    player1_process = subprocess.Popen(
        ["pypy3", p1, "--port", str(i1)]
    )
    player2_process = subprocess.Popen(
        ["pypy3", p2, "--port", str(i2)]
    )

    os.environ['PLAYER_1_NAME'] = p1[16:-3]
    os.environ['PLAYER_2_NAME'] = p2[16:-3]
    os.environ['PLAYER_1_DNS'] = f'localhost:{i1}'
    os.environ['PLAYER_2_DNS'] = f'localhost:{i2}'

    engine_process = subprocess.Popen(
        ["pypy3", 'enginerun.py']
    )

    def continuation():
        engine_process.wait()
        player1_process.terminate()
        player2_process.terminate()

    return continuation

if __name__ == "__main__":
    args = parse_args()

    processes = []
    os.environ['NUM_GAMES'] = str(NUM_GAMES)
    os.environ['NUM_ROUNDS'] = str(NUM_ROUNDS)

    #p1 = P1F
    i = 0
    ended = 0
    #for p2 in p2s:
    for p1, p2 in pairings:
        for _ in range(PROCESS_MULT):
            #game_engine_process = Process(target=run_game_engine, args=(i,))
            #game_engine_process.start()
            processes.append(run_game_engine(i, f'python_skeleton/{p1}.py', f'python_skeleton/{p2}.py'))
            if len(processes) > NUM_CORES + ended:
                processes[ended]()
                ended += 1
            i += 1

    print('number of processes:',i)

    for p in processes[ended:]:
        p()
