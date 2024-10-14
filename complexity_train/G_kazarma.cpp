#include <iostream>
using namespace std;

int finish(int x,int y, int s, int p){
    int ans = 0;
    while(x>0 && s+y>0 && ans < 5001){
        if(y>0){
            int t = min(x,y);
            y -= t;
            s = max(s-(x-t), 0); 
        }else{
            int t = min(x,s);
            s -= t;
            y = max(y-(x-t), 0);          
        }
        if(s>0){x-=s;}
        if(y>0){s+=p;}
        ans += 1;
    }
    if(s+y > 0){return 1e6;}
    else{return ans;}
}


int main(){
    
    int x,y,p; cin>>x>>y>>p;
    int s = 0;
    int ans = 5001;

    int dt = 0;
    while(x>0 && s+y>0 && dt<5001){
        ans = min(ans, dt+finish(x,y,s,p));     
        int t = min(x,s);
        s -=t;
        y = max(y-(x-t), 0); 
        if(s>0){x-=s;}
        if(y>0){s+=p;}
        dt+=1;

    }

    if(ans <= 5000){cout<<ans;}
    else{cout<<-1;}
    


}