#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void fill_hor_ver(int i, int j, vector<string>&field){
	//низ
	for(int k=i+1;k<8;k++){
		if(field[k][j]=='*' || field[k][j]=='#'){
			field[k][j] = '#';
		}else{
			break;
		}
	}
	//вверх
	for(int k=i-1;k>=0;k--){
		if(field[k][j]=='*'|| field[k][j]=='#'){
			field[k][j] = '#';
		}else{
			break;
		}
	}

	//право
	for(int k=j+1;k<8;k++){
		if(field[i][k] == '*' || field[i][k]=='#'){
			field[i][k] = '#';
		}else{
			break;
		}
	}

	//лево
	for(int k=j-1;k>=0;k--){
		if(field[i][k]=='*' || field[i][k]=='#'){
			field[i][k] = '#';
		}else{
			break;
		}
	}
}


void fill_diags(int i, int j, vector<string>&field){
	int ki = i+1;
	int kj = j+1;

	while(ki<8 && kj<8){

		if(field[ki][kj]=='*' || field[ki][kj]=='#'){
			field[ki][kj] = '#';
		}else{
			break;
		}

		ki++;
		kj++;
	}

	ki = i-1;
	kj = j-1;

	while(ki>=0 && kj>=0){

		if(field[ki][kj]=='*' || field[ki][kj]=='#'){
			field[ki][kj] = '#';
		}else{
			break;
		}

		ki--;
		kj--;
	}

	ki = i-1;
	kj = j+1;

	while(ki>=0 && kj<8){

		if(field[ki][kj]=='*' || field[ki][kj]=='#'){
			field[ki][kj] = '#';
		}else{
			break;
		}

		ki--;
		kj++;
	}

	ki = i+1;
	kj = j-1;

	while(ki<8 && kj >= 0){

		if(field[ki][kj] == '*' || field[ki][kj] == '#'){
			field[ki][kj] = '#';
		}else{
			break;
		}

		ki++;
		kj--;
	}				
}

int main(){
	vector<string>field(8);
	for(int i=0;i<8;i++){
		cin>>field[i];
	}

	for(int i=0;i<8;i++){
		for(int j =0;j<8;j++){
			if(field[i][j]=='R'){
				fill_hor_ver(i,j,field);
			}

			if(field[i][j]=='B'){
				fill_diags(i,j,field);
			}
		}
	}

	int ans = 0;
	for(int i=0;i<8;i++){
		for(int j=0;j<8;j++){
			if(field[i][j]=='*'){
				ans++;
			}
			//cout<<field[i][j]<<" ";
		}
		//cout<<"\n";
	}
	cout<<ans;
}