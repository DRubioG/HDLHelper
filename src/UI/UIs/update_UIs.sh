for f in *.ui;  
do 
    FILENAME=`basename ${f%%.*}`;
    echo ${FILENAME};
    pyside6-uic ${FILENAME}.ui -o ../${FILENAME%%.*}.py;
done;

exit