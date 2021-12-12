run() {
    if [[ $1 == *.cpp ]]; then
        clear
        output=${1%.*}
        g++ '-std=c++17' $1 -o $output.out
        echo $output.out
        echo '-----------'
        echo ''
        ./$output.out
    else
        if [[ $1 == *.py ]]; then
            clear
            output=${1%.*}
            echo $output.py
            echo '-----------'
            echo ''
            python3 $1
            echo ''
        else
            echo 'Specify full filename.'
        fi
    fi
}