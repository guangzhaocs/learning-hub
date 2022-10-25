#include <iostream>
#include <vector>
using namespace std;


class Class{
    public:
       Class(int n_student, vector<int>& studentID_arr):
           _n_student(n_student),
           _studentID_arr(studentID_arr)
           {}
       void show(void);
       void set_ID(int, int);
       vector<int>& _studentID_arr;
       int _n_student;
};

void Class::show(){
  cout << "Class          : ";
   for(auto x: _studentID_arr)
        cout << x << " ";
    cout << endl;
}


void Class::set_ID(int idx, int ID){
   _studentID_arr[idx] = ID;
}





class School{
    public:
       School(int n_class, Class& class1, Class& class2):
           _n_class(n_class),
           _class1(class1),
           _class2(class2)
           {}
       void show(void);
       void set_class1_student_ID(int, int);
       void set_class2_student_ID(int, int);
       Class& _class1;
       Class& _class2;
       int _n_class;



};


void School::set_class1_student_ID(int idx, int ID){
   _class1._studentID_arr[idx] = ID;
}

void School::show(){
  cout << "School Class 1 : ";
   for(auto x: _class1._studentID_arr)
        cout << x << " ";
    cout << endl;
}




int main()
{
    vector<int> class1_studentID_arr;
    vector<int> class2_studentID_arr;
    for(int i=1;i<11;i++){
        class1_studentID_arr.push_back(i);
        class2_studentID_arr.push_back(i*i);
    }

    Class class1 = Class(class1_studentID_arr.size(), class1_studentID_arr);
    Class class2 = Class(class2_studentID_arr.size(), class2_studentID_arr);
    School school = School(2, class1, class2);


    cout << " ------------ Initilization ----------" << endl;

    cout << "original       : ";
    for(auto x: class1_studentID_arr){
        cout << x << " ";
    }
    cout << endl;
    class1.show();
    school.show();


    cout << " ------------ Modify in arr ----------" << endl;
    class1_studentID_arr[0] = -1;

    cout << "original       : ";
    for(auto x: class1_studentID_arr){
        cout << x << " ";
    }
    cout << endl;
    class1.show();
    school.show();



    cout << " ------------ Modify in Class ----------" << endl;
    class1.set_ID(1, -2);

    cout << "original       : ";
    for(auto x: class1_studentID_arr){
        cout << x << " ";
    }
    cout << endl;
    class1.show();
    school.show();


    cout << " ------------ Modify in School ----------" << endl;
    school.set_class1_student_ID(2, -3);

    cout << "original       : ";
    for(auto x: class1_studentID_arr){
        cout << x << " ";
    }
    cout << endl;
    class1.show();
    school.show();
	
    return 0;
}
