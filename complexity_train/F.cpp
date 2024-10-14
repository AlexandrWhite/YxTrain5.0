#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main(){
	int n; cin>>n;
	vector<int>a(n);
	int odd_cnt = 0;
	for(int i=0;i<n;i++){
		cin>>a[i];
		a[i] = abs(a[i])%2;
		if(a[i]==1){odd_cnt++;}
	}

	if(odd_cnt%2==1){
		for(int i=0;i<n-1;i++){
			cout<<'+';
		}
	}else{
		for(int i=0;i<n-1;i++){
			if(odd_cnt%2 == 0 && a[i]==1){
				cout<<'x';
				odd_cnt -=1;
			}else{
				cout<<'+';
			}
		}
	}
}