class Solution {
    bool f(vector<int> &a) {
        const int n = a.size();
        for (int i = 0; i + 1< n; ++i)
            if (a[i] > a[i+1])
                return false;
        return true;
    }
public:
    bool checkPossibility(vector<int>& a) {
        const int n = a.size();
        for (int i = 0; i + 1 < n; ++i)
            if (a[i] > a[i + 1]) {
                vector<int> b = a, c = a;
                b[i] = i == 0 ? INT_MIN : b[i - 1];
                c[i+1] = c[i];
                return f(b) || f(c);
            }
        return true;
    }
};

// Solution by cchao: Just do a simulation. b and c represent thw two possible ways to adjust the element.
