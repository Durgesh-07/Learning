#include <iostream>
#include <vector>
#include <stack>
#include <sstream>  // for stringstream which reades from a string just like cin reads from keyboard
#include <cassert>

using namespace std;

struct Log {
    int id;
    string status;
    int timestamp;
};

class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<int> times(n, 0);
        stack<Log> st;
        for(string log: logs) {
            stringstream ss(log);  //  log is stored in ss
            string temp, temp2, temp3;
            getline(ss, temp, ':');  //  read from ss until ':' is found and store it in temp, then move the pointer to the next character after ':'
            getline(ss, temp2, ':');  // read from ss until ':' is found and store it in temp2, then move the pointer to the next character after ':'
            getline(ss, temp3, ':');  // read from ss until ':' is found and store it in temp3, then move the pointer to the next character after ':'

            Log item = {stoi(temp), temp2, stoi(temp3)};
            if(item.status == "start") {
                st.push(item);
            } else {
                assert(st.top().id == item.id);

                int time_added = item.timestamp - st.top().timestamp + 1;
                times[item.id] += time_added;
                st.pop();

                if(!st.empty()) {
                    assert(st.top().status == "start");
                    times[st.top().id] -= time_added;
                }
            }
        }

        return times;
    }
};