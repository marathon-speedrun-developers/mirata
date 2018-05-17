# mirata

Mirata is a project for creating both a guided installer for the Aleph One source port AND in the future a launcher for opening scenarios of and based on Bungie's Marathon Trilogy.

# What will this do exactly?
Through various prompts, the installer part of the project will download both the current stable or git master of Aleph One. It will then download the necessary dependencies and attempt to install the code.

In some instances (mainly with certain linux distributions), the installer will ask if the user would like to install a premade package from a package repository. Gentoo and openSUSE are perfect examples.

The installer is currently in idea phase, but would mainly work just like launchers for various DOOM source ports, where all of the scenarios are organized in a list and can be started from the launcher.

# Why is this in ANSI C with system calls?
Two reasons:

1. I can't batch script well atm
2. I thought it would be a good exercise in programming.