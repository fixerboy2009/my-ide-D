# F-IDE README

## Fixing errors
Getting errors? Run install-requirements.bat or see below for fixing other errors.

If your getting a error from the filesystem, check the file paths in the script and change them to the correct paths on your system.

## Supported languages
1. Python (mode py OR mode python)
2. Lua (BETA) (mode lua)
3. Batch (mode bat)

## Other Modes
1. File (mode file)
   * Type file path (FULL PATH)
   * Prints file data.

2. Web/HTTP (DISABLED) (mode web)
   * Currently disabled in V1, however will be fixed if I feel like it.
   * Prints the raw data from the wensite requested

## Q/A
1. Q: How do I change the default mode?
2. A: Edit the dm file in defaults folder.
           
3. Q: Why does the Lua language not work?
4. A: The Lua mode is current bugged, as I am still figuring out how to execute files with the .lua extension inside of python.

## Varibles in executing code
1. wait(float sec)
   * Pauses the script for the time specified

## How to run
Just run the python file in the command line!

## Future Updates
1. Adding colored text
2. Fixing audio-preset mode
