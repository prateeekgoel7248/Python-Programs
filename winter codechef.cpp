#include <bits/stdc++.h>
#define ll long long
#define pb push_back
using namespace std;
vector<ll> v[200005];
int main() {
  ll n,m,Q,x,y;
  cin>>n>>m>>Q;
  while(m--) {
    cin>>x>>y;
    v[x].pb(y);
    v[y].pb(x);
  }
  map<ll,ll> mp;
  queue<ll> q;
  while(Q--) {
    cin>>x>>y;
    if(x==3) {
      if(mp[y]==1) cout<<"YES\n";
      else cout<<"NO\n";
    }
    else if(x==1) {
      if(mp[y]==0) q.push(y);
      mp[y]=1;
    }
    else {
      for(int i=0;i<y && !q.empty();i++) {
        int kiq=q.size();
        while(kiq--) {
          ll u=q.front();
          q.pop();
          for(auto x:v[u]) {
            if(mp[x]==0) {
              mp[x]=1;
              q.push(x);
            }
          }
        }
      }
    }
  }
  return 0;
}


// #include <bits/stdc++.h>
// using namespace std;

// #define ll long long
// #define fo(i,j) for(i=0;i<j;i++)



// void solve() {
//     ll int i, j, n, m, k;
//     //TODO
//     cin >> n >> m >>k; 
//     vector<int> vis(n+1,0);
//     vector<int> adj[n+1]; 
//     for(int i = 0;i<m;i++) {
//         int u, v; 
//         cin >> u >> v;
//         adj[u].push_back(v); 
//         adj[v].push_back(u); 
//     }
//     vector<pair<int,int>> query;
//     fo(i,k){
//       int t1,t2;
//       cin>>t1>>t2;
//       query.push_back(make_pair(t1,t2));
//     }
    
//     for(auto p : query){
//       int type = p.first;
//       int u = p.second;
//       if(type==1){
//         vis[u] = 1;
//       }
//       else if(type==2)
//       {
//           queue<int> q;
//           fo(i,n+1){
//             if(vis[i]==1) q.push(i);
//           }
//             int time  = u;
//             while(time > 0){
//               while(q.size() > 0){
//                 int cur = q.front();
//                 q.pop();
//                 for(auto it : adj[cur]) {
//                   if(!vis[it]) { 
//                       vis[it] = 1; 
//                     }
//                 }
//               }
//               time--;
//             }
//         }      
//       else{
//         if(vis[u]==1) cout<<"YES"<<endl;
//         else cout<<"NO"<<endl;
//       }
//     }
//   }


// int main(){
//     solve();
//     return 0;
// } 
 
 