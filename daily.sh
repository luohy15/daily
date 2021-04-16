set -e
dir=$(date +%Y/%m/%d)
case $1 in
add)
    if [[ ! -n $(find . -name "test_$2.py") ]]
    then
        mkdir -p $dir
        echo "add $dir/$2-$3"
        if [[ -n $4 ]]
        then
            cp -r template/$4 $dir/$2-$3
        else
            cp -r template/python $dir/$2-$3
        fi
        mv $dir/$2-$3/main.py $dir/$2-$3/main_$2.py
        mv $dir/$2-$3/test.py $dir/$2-$3/test_$2.py
        sed -i'.original' -e "s/main/main_$2/g" $dir/$2-$3/test_$2.py
        rm $dir/$2-$3/test_$2.py.original
    else
        echo "$dir/$2-$3 exists"
    fi
    ;;
move)
    echo "move $2 $3 $4"
    dir=$(dirname $(find . -name "test_$2.py"))
    mv $dir/main_$2.py $dir/main_$3.py
    sed -i'.original' -e "s/main_$2/main_$3/g" $dir/test_$2.py
    rm $dir/test_$2.py.original
    mv $dir/test_$2.py $dir/test_$3.py
    mv $dir $(dirname $dir)/$3-$4
    ;;
remove)
    echo "remove $dir/$2-*"
    find . -name "test_$2.py" | xargs dirname | xargs rm -rf
    ;;
test)
    pytest -v $(find . -name "test_$2.py")
    ;;
*)
    echo "Usage:"
    echo "  ./daily.sh add [id] [name]"
    echo "  ./daily.sh move [id(old)] [id(new)] [name(new)]"
    echo "  ./daily.sh remove [id]"
    echo "  ./daily.sh test [id]"
esac
