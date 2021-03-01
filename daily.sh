dir=$(date +%Y/%m/%d)
case $1 in
add)
    if [[ ! -d $dir/$2-$3 ]]
    then
        echo "add $dir/$2-$3"
        cp -r template/python $dir/$2-$3
        mv $dir/$2-$3/main.py $dir/$2-$3/main_$2.py
        mv $dir/$2-$3/test.py $dir/$2-$3/test_$2.py
        sed -i'.original' -e "s/main/main_$2/g" $dir/$2-$3/test_$2.py
        rm $dir/$2-$3/test_$2.py.original
    else
        echo "$dir/$2-$3 exists"
    fi
    ;;
remove)
    echo "remove $dir/$2-*"
    rm -rf $dir/$2-*
    ;;
test)
    pytest -v $(find . -name "test_$2.py")
    ;;
*)
    echo "Usage:"
    echo "  ./daily.sh add [id] [name]"
    echo "  ./daily.sh remove [id]"
    echo "  ./daily.sh test [id]"
esac
