#include <iostream>
#include <limits>
#include <vector>

using namespace std;


class Node{
    public:
        Node(bool aZatopeno){
            bool zatopeno = aZatopeno;
            bool visited = false;

            int distance = numeric_limits<int>::max();

            vector<Node> *connected_nodes[] = {};            
        }

        void connect(Node *other){
            this->connected_nodes.push_back(other);
        }
};

int main()
{
    cout << "Hello Cpp" << endl;
}