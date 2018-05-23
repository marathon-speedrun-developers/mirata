//A1Bootstrap: Guided Installation of AlephOne on Linux Systems
//Version 0.1 by tbcr/Brandon Clark in ANSI C
//This application was compiled with gcc on Fedora 27/28
//Released under the GNU General Public License v3
//Please file any package problems as an issue on the Github.
//You can also discuss about this program in #chocothon on freenode, since this program will later be implemented for that as well
//
//This program downloads proprietary freeware files that are the copyright of Bungie LLC.

/*Preface

This idea for this program came from the last time I personally tried setting up AlephOne on my speedrunning laptop. The process for installing the application can get convoluted sometimes (I particulary had problems with the compilation setp)

To answer the question as to why I am not just making this as a bash script; I know more C than I do bash scripting. I do plan on making a bash script version later when I get a better hang of bash scripting.

-----------------------------------------
Version 0.1 Changelog:

*Added Fedora,Ubuntu,Arch,Gentoo,Sabayon support
*Added option to program to pause for manual installation of dependencies(this is 
 good for distros such as slackware)
*Fixed system calls to actually work on Linux systems
*Added Neat-o colors

*/


//The Library Inclusion(and all that jazz)
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

//Neat-o Colors
#define CYAN "\x1B[36m"
#define BLUE "\x1B[34m"
#define RESET "\x1B[0m"

//This is a dumb variable that is only used for system calls
int dumb;

//These are global variables dealing with linux distribution and source code version
int distro;
int stab;
int pkg;
/*This "flag" helps the program in determining if the user has selected an option
that requires compilation */
int compile_flag;

//Functions for the current operating systems that are supported.
void fedora());
void ubuntu();
void arch();
void gentoo();
void sabayon();
void suse();
void source();

void introduction();
int distroSelect();
int stableMaster();
void compile();
void sourcecode(int);

int main()
{
	//Option Variables
	
	
	
	introduction();

distro:
	distroSelect();

prompt:

	if(distro> 0 && distro < 8)
	{
		stableMaster();
	}
	else if(distro == 8)
	{
		printf(CYAN "MANUAL DEPENDENCY RESOLUTION SELECTED\n" RESET);
		printf("We are assuming you have or will install these\n");
		scanf("%d",dumb);
		compile_flag = 1;

		printf("Skipping to Step 2 ");
		dumb = system("sleep 2");
		
		
	}
	else
	{
		printf("ERROR!!!! RELOADING PROMPT");
		dumb = system("sleep 3");
		dumb = system("clear");
		goto prompt;
	}

	dumb = system("sleep 1");

	printf("Starting installation in ");

	dumb = system("sleep 1");

	for(int i = 5,i > 0,i--)
	{
		print("%d",i);
	}

	switch(distro)
	{
		case 1:
			fedora();
			break;
		case 2:
			debian();
			break;
		case 3:
			arch();
			break;
		case 4:
			gentoo();
			break;
		case 5:
			sabayon();
			break;
		case 6:
			suse();
			break;
		case 7:
			sourcecode();
			break;
		default:
			break;
	}


}

void gentoo()
{

	printf("Step 1.G)Gentoo A1 Installation\n");
	dumb = system("sleep 1");
	printf("You have the easiest installation of the bunch!\n\n");

	dumb = system("sleep 2")
	dumb = system("sudo emerge alephone &> /dev/null");

	printf(CYAN "DONE! " RESET);
	printf("Moving to Game Downloads\n");

	return 0;
}

void debian()
{
//DEPENDENCY INSTALLATION
	if(stab == 1)
	{
		//Packages provided by playdeb can allow
		printf("Before we begin: It should be noted that there is a package on playdeb.\n");
		printf("This version is 20150620 (the current stable as of May 11, 2018\n\n");
		printf("This will involve adding the playdeb repository into your repo list\n\n");
		printf("THIS IS FOR UBUNTU. IF USING DEBIAN, PLEASE CONTINUE BY ENTERING 2")
		
		printf("Would you like to install this package:\n");
		printf("1)Yes\n");
		printf("2)No\n\n");

		printf("Selection: ");
		scanf("%d",pkg);

		if(pkg == 1)
		{
			dumb = system("deb http://archive.getdeb.net/ubuntu zesty-getdeb games");
			dumb = system("")
		}




		printf("Step 1. Prerequisites-----> ");
		dumb = system("sudo apt install git libboost-all-dev libsdl2-dev libsdl2-image-dev libsdl2-net-dev libsdl2-ttf-dev libspeexdsp-dev libzzip-dev libavcodec-dev libavformat-dev libavutil-dev libswscale-dev &> /dev/null");
	}
	else if(stab == 2)
	{
		printf("Step 1. Prerequisites-----> ");
		dumb = system("sudo apt install git libboost-all-dev libsdl1.2-dev libsdl-image1.2-dev libsdl-net1.2-dev libsdl-ttf1.2-dev libspeexdsp-dev libzzip-dev libavcodec-dev libavformat-dev libavutil-dev libswscale-dev &> /dev/null");

	}

	printf("DONE!\n");
	dumb = system("sleep 3");

	return 0;
}

void fedora()
{

}

void suse()
{
	dumb = system("clear");

	if(stab == 2)
	{
	printf("Please select version of openSUSE :\n");
	printf("1)Tumbleweed\n");
	printf("2)Leap 42.3\n\n");


	}


	if
	
	dumb = system("wget ")
}

//User selects which distro out of the bunch they run.
void distroSelect()
{

	printf("Please Select from the Following Options\n");
	printf("----------------------------------------\n");

	printf("1)Fedora\n");
	printf("2)Debian/Ubuntu\n");
	printf("3)Arch\n");
	printf("4)Gentoo\n");
	printf("5)Sabayon\n");
	printf("6)SUSE\n");
	printf("7)Skip[Use if Preq already installed]\n\n");

	printf("Selection: ");
	scanf("%d",distro);

	return 0;
}

int stableMaster()
{
	printf("Do you want to install the development or stable version: \n");
    printf("1)Development\n");
    printf("2)Stable\n");

    printf("Selection: ");
	scanf("%d", stab);

	return 0;
}

void gameSelect()
{

	int marathon;
	int marathon2;
	int infinity;

	printf("Would you like to download Marathon 1? \n");
	printf("1)Yes\n");
	printf("2)No\n");

	printf("Selection: ");
	scanf("%d",marathon);

	printf("Would you like to download Marathon 2:Durandal? \n");
	printf("1)Yes\n");
	printf("2)No\n");

	printf("Selection: ");
	scanf("%d",marathon2);

	printf("Would you like to download Marathon Infinity? \n");
	printf("1)Yes\n");
	printf("2)No\n");

	printf"Selection: ");
	scanf("%d",infinity);

	dumb = system("mkdir ~/scenarios;cd ~/scenarios");

	if(marathon == 1)
	{
		dumb = system("wget https://github.com/Aleph-One-Marathon/alephone/releases/download/release-20150620/Marathon-20150620-Data.zip");
        	dumb = system("unzip Marathon-20150620-Data.zip &> /dev/null");
	}

	if(marathon2 == 1)
	{
		dumb = system("wget https://github.com/Aleph-One-Marathon/alephone/releases/download/release-20150620/Marathon2-20150620-Data.zip");
		dumb = system("unzip Marathon2-20150620-Data.zip &> /dev/null")
	}

	if(infinity == 1)
	{

		dumb = system("wget https://github.com/Aleph-One-Marathon/alephone/releases/download/release-20150620/Marathon2-20150620-Data.zip");
		dumb = system("unzip Marathon2-Data.zip &> /dev/null");

    }

    printf("Step 4)Scenario Download: DONE\n");
    printf("Be sure to put future scenarios you download in ~/scenarios\n");

    return 0;

}

void sourcecode();
{

	printf("Step 2)Downloading Sourcecode-----> ");
	
	if(stab == 1)
	{
		//This clones the current Alephone master branch to ~/alephone
		dumb = system("cd;git clone https://github.com/Aleph-One-Marathon/alephone.git &> /dev/null; cd alephone");
	}
	else
	{
		//this downloads the current stable build and extracts it in ~/alephone
		dumb = system("cd;mkdir alephone; cd alephone");
		dumb = system("wget https://github.com/Aleph-One-Marathon/alephone/releases/download/release-20150620/AlephOne-20150620.tar.bz2 &> /dev/null");
		dumb = system("tar -xjf AlephOne-20150620.tar.bz2 --strip 1");
	}
	printf("DONE!\n");
	dumb = system("sleep 3");

	return 0;
}

void introduction()
{
	printf("AlephOne Bootstrap: Guided Install\n");
	printf("version 0.1\n");

	printf("Please post installation problems on github\n");
	dumb = system("sleep 3");

	printf("Loading Initial Options\n");
	dumb = system("sleep 1");
	dumb = system("clear");
	
	return 0;
}
	
