#include <iostream>
#include <vector>
using namespace std;


class Region
{
   public:
      Region(int _st_b_ind, int _en_b_ind):
          st_b_ind(_st_b_ind),
          en_b_ind(_en_b_ind)
          {}

      int st_b_ind;
      int en_b_ind;

      void set_st_b_ind(int);
};


void Region::set_st_b_ind(int a){
     st_b_ind = a;
}



int main()
{
    vector<Region> reg_list;
    for(int i=0;i<2;i++){
        Region reg = Region(i, i+2);
        reg_list.push_back(reg);
    }

    cout << "Initialization " << endl;
    for(auto reg: reg_list){
        cout << reg.st_b_ind << ", " << reg.en_b_ind << endl;
    }

    cout << "Using auto to modify: " << endl;
    for(auto reg: reg_list){
        reg.set_st_b_ind(8);
    }

    for(auto reg: reg_list){
        cout << reg.st_b_ind << ", " << reg.en_b_ind << endl;
    }


    cout << "Using auto& to modify: " << endl;
    for(auto &reg: reg_list){
        reg.set_st_b_ind(7);
    }

    for(auto reg: reg_list){
        cout << reg.st_b_ind << ", " << reg.en_b_ind << endl;
    }

    cout << "Using for loop to modify: " << endl;
    for(int i=0;i<reg_list.size();i++){
        reg_list[i].set_st_b_ind(8);
    }

    for(auto reg: reg_list){
        cout << reg.st_b_ind << ", " << reg.en_b_ind << endl;
    }

    return 0;
}
