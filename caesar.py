# feito por: maquinzz
import argparse, sys

def rot(text: str, shift: int, decrypt: bool) -> str:
    s = shift % 26
    if decrypt:
        s = (26 - s) % 26
    out = []
    for ch in text:
        if "A" <= ch <= "Z":
            out.append(chr((ord(ch) - ord("A") + s) % 26 + ord("A")))
        elif "a" <= ch <= "z":
            out.append(chr((ord(ch) - ord("a") + s) % 26 + ord("a")))
        else:
            out.append(ch)
    return "".join(out)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--text", default="")
    p.add_argument("--shift", type=int, default=3)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--encrypt", action="store_true")
    g.add_argument("--decrypt", action="store_true")
    a = p.parse_args()
    if not a.text:
        text = sys.stdin.read()
    else:
        text = a.text
    if a.shift < 0 or a.shift > 25:
        print("bad_shift: use 0-25", file=sys.stderr); sys.exit(1)
    print(rot(text, a.shift, a.decrypt), end="" if text.endswith("\n") else "\n")

if __name__ == "__main__":
    main()
