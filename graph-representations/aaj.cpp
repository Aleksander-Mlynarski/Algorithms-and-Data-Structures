#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

class Matrix {
public:
    int r, c;
    vector<vector<int>> data;

    Matrix() {
        r = 0;
        c = 0;
    }

    Matrix(int rows, int cols, int default_val = 0) {
        r = rows;
        c = cols;
        data = vector<vector<int>>(r, vector<int>(c, default_val));
    }

    Matrix(const vector<vector<int>>& init) {
        data = init;
        r = (int)data.size();
        c = r > 0 ? (int)data[0].size() : 0;
    }

    vector<int>& operator[](int i) {
        return data[i];
    }

    const vector<int>& operator[](int i) const {
        return data[i];
    }
};

class Vertex {
public:
    string key;

    Vertex() {}
    Vertex(string k) {
        key = k;
    }

    bool operator==(const Vertex& other) const {
        return key == other.key;
    }

    bool operator<(const Vertex& other) const {
        return key < other.key;
    }

    bool operator!=(const Vertex& other) const {
        return key != other.key;
    }

    friend ostream& operator<<(ostream& os, const Vertex& v) {
        os << v.key;
        return os;
    }
};

class Lista_sasiedztwa {
public:
    map<Vertex, map<Vertex, int>> nodes;

    bool is_empty() {
        return nodes.empty();
    }

    void insert_vertex(const Vertex& vertex) {
        if (nodes.find(vertex) == nodes.end()) {
            nodes[vertex] = map<Vertex, int>();
        }
    }

    void insert_edge(const Vertex& v1, const Vertex& v2, int edge = 1) {
        insert_vertex(v1);
        insert_vertex(v2);
        nodes[v1][v2] = edge;
        nodes[v2][v1] = edge;
    }

    void delete_vertex(const Vertex& vertex) {
        for (auto it = nodes.begin(); it != nodes.end(); ++it) {
            it->second.erase(vertex);
        }
        nodes.erase(vertex);
    }

    void delete_edge(const Vertex& v1, const Vertex& v2) {
        nodes[v1].erase(v2);
        nodes[v2].erase(v1);
    }

    int get_edge(const Vertex& v1, const Vertex& v2) {
        return nodes[v1][v2];
    }

    vector<Vertex> vertices() {
        vector<Vertex> out;
        for (auto it = nodes.begin(); it != nodes.end(); ++it) {
            out.push_back(it->first);
        }
        return out;
    }

    vector<pair<Vertex, int>> neighbours(const Vertex& vertex_id) {
        vector<pair<Vertex, int>> out;
        for (auto it = nodes[vertex_id].begin(); it != nodes[vertex_id].end(); ++it) {
            out.push_back(*it);
        }
        return out;
    }

    Vertex get_vertex(const Vertex& vertex_id) {
        return vertex_id;
    }
};

class Macierz_sasiedztwa {
public:
    vector<Vertex> nodes;
    Matrix matrix;
    int _default;

    Macierz_sasiedztwa(int default_val = 0) {
        _default = default_val;
        matrix = Matrix(0, 0, _default);
    }

    bool is_empty() {
        return nodes.empty();
    }

    int _index_of(const Vertex& vertex) {
        int i = 0;
        while (i < (int)nodes.size()) {
            if (nodes[i] == vertex) {
                return i;
            }
            i++;
        }
        return -1;
    }

    void insert_vertex(const Vertex& vertex) {
        if (_index_of(vertex) != -1) {
            return;
        }

        int n = (int)nodes.size();
        Matrix new_matrix(n + 1, n + 1, _default);

        int i = 0;
        while (i < n) {
            int j = 0;
            while (j < n) {
                new_matrix[i][j] = matrix[i][j];
                j++;
            }
            i++;
        }

        matrix = new_matrix;
        nodes.push_back(vertex);
    }

    void insert_edge(const Vertex& v1, const Vertex& v2, int edge = 1) {
        if (_index_of(v1) == -1) {
            insert_vertex(v1);
        }
        if (_index_of(v2) == -1) {
            insert_vertex(v2);
        }

        int i = _index_of(v1);
        int j = _index_of(v2);

        matrix[i][j] = edge;
        matrix[j][i] = edge;
    }

    void delete_vertex(const Vertex& vertex) {
        int idx = _index_of(vertex);
        if (idx == -1) {
            return;
        }

        vector<Vertex> new_nodes;
        int i = 0;
        while (i < (int)nodes.size()) {
            if (i != idx) {
                new_nodes.push_back(nodes[i]);
            }
            i++;
        }
        nodes = new_nodes;

        int old_n = (int)matrix.r;
        Matrix new_matrix(old_n - 1, old_n - 1, _default);

        int r = 0;
        int nr = 0;
        while (r < old_n) {
            if (r == idx) {
                r++;
                continue;
            }

            int c = 0;
            int nc = 0;
            while (c < old_n) {
                if (c == idx) {
                    c++;
                    continue;
                }
                new_matrix[nr][nc] = matrix[r][c];
                c++;
                nc++;
            }

            r++;
            nr++;
        }

        matrix = new_matrix;
    }

    void delete_edge(const Vertex& v1, const Vertex& v2) {
        int i = _index_of(v1);
        int j = _index_of(v2);
        if (i == -1 || j == -1) {
            return;
        }
        matrix[i][j] = _default;
        matrix[j][i] = _default;
    }

    int get_edge(const Vertex& v1, const Vertex& v2) {
        int i = _index_of(v1);
        int j = _index_of(v2);
        return matrix[i][j];
    }

    vector<int> vertices() {
        vector<int> out;
        int i = 0;
        while (i < (int)nodes.size()) {
            out.push_back(i);
            i++;
        }
        return out;
    }

    vector<pair<int, int>> neighbours(int vertex_id) {
        vector<pair<int, int>> out;
        int j = 0;
        while (j < (int)nodes.size()) {
            if (matrix[vertex_id][j] != _default) {
                out.push_back({j, matrix[vertex_id][j]});
            }
            j++;
        }
        return out;
    }

    Vertex get_vertex(int vertex_id) {
        return nodes[vertex_id];
    }
};

void print_list_graph(Lista_sasiedztwa& g) {
    auto vs = g.vertices();
    int i = 0;
start_v:
    if (i >= (int)vs.size()) goto end_v;
    cout << vs[i] << ": ";
    {
        auto ns = g.neighbours(vs[i]);
        int j = 0;
    start_n:
        if (j >= (int)ns.size()) goto end_n;
        cout << "(" << ns[j].first << "," << ns[j].second << ") ";
        j++;
        goto start_n;
    end_n:
        cout << "\n";
    }
    i++;
    goto start_v;
end_v:
    cout << "\n";
}

void print_matrix_graph(Macierz_sasiedztwa& g) {
    auto vs = g.vertices();
    int i = 0;
start_v2:
    if (i >= (int)vs.size()) goto end_v2;
    cout << g.get_vertex(vs[i]) << ": ";
    {
        auto ns = g.neighbours(vs[i]);
        int j = 0;
    start_n2:
        if (j >= (int)ns.size()) goto end_n2;
        cout << "(" << g.get_vertex(ns[j].first) << "," << ns[j].second << ") ";
        j++;
        goto start_n2;
    end_n2:
        cout << "\n";
    }
    i++;
    goto start_v2;
end_v2:
    cout << "\n";
}

int main() {
    vector<pair<string, string>> graf = {
        {"Z","G"}, {"Z","P"}, {"Z","F"},
        {"G","Z"}, {"G","P"}, {"G","C"}, {"G","N"},
        {"N","G"}, {"N","C"}, {"N","W"}, {"N","B"},
        {"B","N"}, {"B","W"}, {"B","L"},
        {"F","Z"}, {"F","P"}, {"F","D"},
        {"P","F"}, {"P","Z"}, {"P","G"}, {"P","C"}, {"P","E"}, {"P","O"}, {"P","D"},
        {"C","P"}, {"C","G"}, {"C","N"}, {"C","W"}, {"C","E"},
        {"E","P"}, {"E","C"}, {"E","W"}, {"E","T"}, {"E","S"}, {"E","O"},
        {"W","C"}, {"W","N"}, {"W","B"}, {"W","L"}, {"W","T"}, {"W","E"},
        {"L","W"}, {"L","B"}, {"L","R"}, {"L","T"},
        {"D","F"}, {"D","P"}, {"D","O"},
        {"O","D"}, {"O","P"}, {"O","E"}, {"O","S"},
        {"S","O"}, {"S","E"}, {"S","T"}, {"S","K"},
        {"T","S"}, {"T","E"}, {"T","W"}, {"T","L"}, {"T","R"}, {"T","K"},
        {"K","S"}, {"K","T"}, {"K","R"},
        {"R","K"}, {"R","T"}, {"R","L"}
    };

    Lista_sasiedztwa lista;
    Macierz_sasiedztwa macierz;

    int i = 0;
start_build:
    if (i >= (int)graf.size()) goto end_build;

    Vertex a(graf[i].first);
    Vertex b(graf[i].second);

    lista.insert_edge(a, b, 1);
    macierz.insert_edge(a, b, 1);

    i++;
    goto start_build;
end_build:

    Vertex malopolskie("K");
    Vertex mazowieckie("W");
    Vertex lodzkie("E");

    lista.delete_vertex(malopolskie);
    macierz.delete_vertex(malopolskie);

    lista.delete_edge(mazowieckie, lodzkie);
    macierz.delete_edge(mazowieckie, lodzkie);

    cout << "Lista sasiedztwa:\n";
    print_list_graph(lista);

    cout << "Macierz sasiedztwa:\n";
    print_matrix_graph(macierz);

    return 0;
}