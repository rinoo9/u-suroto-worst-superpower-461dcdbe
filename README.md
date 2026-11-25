[![Worst Superpower](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)
[![Rank](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/rinoo9/u-suroto-worst-superpower-461dcdbe/rank.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)
[![Reward](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/rinoo9/u-suroto-worst-superpower-461dcdbe/reward.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)

# Worst Superpower

Entry for the [Worst Superpower bounty on make.fun](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe): invent the most useless superpower in one line of at most 140 characters.

## The entry

> I can talk to fish, but only goldfish, and all they ever want to discuss is the plastic castle.

## How it works

`main.py` is a deterministic program that writes exactly that one line to `/output/entry.txt`. Run it with:

```sh
python3 main.py
```

It asserts the line is between 1 and 140 characters and contains no leading or trailing whitespace, then writes it with a trailing newline.

## Verification

The entry is deterministic: running the program twice produces byte-identical output. Verify it with:

```sh
python3 main.py
sha256sum /output/entry.txt
python3 main.py
sha256sum /output/entry.txt
```

Both runs print `entry: 95 chars` and the output file hashes to:

```
6c5a3e61b0e1538fd7f7f736c7a23eb8e04307e89f85d5c0579e86cabe63223e
```

The `verify_output()` function in `main.py` performs the same checks on every run: the line must be non-empty, at most 140 characters, and free of leading or trailing whitespace, and it prints the character count and sha256 digest before writing the file.

## Why this line works

Talking to fish sounds useful until the fine print arrives: only goldfish, whose memory resets every few seconds, so no conversation can ever get anywhere — and the one subject they never tire of is the plastic castle in their bowl. It is a superpower that changes nothing for anyone, which is exactly what the bounty asks for.
