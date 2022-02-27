#!/bin/bash

clone() {
	cd ../;
	echo $GITTOKEN;
	git clone https://github.com/MrFanCode/$1.git
}

clone $1



