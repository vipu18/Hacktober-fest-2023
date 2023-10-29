#include <bits/stdc++.h>
using namespace std;

class Graph{
public:

    unordered_map<int, bool> visited;
    unordered_map<int, list<int>> adj;

    void addEdge(int u, int v);
    unordered_map<int, int> BFS(int s);
    void shortestPath(int s, int d);
};

void Graph::addEdge(int u, int v) {
    adj[u].push_back(v);
    adj[v].push_back(u);
}

unordered_map<int, int> Graph::BFS(int s) {
    unordered_map<int, int> prev;
    visited[s] = true;
    queue<int> q;
    q.push(s);

    while(!q.empty()) {
        int k = q.front();
        q.pop();
        cout << k << " ";

        for(auto i = adj[k].begin(); i != adj[k].end(); i++) {
            if(!visited[*i]) {
                q.push(*i);
                visited[*i] = true;
                prev[*i] = k;
            }
        }
    }

    return prev;
}

void Graph::shortestPath(int s, int d) {

    unordered_map<int, int> prev = BFS(s);
    int at = d;
    
    for(auto i = prev.begin(); i != prev.end(); i++) {
        cout << i->first << " " << i->second << endl;
    }

    while(prev[at] != s) {
        // cout << at << " ";
        at = prev[at];
    }
}


int main()
{
    Graph g;

    g.addEdge(0, 1);
    g.addEdge(0, 3);
    g.addEdge(1, 2);
    g.addEdge(3, 4);
    g.addEdge(3, 7);
    g.addEdge(4, 5);
    g.addEdge(4, 6);
    g.addEdge(4, 7);
    g.addEdge(5, 6);
    g.addEdge(6, 7);

    int source = 0, dest = 7;
    g.shortestPath(source, dest);

        return 0;
}