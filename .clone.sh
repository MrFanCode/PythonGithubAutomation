#!/bin/bash

clone() {
	cd ../;
	echo Your repo has been cloned into $PWD folder.;
	git clone https://github.com/$2/$1.git
}

clone $1 $2



