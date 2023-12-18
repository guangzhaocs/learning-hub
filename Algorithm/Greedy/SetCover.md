# The set cover problem [Greedy]

![image](https://user-images.githubusercontent.com/85612159/200556612-64c3d4d5-c648-401c-85df-a335e1045a85.png)

```
#include <iostream>
#include <vector>
using namespace std;


void solver(int n, int m, const int *p, const int *f, int &k, int *r)
{
    k = 0;
    if(m==0){
        return;
    }

    vector<int> not_cover(n, 0);
    vector<int> m_flag(m, 0);

    for(int i = 1; i < n; i++)
    {
       not_cover[i] = i;
    }

    int update_time = 0;
    int max_num, i_num;
    int max_idx;
    while(update_time < n){

        max_num = 0;
        max_idx = -1;

        //find intersection maximum idex
        for(int i=0;i<m;i++){
            if(m_flag[i] == 0){
                i_num = 0;
                for(int j=p[i];j<p[i+1];j++){
                    if(not_cover[f[j]] != -1){
                        i_num += 1;
                    }
                }
                if(i_num > max_num){
                    max_num = i_num;
                    max_idx = i;
                }
            }
        }



        // update not cover arr
        if(max_idx != -1){
            for(int j=p[max_idx];j<p[max_idx+1];j++){
                if(not_cover[f[j]] != -1){
                   not_cover[f[j]] = -1;
                   update_time = update_time + 1;
                }
            }
            m_flag[max_idx] = 1;
            r[k] = max_idx;
            k+=1;
        }else{
            k = 0;
            return;
        }

    }
}



int main()
{
    int n = 12;
    int m = 20;
    int p[m+1]={0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60};
    int f[p[m]]={0, 6, 10,
    0, 6, 11,
    1, 8, 11,
    2, 5, 6,
    4, 7, 8,
    9, 10, 11,
    0, 9, 10,
    0, 1, 5,
    7, 8, 11,
    1, 2, 7,
    3, 8, 9,
    4, 5, 10,
    2, 5, 7,
    2, 3, 6,
    4, 5, 10,
    3, 4, 7,
    2, 3, 9,
    3, 8, 9,
    0, 1, 6,
    1, 4, 11};


    int k = 0;
    int r[m]={0};
    solver(n, m, p, f, k, r);

    cout << "k : " << k << endl;
    cout << "r : " ;
    for(int i=0;i<m;i++){
        cout<< r[i] << " ";
    }

    return 0;
}

```
