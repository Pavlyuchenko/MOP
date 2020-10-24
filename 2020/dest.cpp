#include <iostream>
#include <limits>
#include <vector>
#include <string>
#include <sstream>
#include <bits/stdc++.h>

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
};

void init()
{
    int nodes_count, paths_count, limit_count;

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

    for (int i = 0; i < paths_count; i += 1)
    {
        Node *node1 = nodes[paths[i * 2]];
        Node *node2 = nodes[paths[i * 2 + 1]];
        node1->connected_nodes.push_back(node2);
        node2->connected_nodes.push_back(node1);
        // nodes[paths[i + 1]]->connect(nodes[paths[i]]);
    }

    // Testing
    /*
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

        cout << nodes[i]->connected_nodes[0] << endl;
        if (nodes[i]->connected_nodes.size() > 1)
        {
            cout << nodes[i]->connected_nodes[1] << endl;
        }
        if (nodes[i]->connected_nodes.size() > 2)
        {
            cout << nodes[i]->connected_nodes[2] << endl;
        }
    }*/

    nodes.back()->distance = 0;
    vector<Node *> queue;
    queue.push_back(nodes.back());

    // Experimental
    for (int i = 0; i < nodes.back()->connected_nodes.size(); i++)
    {
        Node *next = nodes.back()->connected_nodes[i];
        auto finder = find(next->connected_nodes.begin(), next->connected_nodes.end(), nodes.back());
        int index = distance(next->connected_nodes.begin(), finder);

        next->connected_nodes.erase(next->connected_nodes.begin() + index);
    }

    int min_distance = -1;
    int steps = 0;

    while (queue.size() != 0)
    {
        Node *curr = queue.front();
        queue.erase(queue.begin());

        for (int i = 0; i < curr->connected_nodes.size(); i++)
        {
            steps++;
            Node *next = curr->connected_nodes[i];
            if (!next->visited)
            {
                if (!(curr->zatopeno && curr->distance > limit_count))
                {
                    queue.push_back(next);

                    next->distance = curr->distance + 1;
                    next->visited = true;
                }
            }
        }
        if (!(curr->zatopeno && curr->distance > limit_count))
        {
            if (curr == nodes[0])
            {
                min_distance = curr->distance;
                break;
            }
        }
    }
    cout << min_distance << endl;
    cout << "steps: " << steps << endl;
};

int main()
{
    init();
}