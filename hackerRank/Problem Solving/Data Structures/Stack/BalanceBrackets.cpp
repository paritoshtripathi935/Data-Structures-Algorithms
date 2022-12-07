
string isBalanced(string store) {
    stack<char> res;
    bool ans = true;
    for(char & i : store){
        if (i == '(' || i == '{' || i == '['){
            res.push(i);
        }
        else if (i == ']' || i == '}' || i == ')'){
            if (res.empty()){
                ans = false;
                break;
            }
            auto current = res.top();
            if (i == ']'){
                if (current == '['){
                    res.pop();
                    continue;
                }
                else ans = false;
                break;
            }
            if (i == ')'){
                if (current == '('){
                    res.pop();
                    continue;
                }else{
                    ans = false;
                    break;
                }
            }
            if (i == '}'){
                if (current == '{'){
                    res.pop();
                    continue;
                }else{
                    ans = false;
                    break;
                }
            }
        }
    }
    if (!ans || !res.empty()){
        return "NO";
    }
    return "YES";
}
