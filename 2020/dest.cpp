#include <iostream>
#include <limits>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

class Node
{
public:
    bool visited = false;
    int distance = numeric_limits<int>::max();
    vector<Node *> connected_nodes;
    bool zatopeno;

    Node(bool aZatopeno)
    {
        zatopeno = aZatopeno;
    }

    void connect(Node *other)
    {
        connected_nodes.push_back(other);
        other->connected_nodes.push_back(this);
    }
};

void init(int priklad_choose)
{
    int nodes_count, paths_count, limit_count;

    if (priklad_choose == 1)
    {
        // Nodes, Paths, Limit input
        cin >> nodes_count >> paths_count >> limit_count;

        // Zatopene Nodes
        int zatopene_nodes[nodes_count];
        string zatopenost_str;

        cin.ignore();
        getline(cin, zatopenost_str);

        string buf;                      // Have a buffer string
        stringstream ss(zatopenost_str); // Insert the string into a stream

        vector<string> zatopeno; // Create vector to hold our words

        while (ss >> buf)
            zatopeno.push_back(buf);

        // Ukládám: stoi() -> str to int

        // Nodes array
        vector<Node *> nodes;

        for (int i = 0; i < nodes_count; i++)
        {
            if (zatopeno[i] == "1")
            {
                nodes.push_back(new Node(true));
            }
            else
            {
                nodes.push_back(new Node(false));
            }
        }

        // Paths connection
        int paths[paths_count * 2];
        int first_input, second_input;

        for (int i = 0; i < paths_count; i++)
        {
            cin >> first_input >> second_input;
            paths[i * 2] = first_input;
            paths[i * 2 + 1] = second_input;
        }

        for (int i = 0; i < paths_count * 2; i += 2)
        {
            nodes[paths[i]]->connect(nodes[paths[i + 1]]);
            // nodes[paths[i + 1]]->connect(nodes[paths[i]]);
        }

        // Testing
        cout << "Nodes: " << nodes_count << " Paths: " << paths_count << " Limit: " << limit_count << endl;
        cout << "Zatopenost: " << endl;
        for (int i = 0; i < nodes_count; i++)
        {
            cout << zatopeno[i] << endl;
        }

        for (int i = 0; i < paths_count; i++)
        {
            cout << paths[i * 2] << "<->" << paths[i * 2 + 1] << endl;
        }

        for (int i = 0; i < nodes_count; i++)
        {
            cout << nodes[i] << endl;
        }

        for (int i = 0; i < nodes_count; i++)
        {
            cout << nodes[i]->zatopeno << endl;
            for (int j = 0; i < nodes[j]->connected_nodes.size(); j++)
            {
                cout << nodes[i]->connected_nodes[j] << endl;
            }
        }
    }
};

int main()
{
    /*cout << "Hello Cpp" << endl;

    Node first(false);
    Node second(true);

    first.connect(&second);
    second.connect(&first);

    cout << first.connected_nodes[0] << endl;
    cout << second.connected_nodes[0] << endl;*/

    init(1);
}