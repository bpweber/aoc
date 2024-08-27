#include <iostream>
#include <fstream>

std::string getCalibrationFromString(std::string s) {
    std::string left = "";
    std::string right = "";
    for(char& c : s) {
        if(isdigit(c)){
            left += c;
            break;
        }
    }
    for(int i = s.length(); i >= 0; i--){
        if(isdigit(s[i])){
            right += s[i];
            break;
        }
    }
    std::string rs = "";
    rs += left;
    rs += right;
    return (left + right);
}

void readDataFromFile(){
    int total = 0;
    std::string s; 
    std::ifstream f("input.txt");
    while(getline(f, s)){
        int val = stoi(getCalibrationFromString(s));
        total += val;
        std::cout << val << std::endl;
    }
    std::cout << total << std::endl;
    f.close();
    return;
}

int main() {
    readDataFromFile();
    return 0;
}
