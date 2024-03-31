from argparse import ArgumentParser
from multiprocessing import Process
import os, sys, subprocess, time

robin = list(filter(lambda x: x.endswith('.py'), os.listdir('python_skeleton/')))
robin = list(map(lambda x: x + '.py',['og', 'birai', 'ogcp', 'j', 'player', 'bipot','pcp','pnp']))

print(robin)

#sys.exit(0)
pairings = []
players = []

for i, x in enumerate(robin):
    players.append(subprocess.Popen(
        ["pypy3", 'python_skeleton/'+x, "--port", str(24000 + i)]
    ))
    for j in range(i):
        pairings.append((j,i))
        #pairings.append((y+'.py',x+'.py'))

#print(pairings)
#sys.exit(0)

#p2s = list(filter(lambda x: x.endswith('.py'), os.listdir('python_skeleton/')))+['player.py']*2

NUM_CORES = 30
NUM_GAMES = 1
PROCESS_MULT = 1
NUM_ROUNDS = 5000

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--docker", action="store_true", help="Running in containers")
    return parser.parse_args()


def run_game_engine(i1, i2):
    """
    Runs the game engine process.
    """
    os.environ['PLAYER_1_NAME'] = robin[i1][:-3]
    os.environ['PLAYER_2_NAME'] = robin[i2][:-3]
    os.environ['PLAYER_1_DNS'] = f'localhost:{24000 + i1}'
    os.environ['PLAYER_2_DNS'] = f'localhost:{24000 + i2}'

    engine_process = subprocess.Popen(
        ["pypy3", 'enginerun.py']
    )

    return engine_process

if __name__ == "__main__":
    args = parse_args()

    processes = set()
    os.environ['NUM_GAMES'] = str(NUM_GAMES)
    os.environ['NUM_ROUNDS'] = str(NUM_ROUNDS)

    #p1 = P1F
    #i = 0
    ended = 0
    #for p2 in p2s:
    for p1, p2 in pairings:
        print('w')
        for _ in range(PROCESS_MULT):
            #game_engine_process = Process(target=run_game_engine, args=(i,))
            #game_engine_process.start()
            processes.add(run_game_engine(p1, p2))#f'python_skeleton/{p1}', f'python_skeleton/{p2}'))
            while len(processes) > NUM_CORES:
                time.sleep(1)
                print(processes)
                print(len(processes))
                for process in processes:
                    if process.poll() is not None:
                        processes.remove(process)
                        break
                print(len(processes))

    print('number of processes left:', len(processes))

    for p in processes:
        p.wait()

    for pl in players:
        pl.terminate()

    print('terminated')
