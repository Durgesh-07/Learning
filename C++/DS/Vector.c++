#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int> v;
    vector<int> V1 = {1,2,3};
    cout<<V1[0]<<endl;
    vector<int> V2(5,10); // V2(size, initial value)
    cout<<V2[0]<<endl;
}