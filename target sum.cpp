
int findWays(vector<int> &num, int tar)
{
    //You can get pretty suicidal if you fill up the vector with -1 instead of 0's.
    vector<vector<int>> dp(num.size(), vector<int>(tar+1, 0));

    if(num[0] == 0)    dp[0][0] = 2;
    else dp[0][0] = 1; 
    
    //if check is needed to prevent array index out of bounds
    if(num[0] != 0 and num[0] <= tar)
    {
        dp[0][num[0]] = 1;         
    }
    
    for(int index=1; index<num.size(); index++)
    {
        for(int sum=0; sum <= tar; sum++)
        {
            int way1=0, way2=0;

            //The if condition check is necessary to prevent array index out of bounds!
            if(num[index] <= sum)
                way1 = dp[index-1][sum-num[index]];
            
            way2 = dp[index-1][sum];
            
            dp[index][sum] = (way1 + way2); 
        }
    }
    
    return dp[num.size()-1][tar];
}

int countPartitions(int n, int d, vector<int> &arr) {
    int total = 0;
    for(auto &it: arr)    total+=it;
    
    if(total - d < 0 or (total - d)%2)    return 0;
    
    return findWays(arr, (total-d)/2);
}
int targetSum(int n, int target, vector<int>& arr) {
    return countPartitions(n,target,arr);
}