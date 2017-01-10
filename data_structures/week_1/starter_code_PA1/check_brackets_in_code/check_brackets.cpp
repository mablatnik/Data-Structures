#include <iostream>
#include <stack>
#include <string>


struct Bracket {
    Bracket(char type, int position):
        type(type),
        position(position)
    {}

    bool Match(char c) {
        if (type == '[' && c == ']')
            return true;
        if (type == '{' && c == '}')
            return true;
        if (type == '(' && c == ')')
            return true;
        return false;
    }

    char type;
    int position;
};

int main() {
    std::string text;
    // getline(std::cin, text);
    text = "[]";

    std::stack <Bracket> opening_brackets_stack;
    bool flag = false;
    for (int position = 0; position < text.length(); ++position) {
        char next = text[position];

        if (next == '(' || next == '[' || next == '{') {
            opening_brackets_stack.push(Bracket(next, position));

        } else if (next == ')' || next == ']' || next == '}') {
            if (opening_brackets_stack.size() > 0) {
                std::cout << position;
                flag = true;
                break;
            }
            Bracket* top = opening_brackets_stack.pop();
            if (top.Match(next) == false) {
                std::cout << opening_brackets_stack.pop().position;
                flag = true;
                break;
            }
        }
    }

    if (opening_brackets_stack.size() > 0) {
        Bracket* top = opening_brackets_stack.pop();
        std::cout << top.position;
        flag = true;
    }

    if (flag == false) {
        std::cout << "Success";
    }
}
