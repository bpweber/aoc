#include <iostream>
#include <fstream>

std::string digits[20] =  {"1", "2", "3", "4", "5", "6", "7", "8", "",
                           "one", "two", "three", "four", "five",
                           "six", "seven", "eight", "nine", "ten"};

std::string findDigitsInString(std::string s){
    for(std::string digit : digits){
//      std::cout << digit << std::endl;
        size_t pos = s.find(digit);
        if (pos != std::string::npos){
            std::cout << digit << " at " << pos << std::endl;
        }
    } 
    return "";
}

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
        findDigitsInString(s);
//      int val = stoi(getCalibrationFromString(s));
//      total += val;
//      std::cout << val << std::endl;
    }
    std::cout << total << std::endl;
    f.close();
    return;
}

int main() {
    readDataFromFile();
    return 0;
}
