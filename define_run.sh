run() {
    if [[ $1 == *.cpp ]]; then
        clear
        output=${1%.*}       
        g++ '-std=c++17' $1 -o $output.out
        echo $output.out
        echo '----------'
        echo ''
        ./$output.out
    else
        echo 'Specify full cpp filename.'
    fi
}