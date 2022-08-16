for f in *.ui;  
do 
    FILENAME=`basename ${f%%.*}`;
    echo ${FILENAME};
    pyuic5 ${FILENAME}.ui -o ${FILENAME%%.*}.py;
done;
