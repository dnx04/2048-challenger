#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' Help the user achieve a high score in a real game of 2048 by using a move searcher. '''

from __future__ import print_function
import ctypes
import time
import os

for suffix in ['so', 'dll', 'dylib']:
    dllfn = 'bin/2048.' + suffix
    ailib = ctypes.CDLL(dllfn)

ailib.init_tables()

ailib.find_best_move.argtypes = [ctypes.c_uint64]
ailib.score_toplevel_move.argtypes = [ctypes.c_uint64, ctypes.c_int]
ailib.score_toplevel_move.restype = ctypes.c_float

def to_c_board(m):
    board = 0
    i = 0
    for row in m:
        for c in row:
            board |= int(c) << (4*i)
            i += 1
    return board

from multiprocessing.pool import ThreadPool
pool = ThreadPool(4)
def score_toplevel_move(args):
    return ailib.score_toplevel_move(*args)

def find_best_move(m):
    board = to_c_board(m)

    scores = pool.map(score_toplevel_move, [(board, move) for move in range(4)])
    bestmove, bestscore = max(enumerate(scores), key=lambda x:x[1])
    if bestscore == 0:
        return -1
    return bestmove

def movename(move):
    return ['up', 'down', 'left', 'right'][move]

def play_game(gamectrl):
    moveno = 0
    start = time.time()
    while 1:
        state = gamectrl.get_status()
        if state == 'ended':
            break
        elif state == 'won':
            time.sleep(0.75)
            gamectrl.continue_game()

        moveno += 1
        board = gamectrl.get_board()
        move = find_best_move(board)
        if move < 0:
            break
        gamectrl.execute_move(move)

def main():
    from chromectrl import ChromeDebuggerControl
    port = 32768
    ctrl = ChromeDebuggerControl(port)

    from gamectrl import Hybrid2048Control
    gamectrl = Hybrid2048Control(ctrl)

    if gamectrl.get_status() == 'ended':
        gamectrl.restart_game()

    play_game(gamectrl)

if __name__ == '__main__':
    exit(main())
