//Список
#include <iostream>  
#include <list>  
using namespace std;  
int main() {  
    list<int> myList; // объявляем пустой список  
    for (int i = 0; i < 11; i++) {  
        myList.push_back(i); // добавляем в список новые элементы  
    }  
    cout << "Список: ";  
    copy(myList.begin(), myList.end(), ostream_iterator<int>(cout, " ")); // вывод на экран элементов списка  
    cout << "\nПервый элемент списка: " << myList.front();  
    cout << "\nПоследний элемент списка: " << myList.back();  
    return 0;  
}  


//Стек
std::stack<int> stack;  
stack.push(10);  
stack.push(20);  
stack.push(30);  
