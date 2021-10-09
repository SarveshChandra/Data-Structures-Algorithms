using namespace std;

#define deb(x) cout<<#x<<" "<<x<<endl
#define deb2(x,y) cout<<#x<<" "<<x<<", "<<#y<<" "<<y<<endl
#define deb3(x,y,z) cout<<#x<<" "<<x<<", "<<#y<<" "<<y<<", "<<#z<<" "<<z<<endl

// #define deb4(...) logger(#__VA_ARGS__, __VA_ARGS__)
// template<typename ...Args>
// void logger(string vars, Args&&... values) {
//     cout << vars << " = ";
//     string delim = "";
//     (..., (cout << delim << values, delim = ", "));
// }

template<typename ...T>
void printer(T&&... args) {
    ((cout << args << " "), ...);
    cout<<endl;
}