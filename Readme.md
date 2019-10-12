# CYK

This program is a implementation of the CYK algorithm to obtain if a string belongs to a Context free grammar.

## How to run (NO docker)

To run you only need to run the cyk python file. The program will prompt for the word and the Context Free Grammar in the console:

![Success](./readme/python.png)

## Run with docker

1. First you need to have docker installed in your machine
2. You need to create the docker image, to do this run the command: `docker build -t python-cyk .` you can change the `python-cyk` to whatever you preffer as a name for your image.
![build image](./readme/docker1.png)

3. Then you need to create the container and run it: `docker run -i -t --rm python-cyk`, rember that if you changed the name of the image to change the name also in this command.
4. The docker will start running and the program will prompt for the word and the Context Free Grammar
![run docker](./readme/docker2.png)

## Input

The input of the program is the word to interpret and the Grammar (this grammar must be in **Chomsky Normal Form**) in the next format:

`word production1 production2 ...`

Example:

`aaabbb S->AB|XB T->AB|XB X->AT A->a B->b`

## Output

If the word belongs to the Grammar, then the program will prompt it and print the parse tree.

![Success](./readme/out1.png)

If not, then the program will prompt that it doesn't belong only.

![Fail](./readme/out2.png)
