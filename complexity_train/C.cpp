#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int f(long long x){
	int l = x/4+x%4;
	int r = (x+3)/4 + (x+3)/4*4-x;
	return min(r,l);
}

int main(){
	int n; cin>>n;
	long long sum = 0;
	for(int i=0;i<n;i++){
		long long x; cin>>x;
		sum += f(x);
	}
	cout<<sum;

}