import subprocess

from typing import List


def load_phrases(filename: str) -> List[str]:
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def cowsay(phrase: str) -> str:
    proc = subprocess.run(['cowsay', phrase], capture_output=True)
    return proc.stdout.decode('utf-8')
