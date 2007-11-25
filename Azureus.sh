#!/bin/sh

AZUHOME="$HOME/.azureus"

if [ $(arch) == "x86_64" ]; then
	LIBDIR="/usr/lib64"
else
	LIBDIR="/usr/lib"
fi

if [ -f $AZUHOME/pld.config ]; then
	. $AZUHOME/pld.config
else
	if [ ! -e $AZUHOME ]; then
		mkdir $AZUHOME
	fi
	
	UI="swt"
	
	cat > $AZUHOME/pld.config << 'EOF'
# UI options:
# - swt
# - console

UI="swt"

EOF

fi

CLASSPATH="/usr/share/java/swt.jar:/usr/share/java/commons-cli.jar:/usr/share/java/log4j.jar:/usr/share/Azureus/Azureus.jar"

exec java -cp $CLASSPATH -Djava.library.path=$LIBDIR/swt org.gudy.azureus2.ui.common.Main --ui=$UI
