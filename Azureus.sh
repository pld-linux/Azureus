#!/bin/sh

if [ `arch` == "x86_64" ]; then
	LIBDIR="/usr/lib64"
else
	LIBDIR="/usr/lib"
fi

AZURDIR="$LIBDIR/Azureus"

CLASSPATH="/usr/share/java/swt.jar:/usr/share/java/commons-cli.jar:/usr/share/java/log4j.jar:$AZURDIR/Azureus.jar"

java -cp $CLASSPATH -Djava.library.path=$LIBDIR/swt org.gudy.azureus2.ui.swt.Main

