run() {
    #do things with parameters like $1 such as
    if [[ $1 == *.cpp ]]; then
        output=${1%.*}
        g++ '-std=c++17' $1 -o $output.out
        clear
        echo $output.out
        echo '----------'
        echo ''
        ./$output.out
    else
        echo 'Specify full cpp filename.'
    fi
}