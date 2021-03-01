dir=$(date +%Y/%m/%d)
case $1 in
add)
    if [[ ! -d $dir/$2-$3 ]]
    then
        echo "add $dir/$2-$3"
        cp -r template/python $dir/$2-$3
    else
        echo "$dir/$2-$3 exists"
    fi
    ;;
remove)
    echo "remove $dir/$2-*"
    rm -rf $dir/$2-*
    ;;
test)
    cd $dir/$2-* && python3 main_test.py
    ;;
*)
    echo "Usage:"
    echo "  ./daily.sh add [id] [name]"
    echo "  ./daily.sh remove [id]"
    echo "  ./daily.sh test [id]"
esac
