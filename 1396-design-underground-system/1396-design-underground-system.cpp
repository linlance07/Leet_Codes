class UndergroundSystem { // simulation: 
public: //Time: O(N); Space:O(N)
    void checkIn(int id, string stationName, int t) {
        m[id] = {stationName, t}; //only keep latest checkIn info      
        //m.insert({id, {stationName, t}}); //ERR. keep 1st checkIn info
    }
    
   void checkOut(int id, string stationName, int t) {
        auto& [totDur, cnt] = stats[m[id].first + "_" + stationName];
        totDur += t - m[id].second;
        ++cnt;
    }
    
    double getAverageTime(string startStation, string endStation) {
        auto& [totDur, cnt] = stats[startStation + "_" + endStation];
        return (double)totDur/cnt;
    }
    
private:
    unordered_map<int, pair<string, int>> m;  // id->{station,time}
    unordered_map<string, pair<int, int>> stats;//from_to->{totDur, cnt}
};