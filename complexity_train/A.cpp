#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int section_inter(int L1,int R1, int L2, int R2){
	pair<int,int>most_left;
	pair<int,int>most_right;

	if(L1<=L2){
		most_left = {L1,R1};
		most_right = {L2,R2};
	}else{
		most_left = {L2,R2};
		most_right = {L1,R1};
	}
	
	if(most_right.first > most_left.second){
		return 0;
	}else if (most_right.first >= most_left.first && most_right.second <= most_left.second){
		return most_right.second - most_right.first + 1;
	}else{
		return most_left.second - most_right.first + 1;
	}
}


int main(){
	int p,v; cin>>p>>v;
	int q,m; cin>>q>>m;

	int L1 = p-v;
	int R1 = p+v;

	int L2 = q-m;
	int R2 = q+m;

	int d = min(L1,L2);
	if(d<0){
		L1 += d;
		R1 += d;

		L2 += d;
		R2 += d;
	}

	cout<<2*v+1 + 2*m+1 - section_inter(L1,R1,L2,R2)<<"\n";
}	