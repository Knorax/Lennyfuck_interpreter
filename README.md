# Hi there ( ͡° ͜ʖ ͡°)

Hi! This project is a simple interpreter for the ( ͡° ͜ʖ ͡°)fuck esoteric language by ivancr72. My goal is to learn how to make interpreters and, eventually, compilers for some other esoteric language, because we obviously need it ( ͡~ ͜ʖ ͡°).
What to keep it mind during this project : it's all for that handsome Lenny.

## Opcodes

| Lenny Command | Brainfuck+3 Command | Description |
| --- | --- | --- |
|( ͡° ͜ʖ ͡°) | + | Increment the memory cell under the pointer |
|(> ͜ʖ<) | - | Decrement the memory cell under the pointer |
|(♥ ͜ʖ♥) | . | Output the character signified by the cell at the pointer |
|ᕙ( ͡° ͜ʖ ͡°)ᕗ | , | Input a character and store it in the cell at the pointer |
|(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ.* | < | Move the pointer to the left |
|ᕦ( ͡°ヮ ͡°)ᕥ | > | Move the pointer to the right |
|ᕦ( ͡° ͜ʖ ͡°)ᕥ | ^ | Move the pointer up |
|( ͡°╭͜ʖ╮ ͡°) | v | Move the pointer down |
|ಠ_ಠ | x | Exit program. |
|( ͡°( | [ | Jump past the matching ] if the cell under the pointer is 0 |
|) ͡°) | ] | Jump back to the matching [ if the cell under the pointer is nonzero |

## Files

For now, there is only a python interpreter pending.

## References
Description of the language :[https://esolangs.org/wiki/(_%CD%A1%C2%B0_%CD%9C%CA%96_%CD%A1%C2%B0)fuck](https://esolangs.org/wiki/(_%CD%A1%C2%B0_%CD%9C%CA%96_%CD%A1%C2%B0)fuck)


