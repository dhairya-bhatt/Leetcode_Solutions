#include <string>
class Solution {
public:
    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        //alice arrival count
        int a_a_count = ((275*stoi(arriveAlice.substr(0,2)))/9) -2*((stoi(arriveAlice.substr(0,2))+9)/12)+stoi(arriveAlice.substr(3,2))-30;
        //alice departure count
        int a_d_count = ((275*stoi(leaveAlice.substr(0,2)))/9) -2*((stoi(leaveAlice.substr(0,2))+9)/12)+stoi(leaveAlice.substr(3,2))-30;
        //bob arrival count
        int b_a_count = ((275*stoi(arriveBob.substr(0,2)))/9) -2*((stoi(arriveBob.substr(0,2))+9)/12)+stoi(arriveBob.substr(3,2))-30;
        //bob departure count
        int b_d_count = ((275*stoi(leaveBob.substr(0,2)))/9) -2*((stoi(leaveBob.substr(0,2))+9)/12)+stoi(leaveBob.substr(3,2))-30;
        
        return max(0, min(a_d_count, b_d_count) - max(a_a_count, b_a_count) + 1);
    }
};