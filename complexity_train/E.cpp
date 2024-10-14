#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;



int main(){
	int n,k,d; cin>>n>>k>>d;
    int t = 0;
    bool f = false;
	for(;t<9;t++){
		if((n*10+t)%k==0){
            f = true;
            break;    
        }
	}

    if(f){
        cout<<n;
        cout<<t;
        for(int i=0;i<d-1;i++){
            cout<<0;
        }
    }else{
        cout<<-1;
    }


}