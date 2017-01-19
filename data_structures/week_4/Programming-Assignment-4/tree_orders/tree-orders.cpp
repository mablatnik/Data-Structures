#include <iostream>
#include <vector>
#include <algorithm>
#if defined(__unix__) || defined(__APPLE__)
#include <sys/resource.h>
#endif

using std::vector;
using std::ios_base;
using std::cin;
using std::cout;

class TreeOrders {
  int n;
  vector <int> key;
  vector <int> left;
  vector <int> right;

public:
  void read() {
    cin >> n;
    key.resize(n);
    left.resize(n);
    right.resize(n);
    for (int i = 0; i < n; i++) {
      cin >> key[i] >> left[i] >> right[i];
    }
  }

  struct Node
  {
    int key;
    int left;
    int right;
  };

  void inorder_traversal( std::vector<int> &result, int nodeIdx)
  {
    if (nodeIdx == -1)
      return;
    int k = key[nodeIdx];
    int l = left[nodeIdx];
    int r = right[nodeIdx];

    inorder_traversal( result, l);
    result.push_back( k );
    inorder_traversal( result, r);
  }

  vector<int> in_order()
  {
    if (key.empty())
      return std::vector<int>();

    vector<int> result;
    inorder_traversal(result, 0);
    return result;
  }

  void preorder_traversal(std::vector<int> &result, int nodeIdx)
  {
    if ( nodeIdx == -1 )
      return;

    result.push_back( key[ nodeIdx ] );
    preorder_traversal( result, left[ nodeIdx ] );
    preorder_traversal( result, right[ nodeIdx ] );
  }

  vector<int> pre_order()
  {
    if ( key.empty() )
      return std::vector<int>();

    vector<int> result;
    preorder_traversal(result, 0);
    return result;
  }

  void postorder_traversal(std::vector<int> &result, int nodeIdx)
  {
    if ( nodeIdx == -1 )
      return;

    postorder_traversal( result, left[ nodeIdx ] );
    postorder_traversal( result, right[ nodeIdx ] );
    result.push_back( key[ nodeIdx ] );
  }

  vector<int> post_order()
  {
    if ( key.empty() )
      return std::vector<int>();

    vector<int> result;
    postorder_traversal(result, 0);
    return result;
  }
};

void print(vector <int> a) {
  for (size_t i = 0; i < a.size(); i++) {
    if (i > 0) {
      cout << ' ';
    }
    cout << a[i];
  }
  cout << '\n';
}

int main_with_large_stack_space() {
  ios_base::sync_with_stdio(0);
  TreeOrders t;
  t.read();
  print(t.in_order());
  print(t.pre_order());
  print(t.post_order());
  return 0;
}

int main (int argc, char **argv)
{
#if defined(__unix__) || defined(__APPLE__)
  // Allow larger stack space
  const rlim_t kStackSize = 16 * 1024 * 1024;   // min stack size = 16 MB
  struct rlimit rl;
  int result;

  result = getrlimit(RLIMIT_STACK, &rl);
  if (result == 0)
  {
      if (rl.rlim_cur < kStackSize)
      {
          rl.rlim_cur = kStackSize;
          result = setrlimit(RLIMIT_STACK, &rl);
          if (result != 0)
          {
              std::cerr << "setrlimit returned result = " << result << std::endl;
          }
      }
  }
#endif

  return main_with_large_stack_space();
}

