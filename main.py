#!/usr/bin/env python3
# Sender - entry point

from sender import Sender

def main():
    print("[*] Sender v1.0.0")
    print("[*] Educational tool. Use only for authorized testing.")
    s = Sender()
    s.run()

if __name__ == "__main__":
    main()